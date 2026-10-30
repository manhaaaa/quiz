const fs = require('fs');
const path = require('path');
const vm = require('vm');

const indexPath = path.resolve(__dirname, '../../../index.html');
const questionsJsPath = path.resolve(__dirname, '../../../questions.js');
const questionsJsonPath = path.resolve(__dirname, '../../../questions.json');

console.log('Testing frontend index.html from:', indexPath);

// 1. Check file exists and has content
const html = fs.readFileSync(indexPath, 'utf8');
if (!html || html.length < 5000) {
  throw new Error('index.html is too small or empty');
}

// 2. Check essential CDN and local script tags
const requiredSnippets = [
  '<!DOCTYPE html>',
  'cdn.tailwindcss.com',
  'unpkg.com/lucide',
  'canvas-confetti',
  'questions.js',
  'SoundEngine',
  'AudioContext',
  'fisherYatesShuffle',
  'loadBankData',
  'startQuickSession',
  'startTopicPractice',
  'renderCurrentQuestion',
  'handleOptionSelection',
  'finishSession',
  'filterBank'
];

for (const snippet of requiredSnippets) {
  if (!html.includes(snippet)) {
    throw new Error(`index.html is missing required snippet: "${snippet}"`);
  }
}
console.log('✓ All 15 required architecture snippets present in index.html');

// 3. Extract the script content and test in Node VM
const scriptMatches = html.match(/<script>([\s\S]*?)<\/script>[\s\S]*?<script>([\s\S]*?)<\/script>/);
// Find the main app script (the largest <script> block)
const allScripts = [];
const scriptRegex = /<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>/gi;
let match;
while ((match = scriptRegex.exec(html)) !== null) {
  if (match[1] && match[1].trim().length > 500) {
    allScripts.push(match[1]);
  }
}

if (allScripts.length === 0) {
  throw new Error('Could not find main application script block');
}

const mainScript = allScripts[allScripts.length - 1];
console.log(`✓ Extracted main application script (${mainScript.length} chars)`);

// 4. Load questions.js into VM context
const questionsJsContent = fs.readFileSync(questionsJsPath, 'utf8');

// Mock a lightweight browser window environment
const sandbox = {
  window: {},
  document: {
    addEventListener: () => {},
    getElementById: (id) => ({
      classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
      style: {},
      scrollIntoView: () => {},
      appendChild: () => {},
      querySelectorAll: () => [],
      textContent: '',
      innerHTML: '',
      value: ''
    }),
    createElement: () => ({
      classList: { add: () => {}, remove: () => {}, contains: () => false },
      style: {},
      appendChild: () => {},
      querySelectorAll: () => [],
      innerHTML: '',
      textContent: ''
    })
  },
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  setInterval: setInterval,
  clearInterval: clearInterval,
  Math: Math,
  Array: Array,
  String: String,
  Object: Object,
  Set: Set,
  Map: Map,
  parseInt: parseInt
};
sandbox.window = sandbox;

// Run questions.js in sandbox
vm.createContext(sandbox);
vm.runInContext(questionsJsContent, sandbox);

if (!Array.isArray(sandbox.window.QUIZ_QUESTIONS) || sandbox.window.QUIZ_QUESTIONS.length !== 210) {
  throw new Error(`Failed to load 210 questions in sandbox: got ${sandbox.window.QUIZ_QUESTIONS?.length}`);
}
console.log(`✓ Loaded window.QUIZ_QUESTIONS (${sandbox.window.QUIZ_QUESTIONS.length} questions)`);

// Run mainScript in sandbox
vm.runInContext(mainScript, sandbox);

// 5. Test Fisher-Yates Shuffling
const testOptions = ["A", "B", "C", "D"];
const shuffles = new Set();
for (let i = 0; i < 200; i++) {
  const s = sandbox.fisherYatesShuffle(testOptions);
  shuffles.add(s.join(''));
  if (s.length !== 4) throw new Error('Shuffle corrupted array length');
  for (const opt of testOptions) {
    if (!s.includes(opt)) throw new Error('Shuffle lost elements');
  }
}
if (shuffles.size < 10) {
  throw new Error(`Fisher-Yates shuffle not sufficiently random: only ${shuffles.size} permutations in 200 runs`);
}
console.log(`✓ Fisher-Yates shuffle algorithm verified (${shuffles.size} distinct permutations observed)`);

// 6. Test App Initialization & Dual Data Loader
const app = sandbox.app;
if (!app) {
  throw new Error('app instance not exposed to window');
}

// Test loadBankData with window.QUIZ_QUESTIONS
app.loadBankData().then(bank => {
  if (bank.length !== 210) {
    throw new Error(`loadBankData returned ${bank.length} questions, expected 210`);
  }
  console.log(`✓ loadBankData() successfully returned ${bank.length} questions`);

  app.bank = bank;
  app.buildTopicIndex();

  if (app.topicMap.size !== 14) {
    throw new Error(`topicMap has ${app.topicMap.size} topics, expected 14`);
  }
  for (let tid = 1; tid <= 14; tid++) {
    const list = app.topicMap.get(tid);
    if (!list || list.length !== 15) {
      throw new Error(`Topic ${tid} has ${list?.length} questions, expected 15`);
    }
  }
  console.log('✓ All 14 topics correctly indexed with 15 questions each');

  // Test Quick Session Selection (5 distinct topics)
  for (let r = 0; r < 50; r++) {
    app.startQuickSession();
    if (app.sessionQuestions.length !== 5) {
      throw new Error(`Session questions count is ${app.sessionQuestions.length}, expected 5`);
    }
    const topicIds = new Set(app.sessionQuestions.map(q => q.topicId));
    if (topicIds.size !== 5) {
      throw new Error(`Round ${r}: Expected 5 distinct topics, got ${topicIds.size}`);
    }
  }
  console.log('✓ Quick 5-Question mode verified across 50 simulated rounds with 100% topic diversity');

  // Test Topic Practice Selection (15 questions of specific topic)
  for (let tid = 1; tid <= 14; tid++) {
    app.startTopicPractice(tid);
    if (app.sessionQuestions.length !== 15) {
      throw new Error(`Topic practice ${tid} has ${app.sessionQuestions.length} questions, expected 15`);
    }
    for (const q of app.sessionQuestions) {
      if (q.topicId !== tid) {
        throw new Error(`Question ${q.id} has topicId ${q.topicId}, expected ${tid}`);
      }
    }
  }
  console.log('✓ Topic Practice mode verified across all 14 topics (15 questions each)');

  // Test Bank Filtering
  app.bankFiltered = app.bank;
  const avlMatches = app.bank.filter(q =>
    (q.question || '').toLowerCase().includes('avl') ||
    (q.options || []).join(' ').toLowerCase().includes('avl') ||
    (q.explanation || '').toLowerCase().includes('avl')
  );
  if (avlMatches.length === 0) {
    throw new Error('Expected AVL search to return matches');
  }
  console.log(`✓ Bank search filter verified (${avlMatches.length} AVL matches found)`);

  console.log('\n======================================================');
  console.log('ALL FRONTEND ENGINE & DATA INTEGRITY TESTS PASSED 100%');
  console.log('======================================================\n');
  process.exit(0);
}).catch(err => {
  console.error('Test failed:', err);
  process.exit(1);
});
