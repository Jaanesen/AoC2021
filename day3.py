import sys

def main():
    file = open('input3.txt', 'r')

    binaries = []
    binaries2 = []

    for line in file:
        binaries.append((map(int,line.strip())))
        binaries2.append(list((map(int,line.strip()))))

    summed = [ sum(x) for x in zip(*binaries) ]

    gamma = []

    for n in summed:
        if n >= 500:
            gamma.append(1)
        else:
            gamma.append(0)

    episilon = []
    for i in range(len(gamma)):
        episilon.append(gamma[i]^1)

    print("Part 1: " + str(binatodeci(gamma) * binatodeci(episilon)))


    sokesett = binaries2.copy()


    oxygen = algo(0, sokesett, True)

    co2 = algo(0, sokesett, False)

    print("Part 2: " + str(binatodeci(oxygen) * binatodeci(co2)))

# bool: 1 = oxygen, 0 = co2
def algo(i, list, bool):
    if len(list) == 1:
        return list[0]

    onelist = []
    zerolist = []

    for n in list:
        if n[i] == 1:
            onelist.append(n)
        else:
            zerolist.append(n)
    
    if bool:
        if len(onelist) >= len(zerolist):
            return algo(i+1, onelist, bool)
        else:
            return algo(i+1, zerolist, bool)
    else:
        if len(onelist) < len(zerolist):
            return algo(i+1, onelist, bool)
        else:
            return algo(i+1, zerolist, bool)
    
def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

if __name__ == "__main__":
    main()
