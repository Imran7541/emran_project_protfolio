/**
 * Emran AI - Floating Portfolio Ambassador & Interactive Assistant Widget
 * Autonomous edge-capable chat assistant for Emran Hosen Portfolio.
 * Provides instant responses on Next Label 3D, AI-Agents-Hub, tech stack, and hiring.
 */

(function () {
  'use strict';

  // Prevent multiple initializations
  if (window.__EMRAN_AI_WIDGET_INIT__) return;
  window.__EMRAN_AI_WIDGET_INIT__ = true;

  // In-memory conversation state
  const state = {
    isOpen: false,
    history: [],
    isTyping: false
  };

  // Client-side fallback knowledge matrix (if API unavailable)
  const CLIENT_FALLBACK_FAQ = [
    {
      keywords: ["who is", "who are you", "about emran", "bio", "intro", "পরিচয়", "কে এমরান", "কে আপনি"],
      answer: "Emran Hosen is a Software Developer and AI Agent Architect based in Dhaka, Bangladesh, working with global clients. He specializes in full-stack cloud systems, autonomous agent workflows, and award-grade WebGL 3D web applications."
    },
    {
      keywords: ["next label", "3d", "particle", "webgl", "canvas", "three.js", "threejs", "৩ডি"],
      answer: "Emran is an expert in real-time WebGL and Three.js 3D development! His flagship project 'Next Label' renders 409,600 simultaneous GPU particles with custom bloom post-processing shaders and sub-50ms edge streaming. You can experience it live right now at <a href='https://next-label-portfolio.pages.dev' target='_blank' class='text-[#FF715B] underline hover:text-[#ff8c77]'>next-label-portfolio.pages.dev</a>."
    },
    {
      keywords: ["ai agent", "agents", "orchestrator", "ai-agents-hub", "autonomous", "hermes", "strix", "এআই"],
      answer: "Emran designs high-performance autonomous multi-agent swarms. His 'AI-Agents-Hub' runs 248+ active skills with cognitive DAG reasoning, zero-trust secrets management, and automated fallback channels. Check it out at <a href='https://github.com/Imran7541/AI-Agents-Hub' target='_blank' class='text-[#FF715B] underline hover:text-[#ff8c77]'>github.com/Imran7541/AI-Agents-Hub</a>."
    },
    {
      keywords: ["video", "reel", "youtube", "automation", "ffmpeg", "as-sunnah-reel", "ভিডিও"],
      answer: "Emran built an autonomous video production and rendering engine combining Playwright frame capture, neural Edge-TTS voiceovers, and 2-pass FFmpeg hardware encoding. Explore it at <a href='https://github.com/Imran7541/as-sunnah-reel' target='_blank' class='text-[#FF715B] underline hover:text-[#ff8c77]'>github.com/Imran7541/as-sunnah-reel</a> or visit the Gallery page."
    },
    {
      keywords: ["stack", "technologies", "tech", "skills", "language", "tools", "টেকনোলজি"],
      answer: "Emran's primary stack includes Node.js 22, TypeScript, Python 3.14, Three.js/WebGL, Next.js 15, PostgreSQL, Cloudflare Pages/Workers, Docker, and cutting-edge AI Agent architectures (Google Antigravity SDK, NVIDIA NIM, Gemini Flash)."
    },
    {
      keywords: ["hire", "contact", "pricing", "rate", "freelance", "contract", "email", "যোগাযোগ", "হায়ার"],
      answer: "Emran is available for select high-impact enterprise contracts, autonomous agent systems, and custom 3D WebGL experiences. You can connect via WhatsApp at <a href='https://wa.me/8801706754148' target='_blank' class='text-[#FF715B] underline hover:text-[#ff8c77]'>+880 1706-754148</a>, join his <a href='https://discord.gg/VxDzexfEN' target='_blank' class='text-[#FF715B] underline hover:text-[#ff8c77]'>Discord Server</a>, or email <a href='mailto:imrandt2001@gmail.com' class='text-[#FF715B] underline hover:text-[#ff8c77]'>imrandt2001@gmail.com</a>."
    },
    {
      keywords: ["whatsapp", "phone", "number", "discord", "কল", "নাম্বার", "হোয়াটসঅ্যাপ", "ডিসকর্ড"],
      answer: "Direct channels for Emran Hosen:<br/>• <strong>WhatsApp:</strong> <a href='https://wa.me/8801706754148' target='_blank' class='text-[#FF715B] underline hover:text-[#ff8c77]'>+880 1706-754148</a><br/>• <strong>Discord Community:</strong> <a href='https://discord.gg/VxDzexfEN' target='_blank' class='text-[#FF715B] underline hover:text-[#ff8c77]'>discord.gg/VxDzexfEN</a><br/>• <strong>Email:</strong> <a href='mailto:imrandt2001@gmail.com' class='text-[#FF715B] underline hover:text-[#ff8c77]'>imrandt2001@gmail.com</a>"
    }
  ];

  // Helper: Format message markdown into safe HTML
  function formatMarkdown(text) {
    if (!text) return '';
    let escaped = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
    
    // Bold
    escaped = escaped.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // Inline code
    escaped = escaped.replace(/`([^`]+)`/g, '<code class="px-1.5 py-0.5 rounded bg-white/10 text-[#FF8C68] font-mono text-xs">$1</code>');
    // URLs
    escaped = escaped.replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener noreferrer" class="text-[#FF715B] underline hover:text-[#ff927e]">$1</a>');
    // Line breaks
    escaped = escaped.replace(/\n/g, '<br/>');
    return escaped;
  }

  // Inject Stylesheet
  const styleEl = document.createElement('style');
  styleEl.textContent = `
    #emran-ai-widget {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    .emran-ai-btn {
      width: 58px;
      height: 58px;
      border-radius: 50%;
      background: linear-gradient(135deg, #FF715B 0%, #FF8C68 100%);
      box-shadow: 0 8px 25px -4px rgba(255, 113, 91, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.2);
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }
    .emran-ai-btn:hover {
      transform: scale(1.08);
      box-shadow: 0 12px 30px -4px rgba(255, 113, 91, 0.7), 0 0 0 2px rgba(255, 255, 255, 0.3);
    }
    .emran-ai-btn:active {
      transform: scale(0.96);
    }
    .emran-ai-pulse {
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      background: rgba(255, 113, 91, 0.35);
      animation: emranAiPulse 2.4s infinite cubic-bezier(0.24, 0, 0.38, 1);
      z-index: -1;
      pointer-events: none;
    }
    @keyframes emranAiPulse {
      0% { transform: scale(0.95); opacity: 0.8; }
      50% { transform: scale(1.25); opacity: 0; }
      100% { transform: scale(0.95); opacity: 0; }
    }
    .emran-ai-box {
      position: absolute;
      bottom: 74px;
      right: 0;
      width: 380px;
      max-width: calc(100vw - 32px);
      height: 540px;
      max-height: calc(100vh - 120px);
      background: rgba(13, 16, 23, 0.94);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 20px;
      box-shadow: 0 24px 60px -12px rgba(0, 0, 0, 0.75), 0 0 40px -10px rgba(255, 113, 91, 0.2);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      opacity: 0;
      transform: translateY(16px) scale(0.96);
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      transform-origin: bottom right;
    }
    .emran-ai-box.active {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: auto;
    }
    @media (max-width: 640px) {
      #emran-ai-widget {
        bottom: 16px;
        right: 16px;
      }
      .emran-ai-box {
        position: fixed;
        inset: 12px;
        bottom: 84px;
        width: auto;
        max-width: none;
        height: auto;
        max-height: none;
        border-radius: 20px;
      }
    }
    .emran-ai-header {
      padding: 14px 18px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(255, 255, 255, 0.02);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .emran-ai-messages {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      scroll-behavior: smooth;
    }
    .emran-ai-messages::-webkit-scrollbar {
      width: 5px;
    }
    .emran-ai-messages::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 4px;
    }
    .emran-ai-msg {
      max-width: 86%;
      padding: 10px 14px;
      border-radius: 16px;
      font-size: 13.5px;
      line-height: 1.5;
      word-break: break-word;
    }
    .emran-ai-msg-assistant {
      align-self: flex-start;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #E2E8F0;
      border-bottom-left-radius: 4px;
    }
    .emran-ai-msg-user {
      align-self: flex-end;
      background: linear-gradient(135deg, #FF715B 0%, #FF8C68 100%);
      color: #ffffff;
      border-bottom-right-radius: 4px;
      box-shadow: 0 4px 14px rgba(255, 113, 91, 0.25);
    }
    .emran-ai-chip {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #94A3B8;
      border-radius: 9999px;
      padding: 5px 11px;
      font-size: 12px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }
    .emran-ai-chip:hover {
      background: rgba(255, 113, 91, 0.15);
      border-color: rgba(255, 113, 91, 0.4);
      color: #FF715B;
    }
    .emran-ai-typing {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 8px 14px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      border-bottom-left-radius: 4px;
      align-self: flex-start;
    }
    .emran-ai-typing span {
      width: 6px;
      height: 6px;
      background: #FF715B;
      border-radius: 50%;
      animation: emranAiBounce 1.2s infinite ease-in-out;
    }
    .emran-ai-typing span:nth-child(2) { animation-delay: 0.2s; }
    .emran-ai-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes emranAiBounce {
      0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
      40% { transform: translateY(-5px); opacity: 1; }
    }
  `;
  document.head.appendChild(styleEl);

  // Build Container DOM
  const widgetContainer = document.createElement('div');
  widgetContainer.id = 'emran-ai-widget';
  widgetContainer.innerHTML = `
    <!-- Trigger Button -->
    <button class="emran-ai-btn" id="emran-ai-trigger" aria-label="Open Emran AI Assistant" title="Chat with Emran AI">
      <div class="emran-ai-pulse"></div>
      <svg id="emran-ai-icon-chat" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        <circle cx="12" cy="11" r="1" fill="currentColor"></circle>
        <circle cx="8" cy="11" r="1" fill="currentColor"></circle>
        <circle cx="16" cy="11" r="1" fill="currentColor"></circle>
      </svg>
      <svg id="emran-ai-icon-close" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display: none;">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>

    <!-- Chat Box -->
    <div class="emran-ai-box" id="emran-ai-box" role="dialog" aria-modal="true" aria-label="Emran AI Assistant">
      <!-- Header -->
      <div class="emran-ai-header">
        <div style="display: flex; align-items: center; gap: 10px;">
          <div style="position: relative;">
            <div style="width: 34px; height: 34px; border-radius: 50%; background: linear-gradient(135deg, #FF715B, #1A1D24); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 13px; color: #fff; border: 1.5px solid rgba(255, 113, 91, 0.6);">
              EH
            </div>
            <span style="position: absolute; bottom: 0; right: 0; width: 9px; height: 9px; background: #10B981; border: 1.5px solid #0D1017; border-radius: 50%;"></span>
          </div>
          <div>
            <div style="font-weight: 600; font-size: 14px; color: #F8FAFC; display: flex; align-items: center; gap: 6px;">
              Emran AI
              <span style="font-size: 10px; padding: 2px 6px; border-radius: 9999px; background: rgba(16, 185, 129, 0.15); color: #34D399; font-weight: 500;">Edge</span>
            </div>
            <div style="font-size: 11px; color: #94A3B8;">Portfolio Ambassador</div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
          <button id="emran-ai-clear" title="Clear Chat History" style="background: transparent; border: none; color: #64748B; cursor: pointer; padding: 6px; border-radius: 8px; display: flex; align-items: center; justify-content: center; transition: color 0.2s;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="1 4 1 10 7 10"></polyline>
              <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path>
            </svg>
          </button>
          <button id="emran-ai-close-box" title="Close" style="background: transparent; border: none; color: #94A3B8; cursor: pointer; padding: 6px; border-radius: 8px; display: flex; align-items: center; justify-content: center; transition: color 0.2s;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
      </div>

      <!-- Messages Area -->
      <div class="emran-ai-messages" id="emran-ai-messages">
        <!-- Default Welcome Message -->
        <div class="emran-ai-msg emran-ai-msg-assistant">
          👋 Hi there! I'm <strong>Emran AI</strong>, autonomous ambassador for Emran Hosen.<br/><br/>
          Ask me anything about Emran's <strong>WebGL 3D projects</strong> (like Next Label), <strong>Autonomous AI Agents</strong>, technical stack, or project availability!
        </div>
      </div>

      <!-- Prompt Chips -->
      <div style="padding: 6px 14px 10px; display: flex; gap: 6px; overflow-x: auto; scrollbar-width: none;" id="emran-ai-chips">
        <button class="emran-ai-chip" data-prompt="Tell me about Next Label 3D">🚀 Next Label 3D</button>
        <button class="emran-ai-chip" data-prompt="What AI Agents has Emran built?">🤖 AI Agents Hub</button>
        <button class="emran-ai-chip" data-prompt="What is Emran's tech stack?">🛠️ Tech Stack</button>
        <button class="emran-ai-chip" data-prompt="How can I hire or contact Emran?">📩 Contact & Hire</button>
      </div>

      <!-- Input Footer -->
      <form id="emran-ai-form" style="padding: 10px 14px 14px; border-top: 1px solid rgba(255, 255, 255, 0.08); background: rgba(255, 255, 255, 0.02); display: flex; gap: 8px; align-items: center;">
        <input 
          type="text" 
          id="emran-ai-input" 
          placeholder="Ask Emran AI..." 
          maxlength="400" 
          autocomplete="off"
          style="flex: 1; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 9999px; padding: 10px 16px; font-size: 13.5px; color: #F1F5F9; outline: none; transition: border-color 0.2s;"
        />
        <button 
          type="submit" 
          id="emran-ai-send" 
          title="Send"
          style="width: 38px; height: 38px; border-radius: 50%; background: linear-gradient(135deg, #FF715B 0%, #FF8C68 100%); border: none; color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; box-shadow: 0 4px 12px rgba(255, 113, 91, 0.35); transition: transform 0.2s;"
        >
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
        </button>
      </form>
    </div>
  `;

  document.body.appendChild(widgetContainer);

  // Element Selectors
  const triggerBtn = document.getElementById('emran-ai-trigger');
  const chatBox = document.getElementById('emran-ai-box');
  const chatIcon = document.getElementById('emran-ai-icon-chat');
  const closeIcon = document.getElementById('emran-ai-icon-close');
  const closeBoxBtn = document.getElementById('emran-ai-close-box');
  const clearBtn = document.getElementById('emran-ai-clear');
  const messagesContainer = document.getElementById('emran-ai-messages');
  const chatForm = document.getElementById('emran-ai-form');
  const chatInput = document.getElementById('emran-ai-input');
  const chipsContainer = document.getElementById('emran-ai-chips');

  // Toggle Chat Box
  function toggleChat(forceState) {
    state.isOpen = typeof forceState === 'boolean' ? forceState : !state.isOpen;
    if (state.isOpen) {
      chatBox.classList.add('active');
      chatIcon.style.display = 'none';
      closeIcon.style.display = 'block';
      setTimeout(() => chatInput.focus(), 200);
    } else {
      chatBox.classList.remove('active');
      chatIcon.style.display = 'block';
      closeIcon.style.display = 'none';
    }
  }

  triggerBtn.addEventListener('click', () => toggleChat());
  closeBoxBtn.addEventListener('click', () => toggleChat(false));

  // Clear Chat History
  clearBtn.addEventListener('click', () => {
    state.history = [];
    messagesContainer.innerHTML = `
      <div class="emran-ai-msg emran-ai-msg-assistant">
        Chat history cleared. How else can I assist you with Emran's portfolio?
      </div>
    `;
    chipsContainer.style.display = 'flex';
  });

  // Append Message to DOM
  function appendMessage(role, content) {
    const msgEl = document.createElement('div');
    msgEl.className = `emran-ai-msg emran-ai-msg-${role}`;
    msgEl.innerHTML = formatMarkdown(content);
    messagesContainer.appendChild(msgEl);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  // Show Typing Indicator
  let typingEl = null;
  function showTyping() {
    if (typingEl) return;
    typingEl = document.createElement('div');
    typingEl.className = 'emran-ai-typing';
    typingEl.innerHTML = '<span></span><span></span><span></span>';
    messagesContainer.appendChild(typingEl);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  function hideTyping() {
    if (typingEl) {
      typingEl.remove();
      typingEl = null;
    }
  }

  // Client-side fallback matcher
  function getClientFallbackAnswer(msg) {
    const lower = (msg || '').toLowerCase();
    for (const item of CLIENT_FALLBACK_FAQ) {
      if (item.keywords.some(kw => lower.includes(kw))) {
        return item.answer;
      }
    }
    return "Emran Hosen is a Senior Full-Stack AI Engineer specializing in Autonomous Multi-Agent Systems, WebGL 3D Interactive Worlds (like Next Label), and Enterprise Cloud Platforms. Feel free to explore his Flagship Projects, or drop a message via the Contact page to collaborate directly!";
  }

  // Send Query to /api/chat
  async function handleSend(userText) {
    const text = (userText || '').trim();
    if (!text || state.isTyping) return;

    // Append user message
    appendMessage('user', text);
    state.history.push({ role: 'user', content: text });
    chatInput.value = '';
    state.isTyping = true;
    showTyping();

    // Hide chips after first message to keep view uncluttered
    chipsContainer.style.display = 'none';

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: text,
          history: state.history
        })
      });

      hideTyping();

      if (response.ok) {
        const data = await response.json();
        const reply = data.reply || getClientFallbackAnswer(text);
        appendMessage('assistant', reply);
        state.history.push({ role: 'assistant', content: reply });
      } else if (response.status === 429) {
        appendMessage('assistant', "⏳ You're asking questions quickly! Please wait a moment before sending another message.");
      } else {
        const fallback = getClientFallbackAnswer(text);
        appendMessage('assistant', fallback);
        state.history.push({ role: 'assistant', content: fallback });
      }
    } catch (err) {
      hideTyping();
      const fallback = getClientFallbackAnswer(text);
      appendMessage('assistant', fallback);
      state.history.push({ role: 'assistant', content: fallback });
    } finally {
      state.isTyping = false;
    }
  }

  // Form Submit Handler
  chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    handleSend(chatInput.value);
  });

  // Prompt Chips Handler
  chipsContainer.addEventListener('click', (e) => {
    const chip = e.target.closest('.emran-ai-chip');
    if (chip) {
      const prompt = chip.getAttribute('data-prompt');
      if (prompt) handleSend(prompt);
    }
  });

  // Keyboard shortcut to toggle chat: Ctrl + Shift + C or Cmd + Shift + C
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === 'c') {
      e.preventDefault();
      toggleChat();
    }
  });

})();
