import subprocess
from datetime import datetime
import os
import random
import requests
import time

def is_internet_available():
    try:
        requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

def add_time_to_file(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + "\n")

def execute_batch_file(batch_file_path):
    batch_dir = os.path.dirname(batch_file_path)
    if batch_dir:
        os.chdir(batch_dir)
    subprocess.run(batch_file_path, shell=True, check=True)

if is_internet_available():
    file_path = r"F:\Desktop\testing\git_pushes.txt"
    batch_file_path = r"F:\Desktop\testing\git.bat"

    quant = int(random.uniform(3, 5))
    print(quant)
    for _ in range(quant):
        add_time_to_file(file_path)
        execute_batch_file(batch_file_path)
        time.sleep(1)
else:
    print("Internet Not Connected !!")
