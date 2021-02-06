python_glossary = {
    'f-string': 'formatted string literal',
    'list': 'a build-in Python sequence',
    'dictionary': 'an associatie array',
    'zen of python': 'python design principles',
}

print("Python glossary:")
print(f"f-string, {python_glossary['f-string']}")
print(f"list, {python_glossary['list']}")
print(f"dictionary, {python_glossary['dictionary']}")
print(f"zen of python: {python_glossary['zen of python']}")

print("\n")
for value in python_glossary.values():
    print(value.title())
