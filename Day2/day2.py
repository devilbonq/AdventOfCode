import time
import collections


def readFile(inputFile):
    with open(inputFile, "r") as f:
        lines = f.readlines()
    return lines


def functionA():
    start = time.clock()
    inputData = readFile("input.txt")
    doubles = triples = 0
    for x in inputData:
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