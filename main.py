nTeacher = None
nStudent = None

class teacher:
    def __init__(self, idName, avCourse):
        self.idName = idName
        self.nSub = len(avCourse)
        self.avSubs = avCourse

class course:
    max_nS = 5
    def __init__(self, idNo, nAvTeacher, nAvStudent, nID):
        self.idNo = idNo
        self.nAvT = nAvT
        self.nAvS = nAvS
        self.nID = nID

def main():
    print("Hi")

    mhy = teacher("mhy", ["math1", "phy1"])
    print(mhy.idName)
    print(mhy.nSub)
    print(mhy.avSubs)

main()
