try:
    a = float(input("Input distance traveled (m): "))
    b = float(input("Input elapse time (s): "))
    print(f"{a:.2f} m")
    print(f"{b:.2f} ")
    a = a / 1000
    b = b / 60 / 60
    c = a / b
    print(f"{c:.2f}")
except ValueError:
    print("invalid input")
