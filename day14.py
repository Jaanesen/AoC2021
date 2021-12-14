import sys

def main():
    file = open('input14.txt', 'r')

    input = file.readline().strip()
    pairs = {}

    file.readline()

    for line in file:
        pair, insert = line.strip().split(' -> ')
        pairs[pair] = insert
    
    for _ in range(10):
        temp = ""
        for i in range(len(input)-1):
            j = i+2
            temp += input[i:i+1]
            if input[i:j] in pairs:
                temp += pairs[input[i:j]]
        temp += input[-1]    
        input = temp

    l = []
    for char in input:
        l.append(input.count(char))
    
    print("Part 1: " + str(max(l) - min(l)))

if __name__ == "__main__":
    main()
