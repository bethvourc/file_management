import os

# script to sort out photos 

# create a source and a target 
source = "/mnt/chromeos/MyFiles/Downloads"
target = "/mnt/chromeos/MyFiles/Downloads/placeholder"


# specify the extensions allowed
EXTS = ("jpg", "png", "jpeg", "mov", "mp4")

files = os.listdir(source)

for file in files:
    if (file.lower().endswith(tuple(EXTS))):
        print(file)