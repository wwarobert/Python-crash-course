sandwich_orders = ["chicken", "egg", "pastrami", "seafood", "pastrami",
                   "roast beef", "grilled cheese", "pastrami", "ham", "meatball", "pastrami"]
finished_sandwiches = []

print("Deli run out of pastrami!\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich.title()} samdwich")
    finished_sandwiches.append(current_sandwich)

print("\nReady sandwiches:")

for ready_sandwich in finished_sandwiches:
    print(f"{ready_sandwich.title()} sandwich is ready!")
