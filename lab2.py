import statistics as stat
from tabulate import tabulate

times, mean, stdev = [], [], []

def main():
    f = open("./initial-serial-times.dat", "r")

    for x in f:
        times.append(float(x))

    for i in range(0, len(times)):
        if i == 2 or i == 4 or i == 9 or i == 99 or i == 999:
            mean.append(stat.mean(times[:i+1]))
            stdev.append(stat.stdev(times[:i+1]))
    
    data = {
            "Average" : [*mean],
            "Standard Deviation": [*stdev]    
            }

    return tabulate(data, headers="keys", tablefmt="github")

if __name__ == "__main__":
    print(main())
















