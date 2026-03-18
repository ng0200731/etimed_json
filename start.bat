@echo off
REM Web server for network access - other users can connect

echo Starting Circle Position Web Server...
echo.
echo This server allows network users to access the application
echo.

cd /d "%~dp0"

REM Start the web server
py tools\web_server.py

pause
