items = []
while True:

    try:
        item = input().upper()
        items.append(item)
    except EOFError:
        print("")
        break


for i in sorted(set(items)):
    print(items.count(i), i)
