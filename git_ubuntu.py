import subprocess
from datetime import datetime
import os
import random
import requests
import time

# ==== CONFIGURATION ====
BASE_DIR = "/media/saad/Downloads/Desktop/testing_files"
FILE_PATH = os.path.join(BASE_DIR, "git_pushes.txt")
REPO_PATH = BASE_DIR  # Assuming the repo is located here
BRANCH_NAME = "master"  # Change if you are using another branch like 'master'
# =======================

def is_internet_available():
    """Check if the internet is reachable by pinging Google."""
    try:
        requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

def reset_file(file_path):
    """Ensure directory exists and clear old content."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        pass  # Clears the file content

def add_time_to_file(file_path):
    """Append current timestamp to file."""
    with open(file_path, "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + "\n")

def run_command(command, cwd=None):
    """Run a shell command and return success status."""
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
        print(f"Successfully executed: {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing: {command}\n{e}")
        return False

def git_commit_and_push():
    """Add, commit, and push changes to the remote repository."""
    print(">> Performing git operations...\n")
    commands = [
        "git add .",
        f'git commit -m "commit at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"',
        f"git push origin {BRANCH_NAME}"
    ]

    for cmd in commands:
        success = run_command(cmd, cwd=REPO_PATH)
        if not success:
            return False
    return True

# ================= MAIN EXECUTION =================
if __name__ == "__main__":
    if is_internet_available():
        print("Internet connected!\n")
        reset_file(FILE_PATH)

        quant = random.randint(5, 15)
        print(f"Will perform {quant} commits and pushes...\n")
        for i in range(quant):
            # Step 1: Add timestamp to the file
            add_time_to_file(FILE_PATH)

            # Step 2: Commit and push
            success = git_commit_and_push()
            if success:
                print(f"Commit & Push {i+1} of {quant} done.\n")
            else:
                print(f"Commit & Push {i+1} of {quant} failed.\n")
            
            time.sleep(1)  # Small delay between commits
    else:
        print("⚠ Internet Not Connected !!")
        time.sleep(5)
