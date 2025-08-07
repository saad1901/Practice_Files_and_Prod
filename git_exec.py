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

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

def is_internet_available(retries=3, delay=2) -> bool:
    """Check if internet is available, with limited retries."""
    for attempt in range(retries):
        try:
            requests.get("http://www.google.com", timeout=3)
            return True
        except requests.ConnectionError:
            logging.warning("Internet check failed, retrying...")
            time.sleep(delay)
    return False

def add_time_to_file(file_path: str) -> None:
    """Append current timestamp to a file (with directory creation)."""
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    with open(file_path, "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + "\n")

def execute_batch_file(batch_file_path: str) -> bool:
    """Run a batch file and report status."""
    try:
        subprocess.run(batch_file_path, shell=True, check=True)
        logging.info(f"Successfully executed: {batch_file_path}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing batch file: {e}")
        return False

def main(file_path, batch_file_path):
    if is_internet_available():
        quant = random.randint(3, 5)
        logging.info(f"Will perform {quant} commits")
        iterator = tqdm(range(quant), desc="Processing") if HAS_TQDM else range(quant)
        for i in iterator:
            add_time_to_file(file_path)
            success = execute_batch_file(batch_file_path)
            if success:
                logging.info(f"Completed commit {i+1} / {quant}")
            else:
                logging.error(f"Failed at commit {i+1} / {quant}")
            time.sleep(1)
    else:
        logging.error("Internet Not Connected !! Exiting.")

if __name__ == '__main__':
    # Accept file and batch paths as optional command line arguments
    default_file_path = r"F:\Desktop\testing_files\git_pushes.txt"
    default_batch_file_path = r"F:\Desktop\testing_files\bat.bat"
    file_path = sys.argv[1] if len(sys.argv) > 1 else default_file_path
    batch_file_path = sys.argv[2] if len(sys.argv) > 2 else default_batch_file_path
    main(file_path, batch_file_path)
