import os
from os import path
import datetime
from datetime import date, time,timedelta
import time

def main():

# Print the name of the os
    print(os.name)

#Check for item existence and type
    print("Item exists: ", path.exists("textfile.txt"))
    print("Item is a file: ", str(path.isfile("textfile.txt")))
    print("Item is a directory: ", str(path.isdir("textfile.txt")))

# work with file path
    print("Item path: ", str(path.realpath("textfile.txt"))) 
    print("Item path and name: ", str(path.split(path.realpath("textfile.txt"))))

# Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

# Calculate how long ago the item wa modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been "+ str(td) + " since the fie was modified")
    print("or, "+ str(td.total_seconds())+ " seconds")





if __name__ == "__main__":
    main()