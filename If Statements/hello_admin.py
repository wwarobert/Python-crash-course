users = ['standard user', 'api user', 'admin', 'portal user']
print("\n5-8")
for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see status report?")
    else:
        print(f"Hello {user}")

print("\n5-9")
users = []
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see status report?")
        else:
            print(f"Hello {user}")
else:
    print("We need to find some users")

print("\n5-10")
current_users = ['user 1', 'USER 2', 'user 3', 'user 4',
                 'user 5', 'user 6', 'user 7', 'user 8']
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

new_users = ['user 2', 'user 6', 'user 9', 'user 10']

for new_user in new_users:
    if new_user in current_users_lower:
        print(f"Username {new_user} already exists, please enter new name!")
    else:
        print(f"Username {new_user} is available!")
