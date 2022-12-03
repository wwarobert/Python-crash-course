def describe_city(city_name, country_name="Canada"):
    """Display city and country"""
    print(f"\n{city_name.title()} is in {country_name.title()}")


describe_city("warsaw", "poland")
describe_city("vancouver")
describe_city("new york", "USA")
