@echo off
REM Installation script for Latin Analyzer on Windows
REM This script installs Python dependencies and downloads CLTK models

echo ============================================================
echo   LATIN ANALYZER - Windows Installation
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.8+ from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed:
python --version
echo.

REM Upgrade pip
echo ============================================================
echo Step 1: Upgrading pip...
echo ============================================================
python -m pip install --upgrade pip
if errorlevel 1 (
    echo [WARNING] Failed to upgrade pip, but continuing...
)
echo.

REM Install requirements
echo ============================================================
echo Step 2: Installing dependencies (cltk)...
echo ============================================================
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install dependencies!
    echo.
    pause
    exit /b 1
)
echo.
echo [OK] Dependencies installed successfully!
echo.

REM Download models
echo ============================================================
echo Step 3: Downloading CLTK models (~250MB)...
echo ============================================================
echo You will be asked to confirm the download.
echo Press 'Y' or Enter when prompted.
echo.
python setup_models.py
if errorlevel 1 (
    echo.
    echo [WARNING] Model download may have failed.
    echo You can try running 'python setup_models.py' manually later.
    echo.
)

echo.
echo ============================================================
echo   Installation Complete!
echo ============================================================
echo.
echo You can now run:
echo   - python latin_analyzer_cli.py (interactive mode)
echo   - python latin_analyzer.py (demo)
echo.
echo ============================================================
pause
