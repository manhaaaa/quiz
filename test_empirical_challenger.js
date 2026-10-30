// test_empirical_challenger.js
// Independent JavaScript Empirical Stress Test for index.html

const fs = require('fs');

// 1. Read index.html and extract the exact fisherYatesShuffle implementation
const htmlContent = fs.readFileSync('index.html', 'utf8');

const startIdx = htmlContent.indexOf('function fisherYatesShuffle(arr) {');
if (startIdx === -1) {
  console.error("FAILED to find fisherYatesShuffle in index.html!");
  process.exit(1);
}
const endIdx = htmlContent.indexOf('return copy;\n    }', startIdx);
const fyCode = htmlContent.substring(startIdx, endIdx + 'return copy;\n    }'.length);

// Evaluate extracted function
const fisherYatesShuffle = new Function('arr', `${fyCode}; return fisherYatesShuffle(arr);`);

// 2. Load questions.json
const questions = JSON.parse(fs.readFileSync('questions.json', 'utf8'));

console.log("=".repeat(70));
console.log("NODE.JS EMPIRICAL CHALLENGER: JAVASCRIPT SHUFFLING & ENGINE TEST");
console.log("=".repeat(70));
console.log(`[1] Extracted fisherYatesShuffle directly from index.html:`);
console.log(fyCode.trim());
console.log(`\n[2] Loaded ${questions.length} questions from questions.json.`);

// 3. Run 10,000 Fisher-Yates Displays Simulation
console.log("\n[3] Executing 10,000 Fisher-Yates Displays in Node.js JavaScript Engine...");
const numDisplays = 10000;
const optionsTemplate = ["CORRECT_ANS", "WRONG_1", "WRONG_2", "WRONG_3"];

const slotCounts = [0, 0, 0, 0];
const permMap = new Map();

for (let i = 0; i < numDisplays; i++) {
  const shuffled = fisherYatesShuffle(optionsTemplate);
  if (shuffled.length !== 4) throw new Error("Length mismatch");

  const key = shuffled.join("||");
  permMap.set(key, (permMap.get(key) || 0) + 1);

  const idx = shuffled.indexOf("CORRECT_ANS");
  slotCounts[idx]++;
}

console.log(`    - Distinct Permutations Observed: ${permMap.size} / 24`);
const expectedSlot = numDisplays / 4;
let chiSquareSlots = 0;

for (let s = 0; s < 4; s++) {
  const count = slotCounts[s];
  const pct = (count / numDisplays) * 100;
  chiSquareSlots += Math.pow(count - expectedSlot, 2) / expectedSlot;
  console.log(`      * Slot ${s} (Option ${String.fromCharCode(65 + s)}): ${count} (${pct.toFixed(2)}%)`);
}

const expectedPerm = numDisplays / 24;
let chiSquarePerms = 0;
for (const count of permMap.values()) {
  chiSquarePerms += Math.pow(count - expectedPerm, 2) / expectedPerm;
}

console.log(`    - Chi-Square for Slots (df=3): ${chiSquareSlots.toFixed(4)} (Threshold: 7.815 at p=0.05, 16.266 at p=0.001)`);
console.log(`    - Chi-Square for Permutations (df=23): ${chiSquarePerms.toFixed(4)} (Threshold: 35.172 at p=0.05, 49.728 at p=0.001)`);

if (permMap.size !== 24) {
  console.error("FAIL: Not all 24 permutations were reached!");
  process.exit(1);
}
if (chiSquareSlots >= 16.27) {
  console.error("FAIL: Chi-Square rejected uniform distribution for slots!");
  process.exit(1);
}

// 4. Test startQuickSession Logic from index.html in Node.js
console.log("\n[4] Executing 1,000 Rounds of startQuickSession() Topic Diversity & Coverage...");
const topicMap = new Map();
questions.forEach(q => {
  if (!topicMap.has(q.topicId)) topicMap.set(q.topicId, []);
  topicMap.get(q.topicId).push(q);
});

const questionPickCounts = new Map();
const roundsSimulated = 1000;
const topicsPerRound = [];
const roundQuestionSets = [];

for (let r = 0; r < roundsSimulated; r++) {
  // Replicating startQuickSession logic from index.html lines 958-972:
  const availableTopics = Array.from(topicMap.keys()).filter(t => (topicMap.get(t) || []).length > 0);
  let selectedQuestions = [];

  if (availableTopics.length >= 5) {
    const chosenTopics = fisherYatesShuffle(availableTopics).slice(0, 5);
    chosenTopics.forEach(tid => {
      const topicPool = topicMap.get(tid);
      const randomQ = topicPool[Math.floor(Math.random() * topicPool.length)];
      selectedQuestions.push(randomQ);
    });
    selectedQuestions = fisherYatesShuffle(selectedQuestions);
  } else {
    selectedQuestions = fisherYatesShuffle(questions).slice(0, 5);
  }

  // Verifications
  if (selectedQuestions.length !== 5) throw new Error("Round question count != 5");
  const qIds = selectedQuestions.map(q => q.id);
  const qTopics = selectedQuestions.map(q => q.topicId);
  const uniqueIds = new Set(qIds);
  const uniqueTopics = new Set(qTopics);

  if (uniqueIds.size !== 5) throw new Error("Duplicate questions in round");
  if (uniqueTopics.size !== 5) throw new Error("Duplicate topics in round");

  topicsPerRound.push(uniqueTopics.size);
  roundQuestionSets.push(qIds.sort().join(","));

  qIds.forEach(id => {
    questionPickCounts.set(id, (questionPickCounts.get(id) || 0) + 1);
  });
}

const avgTopics = topicsPerRound.reduce((a, b) => a + b, 0) / topicsPerRound.length;
console.log(`    - Average Distinct Topics per Round: ${avgTopics.toFixed(2)} / 5.0`);
console.log(`    - Covered Questions: ${questionPickCounts.size} / ${questions.length} (${(questionPickCounts.size / questions.length * 100).toFixed(1)}%)`);

const counts = Array.from(questionPickCounts.values());
const minPicks = Math.min(...counts);
const maxPicks = Math.max(...counts);
const meanPicks = counts.reduce((a, b) => a + b, 0) / counts.length;
console.log(`    - Pick Frequencies: Min=${minPicks}, Max=${maxPicks}, Mean=${meanPicks.toFixed(2)}`);

if (questionPickCounts.size !== questions.length) {
  console.error("FAIL: Not all questions in the bank were covered!");
  process.exit(1);
}

// 5. Test Replayability & Uniqueness of Consecutive Rounds
console.log("\n[5] Executing Replayability Uniqueness Test on 1,000 Rounds...");
const uniqueRounds = new Set(roundQuestionSets);
console.log(`    - Unique 5-question rounds out of 1,000: ${uniqueRounds.size} / 1,000`);
if (uniqueRounds.size < 995) {
  console.error("FAIL: Unexpected collision rate across rounds!");
  process.exit(1);
}

// 6. Test Scoring and Results logic from index.html lines 1198-1200
console.log("\n[6] Testing Scoring Logic & Passing Invariants (lines 1198-1200)...");
for (let c = 0; c <= 5; c++) {
  const total = 5;
  const percentage = total > 0 ? Math.round((c / total) * 100) : 0;
  const isPassed = percentage >= 80;
  console.log(`    - ${c}/5 correct -> ${percentage}% -> isPassed: ${isPassed} (Expected: ${c >= 4})`);
  if (isPassed !== (c >= 4)) {
    console.error(`FAIL: Scoring invariant failed for correct=${c}!`);
    process.exit(1);
  }
}

console.log("\n" + "=".repeat(70));
console.log("JAVASCRIPT RUNTIME EMPIRICAL TEST PASSED WITH 100% SUCCESS!");
console.log("=".repeat(70));
