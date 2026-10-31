# Spec 013: CoolLabs (Coolify) Production Live Deployment

## 1. Overview
Deploy and verify Emran Hosen's portfolio application on the local host's CoolLabs (Coolify v4.5.3) instance, delivering high-performance, containerized service with automated Traefik routing, health monitoring, and direct port mapping.

---

## 2. Infrastructure Specification
- **Platform**: CoolLabs (Coolify v4.5.3)
- **Container Name**: `3lolil9okyxy5wz6ophjozt1-20261031T084922`
- **Application UUID**: `3lolil9okyxy5wz6ophjozt1`
- **Build Pack**: Nixpacks (Node.js runtime)
- **Git Source**: `https://github.com/Imran7541/emran_project_protfolio` (`main` branch)
- **Port Mapping**: `8088:5225`
- **Traefik FQDN**: `http://portfolio.127.0.0.1.sslip.io`, `http://3lolil9okyxy5wz6ophjozt1.103.238.115.33.sslip.io`
- **Coolify UI Dashboard**: `http://localhost:8000/project/v7zcpgjgrgof6t21260vlegp/environment/j4ql5ylgs7jghjoqexxqkrpl/application/3lolil9okyxy5wz6ophjozt1`

---

## 3. BDD Scenarios

### Scenario: Traefik Ingress Reverse Proxy
- **Given** Coolify Traefik reverse proxy is active on port 80
- **When** an HTTP request is made to `http://portfolio.127.0.0.1.sslip.io`
- **Then** Traefik routes the request to application container port 5225 and returns `HTTP 200 OK`

### Scenario: Direct Container Port Mapping
- **Given** container port 5225 is mapped to host port 8088
- **When** an HTTP request is sent to `http://127.0.0.1:8088/` or `http://127.0.0.1:8088/gallery.html`
- **Then** the Node.js server streams the full HTML content with `HTTP 200 OK`

### Scenario: API Health Verification
- **Given** the application container is running
- **When** `GET /api/health` is requested
- **Then** the response status is 200 and payload contains `status: "healthy"` and `service: "Emran Hosen Portfolio Server"`
