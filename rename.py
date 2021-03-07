"""
Renames the filenames within the same directory and delete it self after
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
