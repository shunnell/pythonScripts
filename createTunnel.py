#!/bin/python

import sys
import subprocess

tunnelUser='shunnel'

localIP = []
localPort = []
remoteIP = []
remotePort = []
x = 0

vfile=open('/home/'+tunnelUser+'/development/scripts/port-data','rt')
for line in vfile:
    columns = line.split(',')
    localIP.append(columns[0])
    localPort.append(columns[1])
    remoteIP.append(columns[2])
    remotePort.append(columns[3])
    print remotePort[x]
    subprocess.Popen(['/bin/ssh', '-f', '-N', tunnelUser+"@"+localIP[x],\
        '-R', localPort[x]+":"+remoteIP[x]+":"+remotePort[x].strip()])
    x=x+1
sys.stdout.close()

