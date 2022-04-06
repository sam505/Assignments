def flipItems(dictionary):
    lstNumbers = list()
    for key, value in dictionary.items():
        nTuple = (value, key)
        lstNumbers.append(nTuple)
    return lstNumbers


def sortAndPrint(lstNumbers):
    lstNumbers = sorted(lstNumbers, reverse=True)
    for tuple in lstNumbers:
        print(f"{tuple[1]} -> {tuple[0]}")


# converts the given file to a dictionary of unique values and
def countNumbers(fileName):

    # INSERT YOUR CODE HERE
    dict_numbers = {}
    with open(fileName) as file:
        for line in file:
            for number in line.strip():  # loop through the lines of the file and also remove leading and trailing
                # whitespaces
                try:  # check whether th dictionary has a similar key
                    dict_numbers[number] += 1  # increment the counter for the unique number in the dictionary
                except KeyError:  # if key not in dictionary keys set the value of that key to 1
                    dict_numbers[number] = 1
    return dict_numbers  # return the dictionary


fileName = "numbers.txt"
dictionary = countNumbers(fileName)
lstNumbers = flipItems(dictionary)
sortAndPrint(lstNumbers)
