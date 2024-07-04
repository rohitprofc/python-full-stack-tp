#Constructor
#coding practice 1

class book():
    def __init__(self, id, name, price, author): #paramaterized constructor
        self.id = id
        self.name = name
        self.price = price
        self.author = author

    def display(self):
        print("------------------------------------")
        print(f"Id    : {self.id}")
        print(f"Name  : {self.name}")
        print(f"Price : {self.price}")
        print(f"Author: {self.author}")
        print("------------------------------------")

b1 = book(1, 'The Girl in Room 105', '$2.19', 'Chetan Bhagat')
b1.display()

b2 = book(2, 'Power of Subconcious Mind', '$1.69', 'Paul Joseph')
b2.display()

b3 = book(3, 'One Night @ Call Center', '$1.99', 'Chetan Bhagat')
b3.display()

b4 = book(4, 'Vennello Aadapilla', '$0.99', 'Yandamoori Veerendranadh')
b4.display()

b5 = book(5, 'Idly, Orchid and Will Power', '$3.69', 'Vital Kamath')
b5.display()