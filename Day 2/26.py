#Adult Count & Child Count

age = [45, 12, 34, 15, 18, 90, 45, 12, 14, 11, 21, 20]

adult_list, child_list = [], []
child_count, adult_count = 0, 0

for i in age:
    if i<=18:
        child_list.append(i)
        child_count += 1
    else:
        adult_list.append(i)
        adult_count += 1

print(f"Adults: {adult_list}\nAdult count: {adult_count}")
print(f"Childs: {child_list}\nChild count: {child_count}")