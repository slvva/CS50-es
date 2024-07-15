def main():
    time = input("What time is it? ")
    time = float(time.replace(":", "."))
    print(convert(time))

def convert(time):
    if 7.00 <= time <= 8.00:
        return "It's breakfast time"
    if 12.00 <= time <= 13.00:
        return "It's lunch time"
    if 18.00 <= time <= 19.00:
        return "It's dinner time"

if __name__ == "__main__":
    main()
