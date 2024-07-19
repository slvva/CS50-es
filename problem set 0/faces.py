def main():
    inp = input()
    print(convert(inp))

def convert(inp):
    happy = inp.replace(":)", "🙂").replace(":(", "😕")
    return happy

main()
