#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Empirical Challenger 1 Stress Harness: Milestone 2
Target: d:\\c++\\quiz_game\\server.js
Tests:
  1. Adversarial Path Traversal & Security Boundary
  2. Huge Request Body (>10MB) Handling & Process Liveness
  3. Malformed JSON Syntax & Schema Edge Cases
  4. Concurrency & Isolation Stress (8 parallel evaluations)
  5. Large Asset Streaming (coding_problems.json integrity)
"""

import os
import sys
import json
import time
import socket
import urllib.request
import urllib.error
import http.client
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

QUIZ_GAME_DIR = Path("d:/c++/quiz_game").resolve()
SERVER_JS_PATH = QUIZ_GAME_DIR / "server.js"
CODING_PROBLEMS_JSON = QUIZ_GAME_DIR / "coding_problems.json"
TEST_PORT = 3099
BASE_URL = f"http://127.0.0.1:{TEST_PORT}"

class ServerHarness:
    def __init__(self, port=TEST_PORT):
        self.port = port
        self.proc = None

    def start(self):
        env = os.environ.copy()
        env["PORT"] = str(self.port)
        self.proc = subprocess.Popen(
            ["node", str(SERVER_JS_PATH)],
            cwd=str(QUIZ_GAME_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env
        )
        # Wait for server to become healthy
        start_time = time.time()
        while time.time() - start_time < 6.0:
            try:
                req = urllib.request.Request(f"http://127.0.0.1:{self.port}/api/health")
                with urllib.request.urlopen(req, timeout=1.0) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode("utf-8"))
                        if data.get("status") == "ok":
                            return True
            except Exception:
                time.sleep(0.1)
        raise RuntimeError("Server failed to start within 6 seconds")

    def stop(self):
        if self.proc:
            try:
                subprocess.run(
                    ["taskkill", "/F", "/T", "/PID", str(self.proc.pid)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            except Exception:
                self.proc.kill()
            self.proc = None

def raw_http_get(path, port=TEST_PORT):
    """Raw TCP HTTP GET to prevent urllib from normalizing paths like /../../"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5.0)
    s.connect(("127.0.0.1", port))
    raw_req = f"GET {path} HTTP/1.1\r\nHost: 127.0.0.1:{port}\r\nConnection: close\r\n\r\n"
    s.sendall(raw_req.encode("utf-8"))
    
    response = b""
    while True:
        try:
            chunk = s.recv(4096)
            if not chunk:
                break
            response += chunk
        except socket.timeout:
            break
    s.close()
    
    parts = response.split(b"\r\n\r\n", 1)
    header_part = parts[0].decode("utf-8", errors="replace")
    body_part = parts[1] if len(parts) > 1 else b""
    status_line = header_part.split("\r\n")[0]
    status_code = int(status_line.split()[1]) if len(status_line.split()) > 1 else 0
    return status_code, header_part, body_part

def run_tests():
    harness = ServerHarness(port=TEST_PORT)
    print("=" * 80)
    print("STARTING EMPIRICAL CHALLENGER 1 STRESS SUITE (MILESTONE 2)")
    print(f"Target Server: {SERVER_JS_PATH} on port {TEST_PORT}")
    print("=" * 80)
    
    harness.start()
    results = {}
    
    try:
        # ----------------------------------------------------------------------
        # AREA 1: Adversarial Path Traversal Tests
        # ----------------------------------------------------------------------
        print("\n--- [AREA 1] ADVERSARIAL PATH TRAVERSAL TESTS ---")
        traversal_tests = [
            ("Raw dot-dot win.ini", "/../../windows/win.ini", [403, 404]),
            ("URL encoded dot-dot package.json", "/%2e%2e%2fpackage.json", [403, 404]),
            ("Mixed URL encoded dot-dot questions.json", "/..%2f..%2fquestions.json", [403, 404]),
            ("Null byte with txt extension", "/index.html%00.txt", [403, 404]),
            ("Backslash traversal", "/..%5c..%5cwindows/win.ini", [403, 404]),
            ("Direct backslashes", "/..\\..\\windows\\win.ini", [403, 404]),
            ("Windows drive letter absolute path", "/C:/Windows/win.ini", [403, 404]),
            ("Directory listing on __pycache__", "/__pycache__/", [403, 404]),
            ("Legitimate index.html", "/index.html", [200]),
            ("Legitimate root /", "/", [200]),
            ("Legitimate questions.json", "/questions.json", [200]),
            ("Legitimate coding_problems.json", "/coding_problems.json", [200])
        ]
        
        area1_passes = 0
        area1_details = []
        for name, req_path, allowed_statuses in traversal_tests:
            code, header, body = raw_http_get(req_path, port=TEST_PORT)
            passed = code in allowed_statuses
            # Extra security check: make sure body does not contain any system or secret data
            if code == 200 and "win.ini" in req_path.lower():
                passed = False
            if passed:
                area1_passes += 1
                status_str = "PASS"
            else:
                status_str = "FAIL"
            area1_details.append({
                "test": name,
                "path": req_path,
                "status_code": code,
                "allowed": allowed_statuses,
                "passed": passed
            })
            print(f"  [{status_str}] {name} (path: '{req_path}') -> HTTP {code}")
        
        results["area1_path_traversal"] = {
            "total": len(traversal_tests),
            "passed": area1_passes,
            "details": area1_details
        }

        # ----------------------------------------------------------------------
        # AREA 2: Huge Request Body (>10MB) Stress Test
        # ----------------------------------------------------------------------
        print("\n--- [AREA 2] HUGE REQUEST BODY (>10MB) STRESS TEST ---")
        # 11 MB payload
        payload_11mb = b"x" * (11 * 1024 * 1024)
        print(f"  Generating 11MB ({len(payload_11mb)} bytes) payload...")
        
        req_11mb = urllib.request.Request(
            f"{BASE_URL}/api/evaluate",
            data=payload_11mb,
            headers={"Content-Type": "application/json"}
        )
        
        got_413 = False
        got_conn_reset = False
        server_alive = False
        error_detail = ""
        
        try:
            with urllib.request.urlopen(req_11mb, timeout=10) as resp:
                status = resp.status
                error_detail = f"Unexpected 200 OK with body: {resp.read()[:100]}"
        except urllib.error.HTTPError as e:
            if e.code == 413:
                got_413 = True
                error_detail = f"Received expected HTTP 413: {e.read().decode('utf-8', errors='replace')}"
            else:
                error_detail = f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}"
        except (ConnectionResetError, urllib.error.URLError, http.client.RemoteDisconnected) as e:
            got_conn_reset = True
            error_detail = f"Connection reset / socket aborted by server: {type(e).__name__}: {e}"
        
        # Verify server liveness immediately after huge payload
        try:
            health_req = urllib.request.Request(f"{BASE_URL}/api/health")
            with urllib.request.urlopen(health_req, timeout=2.0) as resp:
                if resp.status == 200:
                    health_data = json.loads(resp.read().decode("utf-8"))
                    server_alive = health_data.get("status") == "ok"
        except Exception as e:
            server_alive = False
            error_detail += f" | Health check failed: {e}"
            
        print(f"  Outcome: got_413={got_413}, got_conn_reset={got_conn_reset}, server_alive={server_alive}")
        print(f"  Detail: {error_detail}")
        
        results["area2_huge_body"] = {
            "payload_size_bytes": len(payload_11mb),
            "got_413": got_413,
            "got_conn_reset": got_conn_reset,
            "server_alive": server_alive,
            "error_detail": error_detail,
            "passed": server_alive and (got_413 or got_conn_reset)
        }

        # ----------------------------------------------------------------------
        # AREA 3: Malformed JSON Syntax & Schema Edge Cases
        # ----------------------------------------------------------------------
        print("\n--- [AREA 3] MALFORMED JSON SYNTAX & SCHEMA EDGE CASES ---")
        malformed_cases = [
            ("Truncated JSON object", b'{"sourceCode": "int main() {', 400),
            ("Trailing comma syntax error", b'{"sourceCode": "int main() {}",}', 400),
            ("Unquoted JavaScript object key", b'{sourceCode: "int main() {}"}', 400),
            ("Raw non-JSON string", b'this is raw text and not json', 400),
            ("JSON primitive string", b'"hello world"', 400),
            ("JSON primitive number", b'12345', 400),
            ("JSON array instead of object", b'["int main() {}"]', 400),
            ("Empty JSON object {}", b'{}', 400),
            ("Missing testCases & invalid problemId", b'{"sourceCode": "int main() {}", "problemId": "INVALID_ID"}', 400),
            ("Whitespace only sourceCode", b'{"sourceCode": "   \n\t  ", "problemId": "CP01"}', 400)
        ]
        
        area3_passes = 0
        area3_details = []
        for name, data, expected_code in malformed_cases:
            req = urllib.request.Request(
                f"{BASE_URL}/api/evaluate",
                data=data,
                headers={"Content-Type": "application/json"}
            )
            try:
                with urllib.request.urlopen(req, timeout=5) as resp:
                    actual_code = resp.status
                    body = resp.read().decode("utf-8", errors="replace")
            except urllib.error.HTTPError as e:
                actual_code = e.code
                body = e.read().decode("utf-8", errors="replace")
            except Exception as e:
                actual_code = -1
                body = str(e)
                
            passed = actual_code == expected_code
            if passed:
                area3_passes += 1
                status_str = "PASS"
            else:
                status_str = "FAIL"
            print(f"  [{status_str}] {name} -> HTTP {actual_code} (expected {expected_code})")
            area3_details.append({
                "test": name,
                "expected": expected_code,
                "actual": actual_code,
                "response_body": body[:120],
                "passed": passed
            })
            
        results["area3_malformed_json"] = {
            "total": len(malformed_cases),
            "passed": area3_passes,
            "details": area3_details
        }

        # ----------------------------------------------------------------------
        # AREA 4: Concurrency & Isolation Stress (8 parallel executions)
        # ----------------------------------------------------------------------
        print("\n--- [AREA 4] CONCURRENCY & ISOLATION STRESS TEST ---")
        # Define 8 diverse evaluation payloads
        concurrent_jobs = [
            {
                "id": "job1_cp01_correct",
                "problemId": "CP01",
                "code": r"""
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    unordered_map<long long, int> seen;
    int best_i = 1e9, best_j = 1e9;
    for (int j = 0; j < n; j++) {
        long long need = k - a[j];
        if (seen.count(need)) {
            int i = seen[need];
            if (i < best_i || (i == best_i && j + 1 < best_j)) {
                best_i = i;
                best_j = j + 1;
            }
        }
        if (!seen.count(a[j])) seen[a[j]] = j + 1;
    }
    if (best_i != 1e9) cout << best_i << " " << best_j << "\n";
    else cout << -1 << "\n";
    return 0;
}
""",
                "expected_compiled": True,
                "expected_min_score": 100
            },
            {
                "id": "job2_cp01_wrong_answer",
                "problemId": "CP01",
                "code": r"""
#include <iostream>
using namespace std;
int main() {
    cout << "999 999\n";
    return 0;
}
""",
                "expected_compiled": True,
                "expected_min_score": 0,
                "expected_max_score": 0
            },
            {
                "id": "job3_div_by_zero",
                "problemId": "CP01",
                "code": r"""
#include <iostream>
using namespace std;
int main() {
    int a = 10;
    int b = 0;
    cout << (a / b) << "\n";
    return 0;
}
""",
                "expected_compiled": True,
                "expected_runtime_error": True,
                "expected_score": 0
            },
            {
                "id": "job4_segfault",
                "problemId": "CP01",
                "code": r"""
#include <iostream>
using namespace std;
int main() {
    int* ptr = nullptr;
    *ptr = 42;
    return 0;
}
""",
                "expected_compiled": True,
                "expected_runtime_error": True,
                "expected_score": 0
            },
            {
                "id": "job5_infinite_loop_tle",
                "problemId": "CP01",
                "code": r"""
#include <iostream>
using namespace std;
int main() {
    volatile int x = 0;
    while (true) {
        x++;
    }
    return 0;
}
""",
                "expected_compiled": True,
                "expected_tle": True,
                "expected_score": 0
            },
            {
                "id": "job6_syntax_error",
                "problemId": "CP01",
                "code": r"""
#include <iostream>
int main() {
    SYNTAX ERROR THIS DOES NOT COMPILE;
}
""",
                "expected_compiled": False,
                "expected_score": 0
            },
            {
                "id": "job7_large_stdout",
                "problemId": "CP01",
                "code": r"""
#include <iostream>
using namespace std;
int main() {
    for (int i = 0; i < 5000; i++) {
        cout << "SPAM_OUTPUT_LINE_" << i << "\n";
    }
    return 0;
}
""",
                "expected_compiled": True,
                "expected_score": 0
            },
            {
                "id": "job8_cp02_correct",
                "problemId": "CP02",
                "code": r"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    long long max_so_far = -1e18, curr_max = -1e18;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        if (i == 0) {
            max_so_far = curr_max = x;
        } else {
            curr_max = max(x, curr_max + x);
            max_so_far = max(max_so_far, curr_max);
        }
    }
    cout << max_so_far << "\n";
    return 0;
}
""",
                "expected_compiled": True,
                "expected_min_score": 100
            }
        ]

        def execute_eval_request(job):
            payload = json.dumps({
                "problemId": job["problemId"],
                "sourceCode": job["code"]
            }).encode("utf-8")
            
            t0 = time.time()
            req = urllib.request.Request(
                f"{BASE_URL}/api/evaluate",
                data=payload,
                headers={"Content-Type": "application/json"}
            )
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    duration = time.time() - t0
                    res_data = json.loads(resp.read().decode("utf-8"))
                    return {"job_id": job["id"], "success": True, "duration": duration, "data": res_data, "job": job}
            except Exception as e:
                duration = time.time() - t0
                return {"job_id": job["id"], "success": False, "duration": duration, "error": str(e), "job": job}

        print(f"  Firing {len(concurrent_jobs)} concurrent compilation and evaluation requests...")
        concurrency_results = []
        t_start = time.time()
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(execute_eval_request, j) for j in concurrent_jobs]
            for f in as_completed(futures):
                concurrency_results.append(f.result())
        t_total = time.time() - t_start
        print(f"  All {len(concurrent_jobs)} requests completed in {t_total:.2f} seconds.")

        area4_passes = 0
        area4_details = []
        for res in concurrency_results:
            job = res["job"]
            job_id = res["job_id"]
            if not res["success"]:
                print(f"  [FAIL] {job_id} encountered exception: {res.get('error')}")
                area4_details.append({"job_id": job_id, "passed": False, "error": res.get("error")})
                continue
            
            data = res["data"]
            compiled = data.get("compiled")
            score = data.get("score")
            results_list = data.get("results", [])
            
            job_pass = True
            mismatch_reasons = []
            
            # Check compilation
            if compiled != job["expected_compiled"]:
                job_pass = False
                mismatch_reasons.append(f"compiled={compiled} != expected {job['expected_compiled']}")
                
            # Check score expectations
            if "expected_min_score" in job and score < job["expected_min_score"]:
                job_pass = False
                mismatch_reasons.append(f"score={score} < min {job['expected_min_score']}")
            if "expected_max_score" in job and score > job["expected_max_score"]:
                job_pass = False
                mismatch_reasons.append(f"score={score} > max {job['expected_max_score']}")
            if "expected_score" in job and score != job["expected_score"]:
                job_pass = False
                mismatch_reasons.append(f"score={score} != expected {job['expected_score']}")
                
            # Check error diagnostics
            if job.get("expected_runtime_error"):
                re_found = any(r.get("status") == "Runtime Error" for r in results_list)
                if not re_found:
                    job_pass = False
                    mismatch_reasons.append("Expected Runtime Error in results but none found")
            if job.get("expected_tle"):
                tle_found = any(r.get("status") == "Time Limit Exceeded" for r in results_list)
                if not tle_found:
                    job_pass = False
                    mismatch_reasons.append("Expected Time Limit Exceeded in results but none found")
                    
            status_str = "PASS" if job_pass else "FAIL"
            if job_pass:
                area4_passes += 1
            print(f"  [{status_str}] {job_id} (duration: {res['duration']:.2f}s, compiled: {compiled}, score: {score})")
            if mismatch_reasons:
                print(f"         Issues: {', '.join(mismatch_reasons)}")
                
            area4_details.append({
                "job_id": job_id,
                "duration_s": round(res["duration"], 2),
                "compiled": compiled,
                "score": score,
                "passed": job_pass,
                "issues": mismatch_reasons
            })

        # Check for orphan sandbox directories in temp
        import tempfile
        tmp_dir = Path(tempfile.gettempdir())
        orphan_sandboxes = list(tmp_dir.glob("quiz_eval_*"))
        print(f"  Sandbox cleanup check: found {len(orphan_sandboxes)} leftover 'quiz_eval_*' folders in temp.")
        
        results["area4_concurrency"] = {
            "total_jobs": len(concurrent_jobs),
            "passed_jobs": area4_passes,
            "total_wall_clock_time_s": round(t_total, 2),
            "orphan_sandboxes_count": len(orphan_sandboxes),
            "details": area4_details
        }

        # ----------------------------------------------------------------------
        # AREA 5: Large Asset Streaming (coding_problems.json)
        # ----------------------------------------------------------------------
        print("\n--- [AREA 5] LARGE ASSET STREAMING (coding_problems.json) ---")
        disk_size = CODING_PROBLEMS_JSON.stat().st_size
        print(f"  On-disk coding_problems.json size: {disk_size} bytes ({disk_size / (1024*1024):.2f} MB)")
        
        # Test 1: GET request
        t0 = time.time()
        req = urllib.request.Request(f"{BASE_URL}/coding_problems.json")
        with urllib.request.urlopen(req, timeout=10) as resp:
            status_code = resp.status
            content_type = resp.headers.get("Content-Type")
            content_length = int(resp.headers.get("Content-Length", 0))
            body_data = resp.read()
            stream_duration = time.time() - t0
            
        received_bytes = len(body_data)
        print(f"  GET response status: {status_code}")
        print(f"  Content-Type header: '{content_type}'")
        print(f"  Content-Length header: {content_length} bytes")
        print(f"  Received payload size: {received_bytes} bytes in {stream_duration*1000:.1f}ms")
        
        # Verify valid JSON
        try:
            parsed_json = json.loads(body_data.decode("utf-8"))
            valid_json = isinstance(parsed_json, list) and len(parsed_json) == 18
            json_error = None
        except Exception as e:
            valid_json = False
            json_error = str(e)
            
        # Test 2: HEAD request
        head_code, head_headers, head_body = raw_http_get("/coding_problems.json", port=TEST_PORT)
        # Check raw HTTP HEAD
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)
        s.connect(("127.0.0.1", TEST_PORT))
        s.sendall(b"HEAD /coding_problems.json HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n")
        head_resp = s.recv(4096).decode("utf-8", errors="replace")
        s.close()
        head_parts = head_resp.split("\r\n\r\n")
        head_status_line = head_parts[0].split("\r\n")[0]
        head_body_len = len(head_parts[1]) if len(head_parts) > 1 else 0
        head_passed = ("200 OK" in head_status_line) and (head_body_len == 0)
        
        area5_passed = (
            status_code == 200 and
            content_type == "application/json; charset=utf-8" and
            content_length == disk_size and
            received_bytes == disk_size and
            valid_json and
            head_passed
        )
        
        print(f"  Valid JSON list of 18 items: {valid_json} (error: {json_error})")
        print(f"  HEAD request check (200 with 0 body bytes): {head_passed}")
        print(f"  [{'PASS' if area5_passed else 'FAIL'}] Large Asset Streaming Overall Verification")
        
        results["area5_large_streaming"] = {
            "status_code": status_code,
            "content_type": content_type,
            "content_length": content_length,
            "disk_size": disk_size,
            "received_bytes": received_bytes,
            "stream_duration_ms": round(stream_duration * 1000, 1),
            "valid_json": valid_json,
            "items_count": len(parsed_json) if valid_json else 0,
            "head_passed": head_passed,
            "passed": area5_passed
        }

    finally:
        print("\nStopping background test server...")
        harness.stop()
        
    print("\n" + "=" * 80)
    print("ALL TESTS COMPLETE — SUMMARY:")
    print(f"  Area 1 (Path Traversal):        {results['area1_path_traversal']['passed']}/{results['area1_path_traversal']['total']} passed")
    print(f"  Area 2 (Huge Body >10MB):       Passed={results['area2_huge_body']['passed']} (conn_reset={results['area2_huge_body']['got_conn_reset']}, alive={results['area2_huge_body']['server_alive']})")
    print(f"  Area 3 (Malformed JSON):        {results['area3_malformed_json']['passed']}/{results['area3_malformed_json']['total']} passed")
    print(f"  Area 4 (Concurrency Stress):    {results['area4_concurrency']['passed_jobs']}/{results['area4_concurrency']['total_jobs']} passed (orphans: {results['area4_concurrency']['orphan_sandboxes_count']})")
    print(f"  Area 5 (Large Asset Streaming): Passed={results['area5_large_streaming']['passed']} ({results['area5_large_streaming']['received_bytes']} bytes in {results['area5_large_streaming']['stream_duration_ms']}ms)")
    print("=" * 80)
    
    # Save results json for report reference
    with open(QUIZ_GAME_DIR / "m2_challenger1_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_tests()
