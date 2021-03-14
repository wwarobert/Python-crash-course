prompt = "\nPlease enter pizza topping you like"
prompt += "\n(Enter 'quite when you are finished.') "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"{topping.title()} has been added to the pizza!")
