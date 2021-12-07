import sys

def main():
    file = open('input7.txt', 'r')

    input = []

    for line in file:
        input= list(map(int, line.strip().split(',')))

    fuel = []

    for position in range(1000):
        currentFuel = 0
        for crab in input:
            currentFuel += abs(crab - position)
        fuel.append(currentFuel)

    print("Part 1: " + str(min(fuel)))

    costs = list(range(1,max(input)+1))

    fuel = []

    for position in range(max(input)+1):
        currentFuel = 0
        for crab in input:
            currentFuel += sum(costs[:abs(crab - position)])
        fuel.append(currentFuel)

    print("Part 2: " + str(min(fuel)))




if __name__ == "__main__":
    main()
