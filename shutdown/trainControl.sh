#!/bin/bash

source noShutdown.inc

########### aqui va el proceso #######
python scriptTest.py
sleep 10
######################################

stopNoShutDown
