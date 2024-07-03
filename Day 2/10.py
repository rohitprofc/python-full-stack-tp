#Inheritance
#access properties from parent class(super class) to child class(sub class)

#Single Inheritance 
#one parent to one child

class demo: #parent class
    def dp(self):
        print("Parent Class")

class demo1(demo): #child class
    def dc(self):
        print("Child Class")

#creating object of child class
d = demo1()
d.dp()
d.dc()