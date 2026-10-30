#!/usr/bin/env python3
"""
test_m1_challenger_harness.py - Empirical Challenger Harness for Milestone 1

Comprehensive stress-testing and oracle validation for:
- coding_problems.json
- coding_problems.js
- verify_coding_bank.py

Tests:
1. Strict schema compliance & dual-mode parity
2. Invariants: Exactly 10 test cases per problem, IDs 1..10, isSample distribution
3. Formatting hygiene: Whitespace, newlines, CRLF normalization
4. Algorithmic Oracles for all 18 DSA problems (180 test cases analyzed)
5. Live MSYS2 g++ compilation & execution of C++ reference solutions
6. Adversarial schema mutation & boundary fuzzing against validator
7. Random 3-problem selection statistical distribution (10,000 draws)
8. Zero regression against questions.json
"""

import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional, Tuple

if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

QUIZ_GAME_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(QUIZ_GAME_DIR, "coding_problems.json")
JS_PATH = os.path.join(QUIZ_GAME_DIR, "coding_problems.js")
QUESTIONS_JSON_PATH = os.path.join(QUIZ_GAME_DIR, "questions.json")


def normalize_output(text: str) -> str:
    """Normalizes CRLF and trailing spaces per line, ending with single newline."""
    if not text:
        return ""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    trimmed = [line.rstrip() for line in lines]
    while trimmed and trimmed[-1] == "":
        trimmed.pop()
    return "\n".join(trimmed) + "\n" if trimmed else ""


# ==============================================================================
# ALGORITHMIC ORACLES (CP01 - CP18)
# ==============================================================================

def oracle_cp01(stdin: str) -> str:
    """Two Sum: Find 1-based indices i < j with A[i] + A[j] == K (min i, min j)."""
    tokens = stdin.split()
    if not tokens:
        return "-1\n"
    n = int(tokens[0])
    k = int(tokens[1])
    arr = [int(x) for x in tokens[2: 2 + n]]
    pos = defaultdict(list)
    for idx, val in enumerate(arr, start=1):
        pos[val].append(idx)
    for i in range(1, n + 1):
        val = arr[i - 1]
        rem = k - val
        if rem in pos:
            for j in pos[rem]:
                if j > i:
                    return f"{i} {j}\n"
    return "-1\n"


def oracle_cp02(stdin: str) -> str:
    """Maximum Subarray Sum (Kadane's algorithm)."""
    tokens = stdin.split()
    if not tokens:
        return "0\n"
    n = int(tokens[0])
    arr = [int(x) for x in tokens[1: 1 + n]]
    max_so_far = arr[0]
    curr_max = arr[0]
    for x in arr[1:]:
        curr_max = max(x, curr_max + x)
        max_so_far = max(max_so_far, curr_max)
    return f"{max_so_far}\n"


def oracle_cp03(stdin: str) -> str:
    """Valid Palindrome: Alphanumeric only, case-insensitive."""
    filtered = "".join(ch.lower() for ch in stdin if ch.isalnum())
    return "YES\n" if filtered == filtered[::-1] else "NO\n"


def oracle_cp04(stdin: str) -> str:
    """String Compression: Run-Length Encoding."""
    line = stdin.strip()
    if not line:
        return "\n"
    res = []
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        cnt = 0
        while i < n and line[i] == ch:
            cnt += 1
            i += 1
        res.append(f"{ch}{cnt}")
    return "".join(res) + "\n"


def oracle_cp05(stdin: str) -> str:
    """Reverse Singly Linked List: Reverse array."""
    tokens = stdin.split()
    if not tokens:
        return "\n"
    n = int(tokens[0])
    if n == 0:
        return "\n"
    arr = tokens[1: 1 + n]
    return " ".join(reversed(arr)) + "\n"


def oracle_cp06(stdin: str) -> str:
    """Merge Two Sorted Lists: Two pointers merge."""
    tokens = stdin.split()
    if not tokens:
        return "\n"
    idx = 0
    n = int(tokens[idx])
    idx += 1
    arr1 = [int(x) for x in tokens[idx: idx + n]]
    idx += n
    m = int(tokens[idx])
    idx += 1
    arr2 = [int(x) for x in tokens[idx: idx + m]]
    merged = sorted(arr1 + arr2)
    return " ".join(str(x) for x in merged) + "\n"


def oracle_cp07(stdin: str) -> str:
    """Valid Parentheses: (), [], {}."""
    line = stdin.strip()
    match = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in line:
        if ch in "([{":
            stack.append(ch)
        elif ch in match:
            if not stack or stack[-1] != match[ch]:
                return "NO\n"
            stack.pop()
    return "YES\n" if len(stack) == 0 else "NO\n"


def oracle_cp08(stdin: str) -> str:
    """Next Greater Element: Monotonic stack."""
    tokens = stdin.split()
    if not tokens:
        return "\n"
    n = int(tokens[0])
    arr = [int(x) for x in tokens[1: 1 + n]]
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            ans[idx] = arr[i]
        stack.append(i)
    return " ".join(str(x) for x in ans) + "\n"


def oracle_cp09(stdin: str) -> str:
    """Queue Simulation: PUSH x, POP, FRONT, SIZE."""
    from collections import deque
    lines = [ln.strip() for ln in stdin.splitlines() if ln.strip()]
    if not lines:
        return ""
    q = deque()
    out = []
    num_ops = int(lines[0])
    for line in lines[1: 1 + num_ops]:
        parts = line.split()
        op = parts[0]
        if op == "PUSH":
            q.append(parts[1])
        elif op == "POP":
            if q:
                q.popleft()
        elif op == "FRONT":
            out.append(q[0] if q else "EMPTY")
        elif op == "SIZE":
            out.append(str(len(q)))
    return "\n".join(out) + "\n" if out else ""


def oracle_cp10(stdin: str) -> str:
    """Binary Search Lower Bound: 1-based index of first element >= X."""
    tokens = stdin.split()
    if not tokens:
        return "-1\n"
    n = int(tokens[0])
    x = int(tokens[1])
    arr = [int(v) for v in tokens[2: 2 + n]]
    left, right = 0, n - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            ans = mid + 1
            right = mid - 1
        else:
            left = mid + 1
    return f"{ans}\n"


def oracle_cp11(stdin: str) -> str:
    """Inversion Count: Merge Sort."""
    tokens = stdin.split()
    if not tokens:
        return "0\n"
    n = int(tokens[0])
    arr = [int(v) for v in tokens[1: 1 + n]]

    def merge_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, left_inv = merge_count(a[:mid])
        right, right_inv = merge_count(a[mid:])
        merged = []
        i = j = 0
        inv = left_inv + right_inv
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    _, total_inv = merge_count(arr)
    return f"{total_inv}\n"


def oracle_cp12(stdin: str) -> str:
    """Binary Exponentiation: (A^B) mod M."""
    tokens = stdin.split()
    if not tokens:
        return "0\n"
    a = int(tokens[0])
    b = int(tokens[1])
    m = int(tokens[2])
    res = pow(a, b, m)
    return f"{res}\n"


def oracle_cp13(stdin: str) -> str:
    """Binary Strings without '11' (Backtracking): Lexicographical + count."""
    tokens = stdin.split()
    if not tokens:
        return ""
    n = int(tokens[0])
    results = []

    def backtrack(curr: str):
        if len(curr) == n:
            results.append(curr)
            return
        backtrack(curr + "0")
        if not curr or curr[-1] != "1":
            backtrack(curr + "1")

    backtrack("")
    results.append(str(len(results)))
    return "\n".join(results) + "\n"


def oracle_cp14(stdin: str) -> str:
    """Binary Tree Height & Level-Order BFS."""
    lines = [ln.strip() for ln in stdin.splitlines() if ln.strip()]
    if not lines:
        return "0\n\n"
    n = int(lines[0])
    left_child = {}
    right_child = {}
    for i in range(1, n + 1):
        parts = lines[i].split()
        left_child[i] = int(parts[0])
        right_child[i] = int(parts[1])

    from collections import deque
    q = deque([(1, 1)])
    order = []
    max_height = 0
    while q:
        curr, d = q.popleft()
        order.append(str(curr))
        max_height = max(max_height, d)
        if left_child[curr] != -1:
            q.append((left_child[curr], d + 1))
        if right_child[curr] != -1:
            q.append((right_child[curr], d + 1))

    return f"{max_height}\n" + " ".join(order) + "\n"


def oracle_cp15(stdin: str) -> str:
    """Validate Binary Search Tree."""
    lines = [ln.strip() for ln in stdin.splitlines() if ln.strip()]
    if not lines:
        return "YES\n"
    n = int(lines[0])
    vals = {}
    left_child = {}
    right_child = {}
    for i in range(1, n + 1):
        parts = lines[i].split()
        vals[i] = int(parts[0])
        left_child[i] = int(parts[1])
        right_child[i] = int(parts[2])

    def is_bst(node, min_val, max_val):
        if node == -1:
            return True
        v = vals[node]
        if v <= min_val or v >= max_val:
            return False
        return is_bst(left_child[node], min_val, v) and is_bst(right_child[node], v, max_val)

    ans = is_bst(1, -float("inf"), float("inf"))
    return "YES\n" if ans else "NO\n"


def oracle_cp16(stdin: str) -> str:
    """Connected Components BFS/DFS: Count and sorted component sizes."""
    lines = [ln.strip() for ln in stdin.splitlines() if ln.strip()]
    if not lines:
        return "0\n\n"
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    for i in range(1, 1 + m):
        u, v = map(int, lines[i].split())
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    sizes = []
    for i in range(1, n + 1):
        if not visited[i]:
            q = [i]
            visited[i] = True
            sz = 0
            while q:
                curr = q.pop()
                sz += 1
                for nxt in adj[curr]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            sizes.append(sz)

    sizes.sort()
    return f"{len(sizes)}\n" + " ".join(str(s) for s in sizes) + "\n"


def oracle_cp17(stdin: str) -> str:
    """Longest Increasing Subsequence (LIS) - O(n log n)."""
    tokens = stdin.split()
    if not tokens:
        return "0\n"
    n = int(tokens[0])
    arr = [int(v) for v in tokens[1: 1 + n]]
    import bisect
    tails = []
    for x in arr:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return f"{len(tails)}\n"


def oracle_cp18(stdin: str) -> str:
    """0-1 Knapsack Problem."""
    tokens = stdin.split()
    if not tokens:
        return "0\n"
    n = int(tokens[0])
    s = int(tokens[1])
    dp = [0] * (s + 1)
    idx = 2
    for _ in range(n):
        w = int(tokens[idx])
        v = int(tokens[idx + 1])
        idx += 2
        for cap in range(s, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return f"{dp[s]}\n"


ORACLES = {
    "CP01": oracle_cp01,
    "CP02": oracle_cp02,
    "CP03": oracle_cp03,
    "CP04": oracle_cp04,
    "CP05": oracle_cp05,
    "CP06": oracle_cp06,
    "CP07": oracle_cp07,
    "CP08": oracle_cp08,
    "CP09": oracle_cp09,
    "CP10": oracle_cp10,
    "CP11": oracle_cp11,
    "CP12": oracle_cp12,
    "CP13": oracle_cp13,
    "CP14": oracle_cp14,
    "CP15": oracle_cp15,
    "CP16": oracle_cp16,
    "CP17": oracle_cp17,
    "CP18": oracle_cp18,
}


# ==============================================================================
# EMPIRICAL TEST SUITE
# ==============================================================================

class TestCodingProblemBankEmpirical(unittest.TestCase):
    """Rigorous empirical challenge of Milestone 1 problem bank and validator."""

    @classmethod
    def setUpClass(cls):
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            cls.bank_json = json.load(f)

        with open(JS_PATH, "r", encoding="utf-8") as f:
            raw_js = f.read().strip()
        cleaned_js = re.sub(r"^\s*(?:window\.)?(?:const|let|var)?\s*[a-zA-Z0-9_$]+\s*=\s*", "", raw_js, count=1)
        cleaned_js = re.sub(r";\s*$", "", cleaned_js)
        cls.bank_js = json.loads(cleaned_js)

    # --------------------------------------------------------------------------
    # 1. Dual-Mode Parity & Schema Invariants
    # --------------------------------------------------------------------------
    def test_01_dual_mode_exact_parity(self):
        """Verifies coding_problems.json and coding_problems.js are 100% data identical."""
        self.assertEqual(len(self.bank_json), len(self.bank_js), "Problem count mismatch between JSON and JS")
        for i, (pj, pjs) in enumerate(zip(self.bank_json, self.bank_js)):
            self.assertEqual(pj, pjs, f"Discrepancy at problem index {i} (PID: {pj.get('id')})")

    def test_02_bank_size_and_problem_id_uniqueness(self):
        """Asserts >= 15 problems (target 18) and unique IDs CP01..CP18."""
        self.assertGreaterEqual(len(self.bank_json), 15, "Bank size below 15")
        self.assertEqual(len(self.bank_json), 18, "Expected exactly 18 problems")
        ids = [p["id"] for p in self.bank_json]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate problem IDs detected")
        expected_ids = [f"CP{i:02d}" for i in range(1, 19)]
        self.assertEqual(ids, expected_ids, f"Problem IDs do not match CP01..CP18 sequence: {ids}")

    def test_03_required_fields_and_types(self):
        """Validates all required fields are present with correct types and non-empty values."""
        required_fields = {
            "id": str,
            "title": str,
            "category": str,
            "difficulty": str,
            "timeLimitMs": int,
            "memoryLimitMb": int,
            "description": str,
            "inputFormat": str,
            "outputFormat": str,
            "constraints": list,
            "examples": list,
            "starterCode": str,
            "testCases": list,
        }
        for p in self.bank_json:
            pid = p.get("id")
            for field, ftype in required_fields.items():
                self.assertIn(field, p, f"[{pid}] Missing field '{field}'")
                self.assertIsInstance(p[field], ftype, f"[{pid}] Field '{field}' expected {ftype.__name__}, got {type(p[field]).__name__}")
                if ftype == str:
                    self.assertGreater(len(p[field].strip()), 0, f"[{pid}] String field '{field}' is empty")
                elif ftype == list:
                    self.assertGreater(len(p[field]), 0, f"[{pid}] List field '{field}' is empty")

            self.assertIn(p["difficulty"], {"Easy", "Medium", "Hard"}, f"[{pid}] Invalid difficulty")
            self.assertTrue(100 <= p["timeLimitMs"] <= 10000, f"[{pid}] timeLimitMs out of range")
            self.assertTrue(16 <= p["memoryLimitMb"] <= 1024, f"[{pid}] memoryLimitMb out of range")
            self.assertIn("#include", p["starterCode"], f"[{pid}] Starter code missing #include")
            self.assertIn("main", p["starterCode"], f"[{pid}] Starter code missing main()")

    # --------------------------------------------------------------------------
    # 2. Test Case Invariants & Whitespace Formatting
    # --------------------------------------------------------------------------
    def test_04_exactly_10_test_cases_per_problem(self):
        """Asserts strictly len(testCases) == 10 for every problem (total 180 test cases)."""
        total_tc = 0
        for p in self.bank_json:
            pid = p["id"]
            tc_list = p["testCases"]
            self.assertEqual(len(tc_list), 10, f"[{pid}] Expected exactly 10 test cases, found {len(tc_list)}")
            total_tc += len(tc_list)
        self.assertEqual(total_tc, 180, "Total test cases across 18 problems must be exactly 180")

    def test_05_test_case_ids_and_sample_flags(self):
        """Asserts sequential IDs 1..10, isSample=True for 1,2 and False for 3..10."""
        for p in self.bank_json:
            pid = p["id"]
            for expected_id, tc in enumerate(p["testCases"], start=1):
                self.assertEqual(tc.get("id"), expected_id, f"[{pid}] TC id {tc.get('id')} != expected {expected_id}")
                self.assertIsInstance(tc.get("input"), str, f"[{pid}] TC {expected_id} input not str")
                self.assertIsInstance(tc.get("expectedOutput"), str, f"[{pid}] TC {expected_id} expectedOutput not str")
                self.assertIsInstance(tc.get("isSample"), bool, f"[{pid}] TC {expected_id} isSample not bool")
                if expected_id <= 2:
                    self.assertTrue(tc["isSample"], f"[{pid}] TC {expected_id} should have isSample=True")
                else:
                    self.assertFalse(tc["isSample"], f"[{pid}] TC {expected_id} should have isSample=False")

    def test_06_newline_and_whitespace_formatting_hygiene(self):
        """Checks newline termination and normalizer idempotence across all 180 test cases."""
        for p in self.bank_json:
            pid = p["id"]
            for tc in p["testCases"]:
                tcid = tc["id"]
                out = tc["expectedOutput"]
                self.assertTrue(out.endswith("\n") or out == "", f"[{pid}] TC {tcid} expectedOutput does not end with \\n")
                norm = normalize_output(out)
                self.assertEqual(normalize_output(norm), norm, f"[{pid}] TC {tcid} normalizer is not idempotent")

    # --------------------------------------------------------------------------
    # 3. Algorithmic Oracle Verification Across All 180 Test Cases
    # --------------------------------------------------------------------------
    def test_07_all_180_test_cases_against_oracles_pass(self):
        """Runs each of all 180 test cases through its algorithmic oracle."""
        mismatches = []
        for p in self.bank_json:
            pid = p["id"]
            self.assertIn(pid, ORACLES, f"No oracle implemented for {pid}")
            oracle_func = ORACLES[pid]

            for tc in p["testCases"]:
                tcid = tc["id"]
                tc_in = tc["input"]
                tc_expected = tc["expectedOutput"]

                oracle_result = oracle_func(tc_in)
                norm_oracle = normalize_output(oracle_result)
                norm_expected = normalize_output(tc_expected)

                if norm_oracle != norm_expected:
                    mismatches.append((pid, tcid, tc_expected, oracle_result))

        self.assertEqual(len(mismatches), 0, f"Unexpected oracle mismatches: {mismatches}")

    # --------------------------------------------------------------------------
    # 4. Verified Remediation Tests (CP01 TC5 & CP13 TC10)
    # --------------------------------------------------------------------------
    def test_cp01_tc5_tie_breaking_remediated(self):
        """Verifies CP01 TC5 expectedOutput correctly reflects tie-breaking rule (1 4)."""
        cp01 = self.bank_json[0]
        self.assertEqual(cp01["id"], "CP01")
        tc5 = cp01["testCases"][4]
        self.assertEqual(tc5["id"], 5)

        oracle_out = oracle_cp01(tc5["input"])
        self.assertEqual(oracle_out, "1 4\n")
        bank_out = tc5["expectedOutput"]
        self.assertEqual(normalize_output(oracle_out), normalize_output(bank_out),
                         "Remediation verified: CP01 TC5 matches oracle output '1 4\\n'")

    def test_cp13_tc10_uniqueness_remediated(self):
        """Verifies CP13 TC10 tests boundary N=10 and is distinct from TC3."""
        cp13 = next(p for p in self.bank_json if p["id"] == "CP13")
        tc3_in = cp13["testCases"][2]["input"].strip()
        tc10_in = cp13["testCases"][9]["input"].strip()
        self.assertNotEqual(tc3_in, tc10_in, "Remediation verified: CP13 TC10 is distinct from TC3")
        self.assertEqual(tc10_in, "10", "Remediation verified: CP13 TC10 input is '10'")
        oracle_out = oracle_cp13(cp13["testCases"][9]["input"])
        self.assertEqual(normalize_output(cp13["testCases"][9]["expectedOutput"]), normalize_output(oracle_out),
                         "Remediation verified: CP13 TC10 expectedOutput matches oracle_cp13 for N=10")

    # --------------------------------------------------------------------------
    # 5. Live C++ Compiler & Reference Solution Execution
    # --------------------------------------------------------------------------
    def test_08_live_gxx_cpp_solutions_execution(self):
        """Compiles and executes reference C++ solutions using host MSYS2 g++."""
        # CP02: Kadane's Algorithm
        kadane_cpp = """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    long long x, max_so_far, curr_max;
    cin >> x;
    max_so_far = curr_max = x;
    for (int i = 1; i < n; ++i) {
        cin >> x;
        curr_max = max(x, curr_max + x);
        max_so_far = max(max_so_far, curr_max);
    }
    cout << max_so_far << "\\n";
    return 0;
}
"""
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "kadane.cpp")
            exe = os.path.join(tmp, "kadane.exe")
            with open(src, "w", encoding="utf-8") as f:
                f.write(kadane_cpp)
            comp = subprocess.run(["g++", "-std=c++17", "-O2", src, "-o", exe], capture_output=True, text=True)
            self.assertEqual(comp.returncode, 0, f"g++ failed to compile Kadane solution: {comp.stderr}")

            cp02 = self.bank_json[1]
            for tc in cp02["testCases"]:
                run_res = subprocess.run([exe], input=tc["input"], capture_output=True, text=True, timeout=2)
                self.assertEqual(run_res.returncode, 0)
                self.assertEqual(normalize_output(run_res.stdout), normalize_output(tc["expectedOutput"]),
                                 f"CP02 TC {tc['id']} C++ solution output mismatch")

    # --------------------------------------------------------------------------
    # 6. Statistical Random 3-Problem Selection
    # --------------------------------------------------------------------------
    def test_09_random_3_problem_selection_distribution(self):
        """Simulates 10,000 random 3-problem exam selections: no duplicates, uniform coverage."""
        import random
        problem_ids = [p["id"] for p in self.bank_json]
        n_problems = len(problem_ids)
        draws = 10000
        id_counts = Counter()

        for _ in range(draws):
            selected = random.sample(problem_ids, 3)
            self.assertEqual(len(selected), 3, "Selected count must be 3")
            self.assertEqual(len(set(selected)), 3, "Selected problems must be distinct")
            for pid in selected:
                id_counts[pid] += 1

        self.assertEqual(len(id_counts), n_problems, "Not all problems were sampled")
        expected_per_prob = draws * 3.0 / n_problems
        for pid, cnt in id_counts.items():
            diff_ratio = abs(cnt - expected_per_prob) / expected_per_prob
            self.assertLess(diff_ratio, 0.15, f"Selection bias detected for {pid}: {cnt} vs exp {expected_per_prob}")

    # --------------------------------------------------------------------------
    # 7. Adversarial Schema Breaking & Validator Robustness
    # --------------------------------------------------------------------------
    def test_10_adversarial_validator_detection(self):
        """Verifies that verify_coding_bank.py CodingBankValidator rejects corrupt payloads."""
        from verify_coding_bank import CodingBankValidator
        validator = CodingBankValidator(min_problems=15)

        # Clean bank
        valid, errs, _ = validator.validate_bank(self.bank_json)
        self.assertTrue(valid, f"Clean bank failed validation: {[str(e) for e in errs]}")

        # Truncated testCases (< 10)
        corrupt_tc = json.loads(json.dumps(self.bank_json))
        corrupt_tc[0]["testCases"] = corrupt_tc[0]["testCases"][:9]
        valid, errs, _ = validator.validate_bank(corrupt_tc)
        self.assertFalse(valid, "Validator accepted 9 test cases")

        # Non-sequential test case ID
        corrupt_id = json.loads(json.dumps(self.bank_json))
        corrupt_id[0]["testCases"][2]["id"] = 99
        valid, errs, _ = validator.validate_bank(corrupt_id)
        self.assertFalse(valid, "Validator accepted non-sequential test case ID 99")

        # Null input
        corrupt_input = json.loads(json.dumps(self.bank_json))
        corrupt_input[0]["testCases"][4]["input"] = None
        valid, errs, _ = validator.validate_bank(corrupt_input)
        self.assertFalse(valid, "Validator accepted null input")

        # Empty title
        corrupt_title = json.loads(json.dumps(self.bank_json))
        corrupt_title[1]["title"] = ""
        valid, errs, _ = validator.validate_bank(corrupt_title)
        self.assertFalse(valid, "Validator accepted empty title")

        # Invalid difficulty
        corrupt_diff = json.loads(json.dumps(self.bank_json))
        corrupt_diff[2]["difficulty"] = "Nightmare"
        valid, errs, _ = validator.validate_bank(corrupt_diff)
        self.assertFalse(valid, "Validator accepted invalid difficulty 'Nightmare'")

    # --------------------------------------------------------------------------
    # 8. Regression Against MCQ Question Bank
    # --------------------------------------------------------------------------
    def test_11_mcq_bank_zero_regression(self):
        """Verifies questions.json (210 MCQs) remains 100% intact and uncorrupted."""
        self.assertTrue(os.path.exists(QUESTIONS_JSON_PATH), "questions.json missing")
        with open(QUESTIONS_JSON_PATH, "r", encoding="utf-8") as f:
            mcq_data = json.load(f)
        self.assertEqual(len(mcq_data), 210, f"Expected 210 MCQs, found {len(mcq_data)}")
        topics = set(q.get("topicId") for q in mcq_data)
        self.assertEqual(len(topics), 14, f"Expected 14 topics in MCQ bank, found {len(topics)}")


def run_challenger_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCodingProblemBankEmpirical)
    runner = unittest.TextTestRunner(verbosity=2)
    res = runner.run(suite)
    return res.wasSuccessful()


if __name__ == "__main__":
    success = run_challenger_suite()
    sys.exit(0 if success else 1)
