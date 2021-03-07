"""
Renames the files in the same directory and delete itself after completion
Usage:
python rename.py
"""
import os

# Current dir
path =  os.getcwd()
# Files in the current directory
filenames = os.listdir(path)

for count, filename in enumerate(filenames):
    newName = "Prefix" + str(count) + ".format"
    os.rename(filename, newName)
