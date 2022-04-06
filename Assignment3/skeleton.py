#Author - Opeyemi Adesina
#Institution - University of the Fraser Valley
#Academic Session - Winter, 2021

import xlrd #importing excel sheet processing module
import json #importing json processing and generating module


#------------------------------UTILITY FUNCTIONS-----------------------------# 

#Generates an excel sheet for processing
def generateSheet( fileName, extension, sheetNum ) :

  #composing a fully-qualified file name
  fileName = str( fileName ) + str('.') + str( extension )

  try: #error handling
    book = xlrd.open_workbook( fileName ) #opening the excel sheet
  except:
    print (f"G---File Not Found!!! {fileName}") #user-readable output
    quit() #program terminates gracefully
        
  try: #error handling
    sheet = book.sheet_by_index( sheetNum ) #refering to the specified sheet     
  except:
    print("Sheet Not Found!!!") #user-readable output
    quit() #program terminates gracefully

  return sheet

#Extracts header from the file
def generateHeader( sheet, rowIndex ) :

  header = [] #header list initialized to empty
  for label in range( sheet.ncols ) :
    header.append( sheet.col(label)[rowIndex].value )

  return header

#builds the frame to be executed as code
def generateFrame( sheetIndex, header ) :

  i = 0
  temp = '{ '
  while ( i < len( header ) - 1 ) :
    temp = str(temp) + str('"') + header[i] + str('": ') + str('sheetIndex.row(row)[') + str(i) + str('].value, \n')
    i += 1

  temp = str(temp) + str('"') + header[i] + str('": ') + str('sheetIndex.row(row)[') + str(i) + str('].value }')

  return temp

#takes in filename, its extension and sheet id of interest
def fileParser( sheetIndex, key, header, startRowIndex ):
  
  #store = []  #List of objects to be parsed into json file
  framenames = []
  store = []
  frameString = generateFrame( sheetIndex, header )
  for row in range( startRowIndex, sheetIndex.nrows ):
    if sheetIndex.row(row)[key].value not in framenames:

      try: #error handling
        framenames.append(sheetIndex.row(row)[key].value)
        frame = eval( frameString ) #converts generated frame string to code
      except:
        print("Row Not Found!!!") #user-readable output
        quit() #program terminates gracefully
            
      #print(store)
      store.append(frame)
    
  return store

#-------------------------------------END----------------------------------#


#JSON Generator -- takes in an excel file (*.xls or *.xslx -- not *.csv) 
#fileName - name of the file (e.g., 'salaries')
#extension - extension of the file (e.g., '.xls' or 'xslx')
#sheetNum - 0  (for the first sheet)
#primaryKey - 0 (in our case 'S/N')
#headerRowIndex - 0 (this row in the file contains the names of the fields)
#dataStartRowIndex - 1 (the row index that begins the data)
def generateJSON( fileName,  extension, sheetNum, primaryKey, headerRowIndex, dataStartRowIndex ) :
  
  sheet = generateSheet( fileName, extension, sheetNum )
  header = generateHeader( sheet, headerRowIndex )
  store = fileParser( sheet, primaryKey, header, dataStartRowIndex )
  fileName = str(fileName) + str('.json') #composing a fully-qualified file name
  
  try: #error handling
      f = open( fileName, 'w')
  except:
      print("File Not Found!!!") #user-readable output
      quit() #program terminates gracefully
  out = json.dumps(store, indent = 2)
  try:
    f.write( out )
    print("JSON File Successfully Generated!!!")
  except:
    print("JSON File Not Successfully Generated!!!")

#Processes the JSON file and generates a list of gross incomes
def extractGrossIncomes ( fileName, extension ) :
  
  grossIncomeList = []
  fileName = str(fileName) + str('.') + str(extension) #composing a fully-qualified file name
  
  try: #error handling
    with open(fileName, 'r') as employeesFile:
      employeesDictionary = json.load( employeesFile )
  except:
    print("File Not Found!!!") #user-readable output
    quit() #program terminates gracefully

  #creating the list of gross incomes from employees' dictionary produced from JSON
  for employee in employeesDictionary:
    grossIncomeList.append( float( format( employee['Gross Income CAD($)'] , '.2f' ) ) )

  return grossIncomeList


#Processes the JSON file and generates a list of gross incomes
def extractEmployeeInfo (fileName, extension ) :
  
  employeeDictionary = {}
  fileName = str(fileName) + str('.') + str(extension) #composing a fully-qualified file name
  
  try: #error handling
    with open(fileName, 'r') as employeesFile:
      employeesDictionary = json.load( employeesFile )
  except:
      print("File Not Found!!!") #user-readable output
      quit() #program terminates gracefully

  #creating the list of gross incomes from employees' dictionary produced from JSON
  for employee in employeesDictionary:
    sn = employee['S/N']
    name = employee['Full Name - First Name, Last Name']
    grossIncome = float( format( employee['Gross Income CAD($)'] , '.2f' ) )
    sex = employee['Sex']
    dob = employee['Date of Birth']
    maritalStatus = employee['Marital Status']
    employeeDictionary[sn] = [name, grossIncome, dob, sex, maritalStatus]

  return employeeDictionary