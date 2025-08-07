# import subprocess
# from datetime import datetime
# import os
# import random
# import requests
# import time

# def is_internet_available():
#     try:
#         requests.get("http://www.google.com", timeout=3)
#         return True
#     except requests.ConnectionError:
#         return False

# def add_time_to_file(file_path):
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#     with open(file_path, "a") as file:
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         file.write(current_time + "\n")

# def execute_batch_file(batch_file_path):
#     try:
#         subprocess.run(batch_file_path, shell=True, check=True)
#         print(f"Successfully executed: {batch_file_path}")
#         return True
#     except subprocess.CalledProcessError as e:
#         print(f"Error executing batch file: {e}")
#         return False

# if is_internet_available():
#     file_path = r"F:\Desktop\testing_files\git_pushes.txt"
#     # Use absolute path to avoid directory confusion
#     batch_file_path = r"F:\Desktop\testing_files\bat.bat"

#     quant = int(random.uniform(3, 5))
#     print(f"Will perform {quant} commits")
#     for i in range(quant):
#         add_time_to_file(file_path)
#         success = execute_batch_file(batch_file_path)
#         if success:
#             print(f"Completed commit {i+1}/{quant}")
#         else:
#             print(f"Failed at commit {i+1}/{quant}")
#         time.sleep(1)
# else:
#     print("Internet Not Connected !!")

import subprocess
from datetime import datetime
import os
import random
import requests
import time
import sys
import logging
from typing import Optional

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

# ---------- Logging Setup ----------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

# ---------- Internet Check ----------
def is_internet_available(retries: int = 3, delay: int = 2) -> bool:
    """Check internet connectivity."""
    for attempt in range(retries):
        try:
            requests.get("http://www.google.com", timeout=3)
            return True
        except requests.ConnectionError:
            logging.warning(f"Internet check failed (attempt {attempt+1})")
            time.sleep(delay)
    return False

# ---------- File Handling ----------
def reset_file(file_path: str) -> None:
    """Clear existing content in the file."""
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    with open(file_path, "w") as f:
        f.write("")

def append_current_time(file_path: str) -> None:
    """Append current timestamp to the file."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(current_time + "\n")

# ---------- Batch File Execution ----------
def execute_batch_file(batch_file_path: str) -> bool:
    """Execute a .bat file."""
    try:
        result = subprocess.run(batch_file_path, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(f"Batch Output:\n{result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Batch execution failed:\n{e.stderr.strip()}")
        return False

# ---------- Main Logic ----------
def main(file_path: str, batch_file_path: str, num_commits: Optional[int] = None, reset: bool = False):
    if not is_internet_available():
        logging.error("Internet not available. Exiting.")
        return

    if reset:
        reset_file(file_path)
        logging.info(f"Cleared contents of {file_path}")

    quant = num_commits if num_commits is not None else random.randint(3, 5)
    logging.info(f"Starting {quant} commit operations")

    iterator = tqdm(range(quant), desc="Committing") if HAS_TQDM else range(quant)
    for i in iterator:
        append_current_time(file_path)
        success = execute_batch_file(batch_file_path)
        if success:
            logging.info(f"Commit {i + 1}/{quant} succeeded")
        else:
            logging.warning(f"Commit {i + 1}/{quant} failed")
        time.sleep(1)

# ---------- Entry Point ----------
if __name__ == '__main__':
    default_file_path = r"F:\Desktop\testing_files\git_pushes.txt"
    default_batch_file_path = r"F:\Desktop\testing_files\bat.bat"

    file_path = sys.argv[1] if len(sys.argv) > 1 else default_file_path
    batch_file_path = sys.argv[2] if len(sys.argv) > 2 else default_batch_file_path
    num_commits = int(sys.argv[3]) if len(sys.argv) > 3 else None
    reset_flag = "--reset" in sys.argv

    main(file_path, batch_file_path, num_commits, reset_flag)
