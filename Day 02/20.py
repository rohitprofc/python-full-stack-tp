#Method Overloading
#same method called multiple times with different arguments

class demo:
    def add(self, a, b):
        print(a+b)
    
class demo1(demo):
    def add(self, a, b):
        print(a+b)
    
d=demo1()
d.add(9,6)
d.add('Rohit','Chess')