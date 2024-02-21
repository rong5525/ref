@echo off
echo Running Git commands...
git add --all
git commit -m "update"
git push
echo Git commands executed successfully.
echo Waiting for 5 seconds before exiting...
timeout /t 5 /nobreak >nul
