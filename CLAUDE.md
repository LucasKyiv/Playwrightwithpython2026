# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Playwright + pytest test automation project targeting [SauceDemo](https://www.saucedemo.com/), structured as a learning template for test automation. Uses Python with the Page Object Model pattern.

## Commands

```bash
# Install dependencies
poetry install

# Install Playwright browsers
poetry run playwright install

# Run all tests
poetry run pytest

# Run a single test file
poetry run pytest tests/test_first_search.py

# Run a single test by name
poetry run pytest tests/test_first_search.py::test_item

# Run tests by marker
poetry run pytest -m smoke
poetry run pytest -m regression

# Run with a specific browser (chromium, firefox, webkit)
poetry run pytest --browser firefox

# Run with HTML report
poetry run pytest --html=playwright-report/report.html --self-contained-html

# Run in headed mode (show browser)
poetry run pytest --headed

# Run in parallel
poetry run pytest -n auto
```

## Architecture

### Structure

- `tests/` — test files (pytest discovers these)
- `login_page/` — Page Object Model classes
- `conftest.py` — root-level fixtures shared across all tests
- `.env` — local credentials (not committed); loaded via `python-dotenv`

### Page Object Model

Page objects live in top-level directories named after the page/feature (e.g., `login_page/`). Each module exposes a class with locators as instance attributes and actions as methods. Tests import these classes and instantiate them with the `page` fixture.

### Key Fixtures (conftest.py)

- `credentials` — loads `SAUCE_USERNAME` / `SAUCE_PASSWORD` from environment
- `logged_in_page_admin` — navigates to base URL, performs login via `LoginPage`, asserts inventory container is visible, returns authenticated `page`
- `browser_context_args` — session-scoped; sets `base_url` and viewport to 1920×1080

### Configuration (pyproject.toml)

pytest settings under `[tool.pytest.ini_options]`:
- `base_url = "https://www.saucedemo.com/"`
- `testpaths = ["tests"]`
- Markers: `smoke`, `regression`, `api`, `ui`

### Credentials

Copy `.env.example` (or create `.env`) with:
```
SAUCE_USERNAME=standard_user
SAUCE_PASSWORD=secret_sauce
LOCKED_USERNAME=locked_out_user
LOCKED_PASSWORD=secret_sauce
```

In CI, credentials are injected via GitHub Actions secrets and passed to pytest with `--sauce-username` / `--sauce-password` (or as env vars).

### CI

GitHub Actions workflow (`.github/workflows/playwright-tests.yml`) runs on push/PR to main/master. Artifacts uploaded on failure include screenshots and page HTML; Playwright HTML reports are retained for 30 days.
