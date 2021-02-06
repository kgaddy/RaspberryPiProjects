import os,signal
from blinkt import clear,set_brightness, set_pixel, show,set_all
from time import sleep

hostlist = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5", "192.168.1.6", "192.168.1.7", "8.8.8.8"]
hostid = ["Device1", "Device2", "Device3", "Device4", "Device5", "Device6", "Device7", "Device8"]

clear()
set_brightness(0.05)
set_all(0,0,255)
show()
sleep(5)

def handler(signum, frame):
   clear()
   show()
   exit(0)

signal.signal(signal.SIGTERM, handler)

while True:
   for hostnum, hostname in enumerate(hostlist):
      response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
      if response == 0:
         set_pixel(hostnum, 0, 0, 255)
      else:
          set_pixel(hostnum, 255, 0, 0)
   show()
   sleep(60)
