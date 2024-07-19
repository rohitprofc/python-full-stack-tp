#Calculator program using inheritance using match function
#coding practrice 1B

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

ch=int(input("enter the choice 1.sum/ 2.sub/ 3.mul/ 4.div ::"))
match(ch):
    case 1:
        print("enter a b values")
        a,b=map(int,input().split())
        c.add(a,b)
    case 2:
        print("enter a b values")
        a,b=map(int,input().split())
        c.sub(a,b)
    case 3:
        print("enter a b values")
        a,b=map(int,input().split())
        c.mul(a,b)
    case 4:
        print("enter a b values")
        a,b=map(int,input().split())
        c.div(a,b)
    case _: #default case
        print("invalid")