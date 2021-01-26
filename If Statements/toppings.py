requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print("\n(1) Finished making your pizza")

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print("\n(2) Finished making your pizza")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\n(3) Finished making your pizza")
else:
    print("\nAre you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green_peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french frites', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don\'t have {requested_topping}")

print("\n(4) Finished making your pizza")
