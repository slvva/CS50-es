while True:
    str_fraction = input("Fraction: ")
    try:
        x, y = str_fraction.split("/")
        x = int(x)
        y = int(y)
        if x < y:
            break
    except (ValueError, ZeroDivisionError):
        continue


percent = 100 * x/y
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")
