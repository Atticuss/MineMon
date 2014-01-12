#!/usr/bin/python

import socket
import json
import sys
import subprocess
from datetime import datetime
from subprocess import call,Popen

LOGFILE="/var/log/minemon.log"
MINERIP="127.0.0.1"
MINERPORT="4028"
CGMINERPATH="/home/miner/Downloads/cgminer/miner.sh"
logentry=""

def publishlog(resp=None):
        global logentry
        with open(LOGFILE,"w") as lfile:
                lfile.write("%s %s:%s:%s\n%s\nCurrent Status\n" % (datetime.now().date(),datetime.now().hour,datetime.now().minute,datetime.now().second,logentry))
                if resp != None:
                        for key in resp['SUMMARY'][0]:
                                lfile.write('%s: %s\n' % (key,resp['SUMMARY'][0][key]))

def log(msg):
        global logentry
        logentry += msg+"\n"

def linesplit(socket):
        buffer = socket.recv(4096)
        done = False
        while not done:
                more = socket.recv(4096)
                if not more:
                        done = True
                else:
                        buffer = buffer+more
                if buffer:
                        return buffer

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)
response = ""
try:
        s.connect((MINERIP,int(MINERPORT)))
        s.send(json.dumps({"command":"summary"}))
        response=linesplit(s)
        s.close()
except socket.error as err:
        if err.errno == socket.errno.ECONNREFUSED:
                log("Connection refused")
        else:
                raise err

if len(response)<1:
        cmd = subprocess.Popen("ps aux | grep cgminer | grep -v grep",stdout=subprocess.PIPE,shell=True)
        cout, cerr = cmd.communicate()
        if len(cout.rstrip()) == 0:
                log("CGMiner not running. Attempting to start.")
                call("/usr/bin/screen -dm sh %s" % CGMINERPATH,shell=True)
        else:
                log("CGMiner running but API not enabled")
        publishlog()
else:
        response=response.replace('\x00','')
        response=json.loads(response)
        hwe = response['SUMMARY'][0]['Hardware Errors']
        if hwe != 0:
                log("ALERT -- Hardware errors occurred: %s" % hwe)
        ctmh = repr(response['SUMMARY'][0]['Total MH']).rstrip()
        ptmh = None
        with open(LOGFILE,'r') as lfile:
                for line in lfile:
                        if 'Total MH' in line:
                                ptmh = line[10:].rstrip()
        if ptmh != None and ptmh == ctmh:
                log("CGMiner frozen. Restarting mining rig.")
                call("/sbin/reboot",shell=True)
        else:
                log("CGMiner currently running.")
        publishlog(response)
