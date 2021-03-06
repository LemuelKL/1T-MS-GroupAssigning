import json
import random
import numpy as np
import matplotlib.pyplot as plt

DEBUG_MODE = False

subjMaster =    ["chinL", "engL", "edu", "engine", "math", "society", "finance", "it", "phy", "medic"]
nCourseMaster = [ 1,       1,      6,     7,        2,      6,         8,         2,    2,     5     ]

# Please don't touch these, yet.
nTeacher = 40
nStudent = 140
nCourse = 40
nSubj = len(subjMaster)

WC_nAvSubj = 10
WC_nConnection = 7

class node:
    def __init__(self, value):
        self.value = value

class connection: 
    def __init__(self, n1, n2):
        self.node1 = node(n1)
        self.node2 = node(n2)

class teacher:
    def __init__(self, idName, avSubjs):
        self.idName = idName
        self.nAvSubj = len(avSubjs)
        self.avSubjs = avSubjs
        self.avIndex = None
        self.nConnection = None

    def calcAvIndex(self):
        if not self.nAvSubj == None or not self.nConnection == None:
            self.avIndex = self.nAvSubj * WC_nAvSubj + self.nConnection * WC_nConnection
            return 'SUCCESS'
        return 'FAILED'

class student:
    def __init__(self, pyccode, choice1, choice2):
        self.pyccode = pyccode
        self.choice1 = choice1
        self.choice2 = choice2
        self.avIndex = None
        self.nConnection = None

    def calcAvIndex(self):
        if not self.nConnection == None:
            self.avIndex = self.nConnection
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

def connectStudentsWithTeachersByCourses(students, teachers, courses):
    connections = []
    for subj in subjMaster:
        subjStudents = [ s for s in students if s.choice1 == subj ]
        subjTeachers = [ t for t in teachers if subj in t.avSubjs ]
        subjCourses = [ c for c in courses if c.subjType == subj ]
        for t in subjTeachers:
            for s in subjStudents:
                conn = connection(t, s)
                connections.append(conn)
    return connections
        
def program():
    #####   START Data Generation    #####
    
    listOfStudentObjs = genRandomStudents()
    listOfTeacherObjs = genRandomTeachers()
    writeStudentData2Json('data/studentInfo.json', listOfStudentObjs)
    writeTeacherData2Json('data/teacherInfo.json', listOfTeacherObjs)

    ret = genRamdomCources()
    listOfCrouseObjs = ret[0]
    ret[1] = objStr2JsonStr(str(ret[1]))
    writeJson('data/coursesInfo.json', ret[1])

    #####   END Data Generation    #####

    connections = connectStudentsWithTeachersByCourses(listOfStudentObjs, listOfTeacherObjs, listOfCrouseObjs)
    print("Number of Connections Associated: ", len(connections))

    # TEACHER
    ci = 0
    ri = 0
    result = []
    for teacher in listOfTeacherObjs:
        connWithThisTeacher = [ c for c in connections if c.node1.value.idName == teacher.idName ]
        nConns = 0
        for conn in connWithThisTeacher: 
            conn.node1.r = 64
            conn.node1.x = 64 + 64*2*ci
            conn.node1.y = 64 + 64*2*ri
            result.append(conn)
            nConns += 1

        teacher.nConnection = nConns
            
        if ci >= 5:
            ci = -1
            ri += 1  
        ci += 1

    print(len(result))
    x = [ conn.node1.x for conn in result ]
    y = [ conn.node1.y for conn in result ]

    if DEBUG_MODE:
        plt.plot(x, y, 'ro')
        plt.axis([0, 1000, 0, 1000])
        plt.show()


    for teacher in listOfTeacherObjs:
        teacher.calcAvIndex()
        
    listOfTeacherObjs.sort(key=lambda t: t.avIndex, reverse=False)

    if DEBUG_MODE:
        for teacher in listOfTeacherObjs:
            print(teacher.idName, teacher.nAvSubj, teacher.nConnection, teacher.avIndex)

    ######  STUDENT  #####

    for student in listOfStudentObjs:
        connWithThisTeacher = [ c for c in connections if c.node2.value.pyccode == student.pyccode ]
        student.nConnection = len(connWithThisTeacher)
        student.calcAvIndex()

    listOfStudentObjs.sort(key=lambda t: t.avIndex, reverse=False)

    if DEBUG_MODE:
        for student in listOfStudentObjs:
            Print(student.pyccode, student.choice1, student.choice2, student.avIndex)
    
    '''
    Per teacher
        Per avSubj by that teacher
            select max 4 S from that Subj group, by lowest score, calc decision impact
        Pick the decision which lower than overall avIndex by the least, write changes to external
        write change includes: decrease all non-selected students' avIndexs

    NOTE: Must first sort all avIndexs or else this will crumble
    '''
    
    decisions = []
    i = 0
    for teacher in listOfTeacherObjs:
        if DEBUG_MODE:
            print('')
            print(len(listOfStudentObjs), 'students and', len(connections), 'connections left to process')
            
        decisions.append('')
        minImpact = 99999
        for subj in teacher.avSubjs:
            studentWithThisSubjChoice = [ s for s in listOfStudentObjs if s.choice1 == subj ]
            if DEBUG_MODE:
                print(teacher.idName, subj, len(studentWithThisSubjChoice), '|', ', '.join([ s.pyccode for s in studentWithThisSubjChoice ]))
            studentWithThisSubjChoice.sort(key=lambda s: s.avIndex, reverse=False)
            if len(studentWithThisSubjChoice) > 4:
                t_selected = studentWithThisSubjChoice[0:4]
            else:
                t_selected = studentWithThisSubjChoice

            if DEBUG_MODE:
                print('t_selected', [s.pyccode for s in t_selected])

            impactedStudentNodes = [ c for c in connections if c.node1.value.idName == teacher.idName and not c.node2.value.choice1 == subj ]
            impact = len(impactedStudentNodes)
            if impact < minImpact:
                if len(studentWithThisSubjChoice) > 4:
                    selected = studentWithThisSubjChoice[0:4]
                else:
                    selected = studentWithThisSubjChoice
                decisions[i] = teacher.idName + '_' + subj + '_' + '-'.join([ s.pyccode for s in selected ])
                minImpact = impact
                
        listOfStudentObjs = [ s for s in listOfStudentObjs if s not in selected ]
        connections = connectStudentsWithTeachersByCourses(listOfStudentObjs, listOfTeacherObjs, listOfCrouseObjs)
        for student in listOfStudentObjs:
            connWithThisTeacher = [ c for c in connections if c.node2.value.pyccode == student.pyccode ]
            student.nConnection = len(connWithThisTeacher)
            student.calcAvIndex()

        listOfStudentObjs.sort(key=lambda t: t.avIndex, reverse=False)
        
        i += 1

    unassignedTeachers = [ d for d in decisions if d.endswith('_')]
    return decisions, len(listOfStudentObjs), len(connections), len(unassignedTeachers)

ret = program()
decisions = ret[0]
decisions = '\n'.join(decisions)
print(decisions)
print('There are', ret[1], 'students cannot be assigned')
print('There are', ret[2], 'connections remaining')
print('There are', ret[3], 'unassigned teachers not needed')
input()





