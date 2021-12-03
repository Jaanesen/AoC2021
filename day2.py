import sys

def main():
    file = open('input2.txt', 'r')

    position = 0
    depth = 0

    for line in file:
        action, n = line.split(' ')
        if action == "forward":
            position += int(n)
        elif action == "down":
            depth += int(n)
        elif action == "up":
            depth -= int(n)

    print("Part 1: " + str(position * depth))

    file = open('input2.txt', 'r')

    position = 0
    depth = 0
    aim = 0

    for line in file:
        action, n = line.split(' ')
        if action == "forward":
            position += int(n)
            depth += aim * int(n)
        elif action == "down":
            aim += int(n)
        elif action == "up":
            aim -= int(n)

    print("Part 2: " + str(position * depth))


if __name__ == "__main__":
    main()
