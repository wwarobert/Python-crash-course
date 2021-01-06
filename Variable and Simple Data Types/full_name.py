first_name = "mick"
last_name = "jenkins"
full_name = f"{first_name} {last_name}"

print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"\n\tHello, {full_name.title()}!"
print(message)

# format example
full_name = "{} {}".format(first_name, last_name)
print(full_name.title())

# whitespace
first_name = "   mick   "
print(f"{first_name}")
print(f"{first_name.lstrip()}")
print(f"{first_name.rstrip()}")
print(f"{first_name.strip()}")