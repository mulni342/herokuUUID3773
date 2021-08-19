import psutil
import time 


while True:
  print(psutil.cpu_percent())
  print(psutil.virtual_memory())  # physical memory usage
  print('memory % used:', psutil.virtual_memory()[2])
  time.sleep(3)
