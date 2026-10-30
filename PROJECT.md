# Project: C++ and Data Structures & Algorithms Quiz Review Game

## Architecture
A standalone, zero-install interactive web application that helps students review C++ and Data Structures & Algorithms concepts across 14 lecture topics.
- **Data Layer:** `questions.json` (and `questions.js` dual-mode fallback) containing 210 comprehensive questions (15 per topic) with exact C++ and CS technical terminology in Vietnamese.
- **Engine Layer:** Client-side quiz engine managing game states (welcome, round in progress, instant feedback, round review, result summary, topic practice, and bank browser/search), 5-question random round selection, and Fisher-Yates answer shuffling.
- **Presentation Layer (`index.html`):** Polished single-page web app built with modern Tailwind CSS, Lucide icons, responsive layout, Web Audio API sound synthesis, and celebratory confetti effects.
- **Verification & Testing Layer:** Automated verification script (`verify_bank.py`) and quiz engine test runner (`test_quiz_engine.py`) ensuring bank integrity and algorithmic randomness.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | 14-Topic Extraction | Survey and extraction of all 14 lecture decks (461 slides) | M1 | Survey |
| 2 | 210-Question Bank | Comprehensive question bank with 15 questions per topic in Vietnamese | M1 | Survey / R1 |
| 3 | Question JSON Schema | Schema with id, topicId, topicName, question, options (4), answer, explanation | M1 | R1 |
| 4 | Dual-Format Data Delivery | questions.json + questions.js (for file:/// CORS bypass) | M1, M3 | Explorer 3 |
| 5 | Quick 5-Question Mode | 5 randomized questions per round across diverse topics | M2 | R2 |
| 6 | Answer Shuffling Engine | Fisher-Yates shuffling of 4 choices on every display with dynamic A-D badges | M2 | R2 |
| 7 | Instant Feedback & Rationale | Real-time right/wrong answer highlight and detailed explanation display | M2, M3 | R2 |
| 8 | Scoring, Timer & Review Mode | Live score counter, session timer, summary percentage, and mistake review | M2, M3 | R2 |
| 9 | One-Click Replayability | Instant restart with a fresh set of 5 random questions | M2, M3 | R2 |
| 10 | Topic Practice & Bank Search | Practice mode by topic and search/filter across the full 210 questions | M2, M3 | R2 |
| 11 | Zero-Install Frontend SPA | index.html with responsive layout, modern design, Lucide icons | M3 | R3 |
| 12 | Sound & Visual Flair | Synthesized Web Audio sound effects and confetti on high scores (>=80%) | M3 | R3 |
| 13 | Bank Verification Script | Automated Python script validating count >= 200, 14 topics, options, schema | E2E | R4 |
| 14 | Randomness Test Runner | Automated script verifying 5-question selection and option permutation distribution | E2E | R4 |
| 15 | Adversarial Hardening | Edge cases, schema stress tests, browser verification, and integrity audit | M4 | Final |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| E2E | E2E Testing Track | Automated test scripts (verify_bank.py, test_quiz_engine.py), test infra, and publication of TEST_READY.md | Survey | DONE |
| M1 | Question Bank Generation | Generate 210 questions in questions.json & questions.js covering all 14 topics | Survey | DONE |
| M2 | Quiz Engine Logic | Implement quiz engine state, 5-question selection, answer shuffling, scoring, search | M1 | DONE |
| M3 | Modern Frontend Web App | Implement index.html with Tailwind, Lucide, Web Audio sound, confetti, practice mode | M2 | DONE |
| M4 | Final Acceptance & Adversarial Hardening | Pass 100% E2E test suite, adversarial testing, browser execution check, integrity audit | E2E, M3 | DONE |

## Code Layout
```
D:\c++\quiz_game\
├── index.html              # Standalone web application (HTML, CSS/Tailwind, JavaScript)
├── questions.json          # Primary 210-question data bank
├── questions.js            # Dual-mode script fallback (window.QUIZ_QUESTIONS)
├── verify_bank.py          # Automated verification script for question bank integrity
├── test_quiz_engine.py     # Automated test runner for engine randomization & shuffling
├── PROJECT.md              # Project architecture, feature inventory, milestones
├── TEST_INFRA.md           # E2E test suite specification and methodology
├── TEST_READY.md           # Signal and summary of E2E test suite readiness
└── .agents/teamwork/       # Agent metadata and coordination directories
```

## Interface Contracts
### Question Object Schema
```json
{
  "id": "q001",
  "topicId": 1,
  "topicName": "Introduction & Overview",
  "question": "Thuật toán có bao nhiêu đặc trưng cơ bản theo giáo trình?",
  "options": [
    "5 đặc trưng: Input, Output, Tính xác định, Tính hữu hạn, Tính hiệu quả",
    "4 đặc trưng: Input, Output, Tính đóng gói, Tính kế thừa",
    "3 đặc trưng: Tính đúng đắn, Tính nhanh chóng, Tính dễ đọc",
    "6 đặc trưng: Bắt đầu, Kết thúc, Nhập, Xuất, Xử lý, Lưu trữ"
  ],
  "answer": "5 đặc trưng: Input, Output, Tính xác định, Tính hữu hạn, Tính hiệu quả",
  "explanation": "Theo bài giảng Lecture 1 (Slide 15), một thuật toán cần thỏa mãn 5 đặc trưng: Input (Đầu vào >= 0), Output (Đầu ra >= 1), Definiteness (Tính xác định rõ ràng), Finiteness (Tính hữu hạn - phải dừng sau số bước hữu hạn), và Effectiveness (Tính hiệu quả/khả thi)."
}
```

### Quiz Engine Contract
- `selectRoundQuestions(bank, count = 5)`: Returns an array of 5 randomly sampled questions from `bank`, guaranteeing distinct `topicId`s where possible.
- `shuffleOptions(options)`: Uses Fisher-Yates algorithm to return a shuffled copy of `options` array without mutating the original question.
- `checkAnswer(selectedOption, correctAnswer)`: Returns boolean `selectedOption === correctAnswer`.
- `calculateScore(userAnswers)`: Returns `{ total, correct, percentage, passed: percentage >= 80 }`.
