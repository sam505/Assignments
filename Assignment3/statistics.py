from math import sqrt


# function computes mean or average of a set of numbers
def mean(inputList):  # Step 3
    if len(inputList) != 0:
        return sum(inputList) / len(inputList)
    else:
        return 0


# function computes the standard deviation of a set of numbers
def standardDeviation(inputList):  # Step 4
    if len(inputList) != 0:
        average = mean(inputList)
        std_dev = (sum((x - average) ** 2 for x in inputList) / len(inputList)) ** 0.5
        return std_dev
    else:
        return 0


def normalize(inputList):
    normalizedList = []
    average = mean(inputList)
    stdev = standardDeviation(inputList)
    for val in inputList:
        if stdev == 0:
            normalizedList.append(1)
        else:
            normalizedList.append((val - average) / stdev)
    return normalizedList


# function computes medians of a set of numbers
def median(inputList):
    new_List = sorted(inputList)
    list_len = len(new_List)
    if list_len % 2 != 0:
        return new_List[list_len // 2]
    else:
        return (new_List[list_len // 2] + new_List[(list_len // 2) - 1]) / 2


# Modes computations for a set of items in a list
def computeModes(inputList):
    modes = []
    frequencies = {}
    for number in inputList:
        if number in frequencies.keys():
            frequencies[number] += 1
        else:
            frequencies[number] = 1
    max_freq = max(frequencies.values())
    for key in frequencies.keys():
        if frequencies[key] == max_freq:
            modes.append(key)
    return modes
