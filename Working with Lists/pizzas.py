pizzas = ['diavola', 'margherita', 'marinara', 'funghi', 'calzone']

for pizza in pizzas:
    print(f"{pizza.title()}")

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza")

print("\nMy pizzas")
print(pizzas)
print("\nFriend pizzas:")
friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('napoli')
friend_pizzas.append('frute di mare')

print("\nMy favourite pizzas are:")
print(pizzas)
print("\nMy friend favourite pizzas are:")
print(friend_pizzas)
