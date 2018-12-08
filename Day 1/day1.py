def readFile(inputFile):
    try:
        file = open(inputFile, "r")
        inputList = file.read().split("\n")
        file.close()
        return inputList
    except Exception:
        print("Cannot read or access file.")


def functionA():
    currentFrequency = 0
    for x in readFile("input.txt"):
        currentFrequency += int(x)
    print("Current frequency: {}".format(currentFrequency))


if __name__ == '__main__':
    functionA()
