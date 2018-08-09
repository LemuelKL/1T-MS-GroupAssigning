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
    def __init__(self, idName, avSubj):
        self.idName = idName
        self.nAvSubj = len(avSubj)
        self.avSubj = avSubj

class course:
    max_nStudent = 5
    def __init__(self, subjType, idNumber, nAvTeacher, nAvStudent, nID):
        self.subjType = subjType
        self.idNumber = idNumber
        self.idName = subjType + "_" + str(idNumber)
        self.nAvTeacher = nAvTeacher
        self.nAvStudent = nAvStudent
        self.nID = nID

def constructCourses(subjType, nCourseToConstruct):
    ret = []
    for i in range (0, nCourseToConstruct):
        tempCourse = course(subjType, i+1, None, None, nCourseToConstruct)
        ret.append(tempCourse)
    return ret

def main():
    print("Hi")

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

main()
