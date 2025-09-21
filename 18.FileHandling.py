# Python has several built in modules for handling files os, shutil and pathlib

import os

folder_original = '/Users/sarah/Desktop/'
folder_destination = '/Users/sarah/Desktop/CleanedUp/'

# scandir list all the entries in the folder
entries = os.scandir(folder_original)
for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory:', entry.name)

os.mkdir(folder_destination)

# Moving a file
for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)
    
    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)