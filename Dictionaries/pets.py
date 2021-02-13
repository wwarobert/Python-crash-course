pet_1 = {
    'animal': 'dog',
    'owner': 'bob',
    }
pet_2 = {
    'animal': 'cat',
    'owner': 'brad',
    }
pet_3 = {
    'animal': 'rabbit',
    'owner': 'babbit'
    }
pet_4 = {
    'animal': 'dog',
    'owner': 'hailey'
    }

pets = [
    pet_1,
    pet_2,
    pet_3,
    pet_4,
]

for pet in pets:
    print(f"This {pet['animal']} is owned by {pet['owner'].title()}")
