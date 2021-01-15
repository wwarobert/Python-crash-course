motorocycles = ['honda', 'yamaha', 'suzuki']
print(motorocycles)

print("\nModify element in the list:")
motorocycles[0] = 'ducati'
print(motorocycles)

print("\nAdd element to the list:")
motorocycles.append('honda')
print(motorocycles)

print("\nCreate list by adding elements:")
motorocycles = []
motorocycles.append('honda')
motorocycles.append('yamaha')
motorocycles.append('suzuki')
print(motorocycles)

print("\nInsert new element:")
motorocycles.insert(2, 'ducati')
print(motorocycles)

print("\nDelete element using del:")
del motorocycles[0]
del motorocycles[2]
print(motorocycles)

print("\nPop motorocycles:")
popped_motorocycles = motorocycles.pop()
print(motorocycles)
print(popped_motorocycles)

print(f"Last motorocycle on the list was: {popped_motorocycles.title()}")

first_motorocycle = motorocycles.pop(0)
print(f"First motorocycle on the list was: {first_motorocycle.title()}")

motorocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorocycles)
print("\nRemove element by value:")
motorocycles.remove('yamaha')
print(motorocycles)

too_expensive = 'ducati'
motorocycles.remove(too_expensive)
print(motorocycles)
print(f"\nA {too_expensive.title()} is just too expensive for me.")

print("\nIf you want access last element on the list use -1")
print(f"{motorocycles[-1]}")
