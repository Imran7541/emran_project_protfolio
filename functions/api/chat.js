/**
 * Cloudflare Pages Function: /api/chat
 * Edge AI ambassador powered by Google Gemini 2.5 Flash with embedded semantic knowledge fallback.
 */

const KNOWLEDGE_FAQ = [
  {
    keywords: ["who is", "who are you", "about emran", "bio", "intro", "পরিচয়", "কে এমরান", "কে আপনি"],
    answer: "Emran Hosen is a Software Developer and AI Agent Architect based in Dhaka, Bangladesh, working with global clients. He specializes in full-stack cloud systems, autonomous agent workflows, and award-grade WebGL 3D web applications."
  },
  {
    keywords: ["next label", "3d", "particle", "webgl", "canvas", "three.js", "threejs", "৩ডি"],
    answer: "Emran is an expert in real-time WebGL and Three.js 3D development! His flagship project 'Next Label' renders 409,600 simultaneous GPU particles with custom bloom post-processing shaders and sub-50ms edge streaming. You can experience it live right now at https://next-label-portfolio.pages.dev."
  },
  {
    keywords: ["ai agent", "agents", "orchestrator", "ai-agents-hub", "autonomous", "hermes", "strix", "এআই"],
    answer: "Emran designs high-performance autonomous multi-agent swarms. His 'AI-Agents-Hub' runs 248+ active skills with cognitive DAG reasoning, zero-trust secrets management, and automated fallback channels. Check it out at https://github.com/Imran7541/AI-Agents-Hub."
  },
  {
    keywords: ["video", "reel", "youtube", "automation", "ffmpeg", "as-sunnah-reel", "ভিডিও"],
    answer: "Emran built an autonomous video production and rendering engine combining Playwright frame capture, neural Edge-TTS voiceovers, and 2-pass FFmpeg hardware encoding. Explore it at https://github.com/Imran7541/as-sunnah-reel or visit the Gallery page."
  },
  {
    keywords: ["stack", "technologies", "tech", "skills", "language", "tools", "টেকনোলজি"],
    answer: "Emran's primary stack includes Node.js 22, TypeScript, Python 3.14, Three.js/WebGL, Next.js 15, PostgreSQL, Cloudflare Pages/Workers, Docker, and cutting-edge AI Agent architectures (Google Antigravity SDK, NVIDIA NIM, Gemini Flash)."
  },
  {
    keywords: ["hire", "contact", "pricing", "rate", "freelance", "contract", "email", "যোগাযোগ", "হায়ার"],
    answer: "Emran is available for select high-impact enterprise contracts, autonomous agent systems, and custom 3D WebGL experiences. You can send a direct inquiry via the Contact page or email him at emranhosen7541@gmail.com."
  }
];

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '86400'
    }
  });
}

export async function onRequestPost(context) {
  const corsHeaders = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  };

  try {
    const data = await context.request.json().catch(() => ({}));
    const message = (data.message || '').trim();
    const history = Array.isArray(data.history) ? data.history : [];

    if (!message || message.length < 1 || message.length > 500) {
      return new Response(JSON.stringify({ ok: false, error: 'Message must be between 1 and 500 characters.' }), {
        status: 400,
        headers: corsHeaders
      });
    }

    const geminiKey = context.env?.GEMINI_API_KEY;
    const geminiModel = context.env?.GEMINI_MODEL || 'gemini-2.5-flash';

    if (geminiKey && !geminiKey.startsWith('[[')) {
      try {
        const systemPrompt = `You are "Emran AI", the autonomous portfolio ambassador and technical representative for Emran Hosen.
Emran Hosen is a Senior Full-Stack AI Engineer and Autonomous Agent Architect based in Dhaka, Bangladesh, working with global clients.
His core skills: Autonomous AI Agents (NVIDIA NIM, Google Antigravity SDK, Hermes, Strix, OpenClaw), WebGL 3D (Three.js, GLSL Shaders, 400K Particle Worlds), Full-Stack (Node.js 22, Next.js 15, PostgreSQL, Docker, Cloudflare Pages).
Flagship works:
1. Next Label: 400K Particle 3D WebGL World (https://next-label-portfolio.pages.dev)
2. AI-Agents-Hub: Multi-cloud persistent orchestrator running 248+ skills (https://github.com/Imran7541/AI-Agents-Hub)
3. Autonomous Video Production Engine: Playwright + Neural Edge-TTS + FFmpeg 2-Pass pipeline (https://github.com/Imran7541/as-sunnah-reel)
4. Enterprise Student-to-Career Platform (Private System)
5. Autonomous Multi-Agent FinTech Settlement Core (bKash/Nagad/Stripe)
6. Real-Time Spatial 3D Showroom (Three.js PBR configurator)

Answer questions concisely, professionally, and warmly. If asked in Bengali, respond in fluent Bengali. If in English, respond in English. Keep answers under 120 words. Offer to connect via the Contact page.`;

        const contents = [];
        for (const item of history.slice(-4)) {
          if (item && item.role && item.content) {
            contents.push({
              role: item.role === 'assistant' ? 'model' : 'user',
              parts: [{ text: item.content }]
            });
          }
        }
        contents.push({
          role: 'user',
          parts: [{ text: message }]
        });

        const geminiRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${geminiModel}:generateContent?key=${geminiKey}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            systemInstruction: { parts: [{ text: systemPrompt }] },
            contents: contents,
            generationConfig: {
              temperature: 0.7,
              maxOutputTokens: 250
            }
          })
        });

        if (geminiRes.ok) {
          const resData = await geminiRes.json();
          const text = resData?.candidates?.[0]?.content?.parts?.[0]?.text;
          if (text) {
            return new Response(JSON.stringify({
              ok: true,
              reply: text.trim(),
              model: geminiModel,
              engine: 'gemini'
            }), {
              status: 200,
              headers: corsHeaders
            });
          }
        }
      } catch (geminiErr) {
        console.warn('Edge Gemini API fallback:', geminiErr);
      }
    }

    // Local semantic FAQ fallback
    const lower = message.toLowerCase();
    for (const item of KNOWLEDGE_FAQ) {
      if (item.keywords.some(kw => lower.includes(kw))) {
        return new Response(JSON.stringify({
          ok: true,
          reply: item.answer,
          model: 'local-knowledge-core',
          engine: 'semantic-matcher'
        }), {
          status: 200,
          headers: corsHeaders
        });
      }
    }

    return new Response(JSON.stringify({
      ok: true,
      reply: "Hello! I am Emran's AI Portfolio Ambassador. Emran Hosen is a Senior Full-Stack AI Engineer specializing in Autonomous Multi-Agent Systems, WebGL 3D Interactive Worlds (like Next Label), and Enterprise Cloud Platforms. Feel free to explore his Flagship Projects, or drop a message via the Contact page to collaborate directly!",
      model: 'local-knowledge-core',
      engine: 'default'
    }), {
      status: 200,
      headers: corsHeaders
    });

  } catch (err) {
    return new Response(JSON.stringify({ ok: false, error: 'Internal edge server error.' }), {
      status: 500,
      headers: corsHeaders
    });
  }
}
