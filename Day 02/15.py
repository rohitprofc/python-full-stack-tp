#Multi-level Inheritance
#coding practice 1

class ceo:
    def cc(self):
        print("IM CEO")
class hr(ceo):
    def hr(self):
        print("IM HR")
class man(hr):
    def mn(self):
        print("Im Manager")
class emp(man):
    def em(self):
        print("Im Employee")

e=emp()
e.em()
e.mn()
e.hr()
e.cc()