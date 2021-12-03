import sys

def main():
    # Part 1
    file = open('input1.txt', 'r')

    numbers = []

    for line in file:
        numbers.append(int(line))

    prev = 0
    count = -1

    for num in numbers:
        if int(num) > int(prev):
            count += 1
        prev = num

    print("Part 1: " + str(count))

    # Part 2
    prev = 0
    count = -1

    for i, n in enumerate(numbers):
        if i < len(numbers)-2:
            if (numbers[i] + numbers[i+1] + numbers[i+2]) > prev:
                count += 1
            prev = (numbers[i] + numbers[i+1] + numbers[i+2])
    
    print("Part 2: " + str(count))

if __name__ == "__main__":
    main()
