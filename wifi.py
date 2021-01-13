import subprocess 
from decouple import config
import os
import sys

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

process = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)

while True:
  line = process.stdout.readline()
  
  if not line:
    break
 
  connected_ip = line.decode('utf-8').split()[3]

  if connected_ip == IP_DEVICE:
      subprocess.Popen(["say", "Someone just connected to the network"])