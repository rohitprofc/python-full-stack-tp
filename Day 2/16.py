#Multi-level Inheritance
#coding practice 2

class college:
    def cg(self):
        print("College")
class principal(college):
    def pr(self):
        print("Principal")
class vicePrincipal(principal):
    def vp(self):
        print("Vice Principal")
class hod(vicePrincipal):
    def hd(self):
        print("HoD")
class classTeacher(hod):
    def ct(self):
        print("Class Teacher")
        
s=classTeacher()
s.ct()
s.hd()
s.vp()
s.pr()
s.cg()