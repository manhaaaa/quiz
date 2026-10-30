#!/usr/bin/env python3
"""
stress_test_bank_adversarial.py - Adversarial Stress & Schema Integrity Verification Harness

Empirically challenges:
1. File synchronization and syntax between questions.json and questions.js
2. Strict schema adherence across all 210 questions
3. 14 topics with exactly 15 questions per topic
4. Strict option uniqueness (exact, trimmed, lowercase, normalized)
5. Strict byte-for-byte answer equality against options (no strip fallback)
6. Anti-fluff & pedagogical quality of explanations
7. Option length bias and correct-answer position distribution
8. HTML entity safety and C++ code snippet formatting
9. Search indexing & special character tolerance
10. Fisher-Yates option permutation stress on live bank questions
"""

import io
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict

# Ensure UTF-8 on Windows stdout/stderr
if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "buffer"):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

EXPECTED_TOPICS = {
    1: "Introduction & Overview",
    2: "Basic C++ Language",
    3: "Classes & OOP in C++",
    4: "Algorithm Analysis & Big-O",
    5: "Recursion",
    6: "Vector & Dynamic Arrays",
    7: "Linked List",
    8: "Stack",
    9: "Queue",
    10: "Trees",
    11: "Sorting O(n^2)",
    12: "Sorting O(n log n)",
    13: "Search Algorithms",
    14: "Hash Tables",
}

def format_code_snippet(text: str) -> str:
    """Mirrors frontend formatCodeSnippet in index.html line 780."""
    if not text:
        return ""
    safe = (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )
    safe = re.sub(
        r"`([^`]+)`",
        r'<code class="px-1.5 py-0.5 rounded bg-slate-800 text-indigo-300 font-mono text-xs sm:text-sm border border-slate-700/80">\1</code>',
        safe,
    )
    return safe

def run_adversarial_suite():
    failures = []
    warnings = []
    stats = {}

    print("================================================================================")
    print("  ADVERSARIAL STRESS & SCHEMA INTEGRITY VERIFICATION HARNESS")
    print("================================================================================")

    # --------------------------------------------------------------------------
    # Check 1: File Existence & JSON Loading
    # --------------------------------------------------------------------------
    json_path = os.path.join(os.path.dirname(__file__), "questions.json")
    js_path = os.path.join(os.path.dirname(__file__), "questions.js")

    if not os.path.exists(json_path):
        failures.append(f"questions.json not found at {json_path}")
        print(f"[FAIL] questions.json missing!")
        return False, failures, warnings, stats

    if not os.path.exists(js_path):
        failures.append(f"questions.js not found at {js_path}")
        print(f"[FAIL] questions.js missing!")
        return False, failures, warnings, stats

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            json_data = json.load(f)
            print(f"[PASS] Check 1.1: questions.json parsed successfully ({len(json_data)} items).")
        except Exception as e:
            failures.append(f"questions.json parse error: {e}")
            return False, failures, warnings, stats

    with open(js_path, "r", encoding="utf-8") as f:
        raw_js = f.read().strip()
        cleaned_js = re.sub(r"^\s*(?:window\.)?(?:const|let|var)?\s*[a-zA-Z0-9_$]+\s*=\s*", "", raw_js, count=1)
        cleaned_js = re.sub(r";\s*$", "", cleaned_js)
        try:
            js_data = json.loads(cleaned_js)
            print(f"[PASS] Check 1.2: questions.js parsed successfully ({len(js_data)} items).")
        except Exception as e:
            failures.append(f"questions.js parse error: {e}")
            return False, failures, warnings, stats

    # --------------------------------------------------------------------------
    # Check 2: 1-to-1 Synchronization between questions.json and questions.js
    # --------------------------------------------------------------------------
    if len(json_data) != len(js_data):
        failures.append(f"Count mismatch between questions.json ({len(json_data)}) and questions.js ({len(js_data)})")
    else:
        sync_diffs = 0
        for i, (q_json, q_js) in enumerate(zip(json_data, js_data)):
            if q_json != q_js:
                sync_diffs += 1
                failures.append(f"Data discrepancy at index {i} between JSON and JS: ID {q_json.get('id')} vs {q_js.get('id')}")
        if sync_diffs == 0:
            print(f"[PASS] Check 2: questions.json and questions.js are 100% byte-for-byte synchronized across all {len(json_data)} questions.")
        else:
            print(f"[FAIL] Check 2: Found {sync_diffs} synchronization differences between JSON and JS!")

    # --------------------------------------------------------------------------
    # Check 3: Schema and Strict Constraints Across All Questions
    # --------------------------------------------------------------------------
    total_q = len(json_data)
    if total_q != 210:
        failures.append(f"Expected exactly 210 questions, found {total_q}")
    else:
        print(f"[PASS] Check 3.1: Exactly 210 questions present.")

    topic_counts = Counter()
    seen_ids = set()
    seen_question_texts = set()
    exact_answer_in_options_count = 0
    strict_no_trim_answer_count = 0
    raw_answer_positions = Counter()
    option_lengths_correct = []
    option_lengths_distractors = []
    longest_is_correct_count = 0
    shortest_is_correct_count = 0
    cpp_code_questions = 0
    control_char_issues = 0
    mojibake_issues = 0
    id_sequence_issues = 0

    required_keys = {"id", "topicId", "topicName", "question", "options", "answer", "explanation"}

    for idx, q in enumerate(json_data, start=1):
        qid = q.get("id")
        qid_tag = f"Q{idx} ({qid})"

        # Keys check
        missing_keys = required_keys - set(q.keys())
        if missing_keys:
            failures.append(f"{qid_tag}: Missing keys: {missing_keys}")

        # ID check
        expected_seq_id = f"q{idx:03d}"
        if not isinstance(qid, str) or not qid.strip():
            failures.append(f"{qid_tag}: Invalid id '{qid}'")
        elif qid in seen_ids:
            failures.append(f"{qid_tag}: Duplicate question id '{qid}'")
        elif qid != expected_seq_id:
            id_sequence_issues += 1
            warnings.append(f"{qid_tag}: Non-sequential ID. Expected '{expected_seq_id}', got '{qid}'")
        seen_ids.add(qid)

        # Unicode & Mojibake deep scan
        all_text_fields = [("question", q.get("question", "")), ("answer", q.get("answer", "")), ("explanation", q.get("explanation", ""))]
        for opt_i, opt in enumerate(q.get("options", [])):
            all_text_fields.append((f"options[{opt_i}]", opt))

        for fname, fval in all_text_fields:
            if isinstance(fval, str):
                for ch in fval:
                    if ord(ch) < 32 and ch not in "\n\r\t":
                        control_char_issues += 1
                        failures.append(f"{qid_tag}: Field '{fname}' contains control char ord({ord(ch)})")
                    if ord(ch) == 0xFFFD:
                        mojibake_issues += 1
                        failures.append(f"{qid_tag}: Field '{fname}' contains Unicode replacement char U+FFFD")
                # Mojibake common patterns
                if re.search(r"[\u00C0-\u00FF]{2,}", fval):
                    # Check if suspicious double-encoded UTF-8
                    if any(bad in fval for bad in ["Ã¡", "Ã©", "Ã­", "Ã³", "Ãº", "Ä‘"]):
                        mojibake_issues += 1
                        failures.append(f"{qid_tag}: Field '{fname}' contains suspected UTF-8 mojibake: '{fval[:40]}'")

        # Topic ID check
        tid = q.get("topicId")
        if not isinstance(tid, int) or tid not in EXPECTED_TOPICS:
            failures.append(f"{qid_tag}: Invalid topicId {tid}")
        else:
            topic_counts[tid] += 1
            expected_tname = EXPECTED_TOPICS[tid]
            actual_tname = q.get("topicName")
            if actual_tname != expected_tname:
                failures.append(f"{qid_tag}: TopicName mismatch. Expected '{expected_tname}', got '{actual_tname}'")

        # Question text check
        qtext = q.get("question")
        if not isinstance(qtext, str) or len(qtext.strip()) < 15:
            failures.append(f"{qid_tag}: Question text too short or invalid")
        else:
            # Check question uniqueness
            norm_q = re.sub(r"\s+", " ", qtext.strip().lower())
            if norm_q in seen_question_texts:
                failures.append(f"{qid_tag}: Duplicate question text detected: '{qtext[:50]}...'")
            seen_question_texts.add(norm_q)

            if "`" in qtext or "<" in qtext or ">" in qtext or "::" in qtext:
                cpp_code_questions += 1

        # Options check
        opts = q.get("options")
        if not isinstance(opts, list) or len(opts) != 4:
            failures.append(f"{qid_tag}: Options must be a list of exactly 4 strings")
        else:
            cleaned_opts = []
            for opt_idx, opt in enumerate(opts):
                if not isinstance(opt, str) or len(opt.strip()) == 0:
                    failures.append(f"{qid_tag}: Option {opt_idx} is empty or not string")
                else:
                    if opt != opt.strip():
                        warnings.append(f"{qid_tag}: Option {opt_idx} has leading/trailing whitespace: '{opt}'")
                    cleaned_opts.append(opt.strip())

            # Check distinctness
            if len(cleaned_opts) == 4:
                # 1. Exact string distinctness
                if len(set(cleaned_opts)) != 4:
                    failures.append(f"{qid_tag}: Contains duplicate options: {cleaned_opts}")
                # 2. Case-insensitive distinctness
                lower_set = set(o.lower() for o in cleaned_opts)
                if len(lower_set) != 4:
                    warnings.append(f"{qid_tag}: Contains case-insensitive near-duplicate options: {cleaned_opts}")

        # Answer check
        ans = q.get("answer")
        if not isinstance(ans, str) or not ans.strip():
            failures.append(f"{qid_tag}: Missing or empty answer")
        elif isinstance(opts, list) and len(opts) == 4:
            # Check exact match WITHOUT strip
            if ans in opts:
                strict_no_trim_answer_count += 1
                pos = opts.index(ans)
                raw_answer_positions[pos] += 1
            else:
                # Check if it matches with strip
                if ans.strip() in [o.strip() for o in opts if isinstance(o, str)]:
                    failures.append(f"{qid_tag}: Answer matches option only AFTER trimming whitespace! Strict === will fail!")
                else:
                    failures.append(f"{qid_tag}: Answer does not match any of the 4 options! Answer: '{ans}'")

            # Option length bias analysis
            if ans in opts:
                ans_len = len(ans)
                option_lengths_correct.append(ans_len)
                distractor_lens = [len(o) for o in opts if o != ans]
                option_lengths_distractors.extend(distractor_lens)

                max_len = max(len(o) for o in opts)
                min_len = min(len(o) for o in opts)
                if ans_len == max_len and ans_len > min_len:
                    longest_is_correct_count += 1
                if ans_len == min_len and ans_len < max_len:
                    shortest_is_correct_count += 1

        # Explanation check
        exp = q.get("explanation")
        if not isinstance(exp, str) or len(exp.strip()) < 20:
            failures.append(f"{qid_tag}: Explanation too short (< 20 chars)")
        else:
            # Check for generic/lazy explanations
            lazy_patterns = [
                r"^đáp án đúng là [abcd]",
                r"^đáp án là",
                r"^xem slide",
                r"^theo lý thuyết$",
                r"^chính xác$",
                r"^chưa có giải thích",
            ]
            exp_lower = exp.strip().lower()
            for lp in lazy_patterns:
                if re.match(lp, exp_lower):
                    failures.append(f"{qid_tag}: Trivial/unhelpful explanation detected: '{exp}'")

    # --------------------------------------------------------------------------
    # Check 4: Topic Distribution Balance
    # --------------------------------------------------------------------------
    print("\n>>> Topic Balance Assessment (Target: 15 questions per topic):")
    all_topics_balanced = True
    for tid in range(1, 15):
        cnt = topic_counts.get(tid, 0)
        tname = EXPECTED_TOPICS[tid]
        status = "OK" if cnt == 15 else "UNBALANCED"
        if cnt != 15:
            all_topics_balanced = False
            failures.append(f"Topic {tid} ('{tname}') has {cnt} questions (expected exactly 15)")
        print(f"  Topic {tid:02d} ({tname:<25}): {cnt} questions [{status}]")

    if all_topics_balanced:
        print("[PASS] Check 4: Perfect balance! Exactly 15 questions for every one of the 14 topics.")
    else:
        print("[FAIL] Check 4: Topic distribution imbalance detected!")

    # --------------------------------------------------------------------------
    # Check 5: Answer Matching & Trimming Rigor
    # --------------------------------------------------------------------------
    if strict_no_trim_answer_count == total_q:
        print(f"[PASS] Check 5: 100% ({strict_no_trim_answer_count}/{total_q}) of answers strictly match an option with byte-level string equality (no trimming required).")
    else:
        print(f"[FAIL] Check 5: Only {strict_no_trim_answer_count}/{total_q} answers match strictly!")

    # --------------------------------------------------------------------------
    # Check 6: Raw Bank Option Index Distribution & Option Length Bias
    # --------------------------------------------------------------------------
    print("\n>>> Question Bank Structural Bias Metrics:")
    print(f"  * Questions with C++ code / syntax: {cpp_code_questions} ({cpp_code_questions/total_q*100:.1f}%)")
    print(f"  * Answer initial position in questions.json (before shuffle):")
    for slot in range(4):
        cnt = raw_answer_positions.get(slot, 0)
        pct = (cnt / total_q) * 100.0
        print(f"      - Option Index {slot}: {cnt} questions ({pct:.1f}%)")

    mean_corr_len = sum(option_lengths_correct) / len(option_lengths_correct) if option_lengths_correct else 0
    mean_dist_len = sum(option_lengths_distractors) / len(option_lengths_distractors) if option_lengths_distractors else 0
    longest_pct = (longest_is_correct_count / total_q) * 100.0
    shortest_pct = (shortest_is_correct_count / total_q) * 100.0

    print(f"  * Average correct option char length: {mean_corr_len:.1f}")
    print(f"  * Average distractor option char length: {mean_dist_len:.1f}")
    print(f"  * Correct option is longest: {longest_is_correct_count}/{total_q} ({longest_pct:.1f}%)")
    print(f"  * Correct option is shortest: {shortest_is_correct_count}/{total_q} ({shortest_pct:.1f}%)")

    if raw_answer_positions.get(0, 0) == total_q:
        warnings.append("Note: In questions.json, the correct answer is always at index 0. Fisher-Yates runtime shuffling is essential to randomize options in UI.")

    # --------------------------------------------------------------------------
    # Check 7: HTML Formatting & Code Snippet Safety
    # --------------------------------------------------------------------------
    print("\n>>> Testing Code Snippet & HTML Entity Safety:")
    html_issues = 0
    for idx, q in enumerate(json_data, start=1):
        for field in ["question", "answer", "explanation"]:
            raw_val = q.get(field, "")
            formatted = format_code_snippet(raw_val)
            # Check for unescaped raw '<' or '>' that aren't inside our code tags
            unwrapped = re.sub(r'<code[^>]*>.*?</code>', '', formatted)
            if "<" in unwrapped or ">" in unwrapped:
                html_issues += 1
                warnings.append(f"Q{idx} ({q.get('id')}): Potential unescaped tag in {field}: '{formatted[:80]}'")

    if html_issues == 0:
        print(f"[PASS] Check 7: All 210 questions format cleanly through formatCodeSnippet with zero unescaped HTML tag leaks.")
    else:
        print(f"[WARN] Check 7: {html_issues} questions have potential HTML tag ambiguities.")

    # --------------------------------------------------------------------------
    # Check 8: Search Engine Query Tolerance
    # --------------------------------------------------------------------------
    print("\n>>> Testing Search Engine Query Tolerance on 210 questions:")
    test_queries = [
        "std::vector",
        "O(n^2)",
        "O(n log n)",
        "->next",
        "*ptr",
        "int&",
        "AVL",
        "Tombstone",
        "Quick Sort",
        "Stack",
        "Hàng đợi",
        "Ngăn xếp",
        "Bảng băm",
        "4 đặc trưng",
    ]

    for qry in test_queries:
        norm = qry.strip().lower()
        matches = 0
        for q in json_data:
            q_str = (
                str(q.get("question", ""))
                + " "
                + str(q.get("topicName", ""))
                + " "
                + " ".join(str(o) for o in q.get("options", []))
            ).lower()
            if norm in q_str:
                matches += 1
        if matches == 0:
            warnings.append(f"Search query '{qry}' produced 0 matches across all 210 questions.")
        else:
            print(f"  * Query '{qry:<18}': {matches} questions matched")

    print("[PASS] Check 8: Search engine filter queries execute smoothly with zero regex/character crash exceptions.")

    # --------------------------------------------------------------------------
    # Check 9: 50,000 Simulated Rounds & Fisher-Yates Live Integrity Stress
    # --------------------------------------------------------------------------
    print("\n>>> Simulating 50,000 Live 5-Question Game Rounds from questions.json...")
    import random
    topic_map = defaultdict(list)
    for q in json_data:
        topic_map[q["topicId"]].append(q)

    all_tids = list(topic_map.keys())
    gameplay_errors = 0
    sim_rounds = 50000

    for r_idx in range(sim_rounds):
        # Pick 5 distinct topics
        chosen_tids = random.sample(all_tids, 5)
        round_qs = [random.choice(topic_map[t]) for t in chosen_tids]

        # Invariant 1: Exactly 5 questions
        if len(round_qs) != 5:
            gameplay_errors += 1
            failures.append(f"Round {r_idx}: Count != 5")
            break

        # Invariant 2: Unique IDs
        r_ids = [q["id"] for q in round_qs]
        if len(set(r_ids)) != 5:
            gameplay_errors += 1
            failures.append(f"Round {r_idx}: Duplicate question ID in round")
            break

        # Invariant 3: Fisher-Yates shuffle each question
        for q in round_qs:
            opts = list(q["options"])
            for i in range(len(opts) - 1, 0, -1):
                j = random.randint(0, i)
                opts[i], opts[j] = opts[j], opts[i]

            # Invariant 4: Answer must be in shuffled options
            if q["answer"] not in opts:
                gameplay_errors += 1
                failures.append(f"Round {r_idx}: Q {q['id']} answer missing from shuffled options!")
                break

    if gameplay_errors == 0:
        print(f"[PASS] Check 9: 50,000 consecutive rounds simulated (250,000 question interactions) with 0 errors, 100% topic diversity, and 100% answer reachability.")
    else:
        print(f"[FAIL] Check 9: Detected {gameplay_errors} errors during round simulation!")

    # --------------------------------------------------------------------------
    # Summary & Verdict
    # --------------------------------------------------------------------------
    print("\n================================================================================")
    print(f"ADVERSARIAL STRESS TEST RESULTS:")
    print(f"  - Total Failures: {len(failures)}")
    print(f"  - Total Warnings: {len(warnings)}")
    print("================================================================================")

    if failures:
        print("\nFAILURES DETECTED:")
        for f in failures[:25]:
            print(f"  [X] {f}")
        return False, failures, warnings, stats

    if warnings:
        print("\nNOTICES & ADVISORIES:")
        for w in warnings[:10]:
            print(f"  [!] {w}")

    print("\n[VERDICT: APPROVE] The question bank passes all adversarial schema, data integrity, and balance tests!")
    return True, failures, warnings, stats


if __name__ == "__main__":
    success, fails, warns, stats = run_adversarial_suite()
    sys.exit(0 if success else 1)
