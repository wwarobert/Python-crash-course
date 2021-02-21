cities = {
    'barcelona': {
        'country': 'Spain',
        'population': '1.620.809',
        'fact': 'La Sagrada Familia takes longer to build than the Egyptian Pyramids',
    },
    'rome': {
        'country': 'Italy',
        'population': '2.856.133',
        'fact': 'modern Rome has 280 fountains and more than 900 churches',
    },
    'paris': {
        'country': 'France',
        'population': '2.187.526',
        'fact': 'The Eiffel Tower was supposed to be a temporary installation, intended to stand for 20 years after being build for the 1889 World Fair',
    },
}

for city, city_info in cities.items():
    print(f"{city.title()}")
    print(f"\tlocation: {city_info['country'].title()}")
    print(f"\tpopulation: {city_info['population']}")
    print(f"\tfact: {city_info['fact'].title()}")
