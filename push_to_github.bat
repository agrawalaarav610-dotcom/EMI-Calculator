@echo off
title Push Bank Loan Calculator to GitHub
cd /d "%~dp0"

echo ========================================================
echo       Bank Loan Calculator (PS No. 70) - GitHub Push
echo ========================================================
echo.

where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git is not installed or not found in PATH!
    echo Please install Git from https://git-scm.com/ and try again.
    pause
    exit /b 1
)

if not exist .git (
    echo [*] Initializing Git repository...
    git init
)

git remote get-url origin >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Please create a new empty repository on GitHub (https://github.com/new)
    echo.
    set /p REPO_URL="Enter your GitHub Repository URL (e.g., https://github.com/username/repo.git): "
    if "%REPO_URL%"=="" (
        echo [ERROR] Repository URL cannot be empty.
        pause
        exit /b 1
    )
    git remote add origin %REPO_URL%
) else (
    echo [*] Remote origin already configured.
)

echo.
echo [*] Staging project files...
git add .

echo.
echo [*] Committing changes...
git commit -m "Complete Bank Loan Calculator (PS No. 70) with documentation and test cases"

echo.
echo [*] Setting branch to main...
git branch -M main

echo.
echo [*] Pushing to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo  [SUCCESS] Code and Documentation pushed to GitHub!
    echo ========================================================
) else (
    echo.
    echo [NOTE] Push failed. Attempting rebase in case remote has initial commits...
    git pull origin main --rebase
    git push -u origin main
)

echo.
pause
