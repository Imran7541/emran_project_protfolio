/**
 * Cloudflare Pages Function: /api/contact
 * Handles contact inquiries, validates payloads, and dispatches instant push notifications to Telegram.
 */

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
    const name = (data.name || '').trim();
    const email = (data.email || '').trim();
    const service = (data.service || data.subject || 'General Inquiry').trim();
    const message = (data.message || '').trim();
    const honeypot = (data._gotcha || data.website || '').trim();

    // Honeypot spam defense
    if (honeypot) {
      return new Response(JSON.stringify({ ok: true, message: 'Message received.' }), {
        status: 200,
        headers: corsHeaders
      });
    }

    if (!name || name.length < 2 || name.length > 100) {
      return new Response(JSON.stringify({ ok: false, error: 'Name must be between 2 and 100 characters.' }), {
        status: 400,
        headers: corsHeaders
      });
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
      return new Response(JSON.stringify({ ok: false, error: 'Please provide a valid email address.' }), {
        status: 400,
        headers: corsHeaders
      });
    }

    if (!message || message.length < 5 || message.length > 2000) {
      return new Response(JSON.stringify({ ok: false, error: 'Message must be between 5 and 2,000 characters.' }), {
        status: 400,
        headers: corsHeaders
      });
    }

    const token = context.env?.TELEGRAM_BOT_TOKEN;
    const chatId = context.env?.TELEGRAM_CHAT_ID;
    const inquiryId = Date.now().toString(36) + Math.random().toString(36).substr(2, 5);

    // Asynchronously dispatch notification if configured
    if (token && chatId && !token.startsWith('[[') && !chatId.startsWith('[[')) {
      const timeStr = new Date().toLocaleString('en-US', { timeZone: 'Asia/Dhaka' });
      const text = `🚨 *New Portfolio Lead / Inquiry*\n\n` +
        `👤 *Name:* ${name}\n` +
        `📧 *Email:* ${email}\n` +
        `💼 *Service:* ${service}\n` +
        `🕒 *Time:* ${timeStr} (Dhaka)\n\n` +
        `📝 *Message:*\n${message}\n\n` +
        `🌐 *Source:* Cloudflare Pages Edge (DAC)`;

      const telegramPromise = fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: chatId,
          text: text,
          parse_mode: 'Markdown'
        })
      }).catch(err => {
        console.error('Telegram dispatch error on edge:', err);
      });

      if (context.waitUntil) {
        context.waitUntil(telegramPromise);
      }
    }

    // Asynchronously dispatch notification to Discord if configured
    const discordWebhook = context.env?.DISCORD_WEBHOOK_URL;
    if (discordWebhook && !discordWebhook.startsWith('[[') && discordWebhook.startsWith('https://discord.com/api/webhooks/')) {
      const timeStr = new Date().toLocaleString('en-US', { timeZone: 'Asia/Dhaka' });
      const discordPromise = fetch(discordWebhook, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: 'Emran Portfolio Lead Core',
          avatar_url: 'https://raw.githubusercontent.com/Imran7541/emran_project_protfolio/main/emran_suit.jpg',
          embeds: [
            {
              title: '🚨 New Client Inquiry Received',
              description: 'A new prospective client submitted a project transmission via the Portfolio Contact Page.',
              color: 16740699, // #FF715B
              fields: [
                { name: '👤 Client Name', value: name || 'Anonymous', inline: true },
                { name: '📧 Email Address', value: email || 'N/A', inline: true },
                { name: '💼 Selected Service', value: service || 'General Inquiry', inline: true },
                { name: '🕒 Timestamp (Dhaka)', value: timeStr + ' (BST)', inline: false },
                { name: '📝 Project Message', value: message || 'No message provided.', inline: false }
              ],
              footer: {
                text: 'Emran Hosen Portfolio Platform • Cloudflare Pages Edge (DAC)'
              }
            }
          ]
        })
      }).catch(err => {
        console.error('Discord dispatch error on edge:', err);
      });

      if (context.waitUntil) {
        context.waitUntil(discordPromise);
      }
    }

    return new Response(JSON.stringify({
      ok: true,
      message: 'Thank you! Your message has been received. Emran Hosen will connect with you within 12 hours.',
      inquiryId: inquiryId
    }), {
      status: 200,
      headers: corsHeaders
    });
  } catch (err) {
    return new Response(JSON.stringify({ ok: false, error: 'Failed to process inquiry.' }), {
      status: 500,
      headers: corsHeaders
    });
  }
}
