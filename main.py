import json
from pprint import pprint
import random

nTeacher = 40
nStudent = 140
nCourse = 40
nSubj = 10

WC_nAvSubj = 10
WC_nConnection = 7

subjMaster =    ["chinL", "engL", "edu", "engine", "math", "society", "finance", "it", "phy", "medic"]
nCourseMaster = [ 1,       1,      6,     7,        2,      6,         8,         2,    2,     5     ]

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
        return 'FAILED'

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
        return 'FAILED'
        
class course:
    max_nStudent = 4
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
    
def genRamdomCources():
    idNo = 1
    i = 0
    toRetObjs = []
    toRetObjStrs = []
    for subj in subjMaster:
        listOfCoursesOfSameType = constructNCoursesBySubjType(subj, nCourseMaster[i])
        for coursesOfSameType in listOfCoursesOfSameType:
            coursesOfSameType.idNumber = idNo
            idNo += 1
            toRetObjs.append(coursesOfSameType)
            toRetObjStrs.append(flattenObjProp2Str(coursesOfSameType))
        i += 1
        
    return [toRetObjs, toRetObjStrs]
    
def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))
    
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
    jsonString = studentObjs2Json(objs)
    writeJson(filename, jsonString)

def writeTeacherData2Json(filename, objs):
    jsonString = teacherObjs2Json(objs)
    writeJson(filename, jsonString)

def flattenObjProp2Str(obj):
    return(obj.__dict__)

def objStr2JsonStr(string):
    retStr = ""
    skip = 0
    for i in range (0, len(string)):
        if skip:
            skip -= 1
            continue 
        if string[i] == '\'':
            retStr += '"'
        elif string[i] == ' ' and string[i+1] == 'N' and string[i+2] == 'o' and string[i+3] == 'n' and string[i+4] == 'e':
            retStr += ' "None"'
            skip = 4
        else:
            retStr += string[i]
    return retStr

def main():
    listOfStudentObjs = genRandomStudents()
    listOfTeacherObjs = genRandomTeachers()
    writeStudentData2Json('data/studentInfo.json', listOfStudentObjs)
    writeTeacherData2Json('data/teacherInfo.json', listOfTeacherObjs)

    ret = genRamdomCources()
    listOfCrouseObjs = ret[0]
    ret[1] = objStr2JsonStr(str(ret[1]))
    writeJson('data/coursesInfo.json', ret[1])
    
main()
