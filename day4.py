import sys
import numpy as np

def main():
    file = open('input4.txt', 'r')

    input = file.readline().strip().split(',')

    boards = []
    temp = []
    file.readline()

    for line in file:
        if line == '\n':
            boards.append(temp)
            temp = []
        else:
            temp.append(line.split())
    boards.append(temp)

    for i, _ in enumerate(input):
        for board in boards:
            checkBoard(board, input[:i+1])


def checkBoard(board, subinput):
    columns = np.array(board).T.tolist()
    for row in board:
        if all(a in subinput for a in row):
            calculateScore(board, subinput, 1)
            exit(0)
    for column in columns:
        if all(a in subinput for a in column):
            calculateScore(board, subinput, 1)
            exit(0)

def calculateScore(board, subinput, part):
    flatboard = [j for sub in board for j in sub]
    for element in subinput:
        if element in flatboard:
            flatboard.remove(element)

    summed = sum(list(map(int, flatboard)))
    lastCalled = int(subinput[len(subinput)-1])

    score = summed * lastCalled

    print("Part " + str(part) + ": " + str(score))
    
    

if __name__ == "__main__":
    main()
