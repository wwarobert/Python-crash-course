person_details_1 = {
    'first_name': 'Bob',
    'last_name': 'Dabolina',
    'age': '48',
    'city': 'San Francisco',
    }
person_details_2 = {
    'first_name': 'Donald',
    'last_name': 'Duck',
    'age': '92',
    'city': 'Los Angeles',
    }
person_details_3 = {
    'first_name': 'George',
    'last_name': 'Clinton',
    'age': '65',
    'city': 'New York City',
    }

people = [person_details_1, person_details_2, person_details_3];

for person_details in people:
    print(f"First name: {person_details['first_name'].title()}")
    print(f"Last name: {person_details['last_name'].title()}")
    print(f"Age: {person_details['age']}")
    print(f"City: {person_details['city']}")
    print("\n")
