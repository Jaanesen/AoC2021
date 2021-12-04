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

    lastbingoboard = []
    lastinput = []

    for i, _ in enumerate(input):
        for board in boards:
            columns = np.array(board).T.tolist() + board
            for row in columns:
                if all(a in input[:i+1] for a in row):
                    lastbingoboard= board
                    lastinput = input[:i+1]
                    boards.remove(board)
                    break

    print(lastinput)
    print(lastbingoboard)
    calculateScore(lastbingoboard, lastinput, 2)

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
