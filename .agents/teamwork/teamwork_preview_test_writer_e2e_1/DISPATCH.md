# Dispatch: E2E Test Writer (Test Track)

## Identity
- Role: E2E Test Suite Engineer
- Archetype: teamwork_preview_test_writer
- Working directory: D:\c++\quiz_game\.agents\teamwork\teamwork_preview_test_writer_e2e_1
- Parent: orchestrator_1 (Conv ID: 8a489974-6dc1-4eb6-a312-7a0c5f793d3b)

## Scope & File Ownership
You exclusively own and write:
- `D:\c++\quiz_game\verify_bank.py`
- `D:\c++\quiz_game\test_quiz_engine.py`
- `D:\c++\quiz_game\TEST_READY.md`

You MUST NOT edit `questions.json`, `questions.js`, or `index.html`.

## Instructions
Read `D:\c++\quiz_game\.agents\teamwork\ORIGINAL_REQUEST.md`.
Read `D:\c++\quiz_game\PROJECT.md`.
Read `D:\c++\quiz_game\TEST_INFRA.md`.

Implement the complete automated verification & validation suite:
1. `verify_bank.py`:
   - Validates `questions.json` (and optionally `questions.js`).
   - Ensures valid JSON format.
   - Asserts total question count >= 200 (target 210).
   - Asserts all 14 topic IDs (1 through 14) are represented with >= 14 questions each.
   - Asserts every question has:
     - `id`: unique string/number
     - `topicId`: integer in range [1, 14]
     - `topicName`: non-empty string
     - `question`: non-empty string
     - `options`: array of exactly 4 non-empty, distinct strings (no duplicates within choices)
     - `answer`: string matching exactly one of the 4 `options`
     - `explanation`: non-empty pedagogical rationale in Vietnamese
   - Prints clear diagnostic output and summary table by topic.
   - Exits with 0 on complete pass, non-zero on failure.
2. `test_quiz_engine.py`:
   - Simulates the quiz engine's selection and shuffling logic:
     - 5-question random selection across the bank (verifying topic diversity, repeatability, and non-deterministic sampling across 1,000 runs).
     - Fisher-Yates answer shuffling across 10,000 displays: verifying all 24 permutations ($4!$) occur and correct answer position is uniformly distributed across index 0, 1, 2, 3 (~25% each).
     - Scoring verification (0% to 100%).
   - Exits with 0 on pass, non-zero on failure.
3. Test your verification scripts on sample data if `questions.json` is not yet available, ensuring the scripts run cleanly with Python (`python verify_bank.py`, `python test_quiz_engine.py`).
4. Generate `TEST_READY.md` at project root summarizing the test suite runner, commands, and tier coverage.
5. Write your handoff report to `handoff.md` in your working directory and notify the orchestrator.


## 2026-10-28T16:45:32Z
[Message] timestamp=2026-10-28T16:45:32Z sender=8a489974-6dc1-4eb6-a312-7a0c5f793d3b priority=MESSAGE_PRIORITY_HIGH content=Read ORIGINAL_REQUEST.md at D:\c++\quiz_game\.agents\teamwork\ORIGINAL_REQUEST.md.
Read your DISPATCH.md at D:\c++\quiz_game\.agents\teamwork\teamwork_preview_test_writer_e2e_1\DISPATCH.md.
Your Working Directory: D:\c++\quiz_game\.agents\teamwork\teamwork_preview_test_writer_e2e_1.
Your Parent: Conv ID 8a489974-6dc1-4eb6-a312-7a0c5f793d3b.

Write the E2E automated test scripts:
1. D:\c++\quiz_game\verify_bank.py (validates questions.json / questions.js for 200+ questions, all 14 topics, 4 unique options, answer in options, non-empty explanation).
2. D:\c++\quiz_game\test_quiz_engine.py (simulates 5-question random round selection and option shuffling across thousands of runs).
3. D:\c++\quiz_game\TEST_READY.md (documents test runner instructions and tier test matrix).

Run and verify your test scripts locally using python.
Write your handoff report to handoff.md in your working directory and notify the parent via send_message.
