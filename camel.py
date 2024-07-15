camelCase = input("camelCase: ")

snake_case = []
for letter in camelCase:
    if letter.isupper():
        letter = letter.replace(letter, "_" + letter).lower()
        snake_case.append(letter)
    else:
        snake_case.append(letter)

print("snake_case:", "".join(snake_case))
