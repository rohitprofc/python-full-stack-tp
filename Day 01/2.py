#Classes & Objects

#note:-
#to access member functions through object we need self as the default parameter
class student:
    college = 'SRGEC' #class member
    branch = 'AI&DS'
    
    def info(self, id, name, phone, city): #member function
        print("---------------------")
        print(f"Roll : {id} | {student.branch}")
        print(f"Name : {name} | {student.college}")
        print(f"Phone: {phone}")
        print(f"City : {city}")
        print("---------------------")

r1 = student()
r1.info(51, 'Rohit', 9494214912, 'Eluru')

r2 = student()
r2.info(15, 'Rushi', 9494064572, 'H.Junction')