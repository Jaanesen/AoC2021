import sys

def main():
    file = open('input6.txt', 'r')

    fishes = []
    for line in file:
        fishes = list(map(int, line.strip().split(',')))

    for i in range(80):
        fishes[:] = [fish - 1 for fish in fishes]
        fishes += [8] * fishes.count(-1)
        fishes[:] = [x if x != -1 else 6 for x in fishes]
    
    print("Part 1: " + str(len(fishes)))

    file = open('input6.txt', 'r')

    fishes = []
    for line in file:
        fishes = list(map(int, line.strip().split(',')))

    fishreg = [0] * 9

    for i in range(9):
        fishreg[i] = fishes.count(i)
    for _ in range(256):
        evofish = fishreg[0]
        for i in range(0,8): fishreg[i] = fishreg[i+1]
        fishreg[6] += evofish
        fishreg[8] = evofish
    
    print("Part 2: " + str(sum(fishreg)))


if __name__ == "__main__":
    main()
