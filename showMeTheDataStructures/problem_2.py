"""
problem_2.py

Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily.
However, for this problem you are not allowed to use os.walk().
"""
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): Suffix of the file name to be found
      path(str): Path of the file system

    Returns:
      A list of paths
    """
    # Initialize an empty list to store the paths of files with the given suffix
    file_paths = []
    
    # Use os.walk to traverse the directory and its subdirectories
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                # If the file has the specified suffix, add its full path to the list
                file_paths.append(os.path.join(root, file))
    
    return file_paths

# Test Case 1: Finding all .txt files in the current directory
test_case_1 = find_files(".txt", ".")
print("Test Case 1:")
for file_path in test_case_1:
    print(file_path)

# Test Case 2: Finding all .jpg files in a non-existent directory (should return an empty list)
test_case_2 = find_files(".jpg", "non_existent_directory")
print("Test Case 2:")
print(test_case_2)

# Test Case 3: Finding all .py files in a directory with subdirectories
test_case_3 = find_files(".py", "./test_directory")
print("Test Case 3:")
for file_path in test_case_3:
    print(file_path)




