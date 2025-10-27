@echo off
title Ein Tzofia Pro v3.0
color 0F
cls

echo ============================================
echo   Ein Tzofia Pro v3.0
echo   Gemini 2.5 Flash Integration
echo ============================================
echo.

cd /d "%~dp0"

echo Installing dependencies...
python -m pip install streamlit google-generativeai pywhatkit --quiet

echo.
echo Starting application...
echo Browser will open at: http://localhost:8501
echo.
echo Press Ctrl+C to stop
echo ============================================
echo.

python -m streamlit run app.py

pause
