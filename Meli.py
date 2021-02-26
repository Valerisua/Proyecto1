# importar lo módulo platform

import platform

# Muestra la aqruitectura del SO
print("[+] Architecture :", platform.architecture()[0])

#Visualización de la maquina virtual
print("[+] Machine :", platform.machine())

# Muestra la versión de SO
print("[+] Operating System Release :", platform.release())

# Muestra el nombre del SO que se esta usando
print("[+] System Name :",platform.system())

# Mostrará la versión del SO
print("[+] Operating System Version :", platform.version())

# Imprimirá o mostrará el hostname
print("[+] Node: " + platform.node())

# Mostrará la plataforma de sitema
print("[+] Platform :", platform.platform())

# Mostrará la info del procesador
print("[+] Processor :",platform.processor())

from datetime import datetime
import psutil

# Se usa la librería psutil para obtener la info de arranque
boot_time = datetime.fromtimestamp(psutil.boot_time())
print("[+] System Boot Time :", boot_time)

# Mostrará el tiempo de uso del sistema
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

# Importa los paquetes psutil
import psutil

# Mostrará el número de núcleos del CPU 
print("[+] Number of Physical cores :", psutil.cpu_count(logical=False))
print("[+] Number of Total cores :", psutil.cpu_count(logical=True))
print("\n")
#  Esto imprimirá la frecuencia de CPU máxima, mínima y actual
cpu_frequency = psutil.cpu_freq()
print(f"[+] Max Frequency : {cpu_frequency.max:.2f}Mhz")
print(f"[+] Min Frequency : {cpu_frequency.min:.2f}Mhz")
print(f"[+] Current Frequency : {cpu_frequency.current:.2f}Mhz")
print("\n")
# Motrará el uso de CPU por núcleo
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"[+] CPU Usage of Core {i} : {percentage}%")
print(f"[+] Total CPU Usage : {psutil.cpu_percent()}%")

# importando los módulos
import psutil

# Función de conversión de bytes a Gb
def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb

# Toma la información del módulo psutil la memoria virtual
virtual_memory = psutil.virtual_memory()

# Mostrará los detalles de la memoria primaria
print("[+] Total Memory present :", bytes_to_GB(virtual_memory.total), "Gb")
print("[+] Total Memory Available :", bytes_to_GB(virtual_memory.available), "Gb")
print("[+] Total Memory Used :", bytes_to_GB(virtual_memory.used), "Gb")
print("[+] Percentage Used :", virtual_memory.percent, "%")
print("\n")

# Mostrará la memoria de apoyo si aplica
swap = psutil.swap_memory()
print(f"[+] Total swap memory :{bytes_to_GB(swap.total)}")
print(f"[+] Free swap memory : {bytes_to_GB(swap.free)}")
print(f"[+] Used swap memory : {bytes_to_GB(swap.used)}")
print(f"[+] Percentage Used: {swap.percent}%")

# Mostrará los usuarios que  se crearon y quienes tienen sesión iniciada
import pwd

users = pwd.getpwall()
for user in users:
    print(user.pw_name, user.pw_shell)
    
import subprocess
from subprocess import Popen, PIPE, STDOUT

who = Popen(['who'],stdin=PIPE, stdout=PIPE, stderr=STDOUT)
print who.stdout.read()

#Exporta todo a un .csv
df.to_csv("infosystem.csv")

