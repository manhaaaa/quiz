#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
  Automated Verification Test Suite: C++ Execution & Evaluation Server
================================================================================
  Target: D:\\c++\\quiz_game\\server.js
  Tests:
    1. test_01_health_check
    2. test_02_evaluate_missing_source_code
    3. test_03_compilation_error
    4. test_04_correct_solution_accepted
    5. test_05_wrong_answer
    6. test_06_runtime_error_division_by_zero
    7. test_07_runtime_error_segfault
    8. test_08_time_limit_exceeded_infinite_loop
    9. test_09_windows_crlf_vs_unix_lf_normalization
    10. test_10_full_evaluation_with_problem_id
    11. test_11_static_file_serving_and_traversal_protection
================================================================================
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error
import subprocess
import unittest
from pathlib import Path

# Base paths
QUIZ_GAME_DIR = Path(__file__).resolve().parent
ROOT_DIR = QUIZ_GAME_DIR.parent
SERVER_JS_PATH = QUIZ_GAME_DIR / "server.js"
CODING_PROBLEMS_JSON_PATH = QUIZ_GAME_DIR / "coding_problems.json"
QUESTIONS_JSON_PATH = QUIZ_GAME_DIR / "questions.json"

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 3000
SERVER_BASE_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"


class ServerProcessManager:
    """Manages the background Node.js server lifecycle with Windows process tree cleanup."""
    process = None
    already_running = False

    @classmethod
    def is_server_healthy(cls) -> bool:
        """Checks if the server is already active and responding to /api/health."""
        try:
            req = urllib.request.Request(f"{SERVER_BASE_URL}/api/health", headers={"User-Agent": "TestRunner"})
            with urllib.request.urlopen(req, timeout=1.0) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8"))
                    return data.get("status") == "ok"
        except Exception:
            return False
        return False

    @classmethod
    def start_server(cls):
        """Starts server.js if not already running."""
        if cls.is_server_healthy():
            cls.already_running = True
            print(f"[TestServer] Attached to already running server at {SERVER_BASE_URL}")
            return

        if not SERVER_JS_PATH.exists():
            raise FileNotFoundError(f"server.js does not exist at {SERVER_JS_PATH}")

        print(f"[TestServer] Launching background server: node {SERVER_JS_PATH}")
        cls.process = subprocess.Popen(
            ["node", str(SERVER_JS_PATH)],
            cwd=str(QUIZ_GAME_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        start_time = time.time()
        while time.time() - start_time < 5.0:
            if cls.is_server_healthy():
                print(f"[TestServer] Server is ready after {time.time() - start_time:.2f}s")
                return
            time.sleep(0.1)

        cls.stop_server()
        raise TimeoutError("Evaluation server failed to become healthy within 5.0 seconds")

    @classmethod
    def stop_server(cls):
        """Cleanly terminates the server process tree on Windows."""
        if cls.already_running:
            return

        if cls.process:
            pid = cls.process.pid
            print(f"[TestServer] Stopping server process (PID: {pid})...")
            if sys.platform == "win32":
                try:
                    subprocess.run(["taskkill", "/F", "/T", "/PID", str(pid)], capture_output=True)
                except Exception as e:
                    print(f"[TestServer] Warning during taskkill: {e}")
            else:
                try:
                    cls.process.kill()
                except Exception:
                    pass

            try:
                cls.process.wait(timeout=2.0)
            except subprocess.TimeoutExpired:
                pass

            if cls.process.stdout:
                try:
                    cls.process.stdout.close()
                except Exception:
                    pass
            if cls.process.stderr:
                try:
                    cls.process.stderr.close()
                except Exception:
                    pass

            cls.process = None


def make_api_request(endpoint: str, method: str = "GET", payload: dict = None) -> tuple:
    """
    Executes an HTTP request to the evaluation server.
    Returns (status_code: int, response_json: dict or None, raw_body: str).
    """
    url = f"{SERVER_BASE_URL}{endpoint}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {"User-Agent": "TestRunner"}
    if data:
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15.0) as resp:
            status = resp.status
            raw_body = resp.read().decode("utf-8")
            try:
                json_data = json.loads(raw_body)
            except json.JSONDecodeError:
                json_data = None
            return status, json_data, raw_body
    except urllib.error.HTTPError as e:
        raw_body = e.read().decode("utf-8") if e.fp else ""
        try:
            json_data = json.loads(raw_body)
        except json.JSONDecodeError:
            json_data = None
        return e.code, json_data, raw_body


class TestExecutionServer(unittest.TestCase):
    """Full functional and edge-case test suite for server.js."""

    @classmethod
    def setUpClass(cls):
        ServerProcessManager.start_server()

    @classmethod
    def tearDownClass(cls):
        ServerProcessManager.stop_server()

    def test_01_health_check(self):
        """GET /api/health returns HTTP 200 with g++ toolchain information."""
        status, data, _ = make_api_request("/api/health")
        self.assertEqual(status, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data.get("status"), "ok")
        self.assertIn("g++", data.get("compiler", "").lower())
        self.assertEqual(data.get("platform"), "win32" if sys.platform == "win32" else sys.platform)
        self.assertTrue(bool(data.get("version")))
        self.assertTrue(bool(data.get("timestamp")))

    def test_02_evaluate_missing_source_code(self):
        """POST /api/evaluate returns HTTP 400 when source code or test cases are missing."""
        # Empty payload
        status1, data1, _ = make_api_request("/api/evaluate", method="POST", payload={})
        self.assertEqual(status1, 400)
        self.assertIn("source code", data1.get("error", "").lower())

        # Whitespace only
        status2, data2, _ = make_api_request("/api/evaluate", method="POST", payload={"sourceCode": "   "})
        self.assertEqual(status2, 400)
        self.assertIn("source code", data2.get("error", "").lower())

        # Valid sourceCode but no testCases and missing/invalid problemId
        status3, data3, _ = make_api_request("/api/evaluate", method="POST", payload={
            "sourceCode": "int main() { return 0; }",
            "problemId": "non_existent_problem_xyz"
        })
        self.assertEqual(status3, 400)
        self.assertTrue("test cases" in data3.get("error", "").lower() or "problemid" in data3.get("error", "").lower())

    def test_03_compilation_error(self):
        """Submitting syntax errors returns compilation.success=False and score 0."""
        cpp_code = """
#include <iostream>
int main() {
    this_undefined_identifier_syntax_error = 42;
    return 0;
}
"""
        payload = {
            "sourceCode": cpp_code,
            "testCases": [
                {"id": 1, "input": "1\n", "expectedOutput": "1\n"}
            ]
        }
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        self.assertEqual(status, 200)
        self.assertTrue(data.get("success"))
        self.assertFalse(data.get("compiled"))
        comp = data.get("compilation", {})
        self.assertFalse(comp.get("success"))
        self.assertIn("this_undefined_identifier_syntax_error", comp.get("output", ""))
        self.assertEqual(data.get("score"), 0)
        self.assertEqual(data.get("passedTestCases"), 0)
        self.assertEqual(len(data.get("results", [])), 0)

    def test_04_correct_solution_accepted(self):
        """Submitting correct C++ solution passes all 10 test cases with score 100."""
        cpp_code = """
#include <iostream>
using namespace std;
int main() {
    long long x;
    while (cin >> x) {
        cout << (x * 2) << "\\n";
    }
    return 0;
}
"""
        test_cases = [
            {"id": i, "input": f"{i}\n", "expectedOutput": f"{i * 2}\n"}
            for i in range(1, 11)
        ]
        payload = {
            "sourceCode": cpp_code,
            "testCases": test_cases
        }
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        self.assertEqual(status, 200)
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("compiled"))
        self.assertEqual(data.get("score"), 100)
        self.assertEqual(data.get("passedTestCases"), 10)
        self.assertEqual(data.get("totalTestCases"), 10)

        results = data.get("results", [])
        self.assertEqual(len(results), 10)
        for res in results:
            self.assertEqual(res.get("status"), "Accepted")
            self.assertTrue(res.get("passed"))
            self.assertEqual(res.get("score"), 10)
            self.assertIsNone(res.get("error"))

    def test_05_wrong_answer(self):
        """Submitting incorrect solution results in Wrong Answer and score 0."""
        cpp_code = """
#include <iostream>
using namespace std;
int main() {
    cout << "completely_wrong_answer\\n";
    return 0;
}
"""
        test_cases = [
            {"id": i, "input": f"{i}\n", "expectedOutput": f"{i}\n"}
            for i in range(1, 11)
        ]
        payload = {
            "sourceCode": cpp_code,
            "testCases": test_cases
        }
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        self.assertEqual(status, 200)
        self.assertTrue(data.get("compiled"))
        self.assertEqual(data.get("score"), 0)
        self.assertEqual(data.get("passedTestCases"), 0)

        for res in data.get("results", []):
            self.assertEqual(res.get("status"), "Wrong Answer")
            self.assertFalse(res.get("passed"))
            self.assertEqual(res.get("score"), 0)

    def test_06_runtime_error_division_by_zero(self):
        """Division by zero triggers Runtime Error with 0xC0000094 diagnostic."""
        cpp_code = """
#include <iostream>
using namespace std;
int main() {
    volatile int a = 0;
    volatile int b = 42 / a;
    cout << b << endl;
    return 0;
}
"""
        payload = {
            "sourceCode": cpp_code,
            "testCases": [
                {"id": 1, "input": "0\n", "expectedOutput": "0\n"}
            ]
        }
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        self.assertEqual(status, 200)
        results = data.get("results", [])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get("status"), "Runtime Error")
        self.assertFalse(results[0].get("passed"))
        self.assertEqual(results[0].get("score"), 0)

        err_msg = results[0].get("error", "").lower()
        self.assertTrue(
            "c0000094" in err_msg or "divide by zero" in err_msg or "chia cho 0" in err_msg,
            f"Expected divide by zero diagnostic, got: {results[0].get('error')}"
        )

    def test_07_runtime_error_segfault(self):
        """Null pointer dereference triggers Runtime Error with 0xC0000005 diagnostic."""
        cpp_code = """
#include <iostream>
int main() {
    int* ptr = nullptr;
    *ptr = 12345;
    return 0;
}
"""
        payload = {
            "sourceCode": cpp_code,
            "testCases": [
                {"id": 1, "input": "1\n", "expectedOutput": "1\n"}
            ]
        }
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        self.assertEqual(status, 200)
        results = data.get("results", [])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get("status"), "Runtime Error")
        self.assertFalse(results[0].get("passed"))
        self.assertEqual(results[0].get("score"), 0)

        err_msg = results[0].get("error", "").lower()
        self.assertTrue(
            "c0000005" in err_msg or "access violation" in err_msg or "segmentation" in err_msg or "truy cập bộ nhớ" in err_msg,
            f"Expected access violation diagnostic, got: {results[0].get('error')}"
        )

    def test_08_time_limit_exceeded_infinite_loop(self):
        """Infinite loop triggers Time Limit Exceeded killed within ~2.0s - 3.5s."""
        cpp_code = """
#include <iostream>
int main() {
    volatile long long counter = 0;
    while (true) {
        counter++;
    }
    return 0;
}
"""
        payload = {
            "sourceCode": cpp_code,
            "testCases": [
                {"id": 1, "input": "1\n", "expectedOutput": "1\n"}
            ]
        }
        start_time = time.time()
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        elapsed = time.time() - start_time

        self.assertEqual(status, 200)
        self.assertGreaterEqual(elapsed, 2.0, "Should enforce at least 2.0s execution timeout")
        self.assertLess(elapsed, 4.0, "Process tree must be forcefully terminated without hanging")

        results = data.get("results", [])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get("status"), "Time Limit Exceeded")
        self.assertFalse(results[0].get("passed"))
        self.assertEqual(results[0].get("score"), 0)

    def test_09_windows_crlf_vs_unix_lf_normalization(self):
        """Code outputting CRLF matches Unix LF expected output cleanly."""
        cpp_code = """
#include <iostream>
int main() {
    std::cout << "100 200  \\r\\n";
    return 0;
}
"""
        payload = {
            "sourceCode": cpp_code,
            "testCases": [
                {"id": 1, "input": "", "expectedOutput": "100 200\n"}
            ]
        }
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        self.assertEqual(status, 200)
        results = data.get("results", [])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get("status"), "Accepted")
        self.assertTrue(results[0].get("passed"))
        self.assertEqual(results[0].get("score"), 10)

    def test_10_full_evaluation_with_problem_id(self):
        """Submitting code with problemId loads 10 test cases from problem bank."""
        # Optimal O(N log N) solution for Problem CP01 (Two Sum)
        cpp_code = """
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> a(n);
    unordered_map<long long, vector<int>> pos;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pos[a[i]].push_back(i + 1);
    }

    for (int i = 0; i < n; ++i) {
        long long need = k - a[i];
        auto it = pos.find(need);
        if (it != pos.end()) {
            const auto& vec = it->second;
            auto ub = upper_bound(vec.begin(), vec.end(), i + 1);
            if (ub != vec.end()) {
                cout << (i + 1) << " " << *ub << "\\n";
                return 0;
            }
        }
    }
    cout << "-1\\n";
    return 0;
}
"""
        payload = {
            "problemId": "CP01",
            "sourceCode": cpp_code
        }
        status, data, _ = make_api_request("/api/evaluate", method="POST", payload=payload)
        self.assertEqual(status, 200)
        self.assertTrue(data.get("success"), f"Evaluation error: {data}")
        self.assertTrue(data.get("compiled"))
        self.assertEqual(data.get("score"), 100)
        self.assertEqual(data.get("passedTestCases"), 10)
        self.assertEqual(data.get("totalTestCases"), 10)
        self.assertEqual(len(data.get("results", [])), 10)

    def test_11_static_file_serving_and_traversal_protection(self):
        """Static file serving delivers assets and guards against path traversal."""
        # 1. Serving index.html
        status_root, _, body_root = make_api_request("/")
        self.assertEqual(status_root, 200)
        self.assertIn("<!DOCTYPE html>", body_root)

        # 2. Serving coding_problems.json
        status_bank, data_bank, _ = make_api_request("/coding_problems.json")
        self.assertEqual(status_bank, 200)
        self.assertIsInstance(data_bank, list)
        self.assertGreaterEqual(len(data_bank), 15)

        # 3. Path traversal attack attempt -> 403 Forbidden
        status_traversal, data_traversal, _ = make_api_request("/../../package.json")
        self.assertEqual(status_traversal, 403)
        self.assertTrue("forbidden" in data_traversal.get("error", "").lower() or "traversal" in data_traversal.get("error", "").lower())

        # 4. Non-existent file -> 404 Not Found
        status_404, data_404, _ = make_api_request("/non_existent_file_xyz_987654.txt")
        self.assertEqual(status_404, 404)
        self.assertIn("not found", data_404.get("error", "").lower())


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("  Automated Verification Test Suite: C++ Execution Server")
    print("=" * 80 + "\n")
    unittest.main(verbosity=2)
