import sys

def main():
    file = open('input11.txt', 'r')

    octo = []
    octo2 = []

    for line in file:
        list1=[]
        list1[:0]=line.strip()
        list1 = [int(i) for i in list1]
        octo.append(list1)
        octo2.append(list1)

    count = 0

    for _ in range(100):

        for x, row in enumerate(octo):
            for y, _ in enumerate(row):
                octo[x][y] += 1

        while checkFlash(octo):
            for x, row in enumerate(octo):
                for y, elem in enumerate(row):
                    if elem > 9:
                        octo[x][y] = 0
                        octo = incAdj(x, y, octo)
                        count += 1

    print("Part 1: " + str(count))

    step = 0

    while not all(element == octo2[0] for element in octo2):
        step += 1

        for x, row in enumerate(octo2):
            for y, _ in enumerate(row):
                octo2[x][y] += 1

        while checkFlash(octo2):
            for x, row in enumerate(octo2):
                for y, elem in enumerate(row):
                    if elem > 9:
                        octo2[x][y] = 0
                        octo2 = incAdj(x, y, octo2)
                        count += 1

    print("Part 2: " + str(step))


def incAdj(x, y, octo):
    i = j = [-1, 0, 1]

    for n in i:
        for m in j:
            if not (n == 0 and m == 0) and n+x >= 0 and n+x < 10 and m+y >= 0 and m+y < 10 and octo[x+n][y+m] != 0:
                octo[x+n][y+m] += 1
    return octo

def checkFlash(octo):
    for x, row in enumerate(octo):
        for y, _ in enumerate(row):
            if octo[x][y] > 9:
                return True
    return False


if __name__ == "__main__":
    main()
