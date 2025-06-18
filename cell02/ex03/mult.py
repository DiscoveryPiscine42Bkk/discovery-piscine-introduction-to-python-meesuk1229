a = int(input())
b = int(input())
r = a * b
print(f"{a} x {b} = {r}")
print("The result is positive." if r > 0 else "The result is negative." if r < 0 else "The result is positive and negative.")