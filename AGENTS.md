# Repository Guidelines

## Project Structure & Module Organization
- `app/main.py` is the FastAPI entrypoint; keep it minimal and delegate to routers.
- HTTP endpoints live in `app/api/v1`; group new routes under versioned subpackages and register them through `router.py`.
- Core business logic stays in `app/domain`; persistence adapters and DB plumbing belong in `app/infrastructure`, including Alembic under `app/infrastructure/db/alembic`.
- Infrastructure manifests sit at the repo root: `compose.yml` for local containers, `terraform/` for cloud provisioning, and `.env.sample` for configuration templates.

## Build, Test, and Development Commands
- `uv sync` installs locked dependencies; rerun after touching `pyproject.toml` or `uv.lock`.
- `uv run uvicorn app.main:app --reload` starts the API with live reload; override host/port via CLI flags when needed.
- `uv run ruff check .` lints the codebase, and `uv run ruff format .` applies canonical formatting.
- `uv run alembic upgrade head` applies migrations; pair with `uv run alembic revision --autogenerate -m "message"` when models change.
- `docker compose up app` launches the devcontainer plus PostgreSQL if you prefer an isolated toolchain.

## Coding Style & Naming Conventions
- Target Python 3.13; follow Ruff defaults (88-character lines, sorted imports, no unused symbols).
- Modules use `snake_case`, classes use `PascalCase`, and async helpers should end with `_async`.
- Declare FastAPI dependencies with explicit type hints and prefer Pydantic models for request/response objects.
- Keep secrets in `.env`; never commit environment-specific values.

## Testing Guidelines
- Create a top-level `tests/` directory that mirrors `app/` (e.g., `tests/api/test_health.py`, `tests/domain/test_user.py`).
- Run suites with `uv run pytest`; use HTTPX clients for API layers and transactional SQLModel sessions for repository tests.
- Every feature or bugfix should include regression coverage, asserting both HTTP payloads and database side effects.

## Commit & Pull Request Guidelines
- Use Conventional Commits as seen in history (`feat:`, `fix:`, `chore:`) with concise, imperative subjects.
- Scope each commit to one logical change plus its tests or migration; avoid mixing unrelated cleanups.
- Pull requests must describe the change, link relevant issues, list validation commands, and call out any Alembic revisions or configuration updates.

## Database & Configuration Notes
- Runtime settings are defined in `app/core/config.py` and loaded from the root `.env`; update `.env.sample` whenever new keys are introduced.
- The `db` service in `docker compose` provides PostgreSQL 17; ensure migrations run before manual testing.
- For local setups outside Docker, set `DB_HOST=localhost` and align credentials with your personal PostgreSQL instance.
