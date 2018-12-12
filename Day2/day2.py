import time
import collections


def readFile(inputFile):
    with open(inputFile, "r") as f:
        lines = f.readlines()
    return lines


def functionB():
    start = time.clock()
    wordsList = readFile("input.txt")
    word_lenght = len(wordsList[0])-1
    for y in wordsList:
        wordsList.pop(0)
        for z in wordsList:
            diffCounter = 0
            for x in range(0, word_lenght):
                if y[x] != z[x]:
                    diffCounter += 1
                    differencePosition = x
                if diffCounter > 1:
                    differencePosition == 0
                    break
            if diffCounter == 1:
                common_chars = list(y)
                common_chars.pop(differencePosition)

    return ''.join(common_chars).rstrip("\n"), time.clock() - start


def functionA():
    start = time.clock()
    doubles = triples = 0
    for x in readFile("input.txt"):
        tempDouble = tempTriple = 0
        for key, value in collections.Counter(x.strip()).items():
            if value == 2:
                tempDouble += 1
            elif value == 3:
                tempTriple += 1
        if tempDouble > 0:
            doubles += 1
        if tempTriple > 0:
            triples += 1
    return doubles*triples, time.clock() - start


if __name__ == '__main__':
    resultA, timeA = functionA()
    print("Checksum: {}. Completed in {}.".format(resultA, timeA))
    resultB, timeB = functionB()
    print("Common chars between two similar (1 difference) strings: {}. Completed in {}.".format(resultB, timeB))
