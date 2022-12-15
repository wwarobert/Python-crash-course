class Restaurant:
    """Simple class to describe restaurant."""

    def __init__(self, restaurant_name, cusine_type):
        self.name = restaurant_name
        self.type = cusine_type

    def describe_restaurant(self):
        """Prints information about information."""
        print(f"Welcome to {self.type} restaurant called {self.name}")

    def open_restaurant(self):
        """Prints information if restaurant is open."""
        print("Restaurant is open.")


restaurant = Restaurant("Ming Cho", "chinese")
print(f"The name of the restaurant is: {restaurant.name}")
print(f"The cusine type is: {restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

fast_food_restaurant = Restaurant("KFC", "fast food")
fast_food_restaurant.describe_restaurant()

indian_restaurant = Restaurant("Toko Chava", "indian")
indian_restaurant.describe_restaurant()

grill_restaurant = Restaurant("Argentinian Grill", "grill")
grill_restaurant.describe_restaurant()
