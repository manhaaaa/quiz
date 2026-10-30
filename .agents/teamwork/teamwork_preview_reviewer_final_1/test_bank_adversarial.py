import json
import io
import sys
from collections import Counter

if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

with open(r'D:\c++\quiz_game\questions.json', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions.")

# 1. Duplicate questions
q_texts = [q['question'].strip() for q in questions]
dup_q = [text for text, count in Counter(q_texts).items() if count > 1]
print(f"Duplicate question texts: {len(dup_q)}")
if dup_q:
    print(f"  Found duplicates: {dup_q}")

# 2. Duplicate IDs
q_ids = [q['id'] for q in questions]
dup_ids = [qid for qid, count in Counter(q_ids).items() if count > 1]
print(f"Duplicate IDs: {len(dup_ids)}")

# 3. Check within-question option collisions
dup_opts_within = []
for q in questions:
    opts = [o.strip() for o in q['options']]
    if len(opts) != len(set(opts)):
        dup_opts_within.append(q['id'])
print(f"Questions with duplicate options within choices: {len(dup_opts_within)}")

# 4. Check answer exact match in options
ans_mismatch = []
for q in questions:
    if q['answer'] not in q['options']:
        ans_mismatch.append(q['id'])
print(f"Questions where answer is not in options: {len(ans_mismatch)}")

# 5. Check technical terms coverage
tech_terms = [
    "C++", "Big-O", "O(n", "O(1)", "O(log n)", "std::vector",
    "Linked List", "Stack", "Queue", "Binary Tree", "BST", "AVL",
    "Bubble Sort", "Quick Sort", "Merge Sort", "Heap Sort", "Hash",
    "đệ quy", "con trỏ", "tham chiếu", "OOP", "kế thừa", "đa hình"
]
all_corpus = " ".join([q['question'] + " " + " ".join(q['options']) + " " + q['explanation'] for q in questions]).lower()
missing_terms = [t for t in tech_terms if t.lower() not in all_corpus]
print(f"Missing core technical terms: {missing_terms}")

# 6. Check lecture slide references in explanations
slide_refs = sum(1 for q in questions if "slide" in q['explanation'].lower() or "bài giảng" in q['explanation'].lower() or "lecture" in q['explanation'].lower())
print(f"Questions with explicit lecture/slide references: {slide_refs}/{len(questions)} ({slide_refs/len(questions)*100:.1f}%)")


print("\n--- Topic 3 (OOP) Questions Sample ---")
for q in [q for q in questions if q['topicId'] == 3][:5]:
    print(f"[{q['id']}] {q['question']}")
    print(f"  Options: {q['options']}")
    print(f"  Answer: {q['answer']}")
    print(f"  Explanation: {q['explanation'][:100]}...\n")


print("\n--- Topics 10, 11, 12, 14 Sample Questions ---")
for tid in [10, 11, 12, 14]:
    q = next(q for q in questions if q['topicId'] == tid)
    print(f"[{q['id']}] Topic {tid}: {q['topicName']}")
    print(f"  Q: {q['question']}")
    print(f"  Ans: {q['answer']}")
    print(f"  Expl: {q['explanation'][:120]}...\n")
