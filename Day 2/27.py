#Even Odd Seperation

l = [45, 12, 34, 15, 18, 90, 45, 12, 14, 11, 21, 20]
even_list = []
odd_list = []

for i in l:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Even List: {even_list}")
print(f"Odd List: {odd_list}")