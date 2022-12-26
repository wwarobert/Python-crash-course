class Restaurant:
    """Simple class to describe restaurant."""

    def __init__(self, restaurant_name, cusine_type):
        self.name = restaurant_name
        self.type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints information about information."""
        print(f"Welcome to {self.type} restaurant called {self.name}")

    def open_restaurant(self):
        """Prints information if restaurant is open."""
        print("Restaurant is open.")

    def set_number_served(self, number_served):
        """Set number of sreved customers."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment number of served customers."""
        self.number_served += number_served


restaurant = Restaurant("Ming Cho", "chinese")
print(f"The name of the restaurant is: {restaurant.name}")
print(f"The cusine type is: {restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

fast_food_restaurant = Restaurant("KFC", "fast food")
fast_food_restaurant.describe_restaurant()
fast_food_restaurant.number_served = 10
fast_food_restaurant.increment_number_served(2)
print(f"Served customers: {fast_food_restaurant.number_served}")

indian_restaurant = Restaurant("Toko Chava", "indian")
indian_restaurant.describe_restaurant()

grill_restaurant = Restaurant("Argentinian Grill", "grill")
grill_restaurant.describe_restaurant()
