# insert import statements here...
from statistics import mean
from statistics import pstdev


def extractSalary(fileName):
    """
    Loops through the lines in the csv file and extract the salary values and appends to the salaries list

    :param
        fileName: string representing the location of the csv file
    :return:
        salaries: a list with all th salary values
    """
    #########################
    # INSERT YOUR CODE HERE #
    #########################
    salaries = []
    with open(fileName) as file:  # open the file and close after execution
        next(file)  # skip the first line in the csv file
        for line in file:  # loop through the lines in the csv file
            data = line.strip().split(",")  # remove leading and trailing whitespaces and split using ","
            value = (data[3] + data[4]).replace("$", "")  # extract values at index 3 and 4 and remove the dollar sign
            float_value = float(value.replace('"', ""))  # remove the quotation marks
            salaries.append(float_value)  # append the value as floats to the salaries list
    return salaries  # return salaries list


list = extractSalary("salaries.csv")  # extractSalary(...) function is invoked here
mean = format(mean(list), '.2f')  # computes and rounds the population mean to 2dp
sdev = format(pstdev(list), '.2f')  # computes and rounds the population standard deviation to 2dp
print("Mean of salaries is: CAD($) %s and the population standard deviation is: CAD($) %s" % (mean, sdev))

############ - If your code is correct, your ouput to the screen should be as follows
# Mean of salaries is: CAD($) 123099.00 and the population standard deviation is: CAD($) 61555.71
