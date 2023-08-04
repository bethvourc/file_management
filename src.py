import os

# script to sort out photos 

# create a source and a target 
source = "/mnt/chromeos/MyFiles/Downloads"
target = "/mnt/chromeos/MyFiles/Downloads/placeholder"


files = os.listdir(source)

for file in files:
    print(file)