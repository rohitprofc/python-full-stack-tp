#Error and Exeptional Handling

a = 45
b = 0

print(f"Addition: {a+b}")

try:
    print(f"Division: {a/b}")
except:
    print("Zero Division Error")

print(f"Multiplication: {a*b}")