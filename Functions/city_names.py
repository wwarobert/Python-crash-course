def city_country(city, country):
    """Combine city and country together"""
    output = f"{city.title()}, {country.title()}"
    return output


print(city_country("warszawa", "polska"))
print(city_country("den haag", "nederland"))
print(city_country("london", "uk"))
