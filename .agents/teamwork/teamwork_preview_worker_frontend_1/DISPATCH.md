# Dispatch: Milestone 2 & 3 Frontend & Quiz Engine Worker

## Identity
- Role: Frontend & Quiz Engine Developer
- Archetype: teamwork_preview_worker
- Working directory: D:\c++\quiz_game\.agents\teamwork\teamwork_preview_worker_frontend_1
- Parent: orchestrator_1 (Conv ID: 8a489974-6dc1-4eb6-a312-7a0c5f793d3b)

## Scope & File Ownership
You exclusively own and write:
- `D:\c++\quiz_game\index.html`

You MUST NOT overwrite `questions.json`, `questions.js`, `verify_bank.py`, `test_quiz_engine.py`, or `TEST_READY.md`.

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Requirements & Specifications
Read:
- `D:\c++\quiz_game\.agents\teamwork\ORIGINAL_REQUEST.md` (R2, R3, Acceptance Criteria)
- `D:\c++\quiz_game\PROJECT.md`
- `D:\c++\quiz_game\TEST_INFRA.md`
- `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_3\report.md` (Architectural & Engine Specs)

### 1. Zero-Install Standalone Architecture
- Single file `index.html` that runs directly when opened in Chrome, Edge, Firefox, or any modern browser via double-click or `file:///` URL or HTTP server.
- Uses CDN links for Tailwind CSS (`https://cdn.tailwindcss.com`), Lucide icons (`https://unpkg.com/lucide@latest`), and Canvas Confetti (`https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js`).
- Dual data loading strategy:
  ```javascript
  // 1. Try fetch('questions.json')
  // 2. If blocked by local file:/// CORS or fetch fails, fallback immediately to window.QUIZ_QUESTIONS loaded from <script src="questions.js"></script>
  ```
  Ensure it never gets stuck on a loading screen.

### 2. Quiz Engine & Gameplay Features (Vietnamese Language)
- **Quick 5-Question Session (Chế độ Đấu Nhanh 5 Câu):**
  - Randomly selects 5 questions from the 210-question bank ensuring diverse topics.
  - Progress bar (1/5 to 5/5) and live elapsed time counter (mm:ss).
  - Current score counter.
- **Fisher-Yates Option Shuffling:**
  - On every question display, shuffle the 4 choices so the position of the correct answer is completely unpredictable.
  - Dynamically assign visual badges: A, B, C, D to the shuffled options.
- **Immediate Feedback:**
  - When the user selects an answer:
    - Disable buttons to prevent double-clicking.
    - If correct: green border/background, check icon, play pleasant success sound effect (via Web Audio API).
    - If wrong: red border/background on chosen answer, green on correct answer, play error sound effect.
    - Reveal detailed pedagogical explanation box with lecture references.
    - Show "Câu tiếp theo" (Next Question) or "Xem kết quả" (View Results) button.
- **Session Results Screen:**
  - Final score (e.g., 4/5), percentage (80%), elapsed time, and performance badge (Xuất sắc / Tốt / Cần cố gắng).
  - If score >= 80% (4/5 or 5/5): trigger celebratory confetti animation and victory fanfare sound.
  - Review button: shows all 5 questions answered in the round with the user's choice vs correct choice and explanation.
  - "Chơi lại vòng mới" (Play Again) button: immediately restarts a fresh 5-question round with different randomized questions.
- **Topic Practice Mode (Luyện tập theo Chủ đề):**
  - Allows the user to select any of the 14 lecture topics and practice all 15 questions of that topic at their own pace.
- **Question Bank Search & Browse Mode (Tra cứu Ngân hàng 210 câu):**
  - Search bar with instant real-time filtering by keyword (Vietnamese text, C++ code, concepts).
  - Filter dropdown by Topic (1 to 14 or All).
  - Expandable question card showing all 4 choices, correct answer, and explanation.

### 3. UI/UX Polishing
- Modern dark/light or polished slate/indigo gradient theme, card shadows, rounded corners, responsive layout (mobile friendly).
- Sound toggle button (Mute/Unmute) with default enabled, using clean Web Audio API oscillator synthesis (no external mp3 files needed!).
- All UI text, badges, buttons, tooltips in natural Vietnamese with exact C++ keywords.

### 4. Verification
- Verify that `index.html` loads and functions cleanly.
- Verify through automated script or browser test that all modes work.
- Write your handoff report to `handoff.md` and notify the orchestrator.


## 2026-10-28T17:01:07Z
Read ORIGINAL_REQUEST.md at D:\c++\quiz_game\.agents\teamwork\ORIGINAL_REQUEST.md.
Read your DISPATCH.md at D:\c++\quiz_game\.agents\teamwork\teamwork_preview_worker_frontend_1\DISPATCH.md.
Your Working Directory: D:\c++\quiz_game\.agents\teamwork\teamwork_preview_worker_frontend_1.
Your Parent: Conv ID 8a489974-6dc1-4eb6-a312-7a0c5f793d3b.

Implement the modern, zero-install, interactive single-page web application in D:\c++\quiz_game\index.html:
- Standalone HTML5 + Tailwind CSS + Lucide icons + Canvas Confetti.
- Dual data loading: fetch('questions.json') with immediate fallback to window.QUIZ_QUESTIONS from questions.js (ensuring zero-install operation when double-clicked or opened via file:///).
- Quick 5-Question Session mode: random 5 questions from diverse topics, elapsed timer, live progress bar, score counter.
- Answer shuffling on every question display using Fisher-Yates algorithm, assigning badges A, B, C, D dynamically.
- Immediate feedback: green/red highlight, Web Audio API pleasant chime/buzzer sounds, detailed pedagogical explanation.
- Session results screen: score summary, percentage, performance badge, review mode for all 5 questions, celebratory confetti on score >= 80%, one-click replayability restarting a new 5-question round.
- Topic Practice mode: select any of the 14 topics to practice all 15 questions.
- Question Bank Browse & Search mode: live search across all 210 questions with topic filters and expandable question details.
- Clean Vietnamese UI with exact C++ technical terms, responsive for desktop and mobile, sound toggle button.
