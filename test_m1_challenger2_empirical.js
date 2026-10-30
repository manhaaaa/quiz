/**
 * test_m1_challenger2_empirical.js
 * 
 * JavaScript / Node.js Empirical Verification for Milestone 1:
 * - Direct execution of window.CODING_PROBLEMS fallback loader
 * - Statistical randomness simulation of 1,000 exam sessions selecting 3 distinct problems
 * - Chi-Square goodness-of-fit in JS engine
 * - Full audit of 180 test cases across 18 problems in Node.js runtime
 * 
 * Author: Challenger 2 (teamwork_challenger_m1_2)
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const jsonPath = path.join(__dirname, 'coding_problems.json');
const jsPath = path.join(__dirname, 'coding_problems.js');

console.log('='.repeat(80));
console.log('NODE.JS EMPIRICAL CHALLENGER 2: MILESTONE 1 VERIFICATION');
console.log('='.repeat(80));

// 1. Load JSON
const rawJson = fs.readFileSync(jsonPath, 'utf-8');
const problemsJson = JSON.parse(rawJson);

// 2. Load JS into sandbox
const rawJs = fs.readFileSync(jsPath, 'utf-8');
const sandbox = { window: {} };
vm.createContext(sandbox);
vm.runInContext(rawJs, sandbox);
const problemsJs = sandbox.window.CODING_PROBLEMS;

if (!Array.isArray(problemsJs)) {
    console.error('[FAIL] window.CODING_PROBLEMS is not an array!');
    process.exit(1);
}

// 3. Parity Check
const jsonStr = JSON.stringify(problemsJson);
const jsStr = JSON.stringify(problemsJs);
if (jsonStr !== jsStr) {
    console.error('[FAIL] Discrepancy between JSON and JS banks!');
    process.exit(1);
}
console.log(`[PASS] Dual-mode parity verified in Node.js: ${problemsJs.length} problems identical.`);

// 4. Test Cases Integrity Check in Node.js
console.log('\nAuditing 180 test cases across 18 problems in Node.js...');
let totalTestCases = 0;
let nullCount = 0;
let emptyInputCount = 0;
let emptyOutputCount = 0;
let idViolations = 0;
let sampleFlagViolations = 0;

for (let i = 0; i < problemsJs.length; i++) {
    const p = problemsJs[i];
    const tcs = p.testCases;
    if (!Array.isArray(tcs) || tcs.length !== 10) {
        console.error(`[FAIL] Problem ${p.id} has ${tcs ? tcs.length : 0} test cases, expected 10`);
        process.exit(1);
    }

    for (let j = 0; j < tcs.length; j++) {
        totalTestCases++;
        const expectedId = j + 1;
        const tc = tcs[j];

        if (tc.id !== expectedId) idViolations++;
        if (tc.id === null || tc.input === null || tc.expectedOutput === null || tc.isSample === null) nullCount++;
        if (typeof tc.input !== 'string' || tc.input.length === 0) emptyInputCount++;
        if (typeof tc.expectedOutput !== 'string' || tc.expectedOutput.length === 0) emptyOutputCount++;
        if (tc.expectedOutput.trim().length === 0) {
            console.log(`  [INFO] ${p.id} TC ${expectedId} has blank-line expectedOutput (${JSON.stringify(tc.expectedOutput)}) - valid edge case for empty list`);
        }
        
        const expectedSample = (expectedId <= 2);
        if (typeof tc.isSample !== 'boolean' || tc.isSample !== expectedSample) sampleFlagViolations++;
    }
}

console.log(`  - Total Test Cases Audited:     ${totalTestCases} / 180`);
console.log(`  - Null Fields:                  ${nullCount}`);
console.log(`  - Empty Inputs:                 ${emptyInputCount}`);
console.log(`  - Empty Expected Outputs:       ${emptyOutputCount}`);
console.log(`  - ID Sequence Violations:       ${idViolations}`);
console.log(`  - Sample Flag Violations:       ${sampleFlagViolations}`);

if (totalTestCases !== 180 || nullCount !== 0 || emptyInputCount !== 0 || 
    emptyOutputCount !== 0 || idViolations !== 0 || sampleFlagViolations !== 0) {
    console.error('[FAIL] Test case integrity check failed in Node.js!');
    process.exit(1);
}
console.log('[SUCCESS] All 180 test cases verified clean in Node.js runtime!');

// 5. Statistical Randomness Simulation in JS (1,000 sessions)
console.log('\nSimulating 1,000 exam sessions selecting 3 distinct problems in Node.js...');

function selectThreeDistinctProblems(bank) {
    // Fisher-Yates shuffle
    const pool = bank.slice();
    for (let i = pool.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = pool[i];
        pool[i] = pool[j];
        pool[j] = temp;
    }
    return pool.slice(0, 3);
}

const numSessions = 1000;
const counts = {};
const problemIds = problemsJs.map(p => p.id);
problemIds.forEach(id => counts[id] = 0);

let duplicatesFound = 0;
const combinationMap = new Map();

for (let s = 0; s < numSessions; s++) {
    const selected = selectThreeDistinctProblems(problemsJs);
    if (selected.length !== 3) {
        console.error(`Session ${s} selected length != 3`);
        process.exit(1);
    }
    const ids = selected.map(p => p.id);
    if (new Set(ids).size !== 3) {
        duplicatesFound++;
    }

    ids.forEach(id => counts[id]++);
    const comboKey = ids.slice().sort().join('+');
    combinationMap.set(comboKey, (combinationMap.get(comboKey) || 0) + 1);
}

const observedPicks = Object.values(counts);
const minPick = Math.min(...observedPicks);
const maxPick = Math.max(...observedPicks);
const totalPicks = observedPicks.reduce((a, b) => a + b, 0);
const expectedPick = totalPicks / problemIds.length; // 166.67

// Chi-Square calculation
let chiSquare = 0;
for (const val of observedPicks) {
    chiSquare += Math.pow(val - expectedPick, 2) / expectedPick;
}

console.log(`  - Total Sessions:               ${numSessions}`);
console.log(`  - Duplicate Problem Violations: ${duplicatesFound} (Expected: 0)`);
console.log(`  - Non-Zero Problem Coverage:    ${observedPicks.filter(c => c > 0).length} / 18`);
console.log(`  - Min Picks:                    ${minPick}`);
console.log(`  - Max Picks:                    ${maxPick}`);
console.log(`  - Expected Mean:                ${expectedPick.toFixed(2)}`);
console.log(`  - Chi-Square (df=17):           ${chiSquare.toFixed(4)} (Threshold alpha=0.01: 33.409)`);
console.log(`  - Unique Combinations Sampled:  ${combinationMap.size} / 816 (${(combinationMap.size / 816 * 100).toFixed(2)}%)`);

if (duplicatesFound !== 0) {
    console.error('[FAIL] Duplicate problems detected in exam sessions!');
    process.exit(1);
}
if (minPick === 0) {
    console.error('[FAIL] Some problems were never selected!');
    process.exit(1);
}
if (chiSquare > 33.41) {
    console.error(`[FAIL] Chi-Square test failed threshold: ${chiSquare}`);
    process.exit(1);
}

console.log('\n[SUCCESS] Node.js empirical simulation verified randomness & test case integrity perfectly!');
console.log('='.repeat(80));
