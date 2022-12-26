class User:
    """Simple class to print out information about the user."""

    def __init__(self, first_name, last_name, login_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.login_name = login_name
        self.email_address = email_address
        self.login_attemtps = 0

    def describe_user(self):
        """Print full information about the user."""
        print(
            f"User name is: {self.first_name.title()} {self.last_name.title()}")
        print(f"Username is: {self.login_name}")
        print(f"Email address: {self.email_address}")

    def greet_user(self):
        """Print personalized message to the user."""
        print(f"Great to meet you {self.first_name}")

    def increment_login_attemtpts(self):
        """Increment login attempts by 1."""
        self.login_attemtps += 1

    def reset_login_attempts(self):
        """Reset login attemtps number."""
        self.login_attemtps = 0


user = User("Michael", "Jordan", "MJ", "mj@test.com")
user.describe_user()
user.greet_user()
user.increment_login_attemtpts()
print(f"Login attempts: {user.login_attemtps}")
user.reset_login_attempts()
print(f"Loggin attempts: {user.login_attemtps}")
