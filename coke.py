amount = 0

while amount < 50:
    coin = input("Insert coin(5, 10, 25 cents): ")
    coin = int(coin)
    if coin in [5, 10, 25]:
        amount += coin
        if amount < 50:
            print("Amount Due:", 50 - amount)
    else:
        print("Invalid coin")


print("Change Owed:", amount - 50)
