import sys

def main():
    file = open('input14.txt', 'r')

    input = file.readline().strip()
    pairs = {}
    charcount = {}
    paircount = {}

    file.readline()

    for line in file:
        pair, insert = line.strip().split(' -> ')
        pairs[pair] = insert
        paircount[pair] = 0
        if insert not in charcount:
            charcount[insert] = 0
    
    for char in input:
        charcount[char] = input.count(char)

    for i in range(len(input)-1):
        j = i+2
        if input[i:j] not in paircount:
            paircount[input[i:j]] = 1
        else:
            paircount[input[i:j]] += 1


    for _ in range(40):
        temppaircount = paircount.copy()
        for key in paircount:
            if paircount[key] > 0:
                charcount[pairs[key]] += paircount[key]
                temppaircount[key] -= paircount[key]
                temppaircount[key[0] + pairs[key]] += paircount[key]
                temppaircount[pairs[key] + key[1]] += paircount[key]
                paircount[key] -= paircount[key]

        paircount = temppaircount.copy()


    l = []
    for d in charcount:
        l.append(charcount[d])

    print("Part 2: " + str(max(l) - min(l)))

if __name__ == "__main__":
    main()
