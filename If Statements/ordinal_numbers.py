numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number < 3:
        print("{}st".format(number))
    elif number == 3:
        print("{}rd".format(number))
    else:
        print("{}th".format(number))
