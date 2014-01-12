MineMon
=======

Quick and dirty python script which will monitor cgminer to keep you as close to 100% up time as you can get. Just make a root cronjob to run however often you want (I did every minute). Change the constant vars to the appropriate locations for your files.

This does not manage config setting for your miner. This is all done inside the miner.sh which would typically call cgminer with a conf file. Ensure API-Listen is enabled.

Requires screen.
