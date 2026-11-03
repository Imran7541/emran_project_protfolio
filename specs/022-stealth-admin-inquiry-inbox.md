# Spec 022: Stealth Admin Client Inquiry Inbox & Management Portal

## 1. Feature Overview
This specification details the architecture, Zero-Trust authorization, REST API contracts, and glassmorphic UI components for the **Stealth Admin Client Inquiry Inbox**.

Currently, client inquiries submitted via `POST /api/contact` are persistently recorded in `data/inquiries.jsonl` and dispatched to Discord/Telegram webhooks. However, the developer cannot inspect, review, or manage these inquiries directly within the portfolio web interface. 

This feature adds a secured, private **Inquiries Inbox** inside the Stealth Executive Admin mode (`Ctrl + Shift + A` / `/gallery?admin=1`).

```yaml
feature_metadata:
  spec_id: "022"
  title: "Stealth Admin Client Inquiry Inbox"
  author: "Emran Hosen"
  status: "Draft"
  security_level: "Zero-Trust Admin-Gated (Bearer Token / Master Passcode)"
  target_endpoints:
    - "GET /api/admin/inquiries"
    - "DELETE /api/admin/inquiries/:id"
    - "functions/api/admin/inquiries.js"
  target_ui_surfaces:
    - "gallery.html (#admin-control-bar & #admin-inbox-modal)"
    - "gallery/index.html"
```

---

## 2. Zero-Trust Security & API Contracts

### 2.1 Backend Endpoints (`server.js` & `functions/api/admin/inquiries.js`)

1. **`GET /api/admin/inquiries`**:
   - **Authentication**: Requires valid admin session via `Authorization: Bearer <token>` or header `x-admin-token: <token>` or `x-admin-passcode: <master_passcode>`.
   - **Unauthorized**: Returns HTTP `401 Unauthorized` with `{ ok: false, error: "Unauthorized access." }`.
   - **Authorized**: Reads `data/inquiries.jsonl`, parses each line into JSON, strips raw IP addresses (for privacy), and sorts descending by `receivedAt` (newest first).
   - **Response** (HTTP 200):
     ```json
     {
       "ok": true,
       "total": 4,
       "inquiries": [
         {
           "id": "mlz8q9w-1a2b",
           "name": "Alex Vance",
           "email": "alex@enterprise.com",
           "service": "Autonomous AI Agent Swarm",
           "message": "We need an autonomous multi-agent pipeline for document processing.",
           "receivedAt": "2026-11-03T01:15:00.000Z"
         }
       ]
     }
     ```

2. **`DELETE /api/admin/inquiries/:id`**:
   - **Authentication**: Requires valid admin session.
   - **Unauthorized**: Returns HTTP 401.
   - **Authorized**: Reads `data/inquiries.jsonl`, filters out the matching inquiry by `id`, and atomically writes back the updated lines.
   - **Response** (HTTP 200):
     ```json
     {
       "ok": true,
       "message": "Inquiry successfully removed.",
       "id": "mlz8q9w-1a2b"
     }
     ```

---

## 3. UI Component Architecture (`gallery.html`)

1. **Inquiries Trigger in Admin Ribbon (`#admin-control-bar`)**:
   - Next to "+ Ingest New Media", add an "📬 Client Inquiries (N)" button with a pulsing notification badge.
   - Displays real-time count of total inquiries.

2. **Executive Inbox Modal (`#admin-inbox-modal`)**:
   - Glassmorphic modal backdrop with blur overlay (`backdrop-blur-2xl`).
   - **Header**: Title ("Client Inquiries Inbox"), total count badge, refresh button, and close trigger (`Escape` or `✕`).
   - **Search Bar**: Real-time client-side filter by client name, email, service, or keywords in message.
   - **Inquiry Cards**:
     - Client Name & Avatar initials badge.
     - Email with 1-click "Reply Mail" (`mailto:`) button.
     - Service category pill (e.g. `Autonomous AI Agent`, `3D WebGL`, etc.).
     - Timestamp formatted to human-readable Dhaka time (`GMT+6`).
     - Expandable full message text box.
     - Danger "Delete" button with confirmation prompt.
   - **Empty State**: Friendly illustration and message when inbox is empty.

---

## 4. Gherkin BDD Scenarios

```gherkin
Feature: Stealth Admin Client Inquiry Management

  Scenario: Unauthenticated visitor attempts to fetch inquiries
    Given a visitor sends a "GET" request to "/api/admin/inquiries" without an admin session token
    Then the server MUST return HTTP 401
    And the response MUST contain "Unauthorized"

  Scenario: Authenticated admin fetches all client inquiries
    Given an administrator holds a valid admin session token
    When the administrator sends a "GET" request to "/api/admin/inquiries" with "Authorization: Bearer <token>"
    Then the server MUST return HTTP 200
    And the response MUST contain a list of inquiries ordered newest first
    And raw IP addresses MUST NOT be exposed in the payload

  Scenario: Authenticated admin deletes an inquiry
    Given an administrator holds a valid admin session token
    And an inquiry with ID "test-inquiry-123" exists in "data/inquiries.jsonl"
    When the administrator sends a "DELETE" request to "/api/admin/inquiries/test-inquiry-123"
    Then the server MUST return HTTP 200
    And the inquiry "test-inquiry-123" MUST be removed from "data/inquiries.jsonl"

  Scenario: Public visitor views gallery page
    Given an unauthenticated visitor loads "gallery.html"
    Then the element "#admin-control-bar" MUST remain hidden
    And the element "#admin-inbox-modal" MUST remain hidden
    And zero inquiry data MUST be loaded into the client DOM
```
