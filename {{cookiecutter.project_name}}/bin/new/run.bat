@REM Creates a new Python file

@echo off
if [%1]==[] goto usage

uv run %~dp0new.py %*
goto :eof

:usage
@echo Usage: %0 [file_name.py ^| folder_name]
exit /B 1

set WINEXITCODE=%ERRORLEVEL%
