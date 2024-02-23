@echo off
python generate_html.py
echo Finished successfully.
echo Waiting for 5 seconds before exiting...
timeout /t 5 /nobreak >nul
