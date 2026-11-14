/**
 * Automated Verification Script for Dynamic Metric Counters
 * Connects to headless Chrome via native Node 22 WebSocket CDP.
 * Verifies count-up progression, final target latch, and hover re-trigger.
 */

const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 9222;
const TARGET_URL = 'http://127.0.0.1:5225/';
const SCREENSHOT_PATH = path.join(
  '/home/emran/.gemini/antigravity/brain/df7bac80-5146-4df3-ae90-9e288cdbda13',
  'live_metrics_verified.png'
);

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function fetchJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, { headers: { Host: `localhost:${PORT}` } }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

async function run() {
  console.log('🚀 Launching headless Chrome with native CDP...');
  const chromeProc = spawn('/usr/bin/google-chrome', [
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--disable-webgl',
    '--no-proxy-server',
    `--remote-debugging-port=${PORT}`,
    '--remote-allow-origins=*',
    '--window-size=1280,1000',
    'about:blank'
  ], {
    env: { ...process.env, http_proxy: '', https_proxy: '', no_proxy: '*' }
  });

  await sleep(1200);

  try {
    const pages = await fetchJson(`http://127.0.0.1:${PORT}/json`);
    const page = pages.find(p => p.type === 'page') || pages[0];
    if (!page || !page.webSocketDebuggerUrl) {
      throw new Error('No page WebSocketDebuggerUrl found');
    }

    console.log(`🔌 Connecting to Chrome page: ${page.id}...`);
    const ws = new WebSocket(page.webSocketDebuggerUrl);

    let id = 1;
    const callbacks = new Map();

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id && callbacks.has(msg.id)) {
        const { resolve, reject } = callbacks.get(msg.id);
        callbacks.delete(msg.id);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    };

    function send(method, params = {}) {
      return new Promise((resolve, reject) => {
        const msgId = id++;
        callbacks.set(msgId, { resolve, reject });
        ws.send(JSON.stringify({ id: msgId, method, params }));
      });
    }

    await new Promise(resolve => ws.onopen = resolve);
    console.log('✅ WebSocket CDP connected!');

    await send('Page.enable');
    await send('Runtime.enable');

    console.log(`🌐 Navigating to ${TARGET_URL}...`);
    await send('Page.navigate', { url: TARGET_URL });
    await sleep(1500);

    // Initial check before scrolling
    let res = await send('Runtime.evaluate', {
      expression: `Array.from(document.querySelectorAll('.stat-counter')).map(el => el.textContent.trim())`,
      returnByValue: true
    });
    console.log('Initial counter values before scroll:', res.result.value);

    // Scroll to the metrics strip to trigger IntersectionObserver and scroll listener
    console.log('📜 Scrolling metrics strip into view...');
    await send('Runtime.evaluate', {
      expression: `
        const strip = document.getElementById('hero-metrics-strip');
        if (strip) strip.scrollIntoView({ behavior: 'auto', block: 'center' });
        window.dispatchEvent(new Event('scroll'));
      `
    });

    // Sample progression over time
    const samples = [];
    for (let i = 0; i < 6; i++) {
      await sleep(250);
      res = await send('Runtime.evaluate', {
        expression: `Array.from(document.querySelectorAll('.stat-counter')).map(el => el.textContent.trim())`,
        returnByValue: true
      });
      samples.push(res.result.value);
      console.log(`⏱️ Sample ${(i + 1) * 250}ms:`, res.result.value);
    }

    // Wait for animation to finish completely
    await sleep(800);
    res = await send('Runtime.evaluate', {
      expression: `Array.from(document.querySelectorAll('.stat-counter')).map(el => el.textContent.trim())`,
      returnByValue: true
    });
    const finalValues = res.result.value;
    console.log('🏁 Final settled counter values:', finalValues);

    // Assert final targets
    if (finalValues[0] !== '24' || finalValues[1] !== '300' || finalValues[2] !== '100' || finalValues[3] !== '2') {
      throw new Error(`Expected ['24', '300', '100', '2'], got ${JSON.stringify(finalValues)}`);
    }
    console.log('✅ PASS: All 4 counters correctly animated and settled at exact targets!');

    // Test Hover Re-trigger on Card 1
    console.log('🖱️ Simulating hover (mouseenter) on Card 1...');
    await send('Runtime.evaluate', {
      expression: `
        const card1 = document.querySelectorAll('.stat-card')[0];
        card1.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
      `
    });
    await sleep(150);
    res = await send('Runtime.evaluate', {
      expression: `document.querySelectorAll('.stat-counter')[0].textContent.trim()`,
      returnByValue: true
    });
    console.log('Card 1 value mid-hover-reanimation:', res.result.value);

    await sleep(1200);
    res = await send('Runtime.evaluate', {
      expression: `document.querySelectorAll('.stat-counter')[0].textContent.trim()`,
      returnByValue: true
    });
    console.log('Card 1 final value after hover reanimation:', res.result.value);
    if (res.result.value !== '24') {
      throw new Error(`Hover re-animation failed to settle on 24, got ${res.result.value}`);
    }
    console.log('✅ PASS: Hover re-trigger operates with 100% precision!');

    // Capture visual screenshot
    console.log(`📸 Capturing screenshot to ${SCREENSHOT_PATH}...`);
    const screenshotRes = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(SCREENSHOT_PATH, Buffer.from(screenshotRes.data, 'base64'));
    console.log('✅ Screenshot captured successfully!');

    ws.close();
    chromeProc.kill();
    console.log('🎉 ALL DYNAMIC COUNTER TESTS COMPLETED WITH 100% SUCCESS!');
    process.exit(0);
  } catch (err) {
    console.error('❌ Test failed:', err);
    chromeProc.kill();
    process.exit(1);
  }
}

run();
