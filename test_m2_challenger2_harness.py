#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Milestone 2 Challenger 2: Adversarial Stress Test & Robustness Harness
================================================================================
Target: d:\\c++\\quiz_game\\server.js
Focus Areas:
  1. Infinite Loop / TLE Enforcement (~2.0s - 3.5s kill, no orphaned processes)
  2. Output Flooding / Buffer Overflow (10M lines, 1MB stdout cap, no OOM)
  3. Memory Exhaustion / Allocation Hog (1GB+, bad_alloc handling)
  4. Crash Code Verification (0xC0000005, 0xC0000094, 0xC00000FD)
  5. Filesystem Escape Attempt & Workspace Integrity
  6. Temporary Directory Cleanup & Orphaned Binary Detection
================================================================================
"""

import sys
import os
import json
import time
import tempfile
import urllib.request
import urllib.error
import subprocess
import unittest
from pathlib import Path

# Ensure utf-8 output safe for Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Paths
QUIZ_GAME_DIR = Path(__file__).resolve().parent
ROOT_DIR = QUIZ_GAME_DIR.parent
SERVER_JS_PATH = QUIZ_GAME_DIR / "server.js"

DEFAULT_PORT = 3045
SERVER_URL = f"http://127.0.0.1:{DEFAULT_PORT}"


def get_running_process_pids(image_name: str) -> list:
    """Returns list of PIDs currently running for a given executable image name on Windows."""
    if sys.platform != "win32":
        return []
    try:
        out = subprocess.check_output(
            ["tasklist", "/FI", f"IMAGENAME eq {image_name}", "/FO", "CSV", "/NH"],
            text=True,
            stderr=subprocess.DEVNULL
        )
        pids = []
        for line in out.strip().splitlines():
            parts = line.split(",")
            if len(parts) >= 2:
                raw_pid = parts[1].strip(' "')
                if raw_pid.isdigit():
                    pids.append(int(raw_pid))
        return pids
    except Exception:
        return []


def count_temp_sandbox_dirs() -> list:
    """Returns list of existing quiz_eval_* directories in tempdir."""
    temp_dir = Path(tempfile.gettempdir())
    try:
        return [d for d in temp_dir.iterdir() if d.is_dir() and d.name.startswith("quiz_eval_")]
    except Exception:
        return []


class ServerFixture:
    process = None
    managed = False

    @classmethod
    def ensure_server(cls):
        try:
            req = urllib.request.Request(f"{SERVER_URL}/api/health")
            with urllib.request.urlopen(req, timeout=1.0) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode())
                    if data.get("status") == "ok":
                        print(f"[Fixture] Attached to active server at {SERVER_URL}")
                        return
        except Exception:
            pass

        print(f"[Fixture] Launching dedicated server on port {DEFAULT_PORT}...")
        cls.process = subprocess.Popen(
            ["node", str(SERVER_JS_PATH), str(DEFAULT_PORT)],
            cwd=str(QUIZ_GAME_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        cls.managed = True
        start_time = time.time()
        while time.time() - start_time < 5.0:
            try:
                req = urllib.request.Request(f"{SERVER_URL}/api/health")
                with urllib.request.urlopen(req, timeout=0.5) as resp:
                    if resp.status == 200:
                        print(f"[Fixture] Server online in {time.time() - start_time:.2f}s")
                        return
            except Exception:
                time.sleep(0.1)
        cls.teardown()
        raise RuntimeError("Failed to start test server on port " + str(DEFAULT_PORT))

    @classmethod
    def teardown(cls):
        if cls.managed and cls.process:
            print("[Fixture] Stopping server...")
            try:
                if sys.platform == "win32":
                    subprocess.run(["taskkill", "/F", "/T", "/PID", str(cls.process.pid)], capture_output=True)
                else:
                    cls.process.terminate()
            except Exception:
                pass
            cls.process = None


def send_evaluate_request(source_code: str, test_cases: list, problem_id: str = None, timeout: float = 30.0) -> dict:
    payload = {"sourceCode": source_code}
    if test_cases is not None:
        payload["testCases"] = test_cases
    if problem_id:
        payload["problemId"] = problem_id

    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{SERVER_URL}/api/evaluate",
        data=req_data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


class TestChallenger2Milestone2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ServerFixture.ensure_server()

    # =========================================================================
    # REQ 1: Infinite Loop / Time Limit Exceeded (TLE) Enforcement
    # =========================================================================

    def test_1_1_infinite_cpu_loop_tle_kill(self):
        """Verify CPU-bound while(true) loop is killed within 2.0s - 3.5s without orphaned processes."""
        code = """
        #include <iostream>
        int main() {
            volatile long long counter = 0;
            while (true) {
                counter++;
            }
            return 0;
        }
        """
        sandboxes_before = count_temp_sandbox_dirs()

        t0 = time.time()
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "done"}])
        elapsed = time.time() - t0

        self.assertTrue(res.get("success"), "Evaluation request should succeed")
        self.assertTrue(res.get("compiled"), "Code should compile cleanly")
        results = res.get("results", [])
        self.assertEqual(len(results), 1)
        r0 = results[0]

        self.assertEqual(r0.get("status"), "Time Limit Exceeded")
        self.assertFalse(r0.get("passed"))
        self.assertEqual(r0.get("score"), 0)
        self.assertIn("Time Limit Exceeded", r0.get("error", ""))

        # Execution time constraint: ~2.0s - 3.5s per testcase
        print(f"       [TLE Test 1.1] Elapsed: {elapsed:.2f}s, reported timeMs: {r0.get('timeMs')}ms")
        self.assertGreaterEqual(elapsed, 1.8, "Should not terminate earlier than ~2.0s timeout")
        self.assertLessEqual(elapsed, 4.0, "Should terminate within ~3.5s timeout window")

        # Check process cleanup
        time.sleep(0.5)
        pids_after = get_running_process_pids("solution.exe")
        self.assertEqual(len(pids_after), 0, f"No orphaned solution.exe processes should remain! Found: {pids_after}")

        # Check sandbox cleanup
        sandboxes_after = count_temp_sandbox_dirs()
        self.assertLessEqual(len(sandboxes_after), len(sandboxes_before), "Temp sandbox should be cleaned up")

    def test_1_2_infinite_io_loop_tle_kill(self):
        """Verify I/O-bound while(true) with cout & sleep is killed within timeout without lock."""
        code = """
        #include <iostream>
        #include <thread>
        #include <chrono>
        int main() {
            while (true) {
                std::cout << "heartbeat\\n";
                std::this_thread::sleep_for(std::chrono::milliseconds(50));
            }
            return 0;
        }
        """
        t0 = time.time()
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "never"}])
        elapsed = time.time() - t0

        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Time Limit Exceeded")
        self.assertGreaterEqual(elapsed, 1.8)
        self.assertLessEqual(elapsed, 4.0)
        print(f"       [TLE Test 1.2 I/O] Elapsed: {elapsed:.2f}s")

    def test_1_3_multithreaded_infinite_loop_kill(self):
        """Verify multithreaded infinite loops are killed along with the entire process tree."""
        code = """
        #include <iostream>
        #include <thread>
        #include <vector>
        void worker() {
            volatile long long c = 0;
            while (true) c++;
        }
        int main() {
            std::vector<std::thread> pool;
            for (int i = 0; i < 4; ++i) {
                pool.emplace_back(worker);
            }
            for (auto& t : pool) {
                t.join();
            }
            return 0;
        }
        """
        t0 = time.time()
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "done"}])
        elapsed = time.time() - t0

        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Time Limit Exceeded")
        print(f"       [TLE Test 1.3 Threads] Elapsed: {elapsed:.2f}s")
        time.sleep(0.5)
        pids = get_running_process_pids("solution.exe")
        self.assertEqual(len(pids), 0, "All worker threads/processes must be killed by taskkill")

    # =========================================================================
    # REQ 2: Output Flooding / Buffer Overflow
    # =========================================================================

    def test_2_1_output_flooding_10_million_lines(self):
        """Submit C++ code outputting 10,000,000 lines; verify 1MB cap and fast kill without server OOM."""
        code = """
        #include <iostream>
        int main() {
            std::ios_base::sync_with_stdio(false);
            std::cin.tie(NULL);
            for (int i = 0; i < 10000000; ++i) {
                std::cout << "Adversarial output flood line " << i << " with lots of payload bytes to test buffer cap.\\n";
            }
            return 0;
        }
        """
        t0 = time.time()
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "none"}])
        elapsed = time.time() - t0

        self.assertTrue(res.get("success"))
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Output Limit Exceeded")
        self.assertFalse(r0["passed"])
        self.assertEqual(r0["score"], 0)
        self.assertIn("Output Limit Exceeded", r0["error"])

        # Check stdout length was capped at ~1MB
        actual_output_len = len(r0.get("actualOutput", ""))
        print(f"       [Output Flood 2.1] Elapsed: {elapsed:.2f}s, stdout length: {actual_output_len} bytes")
        self.assertGreater(actual_output_len, 1024 * 1024, "Stdout should reach the 1MB cap before kill")
        self.assertLess(actual_output_len, 2 * 1024 * 1024, "Stdout must be capped and not grow to 10M lines")
        self.assertLess(elapsed, 3.0, "Output flooding should trigger rapid process termination")

    def test_2_2_stderr_flooding(self):
        """Verify massive stderr flooding also triggers Output Limit Exceeded without crashing."""
        code = """
        #include <iostream>
        int main() {
            for (int i = 0; i < 100000; ++i) {
                std::cerr << "Flood stderr payload chunk 012345678901234567890123456789\\n";
            }
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "none"}])
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Output Limit Exceeded")
        print(f"       [Output Flood 2.2 Stderr] Handled status: {r0['status']}")

    def test_2_3_null_byte_flooding(self):
        """Verify binary output flooding containing null bytes is handled safely in JSON response."""
        code = """
        #include <iostream>
        int main() {
            for (int i = 0; i < 2000000; ++i) {
                std::cout << '\\0';
            }
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "none"}])
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Output Limit Exceeded")
        print(f"       [Output Flood 2.3 Binary] Handled status: {r0['status']}")

    # =========================================================================
    # REQ 3: Memory Hog / Exhaustion
    # =========================================================================

    def test_3_1_huge_memory_allocation_bad_alloc(self):
        """Submit C++ code requesting astronomical memory (1000 GB); verify handled gracefully."""
        code = """
        #include <iostream>
        #include <new>
        int main() {
            // Request 1000 Gigabytes of heap memory
            char* p = new char[1000000000000ULL];
            p[0] = 'X';
            std::cout << p[0] << std::endl;
            delete[] p;
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "X"}])
        self.assertTrue(res.get("success"))
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Runtime Error")
        self.assertFalse(r0["passed"])
        print(f"       [Memory Hog 3.1 Uncaught] Result: {r0['status']}, Error: {repr(r0['error'])}")

    def test_3_2_caught_bad_alloc(self):
        """Verify C++ catching std::bad_alloc executes gracefully to completion."""
        code = """
        #include <iostream>
        #include <new>
        int main() {
            try {
                char* p = new char[1000000000000ULL];
                (void)p;
            } catch (const std::bad_alloc& e) {
                std::cout << "CAUGHT_BAD_ALLOC" << std::endl;
                return 0;
            }
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "CAUGHT_BAD_ALLOC"}])
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Accepted")
        self.assertTrue(r0["passed"])
        self.assertEqual(r0["score"], 10)
        print(f"       [Memory Hog 3.2 Caught] Result: {r0['status']}, Score: {r0['score']}")

    # =========================================================================
    # REQ 4: Crash Code Verification (Windows NTSTATUS Codes)
    # =========================================================================

    def test_4_1_null_pointer_dereference_segfault(self):
        """Verify null pointer dereference yields Runtime Error with 0xC0000005 (Access Violation)."""
        code = """
        #include <iostream>
        int main() {
            volatile int* p = nullptr;
            *p = 42;
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "42"}])
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Runtime Error")
        self.assertFalse(r0["passed"])
        self.assertIn("0xC0000005", r0["error"])
        self.assertIn("STATUS_ACCESS_VIOLATION", r0["error"])
        print(f"       [Crash 4.1 Segfault] Verified: 0xC0000005 STATUS_ACCESS_VIOLATION")

    def test_4_2_integer_division_by_zero(self):
        """Verify integer division by zero yields Runtime Error with 0xC0000094."""
        code = """
        #include <iostream>
        int main() {
            volatile int a = 10;
            volatile int b = 0;
            volatile int c = a / b;
            std::cout << c;
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "0"}])
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Runtime Error")
        self.assertFalse(r0["passed"])
        self.assertIn("0xC0000094", r0["error"])
        self.assertIn("STATUS_INTEGER_DIVIDE_BY_ZERO", r0["error"])
        print(f"       [Crash 4.2 DivZero] Verified: 0xC0000094 STATUS_INTEGER_DIVIDE_BY_ZERO")

    def test_4_3_stack_overflow_infinite_recursion(self):
        """Verify infinite recursion yields Runtime Error with 0xC00000FD."""
        code = """
        #include <iostream>
        void recurse(int x) {
            volatile char buf[8192];
            buf[0] = (char)x;
            recurse(x + 1);
        }
        int main() {
            recurse(1);
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "0"}])
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Runtime Error")
        self.assertFalse(r0["passed"])
        self.assertIn("0xC00000FD", r0["error"])
        self.assertIn("STATUS_STACK_OVERFLOW", r0["error"])
        print(f"       [Crash 4.3 StackOverflow] Verified: 0xC00000FD STATUS_STACK_OVERFLOW")

    def test_4_4_explicit_abort_call(self):
        """Verify std::abort() is mapped to Runtime Error."""
        code = """
        #include <cstdlib>
        int main() {
            std::abort();
            return 0;
        }
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "0"}])
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Runtime Error")
        print(f"       [Crash 4.4 Abort] Handled as Runtime Error")

    # =========================================================================
    # REQ 5: Filesystem Escape Attempt & Workspace Integrity
    # =========================================================================

    def test_5_1_relative_escape_attempt(self):
        """Submit C++ code attempting std::ofstream('../../escaped_test.txt'). Verify server safety."""
        test_file_name = f"escaped_challenger2_{int(time.time())}.txt"
        code = f"""
        #include <iostream>
        #include <fstream>
        int main() {{
            std::ofstream f("../../{test_file_name}");
            if (f.is_open()) {{
                f << "Pawned";
                f.close();
            }}
            std::cout << "Done" << std::endl;
            return 0;
        }}
        """
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "Done"}])
        self.assertTrue(res.get("success"))
        r0 = res["results"][0]
        self.assertEqual(r0["status"], "Accepted")

        # Verify host workspace integrity: No such file should exist in d:\c++ or d:\c++\quiz_game
        self.assertFalse((ROOT_DIR / test_file_name).exists(), "Host root workspace must NOT be written to!")
        self.assertFalse((QUIZ_GAME_DIR / test_file_name).exists(), "quiz_game dir must NOT be written to!")
        print(f"       [FS Escape 5.1 Relative] Workspace integrity preserved. No file created in d:\\c++")

    def test_5_2_local_sandbox_temp_files_cleaned(self):
        """Verify files created inside the local sandbox directory are completely removed upon exit."""
        code = """
        #include <iostream>
        #include <fstream>
        int main() {
            for (int i = 0; i < 50; ++i) {
                std::ofstream f("temp_junk_" + std::to_string(i) + ".bin");
                f << "junk data for cleanup verification";
                f.close();
            }
            std::cout << "FILES_CREATED" << std::endl;
            return 0;
        }
        """
        sandboxes_before = count_temp_sandbox_dirs()
        res = send_evaluate_request(code, [{"id": 1, "input": "", "expectedOutput": "FILES_CREATED"}])
        self.assertTrue(res.get("success"))
        self.assertEqual(res["results"][0]["status"], "Accepted")

        time.sleep(0.3)
        sandboxes_after = count_temp_sandbox_dirs()
        self.assertLessEqual(len(sandboxes_after), len(sandboxes_before), "Sandbox and all generated files must be deleted")
        print(f"       [FS Escape 5.2 Sandbox Cleanup] 50 internal temp files removed cleanly with sandbox")

    # =========================================================================
    # REQ 6: Temporary Directory Cleanup & Orphaned Binary Detection
    # =========================================================================

    def test_6_1_cleanup_across_varied_outcomes(self):
        """Verify that after various outcomes (Accepted, WA, CE, TLE, RE), no quiz_eval_* folder is left behind."""
        test_matrix = [
            ("Accepted", "#include <iostream>\nint main(){ std::cout<<42; return 0; }", "42"),
            ("Wrong Answer", "#include <iostream>\nint main(){ std::cout<<99; return 0; }", "42"),
            ("Compilation Error", "#include <iostream>\nint main(){ broken syntax; }", "42"),
            ("Runtime Error", "#include <iostream>\nint main(){ volatile int* p = 0; *p = 1; }", "42"),
            ("TLE", "#include <iostream>\nint main(){ while(1); }", "42"),
        ]

        for label, src, exp in test_matrix:
            sandboxes_before = count_temp_sandbox_dirs()
            res = send_evaluate_request(src, [{"id": 1, "input": "", "expectedOutput": exp}])
            self.assertTrue(res.get("success"))

            time.sleep(0.3)
            sandboxes_after = count_temp_sandbox_dirs()
            self.assertLessEqual(
                len(sandboxes_after), len(sandboxes_before),
                f"Outcome '{label}' must not leak sandbox directory!"
            )
            print(f"       [Cleanup 6.1 Matrix] Outcome: {label:<18} -> Sandbox cleanly removed")

    def test_6_2_no_orphaned_executables_in_tasklist(self):
        """Verify that tasklist has zero running solution.exe binaries after all tests."""
        pids = get_running_process_pids("solution.exe")
        self.assertEqual(len(pids), 0, f"Zero solution.exe should be active in OS tasklist. Found: {pids}")
        print(f"       [Cleanup 6.2 OS Process List] Zero solution.exe instances detected.")

    # =========================================================================
    # ADV: Additional Adversarial Vectors (Payload Size, Traversal, Concurrency)
    # =========================================================================

    def test_7_1_payload_too_large_rejection(self):
        """Verify payloads exceeding 10MB are rejected (HTTP 413 or connection drop) without crashing server."""
        huge_code = "// " + ("A" * (11 * 1024 * 1024)) + "\nint main(){ return 0; }"
        payload = json.dumps({"sourceCode": huge_code, "testCases": [{"id": 1, "input": "", "expectedOutput": ""}]}).encode("utf-8")

        req = urllib.request.Request(
            f"{SERVER_URL}/api/evaluate",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        rejected = False
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                self.fail("Expected rejection, got " + str(resp.status))
        except urllib.error.HTTPError as err:
            self.assertEqual(err.code, 413, "Should reject >10MB payload with HTTP 413")
            rejected = True
            print(f"       [Adversarial 7.1 Payload >10MB] Rejected with HTTP 413")
        except (ConnectionResetError, urllib.error.URLError) as net_err:
            # Server intentionally aborted connection to protect socket buffer
            rejected = True
            print(f"       [Adversarial 7.1 Payload >10MB] Socket connection dropped cleanly (DOS guard)")

        self.assertTrue(rejected, "Oversized request must be rejected")

        # Verify server remains alive and responsive
        health_req = urllib.request.Request(f"{SERVER_URL}/api/health")
        with urllib.request.urlopen(health_req, timeout=2.0) as h_resp:
            self.assertEqual(h_resp.status, 200, "Server must remain healthy after payload flood")
            print(f"       [Adversarial 7.1 Liveness] Server healthy and operational after 11MB payload")

    def test_7_2_malformed_json_body(self):
        """Verify malformed JSON syntax is rejected with HTTP 400."""
        req = urllib.request.Request(
            f"{SERVER_URL}/api/evaluate",
            data=b'{"sourceCode": "int main(){", broken json syntax...',
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                self.fail("Expected HTTP 400, got " + str(resp.status))
        except urllib.error.HTTPError as err:
            self.assertEqual(err.code, 400, "Should reject invalid JSON syntax with HTTP 400")
            print(f"       [Adversarial 7.2 Bad JSON] Rejected with HTTP {err.code}")

    def test_7_3_static_traversal_attempts(self):
        """Verify static file traversal attempts (/.. /%2e%2e) return HTTP 403 Forbidden."""
        traversal_urls = [
            f"{SERVER_URL}/../server.js",
            f"{SERVER_URL}/..%2fserver.js",
            f"{SERVER_URL}/%2e%2e/server.js",
            f"{SERVER_URL}/..%2f..%2fwindows%2fwin.ini",
        ]
        for url in traversal_urls:
            try:
                with urllib.request.urlopen(url, timeout=3) as resp:
                    self.fail(f"Path traversal {url} should not return HTTP {resp.status}")
            except urllib.error.HTTPError as err:
                self.assertEqual(err.code, 403, f"Traversal {url} must return HTTP 403")
        print(f"       [Adversarial 7.3 Traversal] All 4 traversal vectors blocked with HTTP 403")


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("  Milestone 2 Challenger 2: Adversarial Stress Test Suite")
    print("=" * 80 + "\n")
    unittest.main(verbosity=2)
