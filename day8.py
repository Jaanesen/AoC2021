import sys

def main():
    file = open('input8.txt', 'r')
    output = []
    input = []
 
    for line in file:
        x, y = line.split('|')
        input.append(x.strip())
        output.append(y.strip())

    count = 0

    for digits in output:
        temp = digits.split()
        for digit in temp:
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                count += 1

    print("Part1: " + str(count))

    count = 0
    for i, _ in enumerate(input):
        dic = findPattern(input[i])
        digits = ""
        for digit in output[i].split():
            digits += dic[''.join(sorted(digit))]
        count += int(digits)

    print("Part 2: " + str(count))
    
def findPattern(signals):
    slist = signals.split()
    dic = {}
    revdic = {}

"""
Sortere slist på størrelse
sette størrelser riktig, mulig i list da dictionary oppfører seg merkelig
"""



    while(len(slist) > 0):
        for signal in slist:
            if len(signal) == 2:
                dic[''.join(sorted(signal))] = "1"
                revdic["1"] = ''.join(sorted(signal))
                slist.remove(signal)
            elif len(signal) == 3:
                dic[''.join(sorted(signal))] = "7"
                revdic["7"] = ''.join(sorted(signal))
                slist.remove(signal)  
            elif len(signal) == 4:
                dic[''.join(sorted(signal))] = "4"
                revdic["4"] = ''.join(sorted(signal))
                slist.remove(signal)
            elif len(signal) == 7:
                dic[''.join(sorted(signal))] = "8"
                revdic["8"] = ''.join(sorted(signal))
                slist.remove(signal)

        for signal in slist:
            if len(signal) == 5 and all(a in sorted(signal) for a in sorted(revdic["7"])):
                dic[''.join(sorted(signal))] = "3"
                revdic["3"] = ''.join(sorted(signal))
                slist.remove(signal)
            elif len(signal) == 6 and all(a in sorted(signal) for a in sorted(revdic["4"])):
                dic[''.join(sorted(signal))] = "9"
                revdic["9"] = ''.join(sorted(signal))
                slist.remove(signal)

        for signal in slist:
            if len(signal) == 6 and all(a in sorted(signal) for a in sorted(revdic["1"])):
                dic[''.join(sorted(signal))] = "0"
                revdic["0"] = ''.join(sorted(signal))
                slist.remove(signal)

        for signal in slist:
            if len(signal) == 6:
                dic[''.join(sorted(signal))] = "6"
                revdic["6"] = ''.join(sorted(signal))
                slist.remove(signal)

        for signal in slist:
            if len(signal) == 5 and all(a in sorted(revdic["6"]) for a in sorted(signal)):
                dic[''.join(sorted(signal))] = "5"
                revdic["5"] = ''.join(sorted(signal))
                slist.remove(signal)

        for signal in slist:
            if len(signal) == 5:
                dic[''.join(sorted(signal))] = "2"
                revdic["2"] = ''.join(sorted(signal))
                slist.remove(signal)

        print(dic)

    return dic

# [a, cg, ef, cg, , ef, ]

# 1 = [0, 0, 1, 0, 0, 1, 0] 2
# 2 = [1, 0, 1, 1, 1, 0, 1] 5
# 3 = [1, 0, 1, 1, 0, 1, 1] 5
# 4 = [0, 1, 1, 1, 0, 1, 0] 4
# 5 = [1, 1, 0, 1, 0, 1, 1] 5
# 6 = [1, 1, 0, 1, 1, 1, 1] 6
# 7 = [1, 0, 1, 0, 0, 1, 0] 3
# 8 = [1, 1, 1, 1, 1, 1, 1] 7
# 9 = [1, 1, 1, 1, 0, 1, 1] 6
# 0 = [1, 1, 1, 0, 1, 1 ,1] 6

# 1 3 4 6 7 8 9

# 2 5

# 6, 0 og 9 er 6 lange
# 3 er subset av 9
# 2 og 5 har 2 forskjellig
# 3 har hele 1 i seg

# 5 er subset av 6


# [0, 1, 2, 3, 4, 5, 6]

# 1 3 4 7 8 9

# 2 5 6 0

"""
 0000
1    2
1    2
 3333
4    5
4    5
 6666
"""

if __name__ == "__main__":
    main()
