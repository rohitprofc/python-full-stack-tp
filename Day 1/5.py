#Constructor
#coding practice 2

class book():
    def __init__(self, id, name, price, author):
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

tgr = book(1, 'The Girl in Room 105', '$2.19', 'Chetan Bhagat')
tgr.display()
psm = book(2, 'Power of Subconcious Mind', '$1.69', 'Paul Joseph')
psm.display()
onc = book(3, 'One Night @ Call Center', '$1.99', 'Chetan Bhagat')
onc.display()
vap = book(4, 'Vennello Aadapilla', '$0.99', 'Yandamoori Veerendranadh')
vap.display()
ios = book(5, 'Idly-Orchid-Sky', '$3.69', 'Vital Kamath')
ios.display()