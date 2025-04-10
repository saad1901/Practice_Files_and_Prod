@echo off
cd /d F:\Desktop\testing_files
git add .
set timestamp=%date% %time%
git commit -m "Auto commit on %timestamp%"
git push origin master
if %errorlevel% neq 0 (
    exit /b %errorlevel%
)
