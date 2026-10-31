# Feature Specification: Clean Extensionless URLs Architecture

## 1. Context & Motivation
- **Problem**: When users access the live portfolio at `https://imran7541.github.io/emran_project_protfolio/gallery.html`, the `.html` extension is visible in the URL bar. This looks unpolished and legacy.
- **Root Cause**:
  1. Internal navigation links explicitly referenced `gallery.html`, `contact.html`, and `index.html`.
  2. Static file hosting on GitHub Pages and local servers served files by their literal filenames unless canonicalized.
- **Goal**:
  1. Transform all page URLs into modern, professional, extensionless routes (`/`, `/gallery`, `/contact`).
  2. Clean up browser address bar automatically when `/gallery.html` or `/contact.html` is visited.
  3. Ensure 100% interoperability across GitHub Pages, Node.js server (port 5225), and Coolify Docker container.

## 2. Technical Architecture & Ingress Rules
```text
Client Request                     Server / Host Action                     Address Bar Display
--------------------------------------------------------------------------------------------------
/gallery                           GitHub Pages / Node.js serves gallery.html  /gallery
/contact                           GitHub Pages / Node.js serves contact.html  /contact
/gallery.html                      history.replaceState / 301 redirect         /gallery
/contact.html                      history.replaceState / 301 redirect         /contact
/index.html                        history.replaceState / 301 redirect         /
/gallery/                          404.html auto-rewriter / Node.js normalizer /gallery
/contact/                          404.html auto-rewriter / Node.js normalizer /contact
```

## 3. Implementation Plan
1. **Canonical Client-Side Script**: Embed lightweight script in `<head>` of `index.html`, `gallery.html`, `contact.html` to strip `.html` and `index.html` via `history.replaceState`.
2. **Anchor Link Updates**: Update all internal `href` attributes in `index.html`, `gallery.html`, `contact.html` from `.html` to clean relative paths (`gallery`, `contact`, `./`).
3. **Server-Side Clean URL Ingress**: In `server.js`, normalize `/gallery`, `/gallery/`, `/contact`, `/contact/` to their respective HTML templates, and issue HTTP 301 redirects for `.html` requests.
4. **Resilient GitHub Pages 404 Routing**: Deploy `404.html` with automatic path reconciliation for trailing slash or extensionless subpaths.
5. **Multi-Host Verification**: Verify curl responses on local port 5225, Coolify container, and remote GitHub Pages.
