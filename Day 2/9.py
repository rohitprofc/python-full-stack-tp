#Occurence of Element

l=int(input("Enter length of list::"))
a=[]
count={}

for i in range(0,l+1):
    i=int(input(f"Enter the element {i+1}::"))
    a.append(i)

print(a)

for element in a:
    if element in count:
        count[element] +=1
    else:
        count[element] =1

print(count)