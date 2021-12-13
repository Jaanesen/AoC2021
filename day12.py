import sys

def main():
    file = open('input12.txt', 'r')

    paths = []
    smallcaps = []

    for line in file:
        line = line.strip()
        a, b = line.split('-')
        paths.append([a, b])
        paths.append([b, a])

        if a.islower() and a != 'start' and a != 'end' and a not in smallcaps:
            smallcaps.append(a)
        if b.islower() and b!= 'start' and b!= 'end' and b not in smallcaps:
            smallcaps.append(b)

    results = []

    def smallCaves(path: list):
        for cave in smallcaps:
            if path.count(cave) > 1:
                return False

        return True

    def search(current, path: list):
        if current == 'end':
            results.append(path)
        elif smallCaves(path):
                for n in paths:
                    newpath = []
                    if n[0] == current and n[1] != 'start':
                        newpath = path.copy()
                        newpath.append(n[1])
                        search(n[1], newpath)

    search('start', ['start'])

    print("Part 1: " + str(len(results)))

    results2 = []

    def smallCaves2(path: list):
        f = False
        for cave in smallcaps:
            if path.count(cave) > 2:
                return False
            elif path.count(cave) == 2 and f == False:
                f = True
            elif path.count(cave) == 2 and f == True:
                return False

        return True

    def search2(current, path: list):
        if current == 'end':
            results2.append(path)
        elif smallCaves2(path):
            for n in paths:
                newpath = []
                if n[0] == current and n[1] != 'start':
                    newpath = path.copy()
                    newpath.append(n[1])
                    search2(n[1], newpath)

    search2('start', ['start'])

    print("Part 2: " + str(len(results2)))
    


if __name__ == "__main__":
    main()
