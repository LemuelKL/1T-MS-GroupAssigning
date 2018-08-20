import pandas as pd 
import xlrd as xl 
from pandas import ExcelWriter
from pandas import ExcelFile
import os.path

class student():
    def __init__(self, pyccode, name, hkid):
        self.pyccode = pyccode
        self.name = name
        self.hkid = hkid

schoolYear = '1819'
nColumns = 3

errStr = []
def logErr(err):
    errStr.append(err)

fileDir = 'data/'
filename_AllSchools = fileDir + 'students.xlsx'

def getNumberOfSchools():
    DataF = pd.read_excel(filename_AllSchools, sheet_name = 'Sheet1')
    return len(DataF.index) 

def getSchoolNamesFromExcel():
    DataF = pd.read_excel(filename_AllSchools, sheet_name = 'Sheet1')
    retList = DataF['School Name']
    return retList

def retrieveSchoolDataFromExcel(schoolName):
    fileName = fileDir + schoolName + '.xlsx'
    DataF = pd.read_excel(fileName, sheet_name = schoolYear)
    return [DataF['pyccode'], DataF['Full English Name'], DataF['HKID']]

def extractStudents():
    studentObjsToRet = []
    listOfSchoolNames = getSchoolNamesFromExcel()
    for name in listOfSchoolNames:
        schoolData = retrieveSchoolDataFromExcel(name)
        nStudent = len(schoolData[0])
        for n in range (0, nStudent):
            s = student(schoolData[0][n], schoolData[1][n], schoolData[2][n])
            studentObjsToRet.append(s)

    return studentObjsToRet










    
