import json
from pprint import pprint
import random

nTeacher = 40
nStudent = 140
nCourse = 40
nSubj = 10

# Weighting Constants
WC_nAvSubj = 10
WC_nConnection = 7

# Example of subj type names
# chinL
# engL
# edu
# engine
# math
# society
# finance
# it
# phy
# medic
subjMaster = ["chinL", "engL", "edu", "engine", "math", "society", "finance", "it", "phy", "medic"]

# Example of course idName
# chinL_1
# engL_1
# edu_1
# edu_2
# math_1
# society_1
# society_2
# society_3

listOfStudentObjs = []
listOfTeacherObjs = []
listOfCrouseObjs = []

class teacher:
    avIndex = None
    nConnection = None
    def __init__(self, idName, avSubjs):
        self.idName = idName
        self.nAvSubj = len(avSubjs)
        self.avSubjs = avSubjs

    def calcAvIndex():
        if not nAvSubj == None or not nConnection == None:
            avIndex = nAvSubj * WC_nAvSubj + nConnection * WC_nConnection
            return 'SUCCESS'

class student:
    avIndex = None
    nConnection = None
    def __init__(self, pyccode, choice1, choice2):
        self.pyccode = pyccode
        self.choice1 = choice1
        self.choice2 = choice2

    def calcAvIndex():
        if not nAvSubj == None or not nConnection == None:
            avIndex = nAvSubj * WC_nAvSubj + nConnection * WC_nConnection
            return 'SUCCESS'

class course:
    max_nStudent = 5
    def __init__(self, subjType, idNumber, nAvTeacher, nAvStudent, nID):
        self.subjType = subjType
        self.idNumber = idNumber
        self.idName = subjType + "_" + str(idNumber)
        self.nAvTeacher = nAvTeacher
        self.nAvStudent = nAvStudent
        self.nID = nID
   
def constructNCoursesBySubjType(subjType, nCourseToConstruct):
    ret = []
    for i in range (0, nCourseToConstruct):
        tempCourse = course(subjType, i+1, None, None, nCourseToConstruct)
        ret.append(tempCourse)
    return ret

def genRandomStudents():
    toRet = []
    pyccodes = ["%03d" % x for x in range(1, nStudent + 1)]
    for x in range (0, nStudent):
        twoPicks = random.sample(subjMaster, 2)
        s = student(pyccodes[x], twoPicks[0], twoPicks[1])
        toRet.append(s)
    return toRet

#TODO	
def readListOfTeachersFromFile():
    with open("data/listOfTeachers.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    return content
	
def genRandomAmountOfRandomSubjects():
    length = random.randint(1, 4)
    picks = random.sample(subjMaster, length)
    toRet = []
    for i in range (0, length):
    	toRet.append(picks[i])
    return toRet
	
def genRandomTeachers():
    toRet = []
    teacherIdNames = readListOfTeachersFromFile()
    for teacherIdName in teacherIdNames:
        avSubjs = genRandomAmountOfRandomSubjects()
        t = teacher(teacherIdName, avSubjs)
        toRet.append(t)
    return toRet

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))
    
def main():
    listOfStudentObjs = genRandomStudents()
    listOfTeacherObjs = genRandomTeachers()
    dump(listOfTeacherObjs[0])
    writeTeacherData2Json('data/teacherInfo.json', listOfTeacherObjs)

def studentObjs2Json(objs):
    outStr = '['
    for obj in objs:
        outStr += '{'
        outStr += '"pyccode":"'
        outStr += obj.pyccode
        outStr += '","choice1":"'
        outStr += obj.choice1
        outStr += '","choice2":"'
        outStr += obj.choice2
        outStr += '"},'
    outStr = outStr[:-1]
    outStr += ']'
    return outStr

def teacherObjs2Json(objs):
    outStr = '['
    for obj in objs:
        outStr += '{'
        outStr += '"idName":"'
        outStr += obj.idName
        outStr += '","nAvSubj":"'
        outStr += str(obj.nAvSubj)
        outStr += '","avSubjs":"'
        outStr += flatten2DSubjs(obj.avSubjs)
        outStr += '"},'
    outStr = outStr[:-1]
    outStr += ']'
    return outStr

def flatten2DSubjs(listOfStrs):
    result = listOfStrs[0]
    print(result)
    for i in range(1, len(listOfStrs)):
        result += ', '
        result += listOfStrs[i]   
    return result

def readJson(filename):
    with open(filename, 'r') as dataIn:
        return json.load(dataIn)

def writeJson(filename, jsonString):
    parsed = json.loads(jsonString)
    with open(filename, 'w') as outfile:
        json.dump(parsed, outfile, indent = 4, sort_keys = False)

def writeStudentData2Json(filename, objs):
    jsonString = teacherObjs2Json(objs)
    writeJson(filename, jsonString)

def writeTeacherData2Json(filename, objs):
    jsonString = teacherObjs2Json(objs)
    writeJson(filename, jsonString)
        
main()
