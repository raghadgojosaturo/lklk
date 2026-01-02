# Clinical AI Agent

FastAPI app that uses LangChain + OpenAI for a simple clinical care coordinator agent with a tiny Chroma vector store.

## Quickstart

```powershell
# From repo root on Windows
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt

# Secrets
Copy-Item .env.example .env
# Edit .env and set OPENAI_API_KEY=...

# Run API
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs to try the `/coordinate` endpoint.

## Environment variables
- OPENAI_API_KEY: Your OpenAI API key.
- Optional LangChain tracing vars supported (see `.env.example`).

## Secret hygiene
- Push Protection blocked a prior commit with a secret. The history has been cleaned.
- If that key was real, revoke it and create a new one.
- Keep secrets only in `.env` or CI secrets, not in code or commits.

## Dev tooling
Optionally enable pre-commit hooks for secret scanning and basic hygiene.

```powershell
pip install pre-commit detect-secrets
# Create a baseline (scans current repo and records acceptable findings)
detect-secrets scan > .secrets.baseline
pre-commit install
# Run on all files once
pre-commit run --all-files
```

## Project structure
- app/ — FastAPI app, agents, vector store
- data/ — sample input
- chroma_db/ — local Chroma persistence (ignored)

## Notes
- Ensure `app/__init__.py` exists so `app.main:app` imports reliably.
