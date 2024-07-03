#Constructor
#coding practice 2

class employee():
    def __init__(self, id, name, salary, job): #paramaterized constructor
        self.id = id
        self.name = name
        self.salary = salary
        self.job = job

    def display(self):
        print("--------------------------")
        print(f"Id    : {self.id}")
        print(f"Name  : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"Job: {self.job}")
        print("--------------------------")

r1 = employee(1, 'Rohit', '$51,000', 'SDE')
r1.display()

s = employee(2, 'Sowmya', '$45,000', 'Full Stack Developer')
s.display()

j = employee(3, 'Jaswanth', '$57,000', 'Data Scientist')
j.display()

r2 = employee(4, 'Rushi', '$300,000', 'Business Analyst')
r2.display()

k = employee(5, 'Kavya', '$22,000', 'Data Engineer')
k.display()

g = employee(6, 'Goutham', '$51,000', 'SDE')
g.display()

t = employee(7, 'Tapaswi', '$22,000', 'Data Engineer')
t.display()

sh = employee(8, 'Shagun', '$100,000', 'Graphic Designer')
sh.display()

p = employee(9, 'Pramod', '$69,000', 'Social Media Analyst')
p.display()

c = employee(10, 'Caroline', '$70,000', 'Server Engineer')
c.display()