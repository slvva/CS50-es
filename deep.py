answer= input("What's the Answer to the Greta Question of Life, the Universe and Everything? ")

lowanswer=answer.casefold().strip()

if answer == "42" or lowanswer == "forty-two":
    print ("Yes")
else:
    print("No")
