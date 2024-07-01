#Constructor
#when object is created constructor is automatically called
#initalization of constructor '__init__()'
#two types of constructor
    #default constructor
    #paramaterized constructor

class book():
    def __init__(self):
        print("constructor calling")
    def normal(self):
        print("method calling")

a = book()
a.normal()
b = book()