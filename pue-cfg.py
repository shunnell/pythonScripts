#!/bin/python

import sys

if len(sys.argv) < 2:
    print("You must enter the PUE number!")
    sys.exit(128)

pue = str(sys.argv[1])
pue_ip = "192.168.24."+str((int(pue) + 100))
pue_hostname = "ifdcgsppupwks"+pue+".boilermaker.gar.us.ray.com"

print("Using hostname: "+pue_hostname)
print("Using ip address: "+pue_ip)

part1 = ""
part2 = ""
part3 = ""

vfile=open('pue_rhel7.cfg','rt')
newfile=open("pue_"+pue+".cfg", "w")
#vfile=open('/var/www/html/ks/pue_rhel7.cfg','rt')
#newfile=open('/var/www/html/ks/pue_"+pue+".cfg', 'a')
network_ip = True
for line in vfile:
    # Left all commented code below this code block because
    # I didn't have time to test, but assuming this is right
    if line[0:7] == "network" and network_ip == True:
        columns = line.split(' ')
        part1 = columns[0] + " " + columns[2] + " " + columns[3]
            # skipped columns[1] because of double-space
            # after the first network column
        part2 = columns[4] + " " + "--ip=" + pue_ip + " " + columns[6]
        part3 = columns[7] + " " + columns[8] + " " + columns[9]
        mod_line = part1 + " " + part2 + " " + part3
        network_ip = False
    else
        columns = line.split(' ')
        part1 = columns[0]
        part2 = "--hostname=" + pue_hostname
        mod_line = part1 + " " + part2
    newfile.writelines(mod_line)

#     if line[0:7] == "network" and network_ip == True:
#         columns = line.split(' ')
#         part1 = columns[0] + " " + columns[2] + " " + columns[3]
#             # skipped columns[1] because of double-space
#             # after the first network column
#         part2 = columns[4] + " " + "--ip=" + pue_ip + " " + columns[6]
#         part3 = columns[7] + " " + columns[8] + " " + columns[9]
#         mod_line = part1 + " " + part2 + " " + part3
#         newfile.writelines(mod_line)
#         network_ip = False
#     elif line[0:7] == "network" and network_ip == False:
#         columns = line.split(' ')
#         part1 = columns[0]
#         part2 = "--hostname=" + pue_hostname
#         mod_line = part1 + " " + part2
#         newfile.writelines(mod_line)
#     else:
#         newfile.writelines(line)
vfile.close()
newfile.close()



