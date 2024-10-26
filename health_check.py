#!/usr/bin/env python3

import shutil
import psutil


#define a check disk usage function 
def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	percent_free= (du.free/du.total)*100  #calculate percentage of free disk space
	return percent_free > 20 # Return True if free space is greater than 20%


#define check cpu usage function
def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75 # Check if CPU usage is less than 80%
  

if check_disk_usage("/") == False  or check_cpu_usage() == False:
    print("Health check failed!!!")
else:
    print("Health check passed!!!")
