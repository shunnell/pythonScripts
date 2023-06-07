#!/bin/python3

import sys
import subprocess

weekDay = 'monday'

sunday = []
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
count = 0
num = 0

vfile=open('cal-data','rt')
for line in vfile:
   sunday.append(line[num:num + 2])
   num += 3
   monday.append(line[num:num + 2])
   num += 3
   tuesday.append(line[num:num + 2])
   num += 3
   wednesday.append(line[num:num + 2])
   num += 3
   thursday.append(line[num:num + 2])
   num += 3
   friday.append(line[num:num + 2])
   num += 3
   saturday.append(line[num:num + 2])
   num = 0
   if count > 0:
      if tuesday[count] != "  ":
         if tuesday[count] != "":
            print(tuesday[count])
   count += 1
sys.stdout.close()
