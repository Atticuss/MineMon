#!/bin/bash
sleep 10
export DISPLAY=:0
export GPU_MAX_ALLOC_PERCENT=100
export GPU_USE_SYNC_OBJECTS=1
/home/miner/cgminer/cgminer -c /home/miner/cgminer/miner.conf.multi
