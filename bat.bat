@echo off
cd F:\Desktop\testing_files
git add .
set timestamp=%date% %time%
git commit -m "Auto commit on %timestamp%"
git push origin master
