#!/bin/python
import os
import os.path
import subprocess

# This will clean up a log file

# Put the maximum size you want the log file to be.  If you want 10M, put
# Default size is 10M, as listed in the following line:
# max_size = 10485760

max_size = 10485760

# Enter the location and filename of the log file here:

location = '~/development/practice/logs'
filename = 'logfile'

# The following variable is the total number of backup files you want to keep

max_backup_files = 9

##############################################################

logsize =  os.path.getsize(filename)

my_files = os.listdir('.')
filecount = 0
for file in my_files:
    if filename in file:
        filecount += 1

if filecount < max_backup_files:
    max_backup_files = filecount + 1
max_backup_files -= 1

if logsize >= max_size:
    for counter in range(max_backup_files, 1, -1):
        print counter
        subprocess.Popen(['/bin/mv', '-f', filename+str(counter), filename+str(counter + 1)])
    subprocess.Popen(['/bin/mv', '-f', filename, filename+"2"])
    
