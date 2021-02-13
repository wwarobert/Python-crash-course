favorite_places = {
    'bob': ['barcelona', 'rome', 'saint-tropez'],
    'hailey': ['new york', 'los angeles', 'saint-tropes'],
    'john': ['lisboa', 'berlin', 'san francisco'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}\'s favorite places are:")
    for place in places:
        print(f"{place.title()}")
    print("\n")
