import json
import re
import os
import sys

def audit_question_bank():
    json_path = r"D:\c++\quiz_game\questions.json"
    js_path = r"D:\c++\quiz_game\questions.js"
    
    print("=== FORENSIC QUESTION BANK AUDIT ===")
    
    # 1. Load JSON
    if not os.path.exists(json_path):
        print(f"FAIL: {json_path} does not exist")
        return False
    with open(json_path, "r", encoding="utf-8") as f:
        bank_json = json.load(f)
    print(f"Loaded questions.json: {len(bank_json)} questions")
    
    # 2. Load JS
    if not os.path.exists(js_path):
        print(f"FAIL: {js_path} does not exist")
        return False
    with open(js_path, "r", encoding="utf-8") as f:
        js_text = f.read()
    
    # Extract JSON part from JS
    match = re.search(r"=\s*(\[.*\]);?\s*$", js_text, re.DOTALL)
    if not match:
        # maybe without trailing semicolon or different pattern
        match = re.search(r"(\[.*\])", js_text, re.DOTALL)
    if not match:
        print("FAIL: Could not extract array from questions.js")
        return False
    
    bank_js = json.loads(match.group(1))
    print(f"Loaded questions.js: {len(bank_js)} questions")
    
    # Compare JSON and JS
    if bank_json != bank_js:
        print("FAIL: questions.json and questions.js data structures differ!")
        return False
    else:
        print("PASS: questions.json and questions.js are 100% data-identical.")
    
    # Check count
    if len(bank_json) < 200:
        print(f"FAIL: Question count {len(bank_json)} < 200")
        return False
    
    # 3. Check schema, duplicates, placeholders
    seen_ids = set()
    seen_questions = set()
    topics = {}
    answer_indices = {0: 0, 1: 0, 2: 0, 3: 0}
    placeholder_regex = re.compile(r"(lorem|ipsum|dummy|placeholder|tbd|todo|test1|test2|abcde|xyz)", re.IGNORECASE)
    
    for idx, q in enumerate(bank_json):
        # Schema fields
        for field in ["id", "topicId", "topicName", "question", "options", "answer", "explanation"]:
            if field not in q:
                print(f"FAIL: Question #{idx} missing field '{field}'")
                return False
        
        # ID uniqueness
        qid = q["id"]
        if qid in seen_ids:
            print(f"FAIL: Duplicate ID '{qid}' at question #{idx}")
            return False
        seen_ids.add(qid)
        
        # Question text
        qtext = q["question"].strip()
        if not qtext or len(qtext) < 10:
            print(f"FAIL: Question #{idx} ({qid}) text too short: '{qtext}'")
            return False
        if qtext in seen_questions:
            print(f"WARNING/FAIL: Duplicate question text at {qid}: '{qtext}'")
            return False
        seen_questions.add(qtext)
        
        # Check placeholders
        if placeholder_regex.search(qtext):
            print(f"FAIL: Potential placeholder found in question {qid}: '{qtext}'")
            return False
        
        # Options
        opts = q["options"]
        if not isinstance(opts, list) or len(opts) != 4:
            print(f"FAIL: Question {qid} does not have exactly 4 options (has {len(opts)})")
            return False
        if len(set(opts)) != 4:
            print(f"FAIL: Question {qid} has duplicate options: {opts}")
            return False
        for opt in opts:
            if not isinstance(opt, str) or not opt.strip():
                print(f"FAIL: Question {qid} has empty or non-string option")
                return False
        
        # Answer
        ans = q["answer"]
        if ans not in opts:
            print(f"FAIL: Question {qid} answer '{ans}' not in options {opts}")
            return False
        ans_idx = opts.index(ans)
        answer_indices[ans_idx] += 1
        
        # Explanation
        exp = q["explanation"].strip()
        if not exp or len(exp) < 15:
            print(f"FAIL: Question {qid} explanation too short: '{exp}'")
            return False
        if placeholder_regex.search(exp):
            print(f"FAIL: Potential placeholder in explanation {qid}: '{exp}'")
            return False
        
        # Topic
        tid = q["topicId"]
        tname = q["topicName"]
        if tid not in topics:
            topics[tid] = {"name": tname, "count": 0}
        topics[tid]["count"] += 1
    
    print("\nTopic Breakdown:")
    for tid in sorted(topics.keys()):
        print(f"  Topic {tid:2d} ({topics[tid]['name']}): {topics[tid]['count']} questions")
    
    if len(topics) != 14:
        print(f"FAIL: Expected 14 topics, found {len(topics)}")
        return False
    for tid in range(1, 15):
        if tid not in topics or topics[tid]["count"] < 14:
            print(f"FAIL: Topic {tid} has insufficient questions ({topics.get(tid, {}).get('count', 0)})")
            return False
            
    print("\nRaw Answer Index Distribution (in static bank before shuffling):")
    for s, c in answer_indices.items():
        print(f"  Slot {s}: {c} ({c / len(bank_json) * 100:.1f}%)")
    
    # Are answers hardcoded to a single slot?
    if max(answer_indices.values()) == len(bank_json):
        print("FAIL: All raw answers placed in identical slot!")
        return False
        
    print("\nALL BANK FORENSIC CHECKS PASSED!")
    return True

if __name__ == "__main__":
    success = audit_question_bank()
    sys.exit(0 if success else 1)
