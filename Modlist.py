import os

# List all files in a directory using scandir()
basepath = os.getcwd() + '\\IndustrialDestiny\\mods'

print(basepath)

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)