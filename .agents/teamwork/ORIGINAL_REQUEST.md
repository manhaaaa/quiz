# Original User Request

## 2026-10-28T16:28:13Z

Build an interactive, modern web-based quiz review game for C++ and Data Structures & Algorithms based on 14 lecture slide decks in `D:\c++\drive-download-20261028T155811Z-1-001`. The project extracts knowledge across all lecture topics into a comprehensive 200+ question bank (`questions.json`), provides a 5-question random round mode with randomized topics and shuffled answer choices, and delivers an engaging user experience in Vietnamese.

Working directory: `D:\c++\quiz_game`
Integrity mode: development

## Requirements

### R1. Lecture Content Extraction & 200+ Question Bank
- Process all 14 lecture topics from `D:\c++\drive-download-20261028T155811Z-1-001`:
  1. Introduction & Overview
  2. Basic C++ Language
  3. Classes & OOP in C++
  4. Algorithm Analysis & Big-O
  5. Recursion
  6. Vector & Dynamic Arrays
  7. Linked List (Singly, Doubly, Circular)
  8. Stack
  9. Queue
  10. Trees (Binary Tree, BST, AVL)
  11. Sorting $O(n^2)$ (Bubble, Selection, Insertion)
  12. Sorting $O(n \log n)$ (Merge, Quick, Heap)
  13. Search Algorithms (Linear, Binary)
  14. Hash Tables (Hashing, Collisions, Chaining, Open Addressing)
- Generate at least 200 high-quality multiple-choice questions in Vietnamese (keeping exact C++ and CS technical terms), distributed across all 14 topics (~15 questions per topic).
- Store the entire question bank in `questions.json` with a clear schema: `id`, `topicId`, `topicName`, `question`, `options` (array of 4 choices), `answer` (correct option identifier/text), and `explanation` (detailed rationale).

### R2. Quiz Engine & Gameplay Logic
- **Quick 5-Question Session:** Each round randomly picks 5 questions from the 200+ bank, ensuring variety across different topics.
- **Answer Shuffling:** On every display of a question, the order of the 4 answer choices (A, B, C, D) must be randomly shuffled so the correct answer position is unpredictable.
- **Immediate / Post-Round Feedback:** Display whether the choice was correct, highlight the right answer, and show the explanation.
- **Session Results:** Calculate score, percentage, completion time, and provide review mode for incorrect answers.
- **Replayability:** One-click restart immediately loads a fresh set of 5 random questions.
- **Additional Mode:** Ability to practice all questions by specific topic or browse/search the full 200-question bank.

### R3. Modern Interactive Web Application (Frontend)
- Standalone, zero-install web application runnable directly in modern browsers (e.g., `index.html` with modern CSS/Tailwind, Lucide icons, responsive layout).
- Polished, user-friendly UI with smooth animations, progress bar, score counter, sound effects/visual flair (e.g. celebratory confetti on high scores).
- No external server requirement; all state and question loading handled client-side cleanly.

### R4. Verification & Validation Scripts
- Provide an automated validation script (Python or Node.js) that validates `questions.json`:
  - Total question count $\ge 200$.
  - All 14 topic IDs are present and adequately represented.
  - Every question has exactly 4 distinct options and a valid correct answer matching one of the options.
- Provide a test runner verifying that repeated 5-question selections produce randomized question subsets and randomized option orders.

## Acceptance Criteria

### Data Bank Verification
- [ ] `questions.json` exists, is valid JSON, and contains $\ge 200$ valid questions.
- [ ] Questions cover all 14 lecture topics from Lecture 1 to Lecture 14.
- [ ] Automated validation script passes with zero errors or schema violations.

### Gameplay Verification
- [ ] Starting a quick round presents exactly 5 questions.
- [ ] Shuffling is verified: the same question shown in consecutive runs displays options in different permutations.
- [ ] Answering questions correctly increments the score; answering incorrectly shows the explanation and the correct choice.
- [ ] Result screen accurately summarizes total score (e.g. 4/5 - 80%) with a functional "Chơi lại" button that triggers a new random 5-question set.

### Usability & Delivery
- [ ] Launching `index.html` in Chrome/Edge displays the quiz game immediately without errors.
- [ ] UI is fully in Vietnamese with accurate C++ terminology and responsive on desktop and mobile.
