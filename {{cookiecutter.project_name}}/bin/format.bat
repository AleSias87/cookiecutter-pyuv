@echo off
cd "%~dp0.."

uv run black src
uv run black tests
