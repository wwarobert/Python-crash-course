cars = ['bmw', 'audi', 'toyota', 'subaru', 'renault', 'nissan']
cars.sort()
print(cars)

print("\nSort reverse=True:")
cars.sort(reverse=True)
print(cars)

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse=True))

print("\nHere is the original list:")
print(cars)

print("\nPrinting list in reverse order:")
cars.reverse()
print(cars)

list_length = len(cars)
print("\nThere is {} cars on the list".format(list_length))
