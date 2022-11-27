responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input(
        "If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input(
        "\nWould you like to let another person to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Polling responeses ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response.title()} on holidays!")
