import sys

def main():
    file = open('input9.txt', 'r')

    heightmap = []

    for line in file:
        temp = []
        for char in line.strip():
            temp.append(char)
        heightmap.append(temp)

    lowpoints = []

    count = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if i == 0 and j == 0:
                if heightmap[i][j] < heightmap[i+1][j] and heightmap[i][j] < heightmap[i][j+1]:
                    count += (int(heightmap[i][j]) + 1)
                    lowpoints.append(str(i)+','+str(j))
            elif i == 0:
                if heightmap[i][j] < heightmap[i+1][j] and heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i][j+1]:
                    count += (int(heightmap[i][j]) + 1)
                    lowpoints.append(str(i)+','+str(j))
            elif j == 0:
                if heightmap[i][j] < heightmap[i][j+1] and heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j]:
                    count += (int(heightmap[i][j]) + 1)
                    lowpoints.append(str(i)+','+str(j))
            elif i == len(heightmap)-1:
                if heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i][j+1]:
                    count += (int(heightmap[i][j]) + 1)
                    lowpoints.append(str(i)+','+str(j))
            elif j == len(heightmap[0])-1:
                if heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j]:
                    count += (int(heightmap[i][j]) + 1)
                    lowpoints.append(str(i)+','+str(j))
            elif i == len(heightmap)-1 and j == len(heightmap[0])-1:
                if heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i][j-1]:
                    count += (int(heightmap[i][j]) + 1)
                    lowpoints.append(str(i)+','+str(j))
            elif heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j] and heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j] < heightmap[i][j+1]:
                count += (int(heightmap[i][j]) + 1)
                lowpoints.append(str(i)+','+str(j))

    print("Part 1: " + str(count))


    lister = [''] * len(lowpoints)

    def searchAdj(x: int, y: int, heightmap, index):
        i = j = [-1, 0, 1]

        for n in i:
            for m in j:
                if not (abs(n) == abs(m)) and (n+x >= 0) and (n+x < len(heightmap)) and (m+y >= 0) and (m+y < len(heightmap)) and (int(heightmap[x+n][y+m]) != 9 ):
                    if heightmap[x+n][y+m] > heightmap[x][y] and ((str(x+n)+","+str(y+m)) not in lister[index]):
                        lister[index].append(str(x+n)+","+str(y+m))
                        searchAdj(x+n,y+m, heightmap, index)
                        

    for i, point in enumerate(lowpoints):
        x, y = point.split(',')
        x,y = int(x), int(y)
        lister[i] = [point]
        searchAdj(x,y, heightmap, i)

    lister = list(sorted(lister, key=len))

    print("Part 2: " + str(len(lister[len(lister)-1]) * len(lister[len(lister)-2]) * len(lister[len(lister)-3])))

if __name__ == "__main__":
    main()
