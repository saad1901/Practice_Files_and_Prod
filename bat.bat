@echo off
cd F:\Desktop\testing_files
echo Running git commands...
git add .
set timestamp=%date% %time%
echo Committing changes with timestamp: %timestamp%
git commit -m "Auto commit on %timestamp%"
git push origin master
if %errorlevel% neq 0 (
    echo Error: Git command failed with code %errorlevel%
    exit /b %errorlevel%
)
echo Git operations completed successfully
