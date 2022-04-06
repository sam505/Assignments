#Author: Opeyemi Adesina
#Institution: University of the Fraser Valley

from skeleton import generateJSON, extractEmployeeInfo, extractGrossIncomes
from taxUtilities import computeNetIncomes
from statistics import mean, standardDeviation, median, computeModes
from time import time
from qualityAssurance import gradeAssignment


#defines the entry point logic of the entire program
def _main_() :

    fileName = './data/salaries'
    extension = 'xls'

    #generating the JSON equaivalent of the excel sheet
    generateJSON( fileName,  extension, 0, 0, 0, 1 )
    grossIncomeList = extractGrossIncomes ( fileName, 'json' )

    netIncomeList = computeNetIncomes( grossIncomeList )
    averageGrossIncomes = mean( grossIncomeList )
    averageNetIncomes = mean( netIncomeList )

    print( "\n************* Required Information ************* \n" ) 
    print( f"Average gross-income for employees: ${format( averageGrossIncomes, ',.2f' )} (CAD)" )
    print( f"Average net-income for employees: ${format( averageNetIncomes, ',.2f' )} (CAD)" )
    print( f"Average of all modes for employees: ${format( mean( computeModes( netIncomeList ) ), ',.2f' )} (CAD)" )
    print( f"Population variance for employees: ${format( standardDeviation( netIncomeList ) ** 2, ',.2f' )} (CAD)" )
    print( f"Median for employees: ${format( median( netIncomeList ), ',.2f' )} (CAD)" )
    
    #invokes assignment grader operation
    gradeAssignment()
  
#setting up a time watcher to monitor execution time
start = time()
#invoking the main function
_main_()
print(f"Time taken for execution: {format(time() - start, '.2f')} seconds.")