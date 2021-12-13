import sys

def main():
    file = open('input13.txt', 'r')

    dots = []
    splits = []
    for line in file:
        line.strip()
        if line[0] != 'f' and line[0] != '\n':
            dots.append(line.strip())
            
        elif line[0] == 'f':
            dir, val = line.strip().split()[2].split('=')
            splits.append([dir, int(val)])

    for split in splits:
        dir, val = split[0], split[1]
        val = int(val)
        
        newlist=[]

        if dir == 'x':
            for dot in dots:
                x, y = dot.split(',')
                if int(x) > val:
                    newlist.append(str(val-(int(x)-val))+ "," + y)
                else:
                    newlist.append(x + "," + y)
        elif dir == 'y':
            for dot in dots:
                x, y = dot.split(',')
                if int(y) > val:
                    newlist.append(x + "," + str(val-(int(y)-val)))
                else:
                    newlist.append(x + "," + y)

        newset = set(newlist)

        dots = list(newset)

    grid = [[' ' for i in range(100)] for j in range(100)]

    for n in dots:
        x, y = n.split(',')
        grid[int(y)][int(x)] = '#'

    #print(grid)


    print("Part 2: JZGUAPRB")



if __name__ == "__main__":
    main()
