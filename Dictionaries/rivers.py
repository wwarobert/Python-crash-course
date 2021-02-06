rivers = {
    'nile': 'egypt',
    'vistula': 'poland',
    'mekong': 'china',
    'niger': 'nigeria',
    'volga': 'russia',
    'rhine': 'germany',
}

for river in rivers.keys():
    print(f"{river.title()} runs through {rivers[river].title()}")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())
