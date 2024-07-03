#Multiple Inheritance
#coding practice

class emp:
    def em(self, name, age):
        print(f"Employee Name: {name}\nAge: {age}")

class work:
    def wr(self, sal, exp):
        print(f"Salary: {sal}\nExperience: {exp}years")

class demo(emp, work):
    def data(self):
        print("I'm Employee of Goldmann Saches")

e=demo()
e.data()
e.em('Rohit',20)
e.wr(100000,2)