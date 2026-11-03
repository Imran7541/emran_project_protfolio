/**
 * Cloudflare Pages Function: /api/health
 * Edge health check endpoint.
 */

export async function onRequestGet() {
  return new Response(JSON.stringify({
    status: "healthy",
    service: "cloudflare-pages-edge",
    timestamp: new Date().toISOString()
  }), {
    status: 200,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*"
    }
  });
}
