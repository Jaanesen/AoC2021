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
    slist.sort(key=len)
    dic = {}
    revdic = {}

    dic[''.join(sorted(slist[0]))] = "1"
    revdic["1"] = ''.join(sorted(slist[0]))
    slist.remove(slist[0])
    dic[''.join(sorted(slist[0]))] = "7"
    revdic["7"] = ''.join(sorted(slist[0]))
    slist.remove(slist[0])  
    dic[''.join(sorted(slist[0]))] = "4"
    revdic["4"] = ''.join(sorted(slist[0]))
    slist.remove(slist[0])
    dic[''.join(sorted(slist[6]))] = "8"
    revdic["8"] = ''.join(sorted(slist[6]))
    slist.remove(slist[6])

    while len(slist) != 0:

        for signal in slist:
            if len(signal) == 5 and all(a in sorted(signal) for a in sorted(revdic["7"])):
                dic[''.join(sorted(signal))] = "3"
                revdic["3"] = ''.join(sorted(signal))
                slist.remove(signal)
        
        for signal in slist:
            if len(signal) == 6 and all(a in sorted(signal) for a in sorted(revdic["4"])):
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

    return dic

if __name__ == "__main__":
    main()
