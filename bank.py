greeting = input("Greeting: ")

greeting = greeting.casefold().strip()

if greeting == "hello":
    print("100$")
elif greeting.startswith("h"):
    print("20$")
else:
    print("0$")
