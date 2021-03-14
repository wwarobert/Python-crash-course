prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' to end the program) "

price = 0
while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    if price == 0:
        print("The ticket is free!")
    else:
        print(f"The ticket price is ${price}")  