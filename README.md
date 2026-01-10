# 🛡️ GuardianAuth
GuardianAuth is a high-performance Identity and Access Management (IAM) service. Built for the modern enterprise, it provides a secure foundation for user authentication, JWT-based authorization, and granular Role-Based Access Control (RBAC).

## ✨ Key Features
- Modern Python Stack: Leveraging FastAPI for asynchronous performance and uv for ultra-fast, reproducible builds.

- Security-First Design: Uses Argon2 for password hashing and implements JWT Rotation to mitigate token theft.

- Stateless Scalability: Designed for cloud-native environments with Redis-backed token blacklisting and rate limiting.

- Enterprise Observability: Features structured JSON logging and standardized health-checks for Kubernetes/Docker orchestration.

- Strict Engineering Standards: 100% linted with Ruff and developed using TDD (Test Driven Development) principles.

## 🛠️ Tech Stack
- Backend: Python 3.12+, FastAPI, Pydantic v2

- Database: PostgreSQL (SQLAlchemy 2.0 Async)

- Caching: Redis (Session management & Rate limiting)

- Tooling: uv (Package management), Ruff (Linting), Pytest (Testing)

- DevOps: Docker (Multi-stage builds), GitHub Actions (CI/CD)

## 🚀 Getting Started
### Prerequisites
- Docker Desktop

- uv (for local development)

One-Command Setup
Clone the repository and spin up the entire infrastructure:

```
git clone https://github.com/YOUR_USERNAME/guardian-auth.git
cd guardian-auth
cp .env.example .env
docker-compose up --build
Access the interactive documentation at: http://localhost:8000/docs
```
## 🧪 Quality Control
We maintain high code quality through automated checks.

Run the test suite:

```
uv run pytest
Run the linter/formatter:
```

```
uv run ruff check . --fix
```

## 📐 Architecture & Decisions
- src Layout: Prevents accidental imports of development modules into the production build.

- Multi-Stage Docker: Minimizes attack surface and image size by excluding build-time dependencies (like uv and gcc) from the final runtime image.

- Dependency Injection: Extensively used for database sessions and security checks to ensure the code is highly testable and decoupled.

## 📅 Roadmap
- [ ] OAuth2 Social Login Integration (Google/GitHub)

- [ ] Multi-Factor Authentication (MFA) via TOTP

- [ ] Prometheus/Grafana metrics export

Developed by Mohammad Al-Bdour

[LinkedIn](www.linkedin.com/in/mjbdourdev)

[GitHub Portfolio](www.github.com/mjbdourdev)
