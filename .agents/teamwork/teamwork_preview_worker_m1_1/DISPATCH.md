# Dispatch: Milestone 1 Question Author Worker

## Identity
- Role: Question Bank Author & Content Engineer
- Archetype: teamwork_preview_worker
- Working directory: D:\c++\quiz_game\.agents\teamwork\teamwork_preview_worker_m1_1
- Parent: orchestrator_1 (Conv ID: 8a489974-6dc1-4eb6-a312-7a0c5f793d3b)

## Scope & File Ownership
You exclusively own and write:
- `D:\c++\quiz_game\questions.json`
- `D:\c++\quiz_game\questions.js` (for zero-install browser CORS fallback: `window.QUIZ_QUESTIONS = [...]`)

You MUST NOT edit `verify_bank.py`, `test_quiz_engine.py`, or `index.html`.

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Instructions
Read `D:\c++\quiz_game\.agents\teamwork\ORIGINAL_REQUEST.md`.
Read `D:\c++\quiz_game\PROJECT.md`.
Read the survey reports for all 14 lecture topics:
- Topics 1-5: `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_1\report.md`
- Topics 6-10: `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_2\report.md`
- Topics 11-14: `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_3\report.md`

Generate exactly 210 high-quality, technically sound multiple-choice questions in Vietnamese (keeping exact C++ and CS keywords, syntax, and notations), distributed as exactly 15 questions per topic across all 14 topics:
1. Introduction & Overview (15 questions: q001 - q015)
2. Basic C++ Language (15 questions: q016 - q030)
3. Classes & OOP in C++ (15 questions: q031 - q045)
4. Algorithm Analysis & Big-O (15 questions: q046 - q060)
5. Recursion (15 questions: q061 - q075)
6. Vector & Dynamic Arrays (15 questions: q076 - q090)
7. Linked List (Singly, Doubly, Circular) (15 questions: q091 - q105)
8. Stack (15 questions: q106 - q120)
9. Queue (15 questions: q121 - q135)
10. Trees (Binary Tree, BST, AVL) (15 questions: q136 - q150)
11. Sorting O(n^2) (Bubble, Selection, Insertion) (15 questions: q151 - q165)
12. Sorting O(n log n) (Merge, Quick, Heap) (15 questions: q166 - q180)
13. Search Algorithms (Linear, Binary, BST search/insert/remove) (15 questions: q181 - q195)
14. Hash Tables (Hashing, Collisions, Chaining, Open Addressing) (15 questions: q196 - q210)

### Schema Requirements for each question:
```json
{
  "id": "q001",
  "topicId": 1,
  "topicName": "Introduction & Overview",
  "question": "Nội dung câu hỏi rõ ràng...",
  "options": [
    "Phương án 1",
    "Phương án 2",
    "Phương án 3",
    "Phương án 4"
  ],
  "answer": "Phương án đúng (khớp chính xác 100% với 1 trong 4 lựa chọn ở options)",
  "explanation": "Giải thích chi tiết sư phạm, trích dẫn cơ chế hoạt động..."
}
```
Important note: Do NOT prefix options with "A. ", "B. ", "C. ", "D. " inside the option strings because the quiz engine dynamically shuffles options and assigns badges A-D.

After generating `questions.json`, also generate `questions.js` with:
```javascript
window.QUIZ_QUESTIONS = [ ... ];
```
Run validation on your generated question bank (e.g. check count, topics, unique options, correct answer match).
Write your completion handoff report to `handoff.md` and notify the orchestrator.


## 2026-10-28T16:45:32Z
Read ORIGINAL_REQUEST.md at D:\c++\quiz_game\.agents\teamwork\ORIGINAL_REQUEST.md.
Read your DISPATCH.md at D:\c++\quiz_game\.agents\teamwork\teamwork_preview_worker_m1_1\DISPATCH.md.
Your Working Directory: D:\c++\quiz_game\.agents\teamwork\teamwork_preview_worker_m1_1.
Your Parent: Conv ID 8a489974-6dc1-4eb6-a312-7a0c5f793d3b.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Generate the comprehensive 210-question bank (15 questions per topic across all 14 lecture topics) in:
- D:\c++\quiz_game\questions.json
- D:\c++\quiz_game\questions.js (window.QUIZ_QUESTIONS = [...])

Ensure exact C++ and CS keywords, high pedagogical quality in Vietnamese, exactly 4 distinct options per question, correct answer matching one of the options, and clear explanations.
Verify the file syntax and question integrity.
Write handoff.md and notify the parent via send_message when completed.
