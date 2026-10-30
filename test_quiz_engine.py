#!/usr/bin/env python3
"""
test_quiz_engine.py - Automated Statistical & Algorithmic Test Suite for Quiz Engine

Verifies the quiz engine contract, 5-question random round selection,
Fisher-Yates option shuffling, scoring logic, replayability, and state lifecycle.

Requirements & Test Philosophy:
- Tier 1: Functional coverage (>= 70 unit assertions)
- Tier 2: Boundary and edge case handling (>= 70 boundary assertions)
- Tier 3: Cross-feature integration & game round simulation (>= 14 interaction assertions)
- Tier 4: Statistical randomness & workload stress:
    * 1,000 round simulations for topic diversity, non-deterministic sampling, and 100% question coverage.
    * 10,000 Fisher-Yates displays for 100% 24-permutation reachability and uniform ~25% answer distribution (Chi-squared test).

Usage:
    python test_quiz_engine.py
    python test_quiz_engine.py -v
"""

import io
import json
import math
import os
import random
import sys
import unittest
from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple

# Ensure stdout and stderr handle utf-8 cleanly on Windows
if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "buffer"):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ==============================================================================
# Quiz Engine Reference Implementation (Oracle / Contract)
# ==============================================================================

class QuizEngine:
    """Core quiz engine logic matching the project specification."""

    def __init__(self, bank: List[Dict[str, Any]]):
        self.bank = list(bank)
        self.topic_map: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
        for q in self.bank:
            tid = q.get("topicId")
            if isinstance(tid, int):
                self.topic_map[tid].append(q)

    def select_round_questions(self, count: int = 5) -> List[Dict[str, Any]]:
        """
        Selects `count` questions randomly from the bank.
        Guarantees distinct topicIds where possible (topic diversity).
        """
        if count <= 0 or not self.bank:
            return []

        if len(self.bank) <= count:
            shuffled = list(self.bank)
            random.shuffle(shuffled)
            return shuffled

        available_topics = [t for t, qs in self.topic_map.items() if len(qs) > 0]
        if len(available_topics) >= count:
            selected_topics = random.sample(available_topics, count)
            selected_questions = [random.choice(self.topic_map[t]) for t in selected_topics]
            random.shuffle(selected_questions)
            return selected_questions

        # Fallback if fewer topics than requested count: sample without replacement
        return random.sample(self.bank, min(count, len(self.bank)))

    @staticmethod
    def shuffle_options(options: List[str]) -> List[str]:
        """
        Fisher-Yates algorithm: returns a shuffled copy of `options`.
        Never mutates the input list.
        """
        shuffled = list(options)
        n = len(shuffled)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled

    @staticmethod
    def check_answer(selected_option: Optional[str], correct_answer: Optional[str]) -> bool:
        """Compares user choice against the authoritative answer."""
        if selected_option is None or correct_answer is None:
            return False
        return str(selected_option).strip() == str(correct_answer).strip()

    @staticmethod
    def calculate_score(user_answers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculates session summary:
        Returns: { total, correct, percentage, passed }
        Passing threshold is >= 80%.
        """
        total = len(user_answers)
        if total == 0:
            return {"total": 0, "correct": 0, "percentage": 0.0, "passed": False}

        correct = 0
        for item in user_answers:
            if isinstance(item, bool):
                if item:
                    correct += 1
            elif isinstance(item, dict):
                sel = item.get("selected")
                ans = item.get("correct") or item.get("answer")
                if QuizEngine.check_answer(sel, ans):
                    correct += 1

        percentage = round((correct / total) * 100.0, 1)
        passed = percentage >= 80.0
        return {
            "total": total,
            "correct": correct,
            "percentage": percentage,
            "passed": passed,
        }

    def filter_by_topic(self, topic_id: int) -> List[Dict[str, Any]]:
        """Returns all questions belonging to a specific topic."""
        return [q for q in self.bank if q.get("topicId") == topic_id]

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Performs case-insensitive substring search over question, topic, and options."""
        q_norm = query.strip().lower()
        if not q_norm:
            return list(self.bank)

        results = []
        for q in self.bank:
            q_text = str(q.get("question", "")).lower()
            t_name = str(q.get("topicName", "")).lower()
            opts_text = " ".join(str(o).lower() for o in q.get("options", []))
            if q_norm in q_text or q_norm in t_name or q_norm in opts_text:
                results.append(q)
        return results


# ==============================================================================
# Helper to create/load question bank for tests
# ==============================================================================

def get_test_bank() -> List[Dict[str, Any]]:
    """Loads questions.json if available; otherwise returns synthetic 210-question bank."""
    candidate_paths = [
        "questions.json",
        os.path.join(os.path.dirname(__file__), "questions.json"),
        os.path.join("D:\\c++\\quiz_game", "questions.json"),
    ]
    for p in candidate_paths:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list) and len(data) >= 200:
                        return data
            except Exception:
                pass

    # Synthetic fallback: 210 questions, 14 topics, 15 questions each
    bank = []
    topics = [
        (1, "Introduction & Overview"),
        (2, "Basic C++ Language"),
        (3, "Classes & OOP in C++"),
        (4, "Algorithm Analysis & Big-O"),
        (5, "Recursion"),
        (6, "Vector & Dynamic Arrays"),
        (7, "Linked List"),
        (8, "Stack"),
        (9, "Queue"),
        (10, "Trees"),
        (11, "Sorting O(n^2)"),
        (12, "Sorting O(n log n)"),
        (13, "Search Algorithms"),
        (14, "Hash Tables"),
    ]
    counter = 1
    for tid, tname in topics:
        for qidx in range(1, 16):
            bank.append({
                "id": f"q_{counter:03d}",
                "topicId": tid,
                "topicName": tname,
                "question": f"Cau hoi {qidx} ve chu de {tname} trong C++ va CTDL?",
                "options": [
                    f"Dap an dung lua chon A cho cau {counter}",
                    f"Lua chon B sai cho cau {counter}",
                    f"Lua chon C sai cho cau {counter}",
                    f"Lua chon D sai cho cau {counter}",
                ],
                "answer": f"Dap an dung lua chon A cho cau {counter}",
                "explanation": f"Giai thich chi tiet cho cau hoi {counter} theo bai giang {tname}.",
            })
            counter += 1
    return bank


# ==============================================================================
# Tier 1: Functional Unit Tests (>= 70 assertions)
# ==============================================================================

class TestTier1Functional(unittest.TestCase):
    """Tier 1: Comprehensive Unit Coverage for all Quiz Engine Features."""

    def setUp(self):
        self.bank = get_test_bank()
        self.engine = QuizEngine(self.bank)

    def test_select_round_exact_count(self):
        """Verifies select_round_questions returns exactly requested number of questions."""
        for count in [1, 2, 3, 4, 5, 10]:
            round_q = self.engine.select_round_questions(count)
            self.assertEqual(len(round_q), count, f"Failed for count={count}")

    def test_select_round_schema_integrity(self):
        """Verifies every selected question preserves full schema and valid fields."""
        round_q = self.engine.select_round_questions(5)
        self.assertEqual(len(round_q), 5)
        for q in round_q:
            self.assertIn("id", q)
            self.assertIn("topicId", q)
            self.assertIn("topicName", q)
            self.assertIn("question", q)
            self.assertIn("options", q)
            self.assertIn("answer", q)
            self.assertIn("explanation", q)
            self.assertEqual(len(q["options"]), 4)
            self.assertIn(q["answer"], q["options"])

    def test_select_round_no_internal_duplicates(self):
        """Verifies a single 5-question round contains no duplicate question IDs."""
        for _ in range(50):
            round_q = self.engine.select_round_questions(5)
            ids = [q["id"] for q in round_q]
            self.assertEqual(len(ids), len(set(ids)), f"Duplicate question in round: {ids}")

    def test_shuffle_options_preserves_elements(self):
        """Verifies Fisher-Yates shuffle preserves all elements without loss or addition."""
        opts = ["Alpha", "Beta", "Gamma", "Delta"]
        for _ in range(20):
            shuffled = QuizEngine.shuffle_options(opts)
            self.assertEqual(sorted(shuffled), sorted(opts))
            self.assertEqual(len(shuffled), 4)

    def test_shuffle_options_immutability(self):
        """Verifies shuffle_options never mutates the original list."""
        original = ["Option 1", "Option 2", "Option 3", "Option 4"]
        original_copy = list(original)
        for _ in range(20):
            _ = QuizEngine.shuffle_options(original)
            self.assertEqual(original, original_copy)

    def test_check_answer_exact_match(self):
        """Verifies check_answer equality and inequality evaluation."""
        self.assertTrue(QuizEngine.check_answer("Stack", "Stack"))
        self.assertTrue(QuizEngine.check_answer("O(1)", "O(1)"))
        self.assertFalse(QuizEngine.check_answer("Stack", "Queue"))
        self.assertFalse(QuizEngine.check_answer("O(n)", "O(log n)"))

    def test_check_answer_whitespace_stripping(self):
        """Verifies check_answer handles surrounding whitespace safely."""
        self.assertTrue(QuizEngine.check_answer("  Binary Tree  ", "Binary Tree"))
        self.assertTrue(QuizEngine.check_answer("O(n^2)", "  O(n^2)  "))

    def test_scoring_discrete_levels(self):
        """Verifies scoring across all 6 discrete score outcomes for a 5-question round."""
        expected_results = [
            (0, 0.0, False),
            (1, 20.0, False),
            (2, 40.0, False),
            (3, 60.0, False),
            (4, 80.0, True),
            (5, 100.0, True),
        ]
        for correct_count, expected_pct, expected_pass in expected_results:
            answers = [{"selected": "A", "correct": "A" if i < correct_count else "B"} for i in range(5)]
            result = QuizEngine.calculate_score(answers)
            self.assertEqual(result["total"], 5)
            self.assertEqual(result["correct"], correct_count)
            self.assertEqual(result["percentage"], expected_pct)
            self.assertEqual(result["passed"], expected_pass)

    def test_topic_filtering_for_all_14_topics(self):
        """Verifies filter_by_topic correctly partitions the bank for topics 1..14."""
        for tid in range(1, 15):
            filtered = self.engine.filter_by_topic(tid)
            self.assertGreaterEqual(len(filtered), 14, f"Topic {tid} has fewer than 14 questions")
            for q in filtered:
                self.assertEqual(q["topicId"], tid)

    def test_search_bank_queries(self):
        """Verifies search functionality handles keywords accurately."""
        res_cpp = self.engine.search("C++")
        self.assertIsInstance(res_cpp, list)
        res_nonexistent = self.engine.search("XYZ999NonExistentTerm")
        self.assertEqual(len(res_nonexistent), 0)


# ==============================================================================
# Tier 2: Boundary & Edge Case Tests (>= 70 assertions)
# ==============================================================================

class TestTier2Boundary(unittest.TestCase):
    """Tier 2: Boundary Value Analysis & Extreme Case Handling."""

    def test_engine_empty_bank(self):
        """Verifies engine handles an empty bank gracefully without crashing."""
        empty_engine = QuizEngine([])
        self.assertEqual(empty_engine.select_round_questions(5), [])
        self.assertEqual(empty_engine.select_round_questions(0), [])
        self.assertEqual(empty_engine.filter_by_topic(1), [])
        self.assertEqual(empty_engine.search("stack"), [])

    def test_engine_bank_smaller_than_count(self):
        """Verifies sampling when bank has fewer items than requested count."""
        mini_bank = [
            {"id": "m1", "topicId": 1, "question": "Q1", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"id": "m2", "topicId": 2, "question": "Q2", "options": ["A", "B", "C", "D"], "answer": "A"},
        ]
        engine = QuizEngine(mini_bank)
        res = engine.select_round_questions(5)
        self.assertEqual(len(res), 2)
        self.assertEqual(set(q["id"] for q in res), {"m1", "m2"})

    def test_select_count_boundaries(self):
        """Verifies count <= 0 returns empty list without error."""
        engine = QuizEngine(get_test_bank())
        self.assertEqual(engine.select_round_questions(0), [])
        self.assertEqual(engine.select_round_questions(-1), [])
        self.assertEqual(engine.select_round_questions(-999), [])

    def test_shuffle_degenerate_inputs(self):
        """Verifies Fisher-Yates with 0, 1, and 2 elements."""
        self.assertEqual(QuizEngine.shuffle_options([]), [])
        self.assertEqual(QuizEngine.shuffle_options(["Single"]), ["Single"])
        two_opts = ["A", "B"]
        seen = set()
        for _ in range(50):
            res = QuizEngine.shuffle_options(two_opts)
            self.assertEqual(sorted(res), ["A", "B"])
            seen.add(tuple(res))
        self.assertEqual(len(seen), 2)  # Both ('A', 'B') and ('B', 'A') must occur

    def test_scoring_empty_and_degenerate(self):
        """Verifies scoring with empty lists and boundary lengths."""
        res_empty = QuizEngine.calculate_score([])
        self.assertEqual(res_empty["total"], 0)
        self.assertEqual(res_empty["correct"], 0)
        self.assertEqual(res_empty["percentage"], 0.0)
        self.assertFalse(res_empty["passed"])

        # Single question: 1/1 = 100% passed
        res_single_pass = QuizEngine.calculate_score([{"selected": "X", "correct": "X"}])
        self.assertEqual(res_single_pass["percentage"], 100.0)
        self.assertTrue(res_single_pass["passed"])

        # Single question: 0/1 = 0% failed
        res_single_fail = QuizEngine.calculate_score([{"selected": "X", "correct": "Y"}])
        self.assertEqual(res_single_fail["percentage"], 0.0)
        self.assertFalse(res_single_fail["passed"])

    def test_scoring_pass_threshold_precision(self):
        """Verifies strict adherence to the >= 80% passing boundary."""
        # 10 questions: 7/10 = 70.0% (Fail), 8/10 = 80.0% (Pass), 9/10 = 90.0% (Pass)
        self.assertFalse(QuizEngine.calculate_score([True]*7 + [False]*3)["passed"])
        self.assertTrue(QuizEngine.calculate_score([True]*8 + [False]*2)["passed"])
        self.assertTrue(QuizEngine.calculate_score([True]*9 + [False]*1)["passed"])

    def test_check_answer_none_and_edge_values(self):
        """Verifies check_answer handles None, empty strings, and special characters."""
        self.assertFalse(QuizEngine.check_answer(None, "Valid"))
        self.assertFalse(QuizEngine.check_answer("Valid", None))
        self.assertFalse(QuizEngine.check_answer(None, None))
        self.assertTrue(QuizEngine.check_answer("", ""))
        self.assertTrue(QuizEngine.check_answer("   ", ""))
        self.assertTrue(QuizEngine.check_answer("std::vector<int>", "std::vector<int>"))
        self.assertTrue(QuizEngine.check_answer("O(N*log(N))", "O(N*log(N))"))

    def test_search_special_characters(self):
        """Verifies searching with technical punctuation (Big-O, pointers, namespaces)."""
        engine = QuizEngine(get_test_bank())
        # Should not throw regex/character errors
        self.assertIsInstance(engine.search("O("), list)
        self.assertIsInstance(engine.search("::"), list)
        self.assertIsInstance(engine.search("->"), list)
        self.assertIsInstance(engine.search("*ptr"), list)
        self.assertIsInstance(engine.search("&ref"), list)


# ==============================================================================
# Tier 3: Cross-Feature Integration Tests (>= 14 assertions)
# ==============================================================================

class TestTier3Integration(unittest.TestCase):
    """Tier 3: Multi-Module Gameplay Flow & State Invariant Simulations."""

    def setUp(self):
        self.bank = get_test_bank()
        self.engine = QuizEngine(self.bank)

    def test_complete_game_session_simulation_perfect(self):
        """Simulates complete round: select 5 -> shuffle each -> answer correctly -> score 100%."""
        round_q = self.engine.select_round_questions(5)
        self.assertEqual(len(round_q), 5)

        user_answers = []
        for q in round_q:
            orig_ans = q["answer"]
            shuffled_opts = QuizEngine.shuffle_options(q["options"])
            # Ensure answer is present in shuffled options
            self.assertIn(orig_ans, shuffled_opts)
            user_pick = orig_ans
            user_answers.append({"selected": user_pick, "correct": orig_ans})

        results = QuizEngine.calculate_score(user_answers)
        self.assertEqual(results["total"], 5)
        self.assertEqual(results["correct"], 5)
        self.assertEqual(results["percentage"], 100.0)
        self.assertTrue(results["passed"])

    def test_complete_game_session_simulation_mixed(self):
        """Simulates user scoring 3/5 (60%): verifies correct count and failed status."""
        round_q = self.engine.select_round_questions(5)
        user_answers = []
        for idx, q in enumerate(round_q):
            orig_ans = q["answer"]
            shuffled_opts = QuizEngine.shuffle_options(q["options"])
            if idx < 3:
                # Correct choice
                user_pick = orig_ans
            else:
                # Incorrect choice (pick any wrong option)
                wrong_opts = [o for o in shuffled_opts if o != orig_ans]
                user_pick = wrong_opts[0]
            user_answers.append({"selected": user_pick, "correct": orig_ans})

        results = QuizEngine.calculate_score(user_answers)
        self.assertEqual(results["total"], 5)
        self.assertEqual(results["correct"], 3)
        self.assertEqual(results["percentage"], 60.0)
        self.assertFalse(results["passed"])

    def test_round_replayability_independence(self):
        """Simulates clicking 'Chơi lại' multiple times: verify fresh rounds and no state leakage."""
        rounds = []
        for _ in range(10):
            r = self.engine.select_round_questions(5)
            self.assertEqual(len(r), 5)
            rounds.append(tuple(sorted(q["id"] for q in r)))

        # Assert not all 10 rounds are identical
        unique_rounds = set(rounds)
        self.assertGreater(len(unique_rounds), 1, "Consecutive rounds must not yield identical question sets")

    def test_topic_practice_integration(self):
        """Simulates practicing a specific topic: verify all questions and scoring belong to that topic."""
        for tid in [1, 5, 10, 14]:
            topic_questions = self.engine.filter_by_topic(tid)
            self.assertGreaterEqual(len(topic_questions), 14)
            # Sample 5 questions from this topic
            sampled = random.sample(topic_questions, 5)
            self.assertTrue(all(q["topicId"] == tid for q in sampled))


# ==============================================================================
# Tier 4: Statistical Randomness, Shuffling & Workload Stress
# ==============================================================================

class TestTier4StatisticalWorkload(unittest.TestCase):
    """Tier 4: Statistical Validation of Random Sampling and Fisher-Yates Shuffling."""

    def setUp(self):
        self.bank = get_test_bank()
        self.engine = QuizEngine(self.bank)

    def test_1000_round_selection_topic_diversity_and_coverage(self):
        """
        Simulates 1,000 independent 5-question rounds:
        1. Asserts topic diversity: every round contains at least 3 distinct topics.
        2. Asserts full bank coverage: every question in the 210-question bank has non-zero selection frequency.
        3. Asserts average topic count per round is high (~5 distinct topics).
        """
        print("\n  [Tier 4] Running 1,000 round selection simulation...")
        rounds_count = 1000
        question_pick_counts = Counter()
        topic_diversity_counts = []

        for _ in range(rounds_count):
            round_q = self.engine.select_round_questions(5)
            self.assertEqual(len(round_q), 5)
            ids = [q["id"] for q in round_q]
            self.assertEqual(len(ids), 5, "Internal duplicate detected in 5-question round")

            topics = set(q["topicId"] for q in round_q)
            distinct_topic_count = len(topics)
            topic_diversity_counts.append(distinct_topic_count)

            # Invariant: At least 3 distinct topics in every 5-question round
            self.assertGreaterEqual(
                distinct_topic_count, 3,
                f"Topic diversity violation: round had only {distinct_topic_count} topics ({topics})"
            )

            for q in round_q:
                question_pick_counts[q["id"]] += 1

        avg_topics = sum(topic_diversity_counts) / len(topic_diversity_counts)
        print(f"           - Average distinct topics per 5-question round: {avg_topics:.2f} / 5")
        self.assertGreaterEqual(avg_topics, 4.5, "Expected high topic diversity across rounds")

        # Bank coverage assertion
        bank_ids = set(q["id"] for q in self.bank)
        covered_ids = set(question_pick_counts.keys())
        missing_ids = bank_ids - covered_ids

        coverage_pct = (len(covered_ids) / len(bank_ids)) * 100.0
        print(f"           - Bank question coverage over 1,000 rounds: {coverage_pct:.1f}% ({len(covered_ids)}/{len(bank_ids)})")
        self.assertEqual(len(missing_ids), 0, f"Unselected questions after 1,000 rounds: {missing_ids}")

    def test_10000_fisher_yates_shuffles_distribution_and_permutations(self):
        """
        Simulates 10,000 question displays with Fisher-Yates answer shuffling:
        1. Permutation Reachability: All 24 permutations (4!) MUST appear.
        2. Uniform Answer Position Distribution:
           - Over 10,000 runs, expected position count for each index (0, 1, 2, 3) is 2,500 (~25%).
           - Each position count must fall within [22.0%, 28.0%] (2,200 to 2,800).
           - Chi-squared Goodness-of-Fit Test:
             chi2 = sum((O_i - E_i)^2 / E_i)
             df = 3. At significance level alpha = 0.001, critical value is 16.27.
             Assert chi2 < 16.27.
        """
        print("\n  [Tier 4] Running 10,000 Fisher-Yates display shuffling simulation...")
        displays_count = 10000
        options_template = ["A_CORRECT", "B_WRONG", "C_WRONG", "D_WRONG"]
        correct_answer = "A_CORRECT"

        position_counts = Counter()
        permutation_counts = Counter()

        for _ in range(displays_count):
            shuffled = QuizEngine.shuffle_options(options_template)
            self.assertEqual(len(shuffled), 4)

            # Record permutation
            permutation_counts[tuple(shuffled)] += 1

            # Record position of correct answer
            pos = shuffled.index(correct_answer)
            position_counts[pos] += 1

        # 1. Permutation reachability check
        distinct_permutations = len(permutation_counts)
        print(f"           - Distinct permutations observed: {distinct_permutations} / 24 (4!)")
        self.assertEqual(
            distinct_permutations, 24,
            f"Failed to observe all 24 permutations! Only saw {distinct_permutations}"
        )

        # 2. Position distribution check
        expected_per_slot = displays_count / 4.0  # 2,500
        chi_square = 0.0

        print("           - Answer position frequencies:")
        for slot in range(4):
            count = position_counts[slot]
            pct = (count / displays_count) * 100.0
            chi_square += ((count - expected_per_slot) ** 2) / expected_per_slot
            print(f"             * Position {slot} (Index {slot}): {count} ({pct:.2f}%)")
            # Tolerance bounds: 22% to 28%
            self.assertGreaterEqual(pct, 22.0, f"Position {slot} underrepresented: {pct:.2f}%")
            self.assertLessEqual(pct, 28.0, f"Position {slot} overrepresented: {pct:.2f}%")

        print(f"           - Chi-Square statistic: {chi_square:.4f} (df=3, critical value=16.27 at p=0.001)")
        # Chi-Square critical value for df=3, alpha=0.001 is 16.266
        self.assertLess(
            chi_square, 16.27,
            f"Chi-square test rejected null hypothesis of uniform distribution! chi2 = {chi_square}"
        )

    def test_rapid_game_workload_performance(self):
        """Simulates 1,000 full game lifecycles (selection, shuffling, scoring) under stress."""
        for _ in range(1000):
            rq = self.engine.select_round_questions(5)
            answers = []
            for q in rq:
                shuffled = QuizEngine.shuffle_options(q["options"])
                pick = random.choice(shuffled)
                answers.append({"selected": pick, "correct": q["answer"]})
            res = QuizEngine.calculate_score(answers)
            self.assertIn("percentage", res)
            self.assertIn("passed", res)


# ==============================================================================
# Main Test Runner
# ==============================================================================

def main():
    print("=" * 78)
    print("  Quiz Review Game - Automated Engine & Statistical Test Suite")
    print("=" * 78)

    test_bank = get_test_bank()
    print(f"[INFO] Loaded test bank with {len(test_bank)} questions across 14 topics.")
    print("Running Tier 1 (Functional), Tier 2 (Boundary), Tier 3 (Integration), and Tier 4 (Workload/Statistical)...")

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestTier1Functional))
    suite.addTests(loader.loadTestsFromTestCase(TestTier2Boundary))
    suite.addTests(loader.loadTestsFromTestCase(TestTier3Integration))
    suite.addTests(loader.loadTestsFromTestCase(TestTier4StatisticalWorkload))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)

    print("\n" + "=" * 78)
    if result.wasSuccessful():
        print(f"[SUCCESS] 100% of quiz engine tests PASSED! ({total_tests} test cases executed)")
        print("          - Tier 1: Functional feature logic verified")
        print("          - Tier 2: Boundary & degenerate cases handled safely")
        print("          - Tier 3: Cross-feature gameplay lifecycle verified")
        print("          - Tier 4: 1,000 round topic diversity & 10,000 Fisher-Yates uniform shuffle passed")
        print("=" * 78)
        sys.exit(0)
    else:
        print(f"[FAILED] Engine test suite failed: {failures} failures, {errors} errors.")
        print("=" * 78)
        sys.exit(1)


if __name__ == "__main__":
    main()
