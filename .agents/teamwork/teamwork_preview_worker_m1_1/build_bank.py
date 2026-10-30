# -*- coding: utf-8 -*-
"""
Builder and Integrity Verifier for Question Bank (210 questions).
Generates:
- D:\c++\quiz_game\questions.json
- D:\c++\quiz_game\questions.js
"""

import json
import os
import sys

# Ensure UTF-8 output in Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from topic1_to_5 import get_topics_1_to_5
from topic6_to_10 import get_topics_6_to_10
from topic11_to_14 import get_topics_11_to_14

def main():
    q1_5 = get_topics_1_to_5()
    q6_10 = get_topics_6_to_10()
    q11_14 = get_topics_11_to_14()

    all_questions = q1_5 + q6_10 + q11_14
    total_count = len(all_questions)

    print(f"Loaded questions: {len(q1_5)} (topics 1-5) + {len(q6_10)} (topics 6-10) + {len(q11_14)} (topics 11-14) = {total_count} total")

    # --- Validation Checks ---
    errors = []

    if total_count != 210:
        errors.append(f"Expected exactly 210 questions, found {total_count}")

    # Track IDs and topics
    seen_ids = set()
    topic_counts = {}
    topic_names = {}

    expected_topics = {
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
        14: "Hash Tables"
    }

    required_keys = {"id", "topicId", "topicName", "question", "options", "answer", "explanation"}

    for idx, q in enumerate(all_questions, 1):
        expected_id = f"q{idx:03d}"
        qid = q.get("id")

        # Key existence
        missing_keys = required_keys - set(q.keys())
        if missing_keys:
            errors.append(f"Question #{idx} ({qid}) missing keys: {missing_keys}")

        # ID checks
        if qid != expected_id:
            errors.append(f"Question #{idx} id mismatch: expected '{expected_id}', got '{qid}'")
        if qid in seen_ids:
            errors.append(f"Duplicate id found: '{qid}' at question #{idx}")
        seen_ids.add(qid)

        # Topic checks
        tid = q.get("topicId")
        tname = q.get("topicName")
        if tid not in expected_topics:
            errors.append(f"Question {qid} has invalid topicId: {tid}")
        else:
            topic_counts[tid] = topic_counts.get(tid, 0) + 1
            topic_names[tid] = tname

        # Options checks
        options = q.get("options", [])
        if not isinstance(options, list):
            errors.append(f"Question {qid} options is not a list")
            continue

        if len(options) != 4:
            errors.append(f"Question {qid} does not have exactly 4 options (found {len(options)})")

        # Distinct options
        if len(set(options)) != len(options):
            errors.append(f"Question {qid} contains duplicate options: {options}")

        # Check for bad prefixes like "A. ", "B. ", "C. ", "D. "
        for opt in options:
            if not isinstance(opt, str) or not opt.strip():
                errors.append(f"Question {qid} has empty or non-string option")
            elif any(opt.strip().startswith(prefix) for prefix in ["A. ", "B. ", "C. ", "D. ", "A)", "B)", "C)", "D)"]):
                errors.append(f"Question {qid} has hardcoded option prefix badge: '{opt}'")

        # Answer checks
        ans = q.get("answer")
        if ans not in options:
            errors.append(f"Question {qid} answer '{ans}' does not match any of the 4 options: {options}")

        # Explanation checks
        expl = q.get("explanation", "")
        if not isinstance(expl, str) or len(expl.strip()) < 15:
            errors.append(f"Question {qid} explanation is missing or too brief: '{expl}'")

    # Topic distribution check
    for tid, exp_name in expected_topics.items():
        cnt = topic_counts.get(tid, 0)
        if cnt != 15:
            errors.append(f"Topic {tid} ('{exp_name}') has {cnt} questions (expected 15)")

    if errors:
        print(f"FAILED VALIDATION with {len(errors)} error(s):")
        for err in errors[:20]:
            print(" -", err)
        if len(errors) > 20:
            print(f" ... and {len(errors) - 20} more errors")
        sys.exit(1)

    print("ALL VALIDATION CHECKS PASSED PERFECTLY!")
    print("\nTopic Breakdown:")
    for tid in sorted(topic_counts.keys()):
        print(f"  Topic {tid:02d} [{topic_names.get(tid)}]: {topic_counts[tid]} questions")

    # Output paths (target D:\c++\quiz_game)
    quiz_game_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    json_path = os.path.join(quiz_game_dir, "questions.json")
    js_path = os.path.join(quiz_game_dir, "questions.js")

    # Write questions.json
    print(f"\nWriting questions.json to: {json_path}")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    json_size = os.path.getsize(json_path)
    print(f"  -> questions.json written ({json_size} bytes)")

    # Write questions.js
    print(f"Writing questions.js to: {js_path}")
    json_str = json.dumps(all_questions, ensure_ascii=False, indent=2)
    js_content = f"window.QUIZ_QUESTIONS = {json_str};\n"
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    js_size = os.path.getsize(js_path)
    print(f"  -> questions.js written ({js_size} bytes)")

    # Verify reload
    with open(json_path, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    print(f"Verified reloaded questions.json: successfully parsed {len(reloaded)} questions.")

if __name__ == "__main__":
    main()
