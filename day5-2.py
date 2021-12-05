import sys

def main():
    file = open('input5.txt', 'r')

    grid = [[0 for i in range(1000)] for j in range(1000)]

    for line in file:
        start, finish = line.strip().split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = finish.split(',')

        x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)

        if x1 == x2:
            n = abs(y1-y2)
            
            for y in range(n+1):
                grid[x1][y + min(y1,y2)] += 1

        elif y1 == y2:
            n = abs(x1-x2)

            for x in range(n+1):
                grid[x + min(x1,x2)][y1] += 1
        
        else:
            n = abs(x1-x2) # same as abs(y1-y2)

            for i in range(n+1):
                if (x1-x2) < 0 and (y1-y2) < 0:
                    grid[i + x1][i + y1] += 1
                elif (x1-x2) < 0 and (y1-y2) > 0:
                    grid[i + x1][y1 - i] += 1
                elif (x1-x2) > 0 and (y1-y2) < 0:
                    grid[x1 - i][i + y1] += 1
                else:
                    grid[x1 - i][y1 - i] += 1

    count = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] >= 2:
                count += 1

    print("Part 2: " + str(count))




if __name__ == "__main__":
    main()
