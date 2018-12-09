import time


def readFile(inputFile):
    with open(inputFile, "r") as f:
        lines = f.readlines()
    return lines


def functionA():
    start = time.clock()
    currentFrequency = 0
    for x in readFile("input.txt"):
        currentFrequency += int(x)
    return currentFrequency, time.clock() - start


def functionB():
    start = time.clock()
    currentFrequency = 0
    pastFrequency = []
    frequencyChanges = readFile("input.txt")
    while True:
        for x in frequencyChanges:
            currentFrequency += int(x)
            if currentFrequency in pastFrequency:
                return currentFrequency, time.clock() - start
            else:
                pastFrequency.append(currentFrequency)


if __name__ == '__main__':
    resultA, timeA = functionA()
    print("Current frequency: {}. Completed in {}.".format(resultA, timeA))
    resultB, timeB = functionB()
    print("First frequency reached twice: {}. Completed in {}.".format(resultB, timeB))
