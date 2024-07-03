#ATM Transaction using Inheritance
#coding practrice 2

class cdm: #cash deposit machine
    def __init__(self,bal):
        self.bal=bal
    
    def credit(self):
        amt=float(input("Enter amount to credit::"))
        self.bal+=amt
        print("Credited succesfully")
        print("Balance amount is",self.bal)

class atm(cdm): #automated teller machine
    def debit(self):
        amt=float(input("Enter amount to debit::"))
        
        if amt>self.bal:
            print("Unsufficient balance")
        else:
            self.bal-=amt
            print("Debited succesfully")
            print("Balance amount is",self.bal)

a=atm(10000)
while(True):
    print("=================================================")
    ch=int(input("enter choice 1.credit/ 2.Debit/ 3.exit:: "))
    if ch==1:
        a.credit()
    elif ch==2:
        a.debit()
    else:
        break