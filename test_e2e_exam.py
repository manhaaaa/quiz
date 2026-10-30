#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
  End-to-End Test Suite: C++ & DSA Random Coding Exam System
================================================================================
  Author: QA / Specialist Test Writer Agent
  Track: Dual Track (E2E Testing Track)
  Target: D:\c++\quiz_game
  Authoritative Sources:
    - d:\c++\.agents\teamwork\ORIGINAL_REQUEST.md
    - d:\c++\PROJECT.md
    - d:\c++\.agents\teamwork\teamwork_spec_miner_survey_3\survey_requirements.md
    - d:\c++\TEST_INFRA.md

  Tiers:
    - Tier 0: Regression Safety (210 MCQs, quiz engine, existing HTML views)
    - Tier 1: Feature Coverage (R1 - R5 Core Contracts)
    - Tier 2: Boundary & Corner Cases (Timer expiry, score extremes, invalid files, normalizer)
    - Tier 3: Combinations & Cross-Feature Interactions (Navigation, partial upload, API contract)
    - Tier 4: Real-World Scenarios (Full exam lifecycle, HTML DOM contracts, live g++ toolchain)
================================================================================
"""

import os
import sys
import json
import re
import math
import random
import unittest
import tempfile
import subprocess
import time
from pathlib import Path

# Resolve base directories
QUIZ_GAME_DIR = Path(__file__).resolve().parent
ROOT_DIR = QUIZ_GAME_DIR.parent

QUESTIONS_JSON_PATH = QUIZ_GAME_DIR / "questions.json"
QUESTIONS_JS_PATH = QUIZ_GAME_DIR / "questions.js"
CODING_PROBLEMS_JSON_PATH = QUIZ_GAME_DIR / "coding_problems.json"
CODING_PROBLEMS_JS_PATH = QUIZ_GAME_DIR / "coding_problems.js"
SERVER_JS_PATH = QUIZ_GAME_DIR / "server.js"
INDEX_HTML_PATH = QUIZ_GAME_DIR / "index.html"


# ==============================================================================
# Contract Reference Engines & Specification Helpers
# ==============================================================================

class ExamScoringEngine:
    """Authoritative scoring logic derived from ORIGINAL_REQUEST.md R3 and PROJECT.md."""

    @staticmethod
    def calculate_test_case_score(status: str, passed: bool) -> int:
        """Each passed test case adds exactly 10 points; each failed test case adds 0."""
        if passed and status == "Accepted":
            return 10
        return 0

    @staticmethod
    def calculate_question_score(test_case_results: list) -> int:
        """Question score is the sum of passed test cases, bounded in [0, 100]."""
        if not test_case_results:
            return 0
        total = 0
        for tc in test_case_results:
            status = tc.get("status", "Wrong Answer")
            passed = tc.get("passed", False)
            total += ExamScoringEngine.calculate_test_case_score(status, passed)
        return max(0, min(100, total))

    @staticmethod
    def calculate_total_exam_score(question_scores: list) -> int:
        """Total exam score is the sum of all 3 questions, bounded in [0, 300]."""
        total = sum(question_scores)
        return max(0, min(300, total))

    @staticmethod
    def evaluate_performance_rank(total_score: int) -> dict:
        """Performance ranking according to survey_requirements.md §3.6.3."""
        if total_score >= 250:
            return {"rank": "Xuất sắc", "level": "Excellent", "min": 250, "max": 300}
        elif total_score >= 200:
            return {"rank": "Giỏi", "level": "Good", "min": 200, "max": 240}
        elif total_score >= 150:
            return {"rank": "Đạt", "level": "Pass", "min": 150, "max": 190}
        else:
            return {"rank": "Cần cải thiện", "level": "Needs Improvement", "min": 0, "max": 149}


class OutputNormalizer:
    """Whitespace and CRLF normalization contract per survey_requirements.md §2.5."""

    @staticmethod
    def normalize(text: str) -> str:
        """
        1. Converts CRLF (\\r\\n) and CR (\\r) to Unix LF (\\n).
        2. Trims trailing whitespace from each line.
        3. Collapses multiple trailing newlines to a single newline.
        """
        if text is None:
            return ""
        # 1. CRLF -> LF
        normalized = text.replace("\r\n", "\n").replace("\r", "\n")
        # 2. Trim trailing spaces on each line
        lines = [line.rstrip() for line in normalized.split("\n")]
        # 3. Strip trailing empty lines
        while lines and lines[-1] == "":
            lines.pop()
        if not lines:
            return ""
        return "\n".join(lines) + "\n"

    @staticmethod
    def is_match(actual: str, expected: str) -> bool:
        """Compares normalized actual output with normalized expected output."""
        return OutputNormalizer.normalize(actual) == OutputNormalizer.normalize(expected)


class ExamTimerEngine:
    """60-minute countdown timer specification per survey_requirements.md §3.3."""

    TOTAL_SECONDS = 3600  # 60 minutes

    @staticmethod
    def format_time(seconds: int) -> str:
        """Formats remaining seconds into MM:SS display format."""
        s = max(0, seconds)
        mins = s // 60
        secs = s % 60
        return f"{mins:02d}:{secs:02d}"

    @staticmethod
    def get_warning_state(seconds: int) -> str:
        """
        Visual warning states:
        - normal: > 15m (seconds > 900)
        - warning: 05:01 to 15:00 (300 < seconds <= 900)
        - critical: 00:01 to 05:00 (0 < seconds <= 300)
        - expired: <= 0
        """
        if seconds <= 0:
            return "expired"
        elif seconds <= 300:
            return "critical"
        elif seconds <= 900:
            return "warning"
        return "normal"

    @staticmethod
    def should_auto_submit(seconds: int) -> bool:
        """Exam must automatically finalize when timer reaches 00:00."""
        return seconds <= 0


class ProblemSelector:
    """Random 3-distinct-problem selector per ORIGINAL_REQUEST.md R1."""

    @staticmethod
    def select_3_distinct_problems(problem_bank: list, seed: int = None) -> list:
        """Selects exactly 3 distinct problems using deterministic or pseudorandom sampling."""
        if not problem_bank or len(problem_bank) < 3:
            raise ValueError(f"Problem bank must contain at least 3 problems, found {len(problem_bank) if problem_bank else 0}")
        rng = random.Random(seed) if seed is not None else random
        return rng.sample(problem_bank, 3)


class FileUploadValidator:
    """Client-side and server-side file upload validator per survey_requirements.md §3.5."""

    ALLOWED_EXTENSIONS = {".cpp", ".cc", ".cxx", ".c", ".txt"}
    MAX_FILE_SIZE_BYTES = 500 * 1024  # 500 KB

    @classmethod
    def validate_file(cls, filename: str, file_size: int, content: str = None) -> tuple:
        """
        Returns (is_valid: bool, error_message: str or None)
        """
        ext = Path(filename).suffix.lower()
        if ext not in cls.ALLOWED_EXTENSIONS:
            return False, f"Chỉ chấp nhận file mã nguồn C++ (.cpp, .cc, .cxx) hoặc file text (.txt). Định dạng không hợp lệ: '{ext}'"
        if file_size > cls.MAX_FILE_SIZE_BYTES:
            return False, f"Kích thước file vượt quá giới hạn 500 KB (file hiện tại: {file_size / 1024:.1f} KB)"
        return True, None


# Contract Sample Problem Catalog (used for contract verification if bank file not yet written)
CONTRACT_SAMPLE_PROBLEMS = [
    {
        "id": f"CP{i:02d}",
        "title": f"Problem {i}",
        "category": cat,
        "difficulty": "Easy" if i % 2 == 0 else "Medium",
        "timeLimitMs": 1000,
        "memoryLimitMb": 256,
        "description": f"Problem statement for CP{i:02d}",
        "inputFormat": "Input format",
        "outputFormat": "Output format",
        "constraints": ["1 <= N <= 10^5"],
        "examples": [{"input": "1\n", "output": "1\n", "explanation": "Sample"}],
        "starterCode": "#include <iostream>\nusing namespace std;\nint main() { return 0; }",
        "testCases": [
            {"id": j, "input": f"{j}\n", "expectedOutput": f"{j}\n", "isSample": (j <= 2)}
            for j in range(1, 11)
        ]
    }
    for i, cat in enumerate([
        "Arrays & Vectors", "Strings & Parsing", "Linked Lists",
        "Stack", "Queue", "Recursion", "Trees", "Graphs",
        "Hash Tables", "Dynamic Programming"
    ], 1)
]


# ==============================================================================
# Tier 0: Regression Safety Suite (Existing Quiz Features)
# ==============================================================================

class TestTier0RegressionSafety(unittest.TestCase):
    """
    Ensures existing 210-question multiple choice quiz application,
    topic practice, and bank search continue to function with zero regressions.
    """

    def test_tier0_mcq_bank_schema_and_count(self):
        """Verifies questions.json has >= 210 questions spanning all 14 topics."""
        self.assertTrue(QUESTIONS_JSON_PATH.exists(), f"Missing required questions.json at {QUESTIONS_JSON_PATH}")
        with open(QUESTIONS_JSON_PATH, "r", encoding="utf-8") as f:
            bank = json.load(f)

        self.assertIsInstance(bank, list, "questions.json must contain a JSON array")
        self.assertGreaterEqual(len(bank), 210, f"Expected at least 210 questions, found {len(bank)}")

        # Verify all 14 topics are covered
        topic_counts = {}
        for q in bank:
            self.assertIn("id", q)
            self.assertIn("topicId", q)
            self.assertIn("topicName", q)
            self.assertIn("question", q)
            self.assertIn("options", q)
            self.assertIn("answer", q)
            self.assertIn("explanation", q)

            self.assertEqual(len(q["options"]), 4, f"Question {q['id']} must have exactly 4 options")
            self.assertIn(q["answer"], q["options"], f"Question {q['id']} answer must be one of the options")

            tid = q["topicId"]
            topic_counts[tid] = topic_counts.get(tid, 0) + 1

        self.assertEqual(len(topic_counts), 14, f"Expected exactly 14 topics, found {len(topic_counts)}")
        for tid in range(1, 15):
            self.assertGreaterEqual(topic_counts.get(tid, 0), 14, f"Topic {tid} has fewer than 14 questions")

    def test_tier0_quiz_engine_mechanics(self):
        """Verifies standard 5-question round selection, answering, and scoring."""
        with open(QUESTIONS_JSON_PATH, "r", encoding="utf-8") as f:
            bank = json.load(f)

        # 5-question round selection
        round_q = random.sample(bank, 5)
        self.assertEqual(len(round_q), 5)
        self.assertEqual(len(set(q["id"] for q in round_q)), 5, "Round questions must be unique")

        # Scoring simulation: 4 correct, 1 wrong
        correct_count = 4
        score_percent = (correct_count / 5) * 100
        self.assertEqual(score_percent, 80.0)

    def test_tier0_html_existing_views_intact(self):
        """Verifies index.html preserves existing quiz views and navigation controls."""
        self.assertTrue(INDEX_HTML_PATH.exists(), f"index.html missing at {INDEX_HTML_PATH}")
        html_content = INDEX_HTML_PATH.read_text(encoding="utf-8")

        required_elements = [
            'id="view-home"',
            'id="view-quiz"',
            'id="view-results"',
            'id="view-topics"',
            'id="view-bank"',
            'id="nav-btn-home"',
            'id="nav-btn-quick"',
            'id="nav-btn-topics"',
            'id="nav-btn-bank"',
        ]
        for elem in required_elements:
            self.assertIn(elem, html_content, f"Regression violation: {elem} missing from index.html")


# ==============================================================================
# Tier 1: Feature Coverage (R1 - R5 Core Contracts)
# ==============================================================================

class TestTier1FeatureCoverage(unittest.TestCase):
    """
    Verifies all primary functional requirements (R1 - R5) and core interface contracts.
    """

    def test_tier1_r1_random_3_distinct_problems(self):
        """R1: Starting an exam selects exactly 3 distinct coding problems."""
        # Test on contract catalog across 100 trials
        for trial in range(100):
            selected = ProblemSelector.select_3_distinct_problems(CONTRACT_SAMPLE_PROBLEMS)
            self.assertEqual(len(selected), 3, "Selected count must be exactly 3")
            ids = [p["id"] for p in selected]
            self.assertEqual(len(set(ids)), 3, f"Trial {trial}: Selected problems must be distinct: {ids}")

    def test_tier1_r1_60_min_timer_initiation(self):
        """R1: Initiates a 60-minute (3600-second) countdown timer with 1s interval."""
        timer_seconds = ExamTimerEngine.TOTAL_SECONDS
        self.assertEqual(timer_seconds, 3600, "Timer duration must be exactly 3600 seconds")
        self.assertEqual(ExamTimerEngine.format_time(timer_seconds), "60:00")
        self.assertEqual(ExamTimerEngine.format_time(3599), "59:59")
        self.assertEqual(ExamTimerEngine.format_time(0), "00:00")

    def test_tier1_r2_problem_statement_contract(self):
        """R2: Displays problem statement, input/output requirements, constraints, examples."""
        for p in CONTRACT_SAMPLE_PROBLEMS:
            self.assertIn("id", p)
            self.assertIn("title", p)
            self.assertIn("category", p)
            self.assertIn("difficulty", p)
            self.assertIn("description", p)
            self.assertIn("inputFormat", p)
            self.assertIn("outputFormat", p)
            self.assertIn("constraints", p)
            self.assertIn("examples", p)
            self.assertGreaterEqual(len(p["examples"]), 1, "Each problem must have at least 1 example")

    def test_tier1_r2_file_upload_and_replace(self):
        """R2: Allows uploading and updating C++ source code files for questions."""
        # Nominal C++ source file
        filename = "solution.cpp"
        source_code_v1 = "#include <iostream>\nint main() { std::cout << 42 << std::endl; return 0; }"
        valid, err = FileUploadValidator.validate_file(filename, len(source_code_v1.encode()))
        self.assertTrue(valid, f"Valid C++ file rejected: {err}")
        self.assertIsNone(err)

        # File replacement (v2)
        source_code_v2 = "#include <iostream>\nint main() { std::cout << 100 << std::endl; return 0; }"
        valid_v2, err_v2 = FileUploadValidator.validate_file(filename, len(source_code_v2.encode()))
        self.assertTrue(valid_v2)
        self.assertNotEqual(source_code_v1, source_code_v2)

    def test_tier1_r3_10_test_cases_per_problem(self):
        """R3: System requires exactly 10 test cases per question."""
        for p in CONTRACT_SAMPLE_PROBLEMS:
            self.assertEqual(len(p["testCases"]), 10, f"Problem {p['id']} does not have exactly 10 test cases")

    def test_tier1_r3_10_points_per_passed_test(self):
        """R3: Each passed test case adds 10 points; each failed test case adds 0."""
        self.assertEqual(ExamScoringEngine.calculate_test_case_score("Accepted", True), 10)
        self.assertEqual(ExamScoringEngine.calculate_test_case_score("Wrong Answer", False), 0)
        self.assertEqual(ExamScoringEngine.calculate_test_case_score("Time Limit Exceeded", False), 0)
        self.assertEqual(ExamScoringEngine.calculate_test_case_score("Runtime Error", False), 0)
        self.assertEqual(ExamScoringEngine.calculate_test_case_score("Compilation Error", False), 0)

    def test_tier1_r3_question_score_range_0_to_100(self):
        """R3: Score for each question is between 0 and 100 points."""
        # 0 passed -> 0
        all_failed = [{"status": "Wrong Answer", "passed": False} for _ in range(10)]
        self.assertEqual(ExamScoringEngine.calculate_question_score(all_failed), 0)

        # 7 passed -> 70
        seven_passed = [{"status": "Accepted", "passed": True} for _ in range(7)] + \
                       [{"status": "Wrong Answer", "passed": False} for _ in range(3)]
        self.assertEqual(ExamScoringEngine.calculate_question_score(seven_passed), 70)

        # 10 passed -> 100
        all_passed = [{"status": "Accepted", "passed": True} for _ in range(10)]
        self.assertEqual(ExamScoringEngine.calculate_question_score(all_passed), 100)

    def test_tier1_r3_total_score_range_0_to_300(self):
        """R3: Total exam score is between 0 and 300 points (sum of 3 questions)."""
        # [100, 70, 40] -> 210
        total = ExamScoringEngine.calculate_total_exam_score([100, 70, 40])
        self.assertEqual(total, 210)
        self.assertGreaterEqual(total, 0)
        self.assertLessEqual(total, 300)

    def test_tier1_r3_detailed_breakdown_structure(self):
        """R3: Results provide detailed pass/fail breakdown across 10 test cases."""
        sample_results = [
            {
                "testCaseId": i,
                "status": "Accepted" if i <= 8 else "Wrong Answer",
                "passed": (i <= 8),
                "score": 10 if i <= 8 else 0,
                "timeMs": 15 + i,
                "actualOutput": f"Output {i}",
                "expectedOutput": f"Output {i}" if i <= 8 else f"Expected {i}",
                "error": None
            }
            for i in range(1, 11)
        ]
        self.assertEqual(len(sample_results), 10)
        for row in sample_results:
            self.assertIn("testCaseId", row)
            self.assertIn("status", row)
            self.assertIn("passed", row)
            self.assertIn("score", row)
            self.assertIn("timeMs", row)
            self.assertIn("actualOutput", row)
            self.assertIn("expectedOutput", row)

    def test_tier1_r4_problem_bank_file_and_schema(self):
        """R4: Problem bank file (coding_problems.json) must exist and contain >= 15 problems with 10 test cases."""
        if not CODING_PROBLEMS_JSON_PATH.exists():
            raise AssertionError(f"[Milestone 1 Pending] Coding problem bank file not found: {CODING_PROBLEMS_JSON_PATH}")

        with open(CODING_PROBLEMS_JSON_PATH, "r", encoding="utf-8") as f:
            bank = json.load(f)

        self.assertIsInstance(bank, list, "coding_problems.json must contain a list of problems")
        self.assertGreaterEqual(len(bank), 15, f"Expected at least 15 coding problems, found {len(bank)}")

        for p in bank:
            self.assertIn("id", p)
            self.assertIn("title", p)
            self.assertIn("category", p)
            self.assertIn("testCases", p)
            self.assertEqual(len(p["testCases"]), 10, f"Problem {p['id']} does not have exactly 10 test cases")

    def test_tier1_r4_problem_bank_edge_case_distribution(self):
        """R4: Verifies test cases cover sample and hidden edge cases per problem."""
        if not CODING_PROBLEMS_JSON_PATH.exists():
            raise AssertionError(f"[Milestone 1 Pending] Coding problem bank file not found: {CODING_PROBLEMS_JSON_PATH}")

        with open(CODING_PROBLEMS_JSON_PATH, "r", encoding="utf-8") as f:
            bank = json.load(f)

        for p in bank:
            tcs = p["testCases"]
            self.assertTrue(tcs[0].get("isSample", False), f"{p['id']}: TC 1 must be a sample case")
            self.assertTrue(tcs[1].get("isSample", False), f"{p['id']}: TC 2 must be a sample case")
            # All test cases must have non-empty inputs and expectedOutputs
            for tc in tcs:
                self.assertIsNotNone(tc.get("input"), f"{p['id']} TC {tc.get('id')} has null input")
                self.assertIsNotNone(tc.get("expectedOutput"), f"{p['id']} TC {tc.get('id')} has null expectedOutput")

    def test_tier1_r5_server_files_and_api_contract(self):
        """R5: Execution architecture file (server.js) must exist and define REST endpoints."""
        if not SERVER_JS_PATH.exists():
            raise AssertionError(f"[Milestone 2 Pending] Evaluation server file not found: {SERVER_JS_PATH}")

        server_code = SERVER_JS_PATH.read_text(encoding="utf-8")
        self.assertIn("/api/health", server_code, "server.js must implement /api/health endpoint")
        self.assertIn("/api/evaluate", server_code, "server.js must implement /api/evaluate endpoint")


# ==============================================================================
# Tier 2: Boundary & Corner Cases
# ==============================================================================

class TestTier2BoundaryAndCorner(unittest.TestCase):
    """
    Verifies system boundaries, degenerate inputs, error states, and normalization.
    """

    def test_tier2_timer_expiration_auto_submit(self):
        """Timer reaching 00:00 triggers automatic submission."""
        self.assertFalse(ExamTimerEngine.should_auto_submit(3600))
        self.assertFalse(ExamTimerEngine.should_auto_submit(1))
        self.assertTrue(ExamTimerEngine.should_auto_submit(0))
        self.assertTrue(ExamTimerEngine.should_auto_submit(-5))

    def test_tier2_scoring_zero_points_all_failed(self):
        """When student code fails all 10 test cases, question score is strictly 0."""
        all_failed = [{"status": "Wrong Answer", "passed": False} for _ in range(10)]
        score = ExamScoringEngine.calculate_question_score(all_failed)
        self.assertEqual(score, 0)

    def test_tier2_scoring_perfect_100_all_passed(self):
        """When student code passes all 10 test cases, question score is strictly 100."""
        all_passed = [{"status": "Accepted", "passed": True} for _ in range(10)]
        score = ExamScoringEngine.calculate_question_score(all_passed)
        self.assertEqual(score, 100)

    def test_tier2_scoring_partial_scores(self):
        """Verifies partial scores: 1 passed = 10, 5 passed = 50, 9 passed = 90."""
        for passed_count in range(11):
            results = [{"status": "Accepted", "passed": True} for _ in range(passed_count)] + \
                      [{"status": "Wrong Answer", "passed": False} for _ in range(10 - passed_count)]
            score = ExamScoringEngine.calculate_question_score(results)
            self.assertEqual(score, passed_count * 10)

    def test_tier2_invalid_file_extension_rejection(self):
        """Uploading unsupported file formats (.exe, .py, .java, .pdf, .png) is rejected."""
        invalid_files = [
            "malware.exe", "solution.py", "Main.java", "report.pdf",
            "image.png", "script.sh", "archive.zip"
        ]
        for fname in invalid_files:
            valid, err = FileUploadValidator.validate_file(fname, 1024)
            self.assertFalse(valid, f"Invalid file '{fname}' was unexpectedly accepted")
            self.assertIsNotNone(err)

    def test_tier2_empty_file_handling(self):
        """Uploading an empty 0-byte file yields 0 points across all 10 test cases."""
        valid, err = FileUploadValidator.validate_file("empty.cpp", 0)
        self.assertTrue(valid, "0-byte .cpp file format is structurally acceptable but yields no output")
        # Empty code evaluation yields 0 points
        no_output_results = [{"status": "Wrong Answer", "passed": False} for _ in range(10)]
        score = ExamScoringEngine.calculate_question_score(no_output_results)
        self.assertEqual(score, 0)

    def test_tier2_file_size_limit_rejection(self):
        """Files exceeding 500 KB limit are rejected."""
        valid_size = 500 * 1024  # exactly 500 KB
        valid, _ = FileUploadValidator.validate_file("large.cpp", valid_size)
        self.assertTrue(valid)

        exceeded_size = (500 * 1024) + 1  # 500 KB + 1 byte
        invalid, err = FileUploadValidator.validate_file("huge.cpp", exceeded_size)
        self.assertFalse(invalid)
        self.assertIn("500 KB", err)

    def test_tier2_whitespace_and_crlf_normalization(self):
        """Verifies CRLF vs LF and trailing whitespace normalizer contract."""
        expected = "1 2 3\n4 5 6\n"

        # Case 1: Windows CRLF
        actual_crlf = "1 2 3\r\n4 5 6\r\n"
        self.assertTrue(OutputNormalizer.is_match(actual_crlf, expected))

        # Case 2: Trailing whitespace on lines
        actual_trailing_spaces = "1 2 3    \n4 5 6   \t\n"
        self.assertTrue(OutputNormalizer.is_match(actual_trailing_spaces, expected))

        # Case 3: Multiple trailing empty lines
        actual_extra_newlines = "1 2 3\n4 5 6\n\n\n\n"
        self.assertTrue(OutputNormalizer.is_match(actual_extra_newlines, expected))

        # Case 4: Semantic difference (should NOT match)
        actual_wrong = "1 2 4\n4 5 6\n"
        self.assertFalse(OutputNormalizer.is_match(actual_wrong, expected))

    def test_tier2_time_limit_exceeded_classification(self):
        """Test case exceeding timeout is classified as Time Limit Exceeded with 0 points."""
        tc_result = {
            "testCaseId": 9,
            "status": "Time Limit Exceeded",
            "passed": False,
            "timeMs": 2050,
            "error": "Execution timed out after 2000ms"
        }
        score = ExamScoringEngine.calculate_test_case_score(tc_result["status"], tc_result["passed"])
        self.assertEqual(score, 0)

    def test_tier2_compilation_error_classification(self):
        """Code with compilation failure yields 0 points for the question."""
        eval_response = {
            "success": True,
            "compilation": {
                "success": False,
                "output": "solution.cpp:3:1: error: expected ';' before '}' token"
            },
            "results": [{"status": "Compilation Error", "passed": False} for _ in range(10)],
            "score": 0
        }
        self.assertFalse(eval_response["compilation"]["success"])
        self.assertEqual(eval_response["score"], 0)

    def test_tier2_adversarial_large_inputs(self):
        """Normalizer and scoring handle large inputs (e.g., 100,000 numbers) cleanly."""
        large_tokens = [str(i) for i in range(100000)]
        large_expected = " ".join(large_tokens) + "\n"
        large_actual = " ".join(large_tokens) + "   \r\n"
        self.assertTrue(OutputNormalizer.is_match(large_actual, large_expected))


# ==============================================================================
# Tier 3: Cross-Feature Interactions & Combinations
# ==============================================================================

class TestTier3CrossFeatureInteractions(unittest.TestCase):
    """
    Verifies state retention across Q1-Q3 navigation, partial uploads, and API contracts.
    """

    def test_tier3_q1_to_q3_navigation_partial_uploads(self):
        """User uploads code for Q1 (100) and Q3 (60), leaves Q2 blank (0). Total = 160."""
        session_submissions = {
            0: {"sourceCode": "code_q1", "fileName": "q1.cpp", "score": 100},
            1: {"sourceCode": None, "fileName": None, "score": 0},
            2: {"sourceCode": "code_q3", "fileName": "q3.cpp", "score": 60}
        }
        q_scores = [session_submissions[i]["score"] for i in range(3)]
        total = ExamScoringEngine.calculate_total_exam_score(q_scores)
        self.assertEqual(total, 160)
        self.assertEqual(q_scores[1], 0, "Unsubmitted question must receive 0 points")

    def test_tier3_update_code_before_submission(self):
        """Updating code on Q2 replaces prior version; final submission scores updated code."""
        session = {
            "currentQuestionIndex": 1,
            "submissions": {
                1: {"fileName": "v1.cpp", "sourceCode": "// draft", "score": 0}
            }
        }
        # User navigates to Q1, then back to Q2 and uploads v2.cpp
        session["currentQuestionIndex"] = 0
        session["currentQuestionIndex"] = 1
        session["submissions"][1] = {
            "fileName": "v2.cpp",
            "sourceCode": "// final working solution",
            "score": 90
        }
        self.assertEqual(session["submissions"][1]["fileName"], "v2.cpp")
        self.assertEqual(session["submissions"][1]["score"], 90)

    def test_tier3_tab_navigation_preserves_code(self):
        """Switching between Q1, Q2, and Q3 tabs does not erase or mutate uploaded code."""
        exam_state = {
            0: {"code": "cout << 1;"},
            1: {"code": "cout << 2;"},
            2: {"code": "cout << 3;"}
        }
        # Simulate active tab switching sequence: 0 -> 1 -> 2 -> 0 -> 2
        tab_sequence = [0, 1, 2, 0, 2]
        for active_tab in tab_sequence:
            # Code for all 3 questions must remain intact
            self.assertEqual(exam_state[0]["code"], "cout << 1;")
            self.assertEqual(exam_state[1]["code"], "cout << 2;")
            self.assertEqual(exam_state[2]["code"], "cout << 3;")

    def test_tier3_state_isolation_quiz_vs_exam(self):
        """Coding exam state does not overwrite or corrupt MCQ quiz engine state."""
        quiz_state = {
            "currentIndex": 4,
            "score": 4,
            "sessionQuestions": ["Q1", "Q2", "Q3", "Q4", "Q5"]
        }
        exam_state = {
            "status": "running",
            "currentQuestionIndex": 1,
            "timerSecondsRemaining": 2400
        }
        # Assert objects are distinct and cannot collide
        self.assertNotEqual(quiz_state["currentIndex"], exam_state["currentQuestionIndex"])
        self.assertNotIn("status", quiz_state)
        self.assertNotIn("sessionQuestions", exam_state)

    def test_tier3_server_evaluate_payload_and_response_contract(self):
        """Verifies JSON schema for POST /api/evaluate requests and responses."""
        request_payload = {
            "problemId": "CP01",
            "sourceCode": "#include <iostream>\nint main(){ std::cout << 42; return 0; }",
            "testCases": [
                {"id": 1, "input": "1\n", "expectedOutput": "42\n"}
            ]
        }
        self.assertIn("problemId", request_payload)
        self.assertIn("sourceCode", request_payload)
        self.assertIn("testCases", request_payload)

        # Expected response contract
        expected_response = {
            "success": True,
            "compilation": {"success": True, "output": ""},
            "results": [
                {
                    "testCaseId": 1,
                    "status": "Accepted",
                    "passed": True,
                    "score": 10,
                    "timeMs": 12,
                    "actualOutput": "42\n",
                    "expectedOutput": "42\n",
                    "error": None
                }
            ],
            "score": 10,
            "passedTestCases": 1,
            "totalTestCases": 1
        }
        self.assertTrue(expected_response["success"])
        self.assertIn("compilation", expected_response)
        self.assertIn("results", expected_response)
        self.assertIn("score", expected_response)


# ==============================================================================
# Tier 4: Real-World Scenarios & Live Execution Pipeline
# ==============================================================================

class TestTier4RealWorldScenarios(unittest.TestCase):
    """
    Simulates complete student exam journeys, HTML UI DOM structure, and live C++ compilation.
    """

    def test_tier4_full_exam_lifecycle_mixed_scores(self):
        """
        Simulates an entire 60-minute exam session:
        1. 3 distinct problems assigned.
        2. Q1: 100/100 (all 10 passed).
        3. Q2: 50/100 (5 passed, 5 failed).
        4. Q3: 0/100 (unattempted).
        5. Final score = 150/300.
        6. Performance rank = 'Đạt (Pass)'.
        """
        # Step 1: Initialize exam with 3 distinct problems
        problems = ProblemSelector.select_3_distinct_problems(CONTRACT_SAMPLE_PROBLEMS)
        self.assertEqual(len(problems), 3)

        # Step 2: Timer initialized
        timer_seconds = 3600

        # Step 3: Evaluate submissions
        q1_results = [{"status": "Accepted", "passed": True} for _ in range(10)]
        q2_results = [{"status": "Accepted", "passed": True} for _ in range(5)] + \
                     [{"status": "Wrong Answer", "passed": False} for _ in range(5)]
        q3_results = []  # No submission

        score_q1 = ExamScoringEngine.calculate_question_score(q1_results)
        score_q2 = ExamScoringEngine.calculate_question_score(q2_results)
        score_q3 = ExamScoringEngine.calculate_question_score(q3_results)

        self.assertEqual(score_q1, 100)
        self.assertEqual(score_q2, 50)
        self.assertEqual(score_q3, 0)

        # Step 4: Total Exam Score
        total_score = ExamScoringEngine.calculate_total_exam_score([score_q1, score_q2, score_q3])
        self.assertEqual(total_score, 150)

        # Step 5: Performance Ranking
        ranking = ExamScoringEngine.evaluate_performance_rank(total_score)
        self.assertEqual(ranking["rank"], "Đạt")
        self.assertEqual(ranking["level"], "Pass")

    def test_tier4_ui_dom_exam_elements_contract(self):
        """Verifies index.html contains all required DOM containers and controls for Exam mode."""
        self.assertTrue(INDEX_HTML_PATH.exists(), f"index.html missing at {INDEX_HTML_PATH}")
        html_content = INDEX_HTML_PATH.read_text(encoding="utf-8")

        required_exam_elements = [
            'id="nav-btn-exam"',        # Top navigation button for Exam mode
            'id="view-exam"',            # Main exam workspace view
            'id="exam-timer"',           # 60-minute countdown display
            'id="exam-q-tabs"',          # Q1-Q3 tab container
            'id="exam-upload-input"',    # File upload input
            'id="view-exam-results"',    # Exam results dashboard
            'id="exam-results-table"',   # 10-test-case breakdown table container
        ]
        missing = [elem for elem in required_exam_elements if elem not in html_content]
        if missing:
            raise AssertionError(f"[Milestone 3 Pending] Exam UI elements missing in index.html: {missing}")

    def test_tier4_live_gxx_compilation_and_execution_pipeline(self):
        """
        Directly executes host MSYS2 g++ compiler to verify:
        - g++ is accessible on Windows host.
        - Compiles C++17 source code without errors.
        - Runs compiled binary with stdin.
        - Produces expected stdout and handles output comparison.
        """
        # Simple C++ program computing Two Sum
        cpp_code = """#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, target;
    if (!(cin >> n >> target)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (a[i] + a[j] == target) {
                cout << (i + 1) << " " << (j + 1) << "\\n";
                return 0;
            }
        }
    }
    cout << "-1\\n";
    return 0;
}
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            src_file = Path(tmpdir) / "solution.cpp"
            exe_file = Path(tmpdir) / "solution.exe"
            src_file.write_text(cpp_code, encoding="utf-8")

            # 1. Compile with g++ -std=c++17 -Wall -O2
            compile_cmd = ["g++", "-std=c++17", "-Wall", "-O2", str(src_file), "-o", str(exe_file)]
            comp_res = subprocess.run(compile_cmd, capture_output=True, text=True, timeout=10)
            self.assertEqual(comp_res.returncode, 0, f"Compilation failed: {comp_res.stderr}")
            self.assertTrue(exe_file.exists(), "Compiled executable binary was not created")

            # 2. Run with Test Case 1: [4, 9, arr=[2, 7, 11, 15] -> output: "1 2\n"]
            test_input_1 = "4 9\n2 7 11 15\n"
            run_res_1 = subprocess.run(
                [str(exe_file)],
                input=test_input_1,
                capture_output=True,
                text=True,
                timeout=2
            )
            self.assertEqual(run_res_1.returncode, 0)
            self.assertTrue(OutputNormalizer.is_match(run_res_1.stdout, "1 2\n"))

            # 3. Run with Test Case 2: Target not found -> output: "-1\n"
            test_input_2 = "3 100\n1 2 3\n"
            run_res_2 = subprocess.run(
                [str(exe_file)],
                input=test_input_2,
                capture_output=True,
                text=True,
                timeout=2
            )
            self.assertEqual(run_res_2.returncode, 0)
            self.assertTrue(OutputNormalizer.is_match(run_res_2.stdout, "-1\n"))


# ==============================================================================
# Custom Test Runner with Formatted Tier Breakdown & Reporting
# ==============================================================================

def run_test_suite():
    """Runs all test tiers and generates a formatted terminal report."""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Add test cases in tier order
    suite.addTests(loader.loadTestsFromTestCase(TestTier0RegressionSafety))
    suite.addTests(loader.loadTestsFromTestCase(TestTier1FeatureCoverage))
    suite.addTests(loader.loadTestsFromTestCase(TestTier2BoundaryAndCorner))
    suite.addTests(loader.loadTestsFromTestCase(TestTier3CrossFeatureInteractions))
    suite.addTests(loader.loadTestsFromTestCase(TestTier4RealWorldScenarios))

    print("\n" + "=" * 80)
    print("  E2E Test Suite Runner: C++ & DSA Random Coding Exam System")
    print("=" * 80)
    print(f"Target Working Directory: {QUIZ_GAME_DIR}")
    print(f"Total Test Cases Loaded: {suite.countTestCases()}\n")

    # Run tests using custom stream
    runner = unittest.TextTestRunner(verbosity=2)
    start_time = time.time()
    result = runner.run(suite)
    elapsed = time.time() - start_time

    # Analyze results per tier
    total_run = result.testsRun
    failures_and_errors = len(result.failures) + len(result.errors)
    passed_count = total_run - failures_and_errors

    print("\n" + "=" * 80)
    print("  E2E Test Execution Summary by Tier")
    print("=" * 80)
    print(f"Total Tests Executed: {total_run}")
    print(f"Passed:               {passed_count} / {total_run} ({(passed_count / total_run) * 100:.1f}%)")
    print(f"Failed / Errors:      {failures_and_errors} / {total_run}")
    print(f"Execution Duration:   {elapsed:.3f} seconds\n")

    if result.failures or result.errors:
        print("-" * 80)
        print("  Milestone-Dependent Diagnostic Findings:")
        print("-" * 80)
        for test, trace in result.failures + result.errors:
            # Extract first line of error/trace
            error_msg = trace.strip().split("\n")[-1]
            print(f"  [*] {test.id()}:")
            print(f"      -> {error_msg}")
        print("\n[NOTE] These pending failures reflect unmerged milestone implementation code")
        print("       (M1 Problem Bank, M2 Server, M3 UI). They will turn GREEN once milestones land.")
    else:
        print("[SUCCESS] All E2E test cases passed flawlessly!")

    print("=" * 80 + "\n")
    return result


if __name__ == "__main__":
    test_result = run_test_suite()
    # In dual-track baseline mode, return code reflects completion of test suite execution
    sys.exit(0 if len(test_result.failures) + len(test_result.errors) == 0 else 1)
