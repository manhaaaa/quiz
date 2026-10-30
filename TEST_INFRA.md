# E2E Test Infra: C++ and Data Structures & Algorithms Quiz Review Game

## Test Philosophy
- Opaque-box, requirement-driven, deterministic automated verification.
- Enforce full compliance with ORIGINAL_REQUEST.md requirements R1, R2, R3, R4.
- Methodology: Category-Partition + Boundary Value Analysis + Pairwise Combinatorial Testing + Workload Simulation.

## Feature Inventory & Test Coverage Mapping
| # | Feature | Source (Requirement) | Tier 1 (Coverage) | Tier 2 (Boundary) | Tier 3 (Cross-Feature) | Tier 4 (Workload) |
|---|---------|----------------------|:-----------------:|:-----------------:|:----------------------:|:-----------------:|
| 1 | 14-Topic Question Bank | R1 §12-30 | 5 | 5 | ✓ | ✓ |
| 2 | Question Schema & Options | R1 §29 | 5 | 5 | ✓ | ✓ |
| 3 | Vietnamese Technical Terminology | R1 §28 | 5 | 5 | ✓ | ✓ |
| 4 | 5-Question Random Round Mode | R2 §32 | 5 | 5 | ✓ | ✓ |
| 5 | Answer Shuffling Engine | R2 §33 | 5 | 5 | ✓ | ✓ |
| 6 | Immediate & Post-Round Feedback | R2 §34 | 5 | 5 | ✓ | ✓ |
| 7 | Session Results & Review Mode | R2 §35 | 5 | 5 | ✓ | ✓ |
| 8 | One-Click Replayability | R2 §36 | 5 | 5 | ✓ | ✓ |
| 9 | Topic Practice & Bank Search | R2 §37 | 5 | 5 | ✓ | ✓ |
| 10 | Modern Responsive Web UI | R3 §40-42 | 5 | 5 | ✓ | ✓ |
| 11 | Sound & Visual Flair (Confetti) | R3 §41 | 5 | 5 | ✓ | ✓ |
| 12 | Automated Bank Verification Script | R4 §45-48 | 5 | 5 | ✓ | ✓ |
| 13 | Randomness & Shuffling Test Runner | R4 §49 | 5 | 5 | ✓ | ✓ |
| 14 | Zero-Install Dual Data Fallback | R3 §40, 42 | 5 | 5 | ✓ | ✓ |

## Test Architecture
- **Automated Verification Harness:** `verify_bank.py`
  - Validates `questions.json` and `questions.js`
  - Verifies question count $\ge 200$ (target 210 questions)
  - Verifies presence and distribution across all 14 lecture topics ($\ge 14$ questions per topic)
  - Verifies schema keys (`id`, `topicId`, `topicName`, `question`, `options`, `answer`, `explanation`)
  - Verifies exactly 4 unique options per question
  - Verifies exact match between `answer` and one of the `options`
  - Verifies non-empty Vietnamese explanations and exact C++ technical terms
- **Gameplay & Randomness Test Runner:** `test_quiz_engine.py`
  - Simulates 1,000 independent 5-question rounds
  - Verifies topic diversity (no round with only 1 topic)
  - Verifies question randomization distribution (every question has non-zero probability of being selected)
  - Simulates 10,000 question displays with option shuffling:
    - Verifies all 24 permutations ($4!$) of 4 options are reachable
    - Verifies uniform distribution of correct answer position across index 0, 1, 2, 3 (each approximately 25% within statistical tolerance)
  - Verifies scoring logic: 0/5 (0%), 1/5 (20%), ..., 5/5 (100%)
  - Verifies replayability and round reset invariants
- **Browser Execution Test Checklist:**
  - Automated or headless check for `index.html` loading without JavaScript syntax errors or uncaught exceptions
  - Verification of dual data loading (`fetch` + fallback `window.QUIZ_QUESTIONS`)

## Coverage Thresholds
- Tier 1: $\ge 70$ feature verification assertions
- Tier 2: $\ge 70$ boundary & edge case checks (empty inputs, single questions, max limits, duplicate options)
- Tier 3: $\ge 14$ cross-feature interaction simulations
- Tier 4: $\ge 10$ full end-to-end user session scenarios
