text = input("Text: ")

vowels = ["A", "E", "I" , "O", "U", "a", "e", "i", "o", "u"]

for letter in text :
    if letter in vowels:
        text = text.replace(letter, "")

print(text)
