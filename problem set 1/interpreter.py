expression = input("expression: ")
expression = expression.strip()

if expression[2] == "+":
    result = float(expression[0]) + float(expression[4])
    print(result)
elif expression[2] == "-":
    result = float(expression[0]) - float(expression[4])
    print(result)
elif expression[2] == "*":
    result = float(expression[0]) * float(expression[4])
    print(result)
elif expression[2] == "/":
    result = float(expression[0]) / float(expression[4])
    print(result)
else:
    print("Error")
