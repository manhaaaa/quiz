#!/usr/bin/env node
/**
 * ============================================================================
 * C++ & DSA Quiz Review: Execution & Evaluation HTTP Server
 * ============================================================================
 * Target: d:\c++\quiz_game\server.js
 * Architecture: Pure Node.js Zero-Dependency HTTP & Static File Server
 * Features:
 *   - Zero external npm dependencies (uses only Node.js core modules)
 *   - Streaming static file delivery with path traversal protection
 *   - Permissive CORS on all endpoints (GET, POST, OPTIONS)
 *   - 10MB streaming JSON request body parser
 *   - Diagnostic compiler discovery (GET /api/health)
 *   - C++ compilation (g++ -std=c++17 -Wall) in isolated temp sandbox
 *   - Sequential 10-test-case execution with 2.0s timeout & taskkill process tree kill
 *   - Dual-stage output normalization (CRLF -> LF, line trim, token comparison fallback)
 *   - Windows NTSTATUS crash translation (0xC0000005, 0xC0000094, etc.)
 *   - Guaranteed 5-attempt retry cleanup with exponential backoff
 * ============================================================================
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const { spawn, execFile, execSync } = require('child_process');
const crypto = require('crypto');
const { performance } = require('perf_hooks');

// ============================================================================
// Configuration & Constants
// ============================================================================
const PUBLIC_DIR = path.resolve(__dirname);
const MAX_BODY_BYTES = 10 * 1024 * 1024;      // 10 MB payload limit
const COMPILE_TIMEOUT_MS = 10000;             // 10.0 seconds compile timeout
const TEST_CASE_TIMEOUT_MS = 2000;           // 2.0 seconds per test case
const MAX_OUTPUT_BYTES = 1024 * 1024;        // 1 MB stdout limit

const MIME_MAP = {
  '.html': 'text/html; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
  '.cpp': 'text/plain; charset=utf-8'
};

// ============================================================================
// Port Resolution
// ============================================================================
function resolvePort() {
  if (process.env.PORT) {
    const p = parseInt(process.env.PORT, 10);
    if (!isNaN(p)) return p;
  }
  const args = process.argv.slice(2);
  for (let i = 0; i < args.length; i++) {
    if ((args[i] === '--port' || args[i] === '-p') && args[i + 1]) {
      const p = parseInt(args[i + 1], 10);
      if (!isNaN(p)) return p;
    }
    const directPort = parseInt(args[i], 10);
    if (!isNaN(directPort) && directPort > 0) {
      return directPort;
    }
  }
  return 3000;
}

const PORT = resolvePort();

// ============================================================================
// Toolchain Detection & Problem Bank Caching
// ============================================================================
function probeCompiler() {
  const info = {
    status: 'ok',
    compiler: 'g++',
    version: 'unknown',
    platform: process.platform,
    compilerBanner: '',
    compilerPath: 'g++',
    available: false
  };

  try {
    const banner = execSync('g++ --version', {
      encoding: 'utf-8',
      timeout: 5000,
      stdio: ['ignore', 'pipe', 'ignore']
    });
    info.compilerBanner = banner.split('\n')[0].trim();
    info.available = true;

    const match = info.compilerBanner.match(/(\d+\.\d+\.\d+)/);
    if (match) {
      info.version = match[1];
    }

    try {
      const whereCmd = process.platform === 'win32' ? 'where.exe g++' : 'which g++';
      const out = execSync(whereCmd, {
        encoding: 'utf-8',
        timeout: 3000,
        stdio: ['ignore', 'pipe', 'ignore']
      });
      const lines = out.trim().split(/\r?\n/);
      if (lines.length > 0 && lines[0]) {
        info.compilerPath = lines[0].trim();
      }
    } catch (_) {}
  } catch (err) {
    info.status = 'degraded';
    info.error = err.message;
  }

  return info;
}

const cachedCompiler = probeCompiler();

let problemBank = [];
const problemMap = new Map();

function loadProblemBank() {
  try {
    const p = path.join(PUBLIC_DIR, 'coding_problems.json');
    if (fs.existsSync(p)) {
      const data = fs.readFileSync(p, 'utf-8');
      problemBank = JSON.parse(data);
      problemMap.clear();
      for (const prob of problemBank) {
        if (prob && prob.id) {
          problemMap.set(prob.id, prob);
        }
      }
    }
  } catch (err) {
    console.warn('[WARN] Could not load coding_problems.json:', err.message);
  }
}

loadProblemBank();

// ============================================================================
// Output Normalization & Comparison
// ============================================================================
/**
 * Line ending canonicalization & trailing whitespace trimmer
 */
function normalizeOutput(rawText) {
  if (typeof rawText !== 'string') return '';
  return rawText
    .replace(/\r\n/g, '\n')
    .replace(/\r/g, '\n')
    .split('\n')
    .map(line => line.trimEnd())
    .join('\n')
    .trim();
}

/**
 * Dual-stage comparison:
 * Stage 1: Line-by-line whitespace-normalized equality
 * Stage 2: Whitespace-agnostic token comparison fallback
 */
function compareOutputs(actualRaw, expectedRaw) {
  const actualNorm = normalizeOutput(actualRaw);
  const expectedNorm = normalizeOutput(expectedRaw);

  // Stage 1: Direct normalized match
  if (actualNorm === expectedNorm) {
    return true;
  }

  // Stage 2: Token-based comparison fallback
  const actualTokens = actualNorm.split(/\s+/).filter(Boolean);
  const expectedTokens = expectedNorm.split(/\s+/).filter(Boolean);

  if (actualTokens.length !== expectedTokens.length) {
    return false;
  }

  for (let i = 0; i < actualTokens.length; i++) {
    if (actualTokens[i] !== expectedTokens[i]) {
      return false;
    }
  }

  return true;
}

// ============================================================================
// Windows NTSTATUS Crash Mapping
// ============================================================================
function getRuntimeErrorMessage(exitCode) {
  if (exitCode === null || exitCode === undefined) {
    return 'Runtime Error: Process terminated unexpectedly';
  }
  const unsignedCode = (exitCode >>> 0);
  const hex = '0x' + unsignedCode.toString(16).toUpperCase().padStart(8, '0');

  switch (unsignedCode) {
    case 0xC0000005:
      return `Runtime Error (STATUS_ACCESS_VIOLATION: Lỗi truy cập bộ nhớ / Segmentation Fault ${hex}): Con trỏ null hoặc chỉ số mảng vượt giới hạn`;
    case 0xC0000094:
      return `Runtime Error (STATUS_INTEGER_DIVIDE_BY_ZERO: Lỗi chia cho 0 / Integer Division by Zero ${hex}): Thực hiện phép chia hoặc lấy dư cho 0`;
    case 0xC00000FD:
      return `Runtime Error (STATUS_STACK_OVERFLOW: Tràn bộ nhớ ngăn xếp / Đệ quy vô hạn ${hex}): Đệ quy vô hạn hoặc khai báo mảng tĩnh quá lớn`;
    case 0xC0000409:
      return `Runtime Error (STATUS_STACK_BUFFER_OVERRUN: Abort / Assert thất bại / Tràn bộ đệm ${hex}): Chương trình gọi abort() hoặc kiểm tra tràn bộ đệm thất bại`;
    case 0xC000001D:
      return `Runtime Error (STATUS_ILLEGAL_INSTRUCTION: Thực thi lệnh CPU không hợp lệ ${hex})`;
    case 0xC0000017:
      return `Runtime Error (STATUS_NO_MEMORY: Hết bộ nhớ RAM ${hex})`;
    case 0xC0000374:
      return `Runtime Error (STATUS_HEAP_CORRUPTION: Hỏng bộ nhớ heap ${hex})`;
    default:
      return `Runtime Error: Process exited with code ${exitCode} (${hex})`;
  }
}

// ============================================================================
// Process Control & Cleanup Helpers
// ============================================================================
function killProcessTree(pid) {
  if (!pid) return;
  if (process.platform === 'win32') {
    try {
      execSync(`taskkill /F /T /PID ${pid}`, { stdio: 'ignore' });
    } catch (_) {}
  } else {
    try {
      process.kill(-pid, 'SIGKILL');
    } catch (_) {
      try {
        process.kill(pid, 'SIGKILL');
      } catch (_) {}
    }
  }
}

async function safeRemoveDirectory(dirPath, maxAttempts = 5, baseDelayMs = 50) {
  if (!dirPath || !fs.existsSync(dirPath)) return;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      fs.rmSync(dirPath, { recursive: true, force: true });
      return;
    } catch (err) {
      if (attempt === maxAttempts) {
        console.warn(`[Cleanup Warning] Failed to delete ${dirPath} after ${maxAttempts} attempts:`, err.message);
      } else {
        await new Promise((resolve) => setTimeout(resolve, baseDelayMs * Math.pow(2, attempt - 1)));
      }
    }
  }
}

// ============================================================================
// C++ Compilation & Process Execution Engine
// ============================================================================
function compileCpp(sandboxDir, sourcePath, binaryPath) {
  return new Promise((resolve) => {
    const args = ['-std=c++17', '-Wall', sourcePath, '-o', binaryPath];
    const startTime = performance.now();

    execFile('g++', args, {
      cwd: sandboxDir,
      timeout: COMPILE_TIMEOUT_MS,
      maxBuffer: MAX_BODY_BYTES,
      windowsHide: true
    }, (error, stdout, stderr) => {
      const compileTimeMs = Math.round(performance.now() - startTime);

      if (error) {
        if (error.killed || error.signal === 'SIGTERM') {
          return resolve({
            success: false,
            output: `Compilation timed out after ${(COMPILE_TIMEOUT_MS / 1000).toFixed(1)}s. Your code may contain infinite template recursions or macro expansion loops.`,
            compileTimeMs,
            binaryPath: null
          });
        }
        const combined = (stderr || stdout || error.message || 'Compilation failed').trim();
        return resolve({
          success: false,
          output: combined,
          compileTimeMs,
          binaryPath: null
        });
      }

      const warnings = (stderr || '').trim();
      resolve({
        success: true,
        output: warnings,
        compileTimeMs,
        binaryPath
      });
    });
  });
}

function executeTestCase(binaryPath, input = '', timeoutMs = TEST_CASE_TIMEOUT_MS) {
  return new Promise((resolve) => {
    const sandboxDir = path.dirname(binaryPath);
    const startTime = performance.now();

    const child = spawn(binaryPath, [], {
      cwd: sandboxDir,
      stdio: ['pipe', 'pipe', 'pipe'],
      windowsHide: true
    });

    let stdoutData = '';
    let stderrData = '';
    let timedOut = false;
    let outputLimitExceeded = false;
    let isClosed = false;

    const timer = setTimeout(() => {
      timedOut = true;
      killProcessTree(child.pid);
    }, timeoutMs);

    child.stdin.on('error', () => {});

    try {
      child.stdin.write(input, 'utf-8');
      child.stdin.end();
    } catch (_) {}

    child.stdout.on('data', (chunk) => {
      if (outputLimitExceeded) return;
      stdoutData += chunk.toString('utf-8');
      if (stdoutData.length > MAX_OUTPUT_BYTES) {
        outputLimitExceeded = true;
        killProcessTree(child.pid);
      }
    });

    child.stderr.on('data', (chunk) => {
      if (outputLimitExceeded) return;
      stderrData += chunk.toString('utf-8');
      if (stderrData.length > MAX_OUTPUT_BYTES) {
        outputLimitExceeded = true;
        killProcessTree(child.pid);
      }
    });

    child.on('error', (err) => {
      if (isClosed) return;
      isClosed = true;
      clearTimeout(timer);
      const timeMs = Math.round(performance.now() - startTime);
      resolve({
        exitCode: -1,
        stdout: stdoutData,
        stderr: (stderrData + '\n' + err.message).trim(),
        timeMs,
        timedOut: false,
        outputLimitExceeded: false
      });
    });

    child.on('close', (code) => {
      if (isClosed) return;
      isClosed = true;
      clearTimeout(timer);
      const timeMs = Math.round(performance.now() - startTime);
      resolve({
        exitCode: code,
        stdout: stdoutData,
        stderr: stderrData,
        timeMs,
        timedOut,
        outputLimitExceeded
      });
    });
  });
}

// ============================================================================
// Streaming JSON Request Body Parser (10MB limit)
// ============================================================================
function parseJsonBody(req, maxBytes = MAX_BODY_BYTES) {
  return new Promise((resolve, reject) => {
    let bytesReceived = 0;
    const chunks = [];

    req.on('data', (chunk) => {
      bytesReceived += chunk.length;
      if (bytesReceived > maxBytes) {
        req.destroy();
        const err = new Error(`Payload Too Large: Request body exceeds maximum allowed size of 10MB (${maxBytes} bytes)`);
        err.statusCode = 413;
        reject(err);
        return;
      }
      chunks.push(chunk);
    });

    req.on('end', () => {
      if (chunks.length === 0) {
        return resolve({});
      }
      const bodyText = Buffer.concat(chunks).toString('utf-8');
      if (!bodyText.trim()) {
        return resolve({});
      }
      try {
        const parsed = JSON.parse(bodyText);
        resolve(parsed);
      } catch (syntaxErr) {
        const err = new Error(`Invalid JSON syntax: ${syntaxErr.message}`);
        err.statusCode = 400;
        reject(err);
      }
    });

    req.on('error', (err) => {
      err.statusCode = 400;
      reject(err);
    });
  });
}

// ============================================================================
// Static Asset Delivery Pipeline
// ============================================================================
function serveStaticFile(req, res, decodedPath) {
  // Disallow directory traversal sequences
  if (decodedPath.includes('..')) {
    res.writeHead(403, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    res.end(JSON.stringify({ error: 'Forbidden: Path traversal not permitted' }));
    return;
  }

  let reqPath = decodedPath;
  if (reqPath === '/' || reqPath === '') {
    reqPath = '/index.html';
  }

  const safeSubPath = path.normalize(reqPath);
  const absoluteTarget = path.resolve(PUBLIC_DIR, '.' + safeSubPath);

  // Containment check
  if (!absoluteTarget.startsWith(PUBLIC_DIR)) {
    res.writeHead(403, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    res.end(JSON.stringify({ error: 'Forbidden: Path traversal not permitted' }));
    return;
  }

  fs.stat(absoluteTarget, (statErr, stats) => {
    if (statErr || !stats) {
      res.writeHead(404, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({ error: `File not found: ${path.basename(absoluteTarget)}` }));
      return;
    }

    if (stats.isDirectory()) {
      const indexCandidate = path.join(absoluteTarget, 'index.html');
      if (fs.existsSync(indexCandidate)) {
        return serveStaticFile(req, res, path.join(reqPath, 'index.html').replace(/\\/g, '/'));
      }
      res.writeHead(403, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({ error: 'Directory listing forbidden' }));
      return;
    }

    const ext = path.extname(absoluteTarget).toLowerCase();
    const mimeType = MIME_MAP[ext] || 'application/octet-stream';

    const headers = {
      'Content-Type': mimeType,
      'Content-Length': stats.size,
      'Access-Control-Allow-Origin': '*',
      'Cache-Control': 'no-cache, must-revalidate',
      'X-Content-Type-Options': 'nosniff'
    };

    if (req.method === 'HEAD') {
      res.writeHead(200, headers);
      res.end();
      return;
    }

    res.writeHead(200, headers);
    const stream = fs.createReadStream(absoluteTarget);
    stream.pipe(res);

    stream.on('error', (streamErr) => {
      console.error('[STREAM ERROR]', streamErr);
      if (!res.headersSent) {
        res.writeHead(500, {
          'Content-Type': 'application/json; charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        });
      }
      res.end(JSON.stringify({ error: 'Stream read failure' }));
    });
  });
}

// ============================================================================
// HTTP Request Dispatcher
// ============================================================================
const server = http.createServer(async (req, res) => {
  // CORS Preflight Handler
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, HEAD',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization, Accept, X-Requested-With',
      'Access-Control-Max-Age': '86400'
    });
    res.end();
    return;
  }

  // Parse URL safely
  let parsedUrl;
  try {
    parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  } catch (_) {
    res.writeHead(400, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    res.end(JSON.stringify({ error: 'Malformed request URL' }));
    return;
  }

  // Extract raw path before query string
  const rawPath = (req.url || '/').split('?')[0];

  let decodedPath;
  try {
    decodedPath = decodeURIComponent(rawPath);
  } catch (_) {
    res.writeHead(400, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    res.end(JSON.stringify({ error: 'Malformed URL encoding' }));
    return;
  }

  decodedPath = decodedPath.replace(/\0/g, '');

  // --------------------------------------------------------------------------
  // Endpoint: GET /api/health
  // --------------------------------------------------------------------------
  if (req.method === 'GET' && decodedPath === '/api/health') {
    res.writeHead(200, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    res.end(JSON.stringify({
      status: cachedCompiler.status,
      compiler: cachedCompiler.compiler,
      version: cachedCompiler.version,
      platform: cachedCompiler.platform,
      compilerBanner: cachedCompiler.compilerBanner,
      compilerPath: cachedCompiler.compilerPath,
      nodeVersion: process.version,
      problemsLoaded: problemBank.length,
      uptime: Math.round(process.uptime()),
      timestamp: new Date().toISOString()
    }));
    return;
  }

  // --------------------------------------------------------------------------
  // Endpoint: POST /api/evaluate
  // --------------------------------------------------------------------------
  if (req.method === 'POST' && decodedPath === '/api/evaluate') {
    let body;
    try {
      body = await parseJsonBody(req, MAX_BODY_BYTES);
    } catch (err) {
      const statusCode = err.statusCode || 400;
      res.writeHead(statusCode, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({ success: false, error: err.message }));
      return;
    }

    const sourceCode = body.sourceCode || body.code;
    if (!sourceCode || typeof sourceCode !== 'string' || !sourceCode.trim()) {
      res.writeHead(400, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({ success: false, error: 'Source code is required' }));
      return;
    }

    let testCases = Array.isArray(body.testCases) && body.testCases.length > 0 ? body.testCases : null;
    if (!testCases && body.problemId) {
      const prob = problemMap.get(body.problemId);
      if (prob && Array.isArray(prob.testCases) && prob.testCases.length > 0) {
        testCases = prob.testCases;
      }
    }

    if (!testCases || testCases.length === 0) {
      res.writeHead(400, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({ success: false, error: 'Test cases or valid problemId required' }));
      return;
    }

    // Allocate sandbox directory
    const uniqueId = crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}_${crypto.randomBytes(8).toString('hex')}`;
    const sandboxDir = path.join(os.tmpdir(), `quiz_eval_${uniqueId}`);
    fs.mkdirSync(sandboxDir, { recursive: true });

    try {
      const sourcePath = path.join(sandboxDir, 'source.cpp');
      fs.writeFileSync(sourcePath, sourceCode, 'utf-8');

      const binaryExt = process.platform === 'win32' ? '.exe' : '';
      const binaryPath = path.join(sandboxDir, `solution${binaryExt}`);

      // Compile C++ source
      const compileRes = await compileCpp(sandboxDir, sourcePath, binaryPath);

      if (!compileRes.success) {
        res.writeHead(200, {
          'Content-Type': 'application/json; charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        });
        res.end(JSON.stringify({
          success: true,
          compiled: false,
          compilation: {
            success: false,
            output: compileRes.output
          },
          compileError: compileRes.output,
          compileTimeMs: compileRes.compileTimeMs,
          results: [],
          score: 0,
          passedTestCases: 0,
          passedTests: 0,
          totalTestCases: testCases.length,
          totalTests: testCases.length
        }));
        return;
      }

      // Execute sequential test cases
      const results = [];
      for (let idx = 0; idx < testCases.length; idx++) {
        const tc = testCases[idx];
        const tcId = tc.id !== undefined ? tc.id : (tc.testCaseId !== undefined ? tc.testCaseId : (idx + 1));
        const input = typeof tc.input === 'string' ? tc.input : '';
        const expectedOutput = typeof tc.expectedOutput === 'string' ? tc.expectedOutput : '';

        const execRes = await executeTestCase(binaryPath, input, TEST_CASE_TIMEOUT_MS);

        let status = 'Accepted';
        let passed = false;
        let score = 0;
        let errorMsg = null;

        if (execRes.timedOut) {
          status = 'Time Limit Exceeded';
          passed = false;
          score = 0;
          errorMsg = `Time Limit Exceeded (> ${(TEST_CASE_TIMEOUT_MS / 1000).toFixed(1)}s)`;
        } else if (execRes.outputLimitExceeded) {
          status = 'Output Limit Exceeded';
          passed = false;
          score = 0;
          errorMsg = 'Output Limit Exceeded (> 1MB)';
        } else if (execRes.exitCode !== 0) {
          status = 'Runtime Error';
          passed = false;
          score = 0;
          errorMsg = getRuntimeErrorMessage(execRes.exitCode);
        } else {
          if (compareOutputs(execRes.stdout, expectedOutput)) {
            status = 'Accepted';
            passed = true;
            score = 10;
            errorMsg = null;
          } else {
            status = 'Wrong Answer';
            passed = false;
            score = 0;
            errorMsg = null;
          }
        }

        results.push({
          testCaseId: tcId,
          index: tcId,
          status: status,
          passed: passed,
          score: score,
          timeMs: execRes.timeMs,
          actualOutput: execRes.stdout,
          expectedOutput: expectedOutput,
          error: errorMsg,
          isSample: !!tc.isSample
        });
      }

      const passedTestCases = results.filter(r => r.passed).length;
      const totalScore = passedTestCases * 10;
      const totalExecutionTime = results.reduce((acc, r) => acc + (r.timeMs || 0), 0);

      res.writeHead(200, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({
        success: true,
        compiled: true,
        compilation: {
          success: true,
          output: compileRes.output || ''
        },
        compileError: null,
        compileTimeMs: compileRes.compileTimeMs,
        results: results,
        score: totalScore,
        passedTestCases: passedTestCases,
        passedTests: passedTestCases,
        totalTestCases: testCases.length,
        totalTests: testCases.length,
        totalTimeMs: totalExecutionTime
      }));
    } catch (evalErr) {
      console.error('[EVALUATION ERROR]', evalErr);
      res.writeHead(500, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({
        success: false,
        error: 'Evaluation engine error: ' + evalErr.message
      }));
    } finally {
      await safeRemoveDirectory(sandboxDir);
    }
    return;
  }

  // --------------------------------------------------------------------------
  // Static File Serving
  // --------------------------------------------------------------------------
  if (req.method === 'GET' || req.method === 'HEAD') {
    serveStaticFile(req, res, decodedPath);
    return;
  }

  // Fallback 405 Method Not Allowed
  res.writeHead(405, {
    'Content-Type': 'application/json; charset=utf-8',
    'Access-Control-Allow-Origin': '*'
  });
  res.end(JSON.stringify({ error: `Method ${req.method} not allowed` }));
});

// ============================================================================
// Server Lifecycle & Error Handling
// ============================================================================
server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`\n[FATAL] Port ${PORT} is already in use by another process.`);
    console.error(`[DIAGNOSTIC] To resolve this:`);
    console.error(`  1. Choose a different port: set PORT=3001 && node server.js`);
    console.error(`  2. Or terminate the process currently occupying port ${PORT}:\n`);
    process.exit(1);
  } else {
    console.error('[FATAL] Unexpected server error:', err);
    process.exit(1);
  }
});

process.on('SIGINT', () => {
  server.close(() => {
    process.exit(0);
  });
});

process.on('SIGTERM', () => {
  server.close(() => {
    process.exit(0);
  });
});

server.listen(PORT, () => {
  console.log(`[INFO] C++ Execution & Static Server running at http://localhost:${PORT}`);
  console.log(`[INFO] Compiler detected: ${cachedCompiler.compilerBanner || 'None'}`);
  console.log(`[INFO] Loaded ${problemBank.length} coding problems from problem bank`);
});
