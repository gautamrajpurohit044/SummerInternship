frac = int(input("enter a number to find fractorial :"))
factorial = 1
for i in range(1, frac + 1):
        factorial *= i
print("The factorial of", frac, "is", factorial)