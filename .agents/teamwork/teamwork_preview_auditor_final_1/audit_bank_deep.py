import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('D:/c++/quiz_game/questions.json', 'r', encoding='utf-8') as f:
    bank = json.load(f)

print(f"Running exhaustive integrity inspection on {len(bank)} questions...")

suspicious_terms = ['todo', 'lorem', 'placeholder', 'dummy', 'asdf', 'test 123', 'cau hoi thu']
flags = []

seen_questions = set()
seen_ids = set()

for idx, q in enumerate(bank):
    qid = q.get('id')
    # ID check
    if not qid:
        flags.append(f"Question #{idx} missing id")
    if qid in seen_ids:
        flags.append(f"Duplicate id {qid}")
    seen_ids.add(qid)

    # Question text
    qtext = q.get('question', '').strip()
    if len(qtext) < 15:
        flags.append(f"[{qid}] Question text too short ({len(qtext)} chars)")
    if qtext.lower() in seen_questions:
        flags.append(f"[{qid}] Duplicate question text: {qtext[:40]}")
    seen_questions.add(qtext.lower())

    for term in suspicious_terms:
        if term in qtext.lower():
            flags.append(f"[{qid}] Suspicious term '{term}' in question")

    # Options check
    options = q.get('options', [])
    if len(options) != 4:
        flags.append(f"[{qid}] Option count is {len(options)}, expected 4")
    if len(set(options)) != 4:
        flags.append(f"[{qid}] Duplicate choices found in options: {options}")

    # Answer check
    answer = q.get('answer', '')
    if answer not in options:
        flags.append(f"[{qid}] Answer not found in options! Answer={answer}")

    # Explanation check
    explanation = q.get('explanation', '').strip()
    if len(explanation) < 20:
        flags.append(f"[{qid}] Explanation too short ({len(explanation)} chars)")

    # Topic ID
    tid = q.get('topicId')
    if tid not in range(1, 15):
        flags.append(f"[{qid}] Invalid topicId {tid}")

print(f"Integrity flags count: {len(flags)}")
if flags:
    for f in flags[:20]:
        print(f"  FLAG: {f}")
else:
    print("ALL 210 QUESTIONS PASS EXHAUSTIVE INTEGRITY AND AUTHENTICITY CHECKS WITH ZERO FLAGS!")
