# importing the required modules

import platform

# printing the Architecture of the OS
print("[+] Architecture :", platform.architecture()[0])

# Displaying the machine
print("[+] Machine :", platform.machine())

# printing the Operating System release information
print("[+] Operating System Release :", platform.release())

# prints the currently using system name
print("[+] System Name :",platform.system())

# This line will print the version of your Operating System
print("[+] Operating System Version :", platform.version())

# This will print the Node or hostname of your Operating System
print("[+] Node: " + platform.node())

# This will print your system platform
print("[+] Platform :", platform.platform())

# This will print the processor information
print("[+] Processor :",platform.processor())

from datetime import datetime
import psutil

# Using the psutil library to get the boot time of the system
boot_time = datetime.fromtimestamp(psutil.boot_time())
print("[+] System Boot Time :", boot_time)

# getting thesystem up time from the uptime file at proc directory
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()

uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("[+] System Uptime : " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

import os

pids = []
for subdir in os.listdir('/proc'):
    if subdir.isdigit():
        pids.append(subdir)
print('Total number of processes : {0}'.format(len(pids)))

import pwd

users = pwd.getpwall()
for user in users:
    print(user.pw_name, user.pw_shell)

# importing the required packages
import psutil

# This code will print the number of CPU cores present
print("[+] Number of Physical cores :", psutil.cpu_count(logical=False))
print("[+] Number of Total cores :", psutil.cpu_count(logical=True))
print("\n")
# This will print the maximum, minimum and current CPU frequency
cpu_frequency = psutil.cpu_freq()
print(f"[+] Max Frequency : {cpu_frequency.max:.2f}Mhz")
print(f"[+] Min Frequency : {cpu_frequency.min:.2f}Mhz")
print(f"[+] Current Frequency : {cpu_frequency.current:.2f}Mhz")
print("\n")
# This will print the usage of CPU per core
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"[+] CPU Usage of Core {i} : {percentage}%")
print(f"[+] Total CPU Usage : {psutil.cpu_percent()}%")

# importing the requred modules
import psutil

# writing a function to convert bytes to GigaByte
def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb

# Using the virtual_memory() function it will return a tuple
virtual_memory = psutil.virtual_memory()

#This will print the primary memory details
print("[+] Total Memory present :", bytes_to_GB(virtual_memory.total), "Gb")
print("[+] Total Memory Available :", bytes_to_GB(virtual_memory.available), "Gb")
print("[+] Total Memory Used :", bytes_to_GB(virtual_memory.used), "Gb")
print("[+] Percentage Used :", virtual_memory.percent, "%")
print("\n")

# This will print the swap memory details if available
swap = psutil.swap_memory()
print(f"[+] Total swap memory :{bytes_to_GB(swap.total)}")
print(f"[+] Free swap memory : {bytes_to_GB(swap.free)}")
print(f"[+] Used swap memory : {bytes_to_GB(swap.used)}")
print(f"[+] Percentage Used: {swap.percent}%")
