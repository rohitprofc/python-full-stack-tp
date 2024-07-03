#Linear Search

a = [23, 56, 67, 89, 2, 4, 7, 101, 890]

for i in a:
    if i==4:
        print(f"Found {i} at {a.index(i)+1}th position")