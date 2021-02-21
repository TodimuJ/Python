import statistics as stat

times = []

def main():
    f = open("./initial-serial-times.dat", "r")

    for x in f:
        times.append(float(x))

    for i in range(0, len(times)):
        if i == 2 or i == 4 or i == 9 or i == 99 or i == 999:
            print(stat.mean(times[:i+1]), stat.stdev(times[:i+1]))

if __name__ == "__main__":
    main()

