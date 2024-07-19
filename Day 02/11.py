#Calculator program using inheritance using conditional statements
#coding practrice 1A

class addAndSub:
    def add(self,a,b):
        print("addition:", a+b)
    def sub(self,a,b):
        print("subtraction:", a-b)

class mulAndDiv:
    def mul(self,a,b):
        print("multiplication:", a*b)
    def div(self,a,b):
        print("division", a/b)

class calculator(addAndSub ,mulAndDiv):
    pass

c=calculator()

ch=int(input("Enter the choice 1.sum/ 2.sub/ 3.mul/ 4.div::"))
if ch==1:
    a,b=map(int,input("Enter a b values: ").split())
    c.add(a,b)
elif ch==2:
    a,b=map(int,input("Enter a b values: ").split())
    c.sub(a,b)
elif ch==3:
    a,b=map(int,input("Enter a b values: ").split())
    c.mul(a,b)
elif ch==4:
    a,b=map(int,input("Enter a b values: ").split())
    c.div(a,b)
else:
    print("invalid")