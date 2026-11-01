/**
 * Emran Hosen — Cinematic Portfolio Application Server
 * High-performance, zero-dependency Node.js HTTP server delivering:
 * - Dynamic REST APIs (/api/health, /api/projects, /api/agent/status, /api/contact)
 * - Static asset streaming for WebGL Abyss and Media Gallery
 * - Persistent contact inquiry logging
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = process.env.PORT || 5225;
const PUBLIC_DIR = __dirname;
const DATA_DIR = path.join(__dirname, 'data');
const INQUIRIES_FILE = path.join(DATA_DIR, 'inquiries.jsonl');
const PROJECTS_FILE = path.join(DATA_DIR, 'projects.json');
const VIDEOS_FILE = path.join(DATA_DIR, 'videos.json');

// Ensure data directory exists
if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}

// MIME Types Map
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.mp4': 'video/mp4',
  '.mp3': 'audio/mpeg',
  '.wav': 'audio/wav',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.ttf': 'font/ttf'
};

// Helper: Count loaded skills dynamically from AI-Agents-Hub
function getLoadedSkillsCount() {
  const hubSkillsDir = '/home/emran/Documents/AI-Agents-Hub/skills';
  try {
    if (fs.existsSync(hubSkillsDir)) {
      return fs.readdirSync(hubSkillsDir).length;
    }
  } catch (e) {
    // Fallback if not readable
  }
  return 248;
}

// Helper: Parse video source URL and auto-extract embed + thumbnail
function parseVideoSource(platform, inputUrl) {
  const urlStr = (inputUrl || '').trim();
  let detectedPlatform = platform;
  let embedSrc = '';
  let thumbnail = '';
  let isPortrait = false;

  // Auto-detect platform if not provided
  if (!detectedPlatform || detectedPlatform === 'auto') {
    if (urlStr.includes('youtube.com') || urlStr.includes('youtu.be')) {
      detectedPlatform = 'youtube';
    } else if (urlStr.includes('facebook.com') || urlStr.includes('fb.watch')) {
      detectedPlatform = 'facebook';
    } else if (urlStr.includes('linkedin.com') || urlStr.includes('lnkd.in')) {
      detectedPlatform = 'linkedin';
    } else {
      detectedPlatform = 'youtube';
    }
  }

  if (detectedPlatform === 'youtube') {
    const ytMatch = urlStr.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|shorts\/))([\w-]{11})/);
    if (ytMatch && ytMatch[1]) {
      const videoId = ytMatch[1];
      embedSrc = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
      thumbnail = `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`;
      isPortrait = urlStr.includes('/shorts/');
    } else {
      embedSrc = urlStr;
      thumbnail = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80';
    }
  } else if (detectedPlatform === 'facebook') {
    isPortrait = true;
    embedSrc = `https://www.facebook.com/plugins/video.php?height=600&href=${encodeURIComponent(urlStr)}&show_text=false&width=340&t=0`;
    thumbnail = 'assets/thumbnails/ep05_prompt_vs_context.png';
  } else if (detectedPlatform === 'linkedin') {
    isPortrait = false;
    if (urlStr.includes('/embed/')) {
      embedSrc = urlStr;
    } else {
      const match = urlStr.match(/urn:li:(?:ugcPost|share|activity):(\d+)/);
      if (match && match[1]) {
        embedSrc = `https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:${match[1]}`;
      } else {
        embedSrc = urlStr;
      }
    }
    thumbnail = 'assets/thumbnails/li01_autonomous_systems.jpg';
  }

  return {
    platform: detectedPlatform,
    embedSrc,
    thumbnail,
    isPortrait
  };
}

// Start Server
const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  let pathname = parsedUrl.pathname;

  // Set standard CORS headers for APIs
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight OPTIONS
  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // ==================== REST API ROUTING ====================

  // 1. GET /api/health
  if (pathname === '/api/health' && req.method === 'GET') {
    const mem = process.memoryUsage();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'healthy',
      service: 'Emran Hosen Portfolio Server',
      owner: 'Emran Hosen',
      port: PORT,
      uptime_seconds: Math.floor(process.uptime()),
      memory_mb: {
        rss: (mem.rss / 1024 / 1024).toFixed(1),
        heapUsed: (mem.heapUsed / 1024 / 1024).toFixed(1)
      },
      environment: process.env.NODE_ENV || 'production',
      timestamp: new Date().toISOString()
    }));
    return;
  }

  // 2. GET /api/projects (Flagship Works)
  if (pathname === '/api/projects' && req.method === 'GET') {
    try {
      if (fs.existsSync(PROJECTS_FILE)) {
        const raw = fs.readFileSync(PROJECTS_FILE, 'utf-8');
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(raw);
        return;
      }
    } catch (err) {
      console.error('Error reading projects.json:', err);
    }
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Failed to load projects' }));
    return;
  }

  // 3. GET /api/agent/status (Live AI Agents Hub Telemetry)
  if (pathname === '/api/agent/status' && req.method === 'GET') {
    const skillsCount = getLoadedSkillsCount();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'online',
      gateway: 'Multi-Cloud Persistent Gateway (Render/Railway)',
      hermes_agent: {
        status: 'active',
        model: 'nvidia/nemotron-3.5-super-vl-120b-a12b',
        skills_loaded: skillsCount,
        memory_store: 'SQLite WAL'
      },
      openclaw: {
        status: 'ready',
        version: '2026.5.7'
      },
      strix_security: {
        status: 'ready',
        version: '1.7.0'
      },
      timestamp: new Date().toISOString()
    }));
    return;
  }

  // 4. POST /api/contact (Handle Inquiries)
  if (pathname === '/api/contact' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk;
      // 1MB limit for security
      if (body.length > 1e6) {
        req.destroy();
      }
    });

    req.on('end', () => {
      try {
        const data = JSON.parse(body || '{}');
        const name = (data.name || '').trim();
        const email = (data.email || '').trim();
        const service = (data.service || 'Autonomous AI & Workflow Automation').trim();
        const message = (data.message || '').trim();

        // Validation
        if (!name || name.length < 2 || name.length > 100) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'Please enter a valid name (2–100 characters).' }));
          return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!email || !emailRegex.test(email)) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'Please provide a valid email address.' }));
          return;
        }

        if (!message || message.length < 5 || message.length > 2000) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'Message must be between 5 and 2,000 characters.' }));
          return;
        }

        // Record inquiry
        const inquiryRecord = {
          id: Date.now().toString(36) + Math.random().toString(36).substr(2, 5),
          name,
          email,
          service,
          message,
          ip: req.socket.remoteAddress || 'unknown',
          receivedAt: new Date().toISOString()
        };

        fs.appendFileSync(INQUIRIES_FILE, JSON.stringify(inquiryRecord) + '\n', 'utf-8');

        console.log(`📩 [INQUIRY RECEIVED] From: ${name} <${email}> | Service: ${service}`);

        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          ok: true,
          message: 'Thank you! Your message has been received. Emran Hosen will connect with you within 12 hours.',
          inquiryId: inquiryRecord.id
        }));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: false, error: 'Invalid JSON payload.' }));
      }
    });
    return;
  }

  // 5. GET /api/videos (Fetch all gallery videos)
  if (pathname === '/api/videos' && req.method === 'GET') {
    try {
      if (fs.existsSync(VIDEOS_FILE)) {
        const raw = fs.readFileSync(VIDEOS_FILE, 'utf-8');
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(raw);
        return;
      } else {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end('[]');
        return;
      }
    } catch (err) {
      console.error('Error reading videos.json:', err);
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'Failed to read videos' }));
      return;
    }
  }

  // 6. POST /api/videos (Ingest new video from Facebook, YouTube, LinkedIn)
  if (pathname === '/api/videos' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk;
      if (body.length > 1e6) {
        req.destroy();
      }
    });

    req.on('end', () => {
      try {
        const data = JSON.parse(body || '{}');
        const title = (data.title || '').trim();
        const rawUrl = (data.url || '').trim();
        const platform = (data.platform || 'auto').trim().toLowerCase();
        const category = (data.category || 'Technical Talk').trim();
        const episode = (data.episode || '').trim();
        const summary = (data.summary || '').trim();
        const customThumbnail = (data.thumbnail || '').trim();

        // Validation
        if (!title || title.length < 2 || title.length > 200) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'Title must be between 2 and 200 characters.' }));
          return;
        }

        if (!rawUrl || rawUrl.length < 5 || (!rawUrl.startsWith('http://') && !rawUrl.startsWith('https://'))) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'A valid HTTP or HTTPS video URL is required.' }));
          return;
        }

        // Parse video details
        const parsed = parseVideoSource(platform, rawUrl);
        const videoId = 'vid-' + Date.now().toString(36) + '-' + Math.random().toString(36).substr(2, 4);

        const newVideo = {
          id: videoId,
          platform: parsed.platform,
          title: title,
          url: rawUrl,
          embedSrc: parsed.embedSrc,
          thumbnail: customThumbnail || parsed.thumbnail,
          category: category || (parsed.platform === 'youtube' ? 'Masterclass' : (parsed.platform === 'facebook' ? 'Reel Series' : 'Executive Insight')),
          episode: episode || (parsed.platform === 'facebook' ? 'Reel' : (parsed.platform === 'youtube' ? 'YouTube' : 'Insight')),
          summary: summary || 'Video walkthrough and technical breakdown by Emran Hosen.',
          isPortrait: parsed.isPortrait,
          isCustom: true,
          createdAt: new Date().toISOString()
        };

        // Read and update VIDEOS_FILE
        let videos = [];
        if (fs.existsSync(VIDEOS_FILE)) {
          try {
            videos = JSON.parse(fs.readFileSync(VIDEOS_FILE, 'utf-8'));
          } catch (e) {
            videos = [];
          }
        }

        videos.push(newVideo);
        fs.writeFileSync(VIDEOS_FILE, JSON.stringify(videos, null, 2), 'utf-8');

        console.log(`🎬 [NEW VIDEO INGESTED] [${parsed.platform.toUpperCase()}] ${title}`);

        res.writeHead(201, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          ok: true,
          message: 'Video successfully added to gallery!',
          video: newVideo
        }));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: false, error: 'Invalid JSON payload.' }));
      }
    });
    return;
  }

  // 7. DELETE /api/videos/:id or POST /api/videos/delete (Remove custom video)
  if ((pathname.startsWith('/api/videos/') && req.method === 'DELETE') || (pathname === '/api/videos/delete' && req.method === 'POST')) {
    const handleRemoval = (targetId) => {
      if (!targetId) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: false, error: 'Video ID required.' }));
        return;
      }
      try {
        if (!fs.existsSync(VIDEOS_FILE)) {
          res.writeHead(404, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'Videos database not found.' }));
          return;
        }
        let videos = JSON.parse(fs.readFileSync(VIDEOS_FILE, 'utf-8'));
        const originalCount = videos.length;
        videos = videos.filter(v => v.id !== targetId);
        if (videos.length === originalCount) {
          res.writeHead(404, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'Video not found.' }));
          return;
        }
        fs.writeFileSync(VIDEOS_FILE, JSON.stringify(videos, null, 2), 'utf-8');
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: true, deletedId: targetId }));
      } catch (err) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: false, error: 'Failed to delete video.' }));
      }
    };

    if (req.method === 'DELETE') {
      const targetId = pathname.replace('/api/videos/', '').trim();
      handleRemoval(targetId);
      return;
    } else {
      let body = '';
      req.on('data', chunk => body += chunk);
      req.on('end', () => {
        try {
          const data = JSON.parse(body || '{}');
          handleRemoval(data.id);
        } catch (e) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok: false, error: 'Invalid payload.' }));
        }
      });
      return;
    }
  }

  // ==================== STATIC FILE SERVING & CLEAN URL ROUTING ====================

  // Clean URL Canonical Redirects (301 Permanent)
  if (pathname === '/gallery.html') {
    res.writeHead(301, { 'Location': '/gallery' + (parsedUrl.search || '') });
    res.end();
    return;
  }
  if (pathname === '/contact.html') {
    res.writeHead(301, { 'Location': '/contact' + (parsedUrl.search || '') });
    res.end();
    return;
  }
  if (pathname === '/index.html') {
    res.writeHead(301, { 'Location': '/' + (parsedUrl.search || '') });
    res.end();
    return;
  }

  // Normalize route to file path
  if (pathname === '/' || pathname === '') {
    pathname = '/index.html';
  } else if (pathname === '/gallery' || pathname === '/gallery/') {
    pathname = '/gallery.html';
  } else if (pathname === '/contact' || pathname === '/contact/') {
    pathname = '/contact.html';
  }

  // Sanitize path against directory traversal
  const safeSuffix = path.normalize(pathname).replace(/^(\.\.[\/\\])+/, '');
  const filePath = path.join(PUBLIC_DIR, safeSuffix);

  // Check if file exists within PUBLIC_DIR
  if (!filePath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end('<h1>404 Not Found</h1><p>The requested file does not exist on Emran Hosen Portfolio Server.</p>');
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, {
      'Content-Type': contentType,
      'Content-Length': stats.size,
      'Cache-Control': ext === '.html' ? 'no-cache' : 'public, max-age=86400'
    });

    const readStream = fs.createReadStream(filePath);
    readStream.pipe(res);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 Emran Hosen Portfolio Application Server listening on http://0.0.0.0:${PORT}`);
  console.log(`📡 Endpoints:`);
  console.log(`   - Home:     http://localhost:${PORT}/index.html`);
  console.log(`   - Gallery:  http://localhost:${PORT}/gallery.html`);
  console.log(`   - Contact:  http://localhost:${PORT}/contact.html`);
  console.log(`   - Health:   http://localhost:${PORT}/api/health`);
  console.log(`   - Projects: http://localhost:${PORT}/api/projects`);
  console.log(`   - Agents:   http://localhost:${PORT}/api/agent/status`);
  console.log(`   - Contact:  http://localhost:${PORT}/api/contact (POST)`);
});
