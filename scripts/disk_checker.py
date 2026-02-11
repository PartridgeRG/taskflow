import shutil

total, used, free = shutil.disk_usage('/')

total_GB = total / (1024**3)
used_GB = used / (1024**3)
free_GB = free / (1024**3)

print("Disk Usage Report for /") 
print("---------------------")
print("Total: ", round(total_GB, 2), "GB")
print("Used: ", round(used_GB, 2), "GB")
print("Free: ", round(free_GB, 2), "GB")

usage = (used / total) 

print(f"Usage: {usage:.2%}")

if (usage > 80):
    print("WARNING: Disk usage exceeds 80%")
else:
    print("Status: OK")