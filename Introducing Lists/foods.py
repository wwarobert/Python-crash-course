my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
my_foods.append('dumplings')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend favourite foods are:")
print(friend_foods)

print("\nThe first three items on the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[1:4])

print("\nThree last items on the list are:")
print(my_foods[2:])

print("\nLoops:")
print("1")
for food in my_foods[0:4]:
    print(food.title())
print("2")
for food in my_foods[:3]:
    print(food.title())
print("3")
for food in my_foods[1:]:
    print(food.title())

# That doesn't work
# both variable point to the same list
my_foods = friend_foods
print("\nMy favourite foods are:")
print(my_foods)

print("\nMy friend fabourite foods are:")
print(friend_foods)
