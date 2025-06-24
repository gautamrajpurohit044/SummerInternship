def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b
def calculator(a, b, operation):
    if operation == 'add':
        return add(a, b)
    elif operation == 'sub':
        return sub(a, b)
    elif operation == 'mul':
        return mul(a, b)
    elif operation == 'div':
        return div(a, b)
    else:
        return "Invalid operation"
i = int(input("Enter first number: "))
j = int(input("Enter second number: "))
op = input("Enter operation (add, sub, mul, div): ").strip().lower()
result = calculator(i, j, op)
print(f"The result of {op} operation on {i} and {j} is: {result}")