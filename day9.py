import sys

def main():
    file = open('input9.txt', 'r')

    heightmap = []

    for line in file:
        temp = []
        for char in line.strip():
            temp.append(char)
        heightmap.append(temp)

    count = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if i == 0 and j == 0:
                if heightmap[i][j] < heightmap[i+1][j] and heightmap[i][j] < heightmap[i][j+1]:
                    count += (int(heightmap[i][j]) + 1)
            elif i == 0:
                if heightmap[i][j] < heightmap[i+1][j] and heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i][j+1]:
                    count += (int(heightmap[i][j]) + 1)
            elif j == 0:
                if heightmap[i][j] < heightmap[i][j+1] and heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j]:
                    count += (int(heightmap[i][j]) + 1)
            elif i == len(heightmap)-1:
                if heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i][j+1]:
                    count += (int(heightmap[i][j]) + 1)
            elif j == len(heightmap[0])-1:
                if heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j]:
                    count += (int(heightmap[i][j]) + 1)
            elif i == len(heightmap)-1 and j == len(heightmap[0])-1:
                if heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i][j-1]:
                    count += (int(heightmap[i][j]) + 1)
            elif heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j] and heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i][j+1]:
                count += (int(heightmap[i][j]) + 1)

    print("Part 1: " + str(count))


if __name__ == "__main__":
    main()
