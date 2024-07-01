#Classes & Objects

#note:-
#to access member functions through object we need self as the default parameter
class student:
    college = 'SRGEC' #class member
    branch = 'AI&DS'
    def info(self, id, name, phone, city): #member functions
        print("---------------------")
        print(f"Roll: {id} | {student.branch}")
        print(f"Name: {name} | {student.college}")
        print(f"Phone: {phone}")
        print(f"City: {city}")
        print("---------------------")

r = student()
r.info(51, 'Rohit', 9494214912, 'Eluru')
s = student()
s.info(45, 'Sowmya', 9908271898, 'Gudivada')