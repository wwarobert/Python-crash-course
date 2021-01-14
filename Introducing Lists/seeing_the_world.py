locations = ['Saint Tropez', 'Monaco', 'Nice', 'Marseille', 'Cannes']

print("\nOriginal locations list:")
print(locations)

print("\nOrdered locations list:")
print(sorted(locations))

print("\nIs the list of locations still the same?")
print(locations)

print("\nLocations ordered in reverse order:")
print(sorted(locations, reverse=True))

print("\nIs the list of locations still the same?")
print(locations)

print("\nReverse the list of locations:")
locations.reverse()
print(locations)

locations.reverse()
print(locations)

print("\nSorted locations:")
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
