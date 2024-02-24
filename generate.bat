@echo off
python generate.py
echo Finished successfully.
echo Waiting for 3 seconds before exiting...
timeout /t 3 /nobreak >nul
