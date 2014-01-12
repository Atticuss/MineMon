MineMon
=======

Quick and dirty python script which will monitor cgminer to keep you as close to 100% up time as you can get. Stumbled across cgmon.tcl and wasn't happy with it so I wrote my own. Just make a root cronjob to run however often you want (I did every minute). Change the constant vars to the appropriate locations for your files.

This does not manage config setting for your miner. This is all done inside the miner.sh which would typically call cgminer with a conf file. Ensure API-Listen is enabled. Constant vars at the beginning should be modified to point to the appropriate IP, port, log file, and miner.sh file.

Requires screen.
