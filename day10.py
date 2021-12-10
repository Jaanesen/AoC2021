import sys
from typing import List

def main():
    file = open('input10.txt', 'r')

    corrupts = []
    incompletes = []

    for line in file:
        stack = []
        line = line.strip()
        corruptedStack = False
        for char in line:
            if isOpen(char):
                stack.append(char)
            else:
                if isClose(char, stack[-1]):
                    stack.pop()
                else:
                    corrupts.append(char)
                    corruptedStack = True
                    break
        if not corruptedStack:
            incompletes.append(stack)
            

    print("Part 1: " + str(getScore(corrupts)))

    incompleteScored = []

    for n in incompletes:
        incompleteScored.append(getIncompleteScore(n))

    incompleteScored.sort()
    middle = (len(incompleteScored) - 1)/2

    print("Part 2: " + str(incompleteScored[int(middle)]))

def getIncompleteScore(n: List):
    n.reverse()
    score = 0
    for i in n:
        score = score * 5
        if i == '(':
            score += 1
        elif i == '[':
            score += 2
        elif i == '{':
            score += 3
        elif i == '<':
            score += 4
    return score

def getScore(list):
    return 3 * list.count(')') + 57 * list.count(']') + 1197 * list.count('}') + 25137 * list.count('>')


def isClose(close, open):
    if close == '>' and open == '<':
        return True
    elif close == ')' and open == '(':
        return True
    elif close == '}' and open == '{':
        return True
    elif close == ']' and open == '[':
        return True
    else: return False

def isOpen(char):
    if char == '<' or char == '(' or char == '{' or char == '[':
        return True
    else: return False


if __name__ == "__main__":
    main()
