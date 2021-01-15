mountains = ['mount everest', 'denali', 'k2']
print(f"The highest mountain in the world is {mountains[0].title()} -8.848m")
print(f"Second largest mountain is {mountains[-1].title()} -8.611m")

mountains.append('kilimanjaro')
mountains.append('aconcagua')
mountains.append('kachenjunga')
print(f"\n{mountains}")

mountains.insert(2, 'mount logan')
mountains.insert(4, 'mount gongga')
print(f"\n{mountains}")

popped_mountain = mountains.pop()
print(f"Last mountain on the list was {popped_mountain.title()}")
print(mountains)
popped_mountain = mountains.pop(0)
print(f"First mountain on the list was {popped_mountain.title()}")

mountains.remove('denali')
print("Denali has been removed from the list")
print(mountains)

too_small = 'kilimanjaro'
mountains.remove(too_small)
print(f"{too_small.title()} was too small to be on the list")
print(mountains)

mountains.append('shishaoangma')
mountains.append('matternhorn')
mountains.append('nanga parbat')
mountains.append('elbroes')

print("\nNew list has been created:")
print(mountains)
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
print(sorted(mountains))
print(sorted(mountains, reverse=True))

list_len = len(mountains)
print("We have {} mountains on the list".format(list_len))
