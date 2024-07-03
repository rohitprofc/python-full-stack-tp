#Method Overriding
#same method called multiple times with same arguments

class demo:
    def add(self, a, b):
        return a+b
    
class demo1(demo):
    def add(self, a, b):
        return a+b
    
d=demo1()
print(d.add(5,1))
print(d.add(4,5))