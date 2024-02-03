"""
ex.py

Locally save and call this file ex.py ##
Code to demonstrate the use of some of the OS modules in python
"""
import os
from pathlib import Path

# Get the current working directory
pwd = os.getcwd()
print(pwd)

# List the files in the current directory
print(os.listdir(pwd))

# Check if the file is indeed a file
file_path = "./ex.py"
print(os.path.isfile(file_path))

# Check if the file ends with ".py"
print(file_path.endswith(".py"))

# Check if "testdir" is a directory
print(os.path.isdir("testdir"))

# Change to "testdir" directory and list its contents
os.chdir("testdir")
print("-" * 25)
print(os.listdir("."))

# Change back to the original directory
os.chdir("..")

# Get a list of all directories in the current directory
for item in os.listdir("."):
    if os.path.isdir(item):
        print("-" * 25)
        print(item)

print("=" * 50)

# Function to recursively list files with a specific suffix
def list_files_with_suffix(directory, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                print(os.path.join(root, file))

# Get the current working directory
cwd = os.getcwd()
list_files_with_suffix(cwd, ".c")

print("=" * 50)

# Get the directory where the program is running
dir_path = Path.cwd()
print(dir_path)

# Use pathlib to list files with a specific suffix
suffix = ".c"
for file in dir_path.glob(f"**/*{suffix}"):
    print(file)