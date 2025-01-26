@echo off
cd "%~dp0.."

uv run ruff check
uv run ruff format --check
echo.
uv run mypy
