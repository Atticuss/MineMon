MineMon
=======

Quick and dirty python script which will monitor cgminer to keep you as close to 100% up time as you can get. Stumbled across cgmon.tcl and wasn't happy with it so I wrote my own. Set minemon.py to run via a cronjob every minute as your mining user and set a root cronjob for reboot.py every 5 minutes or so. Had some issues starting cgminer as root so I had to split the functionality between two users.

Functionality includes:
  - Start cgminer if it's not running.
  - Check if cgminer is frozen and reboot if so.
  - Tracks all reboots by datetime to a logfile.
  - TODO: Reboot if a card dies.

This does not manage config setting for your miner. This is all done inside the miner.sh which would typically call cgminer with a conf file. Ensure API-Listen is enabled. Constant vars at the beginning should be modified to point to the appropriate IP, port, log file, and miner.sh file. Ensure log files are identical in both reboot.py and minemon.py.

Requires screen.
