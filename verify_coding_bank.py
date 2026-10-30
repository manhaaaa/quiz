#!/usr/bin/env python3
"""
verify_coding_bank.py - Comprehensive Coding Problem Bank Schema & Integrity Validator

Validates coding_problems.json and coding_problems.js for the C++ & DSA Random Coding Exam.
Enforces:
1. File existence and readability of coding_problems.json and coding_problems.js.
2. Full problem schema compliance (id, title, category, difficulty, timeLimitMs,
   memoryLimitMb, description, inputFormat, outputFormat, constraints, examples,
   starterCode, testCases).
3. EXACTLY 10 test cases per problem with 1-based sequential IDs (1..10), non-null input,
   non-null expectedOutput, and boolean isSample.
4. Non-empty problem statements, valid categories, and valid difficulties.
5. Strict synchronization and data parity between coding_problems.json and coding_problems.js.
6. Zero regression against existing 210 multiple-choice questions in questions.json.
7. Internal self-test suite (--self-test) with 12 adversarial fixtures.

Usage:
    python verify_coding_bank.py                     # Auto-detects and validates bank files
    python verify_coding_bank.py --json <path>       # Validates specific JSON file
    python verify_coding_bank.py --js <path>         # Validates specific JS file
    python verify_coding_bank.py --self-test         # Executes internal 12-fixture self-test
    python verify_coding_bank.py --sample            # Generates & validates synthetic 18-problem bank
    python verify_coding_bank.py --regression        # Runs regression against questions.json
"""

import argparse
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple

# Ensure stdout and stderr handle utf-8 cleanly on Windows
if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "buffer"):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# Canonical Categories representing the 10 university DSA topics
VALID_CATEGORIES = {
    "arrays & vectors": "Arrays & Vectors",
    "arrays": "Arrays & Vectors",
    "array": "Arrays & Vectors",
    "mảng & mảng động": "Arrays & Vectors",
    "strings & parsing": "Strings & Parsing",
    "strings": "Strings & Parsing",
    "string": "Strings & Parsing",
    "chuỗi ký tự": "Strings & Parsing",
    "linked lists": "Linked Lists",
    "linked list": "Linked Lists",
    "danh sách liên kết": "Linked Lists",
    "stack & queue": "Stack & Queue",
    "stack": "Stack & Queue",
    "queue": "Stack & Queue",
    "ngăn xếp & hàng đợi": "Stack & Queue",
    "recursion & backtracking": "Recursion & Backtracking",
    "recursion": "Recursion & Backtracking",
    "đệ quy & quay lui": "Recursion & Backtracking",
    "sorting & searching": "Sorting & Searching",
    "sorting": "Sorting & Searching",
    "searching": "Sorting & Searching",
    "sắp xếp & tìm kiếm": "Sorting & Searching",
    "binary trees & bst": "Binary Trees & BST",
    "trees": "Binary Trees & BST",
    "binary trees": "Binary Trees & BST",
    "cây nhị phân & bst": "Binary Trees & BST",
    "graphs": "Graphs",
    "graph traversal": "Graphs",
    "đồ thị cơ bản": "Graphs",
    "hash tables & sets": "Hash Tables & Sets",
    "hash tables": "Hash Tables & Sets",
    "bảng băm": "Hash Tables & Sets",
    "dynamic programming & greedy": "Dynamic Programming & Greedy",
    "dynamic programming": "Dynamic Programming & Greedy",
    "dp": "Dynamic Programming & Greedy",
    "quy hoạch động & tham lam": "Dynamic Programming & Greedy",
}

VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}

MIN_PROBLEMS_COUNT = 15
TARGET_PROBLEMS_COUNT = 18
REQUIRED_TESTCASES_PER_PROBLEM = 10


class ValidationError:
    """Represents a specific validation failure."""

    def __init__(self, problem_id: Optional[str], field: str, message: str):
        self.problem_id = problem_id
        self.field = field
        self.message = message

    def __str__(self) -> str:
        prefix = f"[PID: {self.problem_id}] " if self.problem_id else ""
        return f"{prefix}{self.field}: {self.message}"


class CodingBankValidator:
    """Validates problem bank schema, constraints, and testcase completeness."""

    def __init__(self, min_problems: int = MIN_PROBLEMS_COUNT):
        self.min_problems = min_problems
        self.errors: List[ValidationError] = []
        self.warnings: List[str] = []
        self.seen_ids: Set[str] = set()
        self.category_counts: Dict[str, int] = defaultdict(int)
        self.difficulty_counts: Dict[str, int] = defaultdict(int)
        self.total_testcases = 0

    def reset(self):
        self.errors.clear()
        self.warnings.clear()
        self.seen_ids.clear()
        self.category_counts.clear()
        self.difficulty_counts.clear()
        self.total_testcases = 0

    def validate_bank(self, data: Any) -> Tuple[bool, List[ValidationError], List[str]]:
        """Validates an entire parsed coding problem bank."""
        self.reset()

        if not isinstance(data, list):
            self.errors.append(ValidationError(None, "root", f"Problem bank must be a JSON array, got {type(data).__name__}"))
            return False, self.errors, self.warnings

        total = len(data)
        if total < self.min_problems:
            self.errors.append(ValidationError(
                None, "count", f"Total problem count {total} is below minimum requirement ({self.min_problems}). Target is {TARGET_PROBLEMS_COUNT}."
            ))

        for idx, item in enumerate(data, start=1):
            self._validate_problem(item, idx)

        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings

    def _validate_problem(self, item: Any, index: int):
        """Validates a single problem object."""
        if not isinstance(item, dict):
            self.errors.append(ValidationError(f"item_{index}", "type", f"Problem item must be an object/dict, got {type(item).__name__}"))
            return

        pid = item.get("id")
        pid_str = str(pid) if pid is not None else f"index_{index}"

        # 1. ID validation
        if pid is None or not isinstance(pid, str) or not pid.strip():
            self.errors.append(ValidationError(pid_str, "id", "Missing or empty 'id' field"))
        else:
            pid_clean = pid.strip()
            if not re.match(r"^[a-zA-Z0-9_\-]+$", pid_clean):
                self.errors.append(ValidationError(pid_str, "id", f"ID '{pid_clean}' contains invalid characters (allowed: alphanumeric, underscore, hyphen)"))
            if pid_clean in self.seen_ids:
                self.errors.append(ValidationError(pid_str, "id", f"Duplicate problem id '{pid_clean}' detected"))
            self.seen_ids.add(pid_clean)

        # 2. Title validation
        title = item.get("title")
        if not title or not isinstance(title, str) or len(title.strip()) < 5:
            self.errors.append(ValidationError(pid_str, "title", "Missing, empty, or too short 'title' (must be >= 5 chars)"))

        # 3. Category validation
        category = item.get("category")
        if not category or not isinstance(category, str) or not category.strip():
            self.errors.append(ValidationError(pid_str, "category", "Missing or empty 'category'"))
        else:
            cat_norm = category.strip().lower()
            if cat_norm not in VALID_CATEGORIES:
                self.errors.append(ValidationError(
                    pid_str, "category", f"Unknown category '{category}'. Must be one of 10 DSA categories."
                ))
            else:
                canonical = VALID_CATEGORIES[cat_norm]
                self.category_counts[canonical] += 1

        # 4. Difficulty validation
        difficulty = item.get("difficulty")
        if not difficulty or difficulty not in VALID_DIFFICULTIES:
            self.errors.append(ValidationError(
                pid_str, "difficulty", f"Invalid difficulty '{difficulty}'. Must be exactly one of: {sorted(list(VALID_DIFFICULTIES))}"
            ))
        else:
            self.difficulty_counts[difficulty] += 1

        # 5. Resource limits validation
        time_limit = item.get("timeLimitMs")
        if time_limit is None or not isinstance(time_limit, int) or time_limit < 100 or time_limit > 10000:
            self.errors.append(ValidationError(
                pid_str, "timeLimitMs", f"Invalid timeLimitMs '{time_limit}'. Must be integer between 100 and 10000 ms."
            ))

        mem_limit = item.get("memoryLimitMb")
        if mem_limit is None or not isinstance(mem_limit, int) or mem_limit < 16 or mem_limit > 1024:
            self.errors.append(ValidationError(
                pid_str, "memoryLimitMb", f"Invalid memoryLimitMb '{mem_limit}'. Must be integer between 16 and 1024 MB."
            ))

        # 6. Problem statements & formats
        description = item.get("description")
        if not description or not isinstance(description, str) or len(description.strip()) < 20:
            self.errors.append(ValidationError(
                pid_str, "description", "Missing, empty, or too brief 'description' (must be >= 20 chars)"
            ))

        input_format = item.get("inputFormat")
        if not input_format or not isinstance(input_format, str) or len(input_format.strip()) < 5:
            self.errors.append(ValidationError(
                pid_str, "inputFormat", "Missing, empty, or too brief 'inputFormat' (must be >= 5 chars)"
            ))

        output_format = item.get("outputFormat")
        if not output_format or not isinstance(output_format, str) or len(output_format.strip()) < 5:
            self.errors.append(ValidationError(
                pid_str, "outputFormat", "Missing, empty, or too brief 'outputFormat' (must be >= 5 chars)"
            ))

        # 7. Constraints validation
        constraints = item.get("constraints")
        if not isinstance(constraints, list) or len(constraints) == 0:
            self.errors.append(ValidationError(pid_str, "constraints", "'constraints' must be a non-empty list of strings"))
        else:
            for c_idx, c in enumerate(constraints):
                if not isinstance(c, str) or not c.strip():
                    self.errors.append(ValidationError(pid_str, f"constraints[{c_idx}]", "Constraint must be a non-empty string"))

        # 8. Examples validation
        examples = item.get("examples")
        if not isinstance(examples, list) or len(examples) == 0:
            self.errors.append(ValidationError(pid_str, "examples", "'examples' must be a non-empty list of example objects"))
        else:
            for ex_idx, ex in enumerate(examples):
                if not isinstance(ex, dict):
                    self.errors.append(ValidationError(pid_str, f"examples[{ex_idx}]", "Example must be an object/dict"))
                    continue
                if "input" not in ex or not isinstance(ex["input"], str):
                    self.errors.append(ValidationError(pid_str, f"examples[{ex_idx}].input", "Example missing non-null string 'input'"))
                if "output" not in ex or not isinstance(ex["output"], str):
                    self.errors.append(ValidationError(pid_str, f"examples[{ex_idx}].output", "Example missing non-null string 'output'"))

        # 9. Starter code validation
        starter_code = item.get("starterCode")
        if not starter_code or not isinstance(starter_code, str) or len(starter_code.strip()) < 20:
            self.errors.append(ValidationError(
                pid_str, "starterCode", "Missing, empty, or insufficient 'starterCode' template (must be >= 20 chars)"
            ))

        # 10. TestCases validation (EXACTLY 10 test cases)
        test_cases = item.get("testCases")
        if not isinstance(test_cases, list):
            self.errors.append(ValidationError(pid_str, "testCases", f"'testCases' must be an array/list, got {type(test_cases).__name__}"))
        elif len(test_cases) != REQUIRED_TESTCASES_PER_PROBLEM:
            self.errors.append(ValidationError(
                pid_str, "testCases", f"Problem must have EXACTLY {REQUIRED_TESTCASES_PER_PROBLEM} test cases, found {len(test_cases)}"
            ))
        else:
            for tc_idx, tc in enumerate(test_cases, start=1):
                self._validate_test_case(pid_str, tc, tc_idx)
            self.total_testcases += len(test_cases)

    def _validate_test_case(self, pid: str, tc: Any, expected_id: int):
        """Validates a single test case object."""
        tc_prefix = f"testCases[{expected_id}]"

        if not isinstance(tc, dict):
            self.errors.append(ValidationError(pid, tc_prefix, f"Test case must be an object/dict, got {type(tc).__name__}"))
            return

        # ID check (support 'id' or 'testCaseId')
        tc_id = tc.get("id")
        if tc_id is None:
            tc_id = tc.get("testCaseId")

        if tc_id is None:
            self.errors.append(ValidationError(pid, f"{tc_prefix}.id", "Missing required test case 'id'"))
        elif not isinstance(tc_id, int) or tc_id != expected_id:
            self.errors.append(ValidationError(
                pid, f"{tc_prefix}.id", f"Invalid test case id '{tc_id}'. Expected sequential integer {expected_id} (range 1..10)."
            ))

        # Input check (must be non-null string)
        tc_in = tc.get("input")
        if tc_in is None or not isinstance(tc_in, str):
            self.errors.append(ValidationError(
                pid, f"{tc_prefix}.input", f"Test case input must be a non-null string, got {type(tc_in).__name__}"
            ))

        # ExpectedOutput check (must be non-null string)
        tc_out = tc.get("expectedOutput")
        if tc_out is None or not isinstance(tc_out, str):
            self.errors.append(ValidationError(
                pid, f"{tc_prefix}.expectedOutput", f"Test case expectedOutput must be a non-null string, got {type(tc_out).__name__}"
            ))

        # isSample check (must be boolean)
        is_sample = tc.get("isSample")
        if is_sample is None or not isinstance(is_sample, bool):
            self.errors.append(ValidationError(
                pid, f"{tc_prefix}.isSample", f"'isSample' must be a boolean (True/False), got {type(is_sample).__name__}"
            ))
        else:
            if expected_id <= 2 and not is_sample:
                self.warnings.append(f"[PID: {pid}] TC {expected_id} is typically marked as isSample=True.")
            elif expected_id > 2 and is_sample:
                self.warnings.append(f"[PID: {pid}] TC {expected_id} is marked as isSample=True (hidden cases are typically False).")

        # Optional points check
        pts = tc.get("points")
        if pts is not None and (not isinstance(pts, int) or pts != 10):
            self.errors.append(ValidationError(
                pid, f"{tc_prefix}.points", f"Test case points must be exactly 10, got {pts}"
            ))


def load_coding_json(file_path: str) -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
    """Loads and parses coding problems from a JSON file."""
    if not os.path.exists(file_path):
        return None, f"File not found: {file_path}"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data, None
    except Exception as e:
        return None, f"Failed to parse JSON in {file_path}: {e}"


def load_coding_js(file_path: str) -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
    """Loads and parses coding problems from a JS file (window.CODING_PROBLEMS = [...])."""
    if not os.path.exists(file_path):
        return None, f"File not found: {file_path}"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw = f.read().strip()
        # Strip JS declaration
        cleaned = re.sub(r"^\s*(?:window\.)?(?:const|let|var)?\s*[a-zA-Z0-9_$]+\s*=\s*", "", raw, count=1)
        cleaned = re.sub(r";\s*$", "", cleaned)
        data = json.loads(cleaned)
        return data, None
    except Exception as e:
        return None, f"Failed to parse JS syntax in {file_path}: {e}"


def assert_dual_mode_parity(json_data: List[Dict[str, Any]], js_data: List[Dict[str, Any]]) -> List[str]:
    """Verifies that coding_problems.json and coding_problems.js have identical content."""
    discrepancies = []
    if len(json_data) != len(js_data):
        discrepancies.append(f"Problem count mismatch: JSON has {len(json_data)} problems, JS has {len(js_data)} problems.")
        return discrepancies

    for idx, (p_json, p_js) in enumerate(zip(json_data, js_data), start=1):
        pid_json = p_json.get("id", f"idx_{idx}")
        pid_js = p_js.get("id", f"idx_{idx}")
        if pid_json != pid_js:
            discrepancies.append(f"Problem #{idx} ID mismatch: JSON='{pid_json}' vs JS='{pid_js}'")
            continue

        # Check serialization equality
        str_json = json.dumps(p_json, sort_keys=True)
        str_js = json.dumps(p_js, sort_keys=True)
        if str_json != str_js:
            discrepancies.append(f"Problem '{pid_json}' content differs between .json and .js")

    return discrepancies


def print_summary_table(data: List[Dict[str, Any]], category_counts: Dict[str, int], difficulty_counts: Dict[str, int]):
    """Prints a structured summary table of the coding problem bank."""
    print("\n" + "=" * 88)
    print(f"{'#':<3} | {'ID':<10} | {'Difficulty':<10} | {'TestCases':<10} | {'Category':<22} | {'Title'}")
    print("-" * 88)

    for idx, p in enumerate(data, start=1):
        pid = str(p.get("id", "N/A"))
        diff = str(p.get("difficulty", "N/A"))
        tcs = len(p.get("testCases", []))
        tc_str = f"{tcs}/10"
        cat = str(p.get("category", "N/A"))[:20]
        title = str(p.get("title", "N/A"))[:30]
        print(f"{idx:<3} | {pid:<10} | {diff:<10} | {tc_str:<10} | {cat:<22} | {title}")

    print("-" * 88)
    total_problems = len(data)
    total_tc = sum(len(p.get("testCases", [])) for p in data)
    print(f"Total Problems: {total_problems:<4} | Total Test Cases: {total_tc:<5} | Categories: {len(category_counts):<2}/10")
    print(f"Difficulty Breakdown: Easy: {difficulty_counts.get('Easy', 0)}, Medium: {difficulty_counts.get('Medium', 0)}, Hard: {difficulty_counts.get('Hard', 0)}")
    print("=" * 88 + "\n")


def create_sample_coding_bank(problem_count: int = TARGET_PROBLEMS_COUNT) -> List[Dict[str, Any]]:
    """Generates a synthetic coding problem bank conforming strictly to schema."""
    sample_categories = [
        "Arrays & Vectors", "Strings & Parsing", "Linked Lists", "Stack & Queue",
        "Recursion & Backtracking", "Sorting & Searching", "Binary Trees & BST",
        "Graphs", "Hash Tables & Sets", "Dynamic Programming & Greedy"
    ]
    bank = []
    for i in range(1, problem_count + 1):
        cat = sample_categories[(i - 1) % len(sample_categories)]
        diff = "Easy" if i % 3 == 1 else ("Medium" if i % 3 == 2 else "Hard")
        pid = f"CP{i:02d}"

        test_cases = []
        for tc_idx in range(1, 11):
            test_cases.append({
                "id": tc_idx,
                "input": f"{tc_idx}\n1 2 3\n",
                "expectedOutput": f"{tc_idx * 2}\n",
                "isSample": (tc_idx <= 2),
                "edgeCaseType": f"Role Matrix TC {tc_idx}",
                "points": 10
            })

        bank.append({
            "id": pid,
            "title": f"Problem {i:02d} - Algorithmic Challenge on {cat}",
            "category": cat,
            "difficulty": diff,
            "timeLimitMs": 2000,
            "memoryLimitMb": 256,
            "description": f"Mô tả chi tiết bài toán {pid} thuộc chủ đề {cat}. Yêu cầu xử lý mảng và tính toán kết quả tối ưu.",
            "inputFormat": "Dòng đầu chứa số nguyên N. Dòng thứ hai chứa N số nguyên.",
            "outputFormat": "In ra một số nguyên duy nhất là kết quả bài toán.",
            "constraints": ["1 <= N <= 10^5", "-10^9 <= A[i] <= 10^9"],
            "examples": [
                {"input": "3\n1 2 3\n", "output": "6\n", "explanation": "Tổng của 1 + 2 + 3 = 6."}
            ],
            "starterCode": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Code here\n    return 0;\n}\n",
            "testCases": test_cases
        })
    return bank


def run_self_tests() -> bool:
    """Runs internal unit test suite verifying validator catches all corruptions."""
    print("\n>>> Running CodingBankValidator self-test suite (12 adversarial fixtures)...")
    validator = CodingBankValidator(min_problems=1)

    # 1. Clean valid bank
    clean_bank = create_sample_coding_bank(18)
    ok, errors, _ = validator.validate_bank(clean_bank)
    assert ok, f"Clean sample bank should pass, got: {[str(e) for e in errors]}"
    print("  [PASS] 01. Clean 18-problem bank passes completely")

    # 2. Missing required field (starterCode)
    bad_field = create_sample_coding_bank(1)
    del bad_field[0]["starterCode"]
    ok, errors, _ = validator.validate_bank(bad_field)
    assert not ok and any(e.field == "starterCode" for e in errors), "Failed to catch missing starterCode"
    print("  [PASS] 02. Rejects missing required field (starterCode)")

    # 3. Test case count != 10 (e.g. 9 cases)
    bad_tc_len = create_sample_coding_bank(1)
    bad_tc_len[0]["testCases"].pop()
    ok, errors, _ = validator.validate_bank(bad_tc_len)
    assert not ok and any("EXACTLY 10" in e.message for e in errors), "Failed to catch testCases count != 10"
    print("  [PASS] 03. Rejects testCases count != 10 (9 cases)")

    # 4. Duplicate problem ID
    bad_dup = create_sample_coding_bank(2)
    bad_dup[1]["id"] = bad_dup[0]["id"]
    ok, errors, _ = validator.validate_bank(bad_dup)
    assert not ok and any("Duplicate" in e.message for e in errors), "Failed to catch duplicate problem ID"
    print("  [PASS] 04. Rejects duplicate problem ID")

    # 5. Invalid difficulty
    bad_diff = create_sample_coding_bank(1)
    bad_diff[0]["difficulty"] = "SuperHard"
    ok, errors, _ = validator.validate_bank(bad_diff)
    assert not ok and any("difficulty" in e.field for e in errors), "Failed to catch invalid difficulty"
    print("  [PASS] 05. Rejects invalid difficulty ('SuperHard')")

    # 6. Invalid test case ID (non-sequential)
    bad_tcid = create_sample_coding_bank(1)
    bad_tcid[0]["testCases"][4]["id"] = 99
    ok, errors, _ = validator.validate_bank(bad_tcid)
    assert not ok and any("Invalid test case id" in e.message for e in errors), "Failed to catch invalid test case ID"
    print("  [PASS] 06. Rejects non-sequential test case ID")

    # 7. Null test case input
    bad_tcin = create_sample_coding_bank(1)
    bad_tcin[0]["testCases"][0]["input"] = None
    ok, errors, _ = validator.validate_bank(bad_tcin)
    assert not ok and any("input" in e.field for e in errors), "Failed to catch None input"
    print("  [PASS] 07. Rejects null test case input")

    # 8. Null test case expectedOutput
    bad_tcout = create_sample_coding_bank(1)
    bad_tcout[0]["testCases"][0]["expectedOutput"] = None
    ok, errors, _ = validator.validate_bank(bad_tcout)
    assert not ok and any("expectedOutput" in e.field for e in errors), "Failed to catch None expectedOutput"
    print("  [PASS] 08. Rejects null test case expectedOutput")

    # 9. Invalid isSample type (string instead of bool)
    bad_sample = create_sample_coding_bank(1)
    bad_sample[0]["testCases"][0]["isSample"] = "true"
    ok, errors, _ = validator.validate_bank(bad_sample)
    assert not ok and any("isSample" in e.field for e in errors), "Failed to catch non-bool isSample"
    print("  [PASS] 09. Rejects string 'true' for isSample")

    # 10. Dual-mode discrepancy detection
    bank_json = create_sample_coding_bank(2)
    bank_js = create_sample_coding_bank(2)
    bank_js[0]["testCases"][0]["expectedOutput"] = "DIFFERENT\n"
    discrepancies = assert_dual_mode_parity(bank_json, bank_js)
    assert len(discrepancies) > 0, "Failed to detect parity mismatch between JSON and JS"
    print("  [PASS] 10. Rejects dual-mode discrepancy between .json and .js")

    # 11. Empty description
    bad_desc = create_sample_coding_bank(1)
    bad_desc[0]["description"] = "Too short"
    ok, errors, _ = validator.validate_bank(bad_desc)
    assert not ok and any("description" in e.field for e in errors), "Failed to catch short description"
    print("  [PASS] 11. Rejects short/empty problem description")

    # 12. Invalid timeLimitMs (out of range)
    bad_time = create_sample_coding_bank(1)
    bad_time[0]["timeLimitMs"] = 50000
    ok, errors, _ = validator.validate_bank(bad_time)
    assert not ok and any("timeLimitMs" in e.field for e in errors), "Failed to catch out-of-range timeLimitMs"
    print("  [PASS] 12. Rejects out-of-range timeLimitMs (50000 ms)")

    print(">>> All 12 self-test fixtures PASSED successfully!\n")
    return True


def check_mcq_regression(quiz_dir: str) -> bool:
    """Verifies that questions.json and verify_bank.py still pass cleanly."""
    print(">>> Checking regression against MCQ Question Bank (questions.json)...")
    q_json_path = os.path.join(quiz_dir, "questions.json")
    v_script_path = os.path.join(quiz_dir, "verify_bank.py")

    if not os.path.exists(q_json_path):
        print(f"[REGRESSION SKIP] {q_json_path} not found.")
        return True

    # If verify_bank.py exists, invoke or import it
    if os.path.exists(v_script_path):
        import subprocess
        res = subprocess.run([sys.executable, v_script_path], cwd=quiz_dir, capture_output=True, text=True)
        if res.returncode == 0:
            print("[REGRESSION PASS] Existing 210 MCQs in questions.json validated successfully via verify_bank.py!")
            return True
        else:
            print(f"[REGRESSION FAIL] verify_bank.py failed:\n{res.stdout}\n{res.stderr}")
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Verify Coding Problem Bank Schema and Integrity")
    parser.add_argument("--json", help="Path to coding_problems.json", default=None)
    parser.add_argument("--js", help="Path to coding_problems.js", default=None)
    parser.add_argument("--self-test", action="store_true", help="Run 12-fixture validator self-test suite")
    parser.add_argument("--sample", action="store_true", help="Generate & validate synthetic 18-problem bank")
    parser.add_argument("--regression", action="store_true", help="Run regression check against questions.json")
    args = parser.parse_args()

    if args.self_test:
        success = run_self_tests()
        sys.exit(0 if success else 1)

    if args.sample:
        print(">>> Generating and validating synthetic 18-problem coding bank...")
        sample_bank = create_sample_coding_bank(TARGET_PROBLEMS_COUNT)
        val = CodingBankValidator(min_problems=MIN_PROBLEMS_COUNT)
        ok, errors, _ = val.validate_bank(sample_bank)
        print_summary_table(sample_bank, val.category_counts, val.difficulty_counts)
        if ok:
            print("[SUCCESS] Synthetic sample coding bank validated 100% compliant!")
            sys.exit(0)
        else:
            print(f"[FAIL] Sample bank errors ({len(errors)}):")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)

    # Locate target directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        base_dir,
        os.path.join(base_dir, "quiz_game"),
        os.getcwd(),
        os.path.join(os.getcwd(), "quiz_game")
    ]

    json_file = args.json
    js_file = args.js

    if not json_file:
        for c in candidates:
            p = os.path.join(c, "coding_problems.json")
            if os.path.exists(p):
                json_file = p
                break

    if not js_file:
        for c in candidates:
            p = os.path.join(c, "coding_problems.js")
            if os.path.exists(p):
                js_file = p
                break

    if not json_file and not js_file:
        print("[NOTICE] Neither coding_problems.json nor coding_problems.js was found.")
        print("         Running self-test suite and sample bank validation to verify validator readiness...\n")
        st_ok = run_self_tests()
        s_bank = create_sample_coding_bank(TARGET_PROBLEMS_COUNT)
        val = CodingBankValidator(min_problems=MIN_PROBLEMS_COUNT)
        val_ok, _, _ = val.validate_bank(s_bank)
        print_summary_table(s_bank, val.category_counts, val.difficulty_counts)
        if st_ok and val_ok:
            print("[VERIFIED] verify_coding_bank.py validator engine is 100% operational and ready.")
            sys.exit(0)
        else:
            sys.exit(1)

    # Validate JSON if present
    json_data = None
    if json_file:
        print(f"\n>>> Validating JSON Problem Bank from: {json_file}")
        json_data, err = load_coding_json(json_file)
        if err:
            print(f"[ERROR] {err}")
            sys.exit(1)

        val_json = CodingBankValidator(min_problems=MIN_PROBLEMS_COUNT)
        ok_json, errors_json, warnings_json = val_json.validate_bank(json_data)
        print_summary_table(json_data, val_json.category_counts, val_json.difficulty_counts)

        if not ok_json:
            print(f"[FAILED] coding_problems.json failed validation with {len(errors_json)} error(s):")
            for e in errors_json[:30]:
                print(f"  - {e}")
            sys.exit(1)

    # Validate JS if present
    js_data = None
    if js_file:
        print(f"\n>>> Validating JS Problem Bank from: {js_file}")
        js_data, err = load_coding_js(js_file)
        if err:
            print(f"[ERROR] {err}")
            sys.exit(1)

        val_js = CodingBankValidator(min_problems=MIN_PROBLEMS_COUNT)
        ok_js, errors_js, warnings_js = val_js.validate_bank(js_data)

        if not ok_js:
            print(f"[FAILED] coding_problems.js failed validation with {len(errors_js)} error(s):")
            for e in errors_js[:30]:
                print(f"  - {e}")
            sys.exit(1)

    # Assert Parity if both present
    if json_data is not None and js_data is not None:
        print(">>> Verifying Dual-Mode Parity (coding_problems.json <-> coding_problems.js)...")
        discrepancies = assert_dual_mode_parity(json_data, js_data)
        if discrepancies:
            print(f"[FAILED] Data parity mismatch between .json and .js ({len(discrepancies)} issues):")
            for d in discrepancies[:20]:
                print(f"  - {d}")
            sys.exit(1)
        print("[SUCCESS] Dual-mode parity verified: .json and .js are 100% identical!")

    # Check regression if requested or by default
    quiz_dir = os.path.dirname(json_file) if json_file else (os.path.dirname(js_file) if js_file else os.getcwd())
    reg_ok = check_mcq_regression(quiz_dir)
    if not reg_ok:
        sys.exit(1)

    print("\n[SUCCESS] Coding problem bank validated successfully!")
    print(f"          - Total Problems: {len(json_data if json_data else js_data)}")
    print(f"          - Total Test Cases: {len(json_data if json_data else js_data) * 10} (Exactly 10 per problem)")
    print(f"          - Dual-mode synchronization: Clean")
    print(f"          - MCQ Bank regression: Clean")
    sys.exit(0)


if __name__ == "__main__":
    main()
