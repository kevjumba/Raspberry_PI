import smbus
import time
import subprocess
import os
bus = smbus.SMBus(1)

#DEVICE_ADDRESS = 0x50
#REGISTRY = 0x00

#bit = bus.read_byte_data(DEVICE_ADDRESS, REGISTRY)
#print(bit)
#time.sleep(0.05)
#bit = bus.read_byte_data(DEVICE_ADDRESS, 0x01)
#print(bit)

proc = subprocess.Popen('sudo i2cget -y 1 0x50 0x00', stdout=subprocess.PIPE, shell = True)
tmp = proc.stdout.read()
print(tmp)
