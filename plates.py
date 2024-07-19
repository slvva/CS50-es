def main():
    vanity_plate = input("Plate: ")
    if is_valid(vanity_plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(vanity_plate):
    y = -1
    if len(vanity_plate) <= 6 and vanity_plate.isalnum() and vanity_plate[:2].isalpha():
        if vanity_plate.isalpha():
            return True
        for value in vanity_plate:
            y += 1
            if value.isdigit():
                if vanity_plate[y] != "0" and vanity_plate[y:].isdigit() and vanity_plate[:y].isalpha():
                    return True

main()
