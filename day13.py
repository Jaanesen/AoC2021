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

    dir, val = splits[0][0], splits[0][1]

    val = int(val)
    
    newlist=[]

    for dot in dots:
        x, y = dot.split(',')
        if int(x) > val:
            newlist.append(str(val-(int(x)-val))+ "," + y)
        else:
            newlist.append(x + "," + y)

    print(dots),
    newset = set(newlist)

    print(newset)
    dots = list(dots)

    print("Part 1: " + str(len(list(newset))))



if __name__ == "__main__":
    main()
