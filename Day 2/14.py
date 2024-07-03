#Multi-level Inheritance
#many parents to many childs

class grandParent:
    def gp(self):
        print("Grand Parent")

class parent(grandParent):
    def pp(self):
        print("Parent")

class child(parent):
    def cc(self):
        print("Child")

class grandChild(child):
    def gc(self):
        print("Grand Child")

g = grandChild()
g.gp() 
g.pp() 
g.cc() 
g.gc() 