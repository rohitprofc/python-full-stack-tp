#Sorting without sort function
#Bubble Sort

l = [5, 1, 4, 2, 3]
for i in range(len(l)):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)