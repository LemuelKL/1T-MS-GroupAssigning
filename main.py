import json
from pprint import pprint
from pprint import pformat
import random

nTeacher = 40
nStudent = 140
nCourse = 40
nSubj = 10

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

class teacher:
    avIndex = None
    def __init__(self, idName, avSubj):
        self.idName = idName
        self.nAvSubj = len(avSubj)
        self.avSubj = avSubj

    def calcAvIndex():
        return

class student:
    def __init__(self, pyccode, choice1, choice2):
        self.pyccode = pyccode
        self.choice1 = choice1
        self.choice2 = choice2

class course:
    max_nStudent = 5
    avIndex = None
    def __init__(self, subjType, idNumber, nAvTeacher, nAvStudent, nID):
        self.subjType = subjType
        self.idNumber = idNumber
        self.idName = subjType + "_" + str(idNumber)
        self.nAvTeacher = nAvTeacher
        self.nAvStudent = nAvStudent
        self.nID = nID

    def calcAvIndex():
        return
   
def constructCourses(subjType, nCourseToConstruct):
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
    
def main():
    mhy = teacher("mhy", ["math1", "phy1"])
    print(mhy.idName)
    print(mhy.nAvSubj)
    print(mhy.avSubj)

    societyCourses = constructCourses("society", 3)
    for societyCourse in societyCourses:
        print("==========")
        print(societyCourse.idName)
        print(societyCourse.subjType)
        print(societyCourse.nAvTeacher)
        print(societyCourse.nAvStudent)
        print(societyCourse.idNumber)
        print(societyCourse.nID)
        print("==========")

def objs2Json(objs):
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

def readJson(filename):
    with open(filename, 'r') as dataIn:
        return json.load(dataIn)

def writeJson(filename, jsonString):
    parsed = json.loads(jsonString)
    with open(filename, 'w') as outfile:
        json.dump(parsed, outfile, indent = 4, sort_keys = False)

def genRandomStudentData2Json(filename):
    jsonString = objs2Json(genRandomStudents())
    writeJson(filename, jsonString)
        
genRandomStudentDataToJson('data/studentChoiesTest.json')
#main()
