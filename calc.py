op = input("Choose operation (+, -, *, /): ")
try:
    a = float(input("Give 1st number: "))
    b = float(input("Give 2nd number: "))
except:
    print("I don't think this is a number")
else:
    result = 0.0
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        try:
            result = a / b
        except ZeroDivisionError:
            print("This program can't reach infinity")
    else:
        print("wrong op")

    print(f"Result: {result}")
