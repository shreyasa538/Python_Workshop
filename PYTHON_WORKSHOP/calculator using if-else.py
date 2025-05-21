a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == '+':
    result = a + b
    print("Result:", result)
elif operator == '-':
    result = a - b
    print("Result:", result)
elif operator == '*':
    result = a * b
    print("Result:", result)
elif operator == '/':
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("infinity")
else:
    print("Invalid operator")