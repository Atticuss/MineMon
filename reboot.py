#!/usr/bin/python
from subprocess import call,Popen
from datetime import datetime

MINEMONLOGFILE="/home/miner/cgminer/minemon.log"
LOGFILE="/var/log/reboot.log"

def log():
	with open(LOGFILE,"a") as lfile:
		lfile.write("[*] Reboot occurred %s %s:%s:%s\n" % (datetime.now().date(), datetime.now().hour, datetime.now().minute, datetime.now().second))

with open(MINEMONLOGFILE,"r") as lfile:
	for line in lfile:
		if "CGMiner frozen" in line:
			log()
			call('echo "" > /home/miner/cgminer/minemon.log',shell=True)
			call("/sbin/reboot", shell=True)
