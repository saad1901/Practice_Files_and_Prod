import subprocess
from datetime import datetime
import os
import random
import requests
import time

def is_internet_available():
    try:
        requests.get("http://www.google.com", timeout=10)
        return True
    except requests.ConnectionError:
        return False

def reset_file(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        pass  # Clears the file

def add_time_to_file(file_path):
    with open(file_path, "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + "\n")

def execute_batch_file(batch_file_path):
    try:
        subprocess.run(batch_file_path, shell=True, check=True)
        print(f"✅ Successfully executed: {batch_file_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing batch file: {e}")
        return False

# Main execution
if is_internet_available():
    file_path = r"F:\Desktop\testing_files\git_pushes.txt"
    batch_file_path = r"F:\Desktop\testing_files\bat.bat"

    reset_file(file_path)  # Clear previous content

    quant = random.randint(3, 5)
    print(f"Will perform {quant} commits...\n")
    for i in range(quant):
        add_time_to_file(file_path)
        success = execute_batch_file(batch_file_path)
        if success:
            print(f"✔ Commit {i+1} of {quant} done.\n")
        else:
            print(f"✘ Commit {i+1} of {quant} failed.\n")
        time.sleep(1)
else:
    print("⚠ Internet Not Connected !!")
