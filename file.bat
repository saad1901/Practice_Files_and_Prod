@echo off
echo %date% %time% - Running git_exec.py >> F:\Desktop\testing_files\script_log.txt
python "F:\Desktop\testing_files\git_exec.py" >> F:\Desktop\testing_files\script_log.txt 2>&1
echo %date% %time% - Finished executing git_exec.py with exit code %errorlevel% >> F:\Desktop\testing_files\script_log.txt
