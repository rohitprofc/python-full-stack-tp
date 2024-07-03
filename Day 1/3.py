#Classes & Objects
#coding practice

class car:
    def info(self, name, color, price, brand):
        print("---------------")
        print(f"Brand: {brand}")
        print(f"Name : {name}")
        print(f"Color: {color}")
        print(f"Price: {price}")
        print("---------------")

a = car()
a.info('Innova Crysta', 'White', '$45,000', 'Toyota')

b = car()
b.info('Swift Dzire', 'Silver', '$17,000', 'Suzuki')

c = car()
c.info('Harrier', 'White', '$39,000', 'Tata')

d = car()
d.info('GLS 200d', 'Black', '$96,000', 'Mercedes Benz')

e = car()
e.info('Hector Plus', 'Red', '$37,000', 'Morris Garages')