@echo off
cd /d F:\Desktop\testing_files
echo %date% %time% - Starting git auto-commit on unlock >> unlock_log.txt

echo Running git commands...
git add .
set timestamp=%date% %time%
echo Committing changes with timestamp: %timestamp%
git commit -m "Auto commit on %timestamp%" >> unlock_log.txt 2>&1
if %errorlevel% neq 0 (
    echo %date% %time% - Error: Git commit failed with code %errorlevel% >> unlock_log.txt
    goto end
)

echo Pushing to remote...
git push origin master >> unlock_log.txt 2>&1
if %errorlevel% neq 0 (
    echo %date% %time% - Error: Git push failed with code %errorlevel% >> unlock_log.txt
    goto end
)

echo %date% %time% - Git operations completed successfully >> unlock_log.txt

:end
echo Task completed
