#Multiple Inheritance
#many parents in one child

#JAVA do not support Multiple inheritance

class mother:
    def mt(self):
        print("Mother")

class father:
    def ft(self):
        print("Father")

class son(mother, father):
    def sn(self):
        print("Son")

s = son()
s.sn()
s.mt()
s.ft()