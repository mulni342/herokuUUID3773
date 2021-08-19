from psutil import virtual_memory

mem = virtual_memory()
print(mem.total)



