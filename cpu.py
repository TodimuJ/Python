import psutil

#Core Information
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

#Frequency Information
frequency = psutil.cpu_freq()
print(f"Max frequency: {frequency.max: .2f}MHz")
print(f"Min frequency: {frequency.min: .2f}MHz")
print(f"Current frequency: {frequency.current: .2f}MHz")

#CPU Information
print("CPU usage per core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i} {percentage}%")
print(f"Total CPU usage: {psutil.cpu_percent()}%")