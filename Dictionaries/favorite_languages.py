favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah\'s favrorite language is {language}")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take out our poll!")


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n")
for language in set(favorite_languages.values()):
    print(language.title())

print("\nPolling:")
polling = ['jen', 'bob', 'phil', 'britney', 'sarah']
for name in polling:
    if name in favorite_languages:
        print(f"{name.title()} thanks for participating in the pool!")
    else:
        print(f"{name.title()} feel invited to the polling!")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'heskell'],
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}\'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
