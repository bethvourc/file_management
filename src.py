import os

# script to sort out photos 

# create a source and a target 
source = "/mnt/chromeos/MyFiles/Downloads"
target = "/mnt/chromeos/MyFiles/Downloads/placeholder"


# specify the extensions allowed
EXTS = ("jpg", "png", "jpeg", "mov", "mp4")

# date formate
DATE_PATTERN = '.*(20\d\d)-?([01\d])-?([0123]\d).*'

# read files in source
files = os.listdir(source)

# get date
def get_date(folder, file):
    print(file)

for file in files:
    if (file.lower().endswith(tuple(EXTS))):
        get_date(source, file)