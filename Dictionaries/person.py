person_details_1 = {
    'first_name': 'bob',
    'last_name': 'dabolina',
    'age': '48',
    'city': 'San Francisco',
    }
person_details_2 = {
    'first_name': 'donald',
    'last_name': 'duck',
    'age': '92',
    'city': 'Los Angeles',
    }
person_details_3 = {
    'first_name': 'george',
    'last_name': 'clinton',
    'age': '65',
    'city': 'New York City',
    }

people = [person_details_1, person_details_2, person_details_3]

for person_details in people:
    print(f"First name: {person_details['first_name'].title()}")
    print(f"Last name: {person_details['last_name'].title()}")
    print(f"Age: {person_details['age']}")
    print(f"City: {person_details['city']}")
    print("\n")

basketball_players = {
    'lebron james': {
        'born': 'akron, ohio',
        'height': '2.06',
        'team': 'los angeles lakers'        
    },
    'michael jordan': {
        'born': 'brooklyn, new york',
        'height': '1.98',
        'team': 'chicago bulls',
    },
    'kobe bryant': {
        'born': 'philadelphia, pennsylvania',
        'height': '1.98',
        'team': 'los angeles lakers',
    },
}

for player, player_details in basketball_players.items():
    print(f"{player.title()}")
    print(f"\tBorn in {player_details['born'].title()}")
    print(f"\tHeight: {player_details['height']}")
    print(f"\tTeam: {player_details['team'].upper()}")
