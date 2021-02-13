favorite_numbers = {
    'Bob': 5,
    'Tom': 9,
    'Andrew': 13,
    'Will': 7,
    'Frank': 9,
    }

print(f"Bob\'s favorite number is {favorite_numbers['Bob']}")
print(f"Tom\'s favorite number is {favorite_numbers['Tom']}")
print(f"Andrew\'s favorite number is {favorite_numbers['Andrew']}")
print(f"Will\'s favorite number is {favorite_numbers['Will']}")
print(f"Frank\'s favorite number is {favorite_numbers['Frank']}")

favorite_numbers = {
    'Bob': ['5', '9', '2'],
    'Tom': ['7', '1', '3'],
    'Andrew': ['5', '4', '8'],
    'Will': ['7', '3', '9'],
    'Frank': ['4', '7', '9'],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}\'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")
    print("\n")
