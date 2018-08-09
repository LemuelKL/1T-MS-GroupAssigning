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
    def __init__(self, subjType, idNo, nAvTeacher, nAvStudent, nID):
        self.idNo = idNo
        self.nAvT = nAvT
        self.nAvS = nAvS
        self.nID = nID

def main():
    print("Hi")

    mhy = teacher("mhy", ["math1", "phy1"])
    print(mhy.idName)
    print(mhy.nAvSubj)
    print(mhy.avSubj)

def constructCourses(subjType, nCourseToConstruct):
    ret = []
    for i in range (0, nCourseToConstruct):
        tempCourse = course(subjType, i+1, None, None, nCourseToConstruct)
        ret.append()
    return ret

main()
