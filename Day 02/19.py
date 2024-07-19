#Hybrid inheritance
#it is combination of one or more types of inheritances

class college:
    def clg(self, name, city, code):
        print(f"College:{name} Location:{city} Code:{code}")

class dept(college): #single inheritance
    def dd(self, name, total):
        print(f"Dept:{name} Strength:{total}")

class principle:
    def pp(self, name):
        print(f"Principal:{name}")

class hod(principle):
    def hh(self, name, dept):
        print(f"HoD:{name}-{dept}")

class student(hod): #multi-level inheritance
    def ss(self, name, roll, dept):
        print(f"Name:{name} Roll:{roll} Dept:{dept}")

class demo(student,dept): #multiple inheritance
    def dm(self):
        print("Hybrid Inheritance")

d = demo()
d.dm()
d.ss("Rohit",5451,"AI&DS")
d.dd("AI&DS", 675)
d.pp("B.Karuna Kumar")
d.hh("Bannu","AI&DS")
d.clg("SRGEC","Gudlavalleru",48)