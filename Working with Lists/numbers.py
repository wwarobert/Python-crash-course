for value in range(1, 6):
    print(value)

print("\n")
for value in range(5):
    print(value)

print("\n")
numbers = list(range(1, 6))
print(numbers)

print("\n")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print("\n")
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

print("\n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Min : {}".format(min(digits)))
print("Max : {}".format(max(digits)))
print("Sum : {}".format(sum(digits)))

print("\n")
squares = [value ** 2 for value in range(1, 11)]
print(squares)

print("\n")
addone = [value + 1 for value in range(1, 11)]
print(addone)

print("\n")
addtwo = [value + 2 for value in range(1, 11)]
print(addtwo)

print("\n")
addthree = [value + 3 for value in range(1, 11)]
print(addthree)

print("\n")
addfour = [value + 4 for value in range(1, 11)]
print(addfour)

print("\nCount to twenty")
for number in range(1, 21):
    print(number)

print("\nOne million")
onemillion = list(range(1, 1000001))
# for number in onemillion:
#    print(number)

print("\nMax, min, sum")
print("Max : {}".format(max(onemillion)))
print("Min : {}".format(min(onemillion)))
print("Sum : {}".format(sum(onemillion)))

print("\nOdd numbers")
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

print("\nThrees")
threes = [value * 3 for value in range(3, 30)]
print(threes)

print("\nCubes")
for value in range(1, 11):
    print(value ** 3)

print("\nCubes in comprehension")
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
