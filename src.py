import os
import re
import platform
import datetime

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

# find the created date (or modified date if not on windows)
def creation_date(path_to_file):
    # Try to get the date that was created, falling back to when it was
    # last modified if that isn't possible.
    if platform.system() == "Windows":
        timestamp = os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            timestamp = stat.st_birthtime
        except AttributeError:
            # we're probably on Linux. No easy way to get creation date here,
            # so we'll settle for when its content was last modified
            timestamp = stat.st_mtime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-d %H:%M%S')

# get folder function (TODO: need to complete)
def getFolder(year, monthNumber):
    if (monthNumber =="01 January"):
            monthFolder = "01 January"
    elif (monthNumber == "02 February"):
        monthFolder = "02 February"
    elif (monthNumber == "03 March"):
        monthFolder == "03 March"

    return year + "/" + monthFolder

# get date
def get_date(folder, file):
    matchObj = re.match(DATE_PATTERN, file)
    if (matchObj):
        year = matchObj.group(1)
        month = matchObj.group(2)
    else:
        dateCreated = creation_date(folder + "/" + file)
        matchObj = re.match(DATE_PATTERN, dateCreated)
        if (matchObj):
            year = matchObj.group(1)
            month = matchObj.group(2)
        else:
            year = "0"
            month = "0"
            print("Unable to get date: " + file)
    return {"year": year, "month":month}

for file in files:
    if (file.lower().endswith(tuple(EXTS))):
        date = get_date(source, file)
        year = date["year"]
        month = date["month"]

        if (year == "0" or month == "0"):
            continue

        