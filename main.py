import os
import time
import logging
import sys
from dirsync import sync


def check_path(current_path):
    """
    Check if folder path exist,
    if path exist returns path
    """
    path_exist = os.path.isdir(current_path)
    while path_exist == False:
        current_path = input("Please enter correct folder path: ")
        path_exist = os.path.isdir(current_path)
    return current_path


def check_positive_int(prompt):
    """
    Check for incorrect and negative number
    returns positive and whole number
    """
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, please enter correct number")
            continue

        if value < 0:
            print("Sorry, number must not be negative.")
            continue
        else:
            break
    return value


# Prompt user to provide Source path and validates if entered path exist or not
source_path = check_path(input("Please enter your source folder path: "))

# Prompt user to provide Destination path and validates if entered path exist or not
# If provided destination path is same as source path, asks user again for corrrect one
destination_path = check_path(
    input("Please enter your destination folder path: "))
while destination_path == source_path:
    destination_path = check_path(
        input("Source and Destination can't be same, Please enter correct destination folder path: "))

# Prompt user to provide log file path and validates if entered path exist or not
# If Source or Destination path is same as log file path, it ask again.
log_path = check_path(input("Please enter log file path: "))
while log_path == destination_path or log_path == source_path:
    log_path = check_path(input(
        "Source or Destination path can't be same as log file path. Please enter correct log file path: "))

# Joins the log_path with sync_folder.log
logfile = os.path.join(log_path, "sync_folder.log")


# Store log on sync_folder.log and also display log on console
logging.basicConfig(level=logging.DEBUG, handlers=[logging.FileHandler(
    logfile), logging.StreamHandler(sys.stdout)])
my_log = logging.getLogger('dirsync')

# Prompt user to enter time in second
sync_interval = check_positive_int("Enter the syncing interval in seconds: ")

# Sync two folder, adds log according to time provided.
while (True):
    sync(source_path, destination_path, 'sync', logger=my_log, purge=True)
    time.sleep(sync_interval)
