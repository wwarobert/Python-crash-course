guest_list = ['nasir jones',
              'bubba sparxx',
              'michael jordan',
              'dr. dre',
              'method man',
              'eminem']
print(guest_list)
print(f"Hi {guest_list[0].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[1].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[2].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[3].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[4].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[5].title()}, I\'d like to invite you for a dinner.")

print(f"\nUnfortunately, {guest_list[3].title()} will not be able to make it")

guest_list[3] = 'Dr. Octagon'
print(guest_list)
print(f"Hi {guest_list[0].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[1].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[2].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[3].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[4].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[5].title()}, I\'d like to invite you for a dinner.")

print("\nGood news, we have a new bigger table, more people will come")
guest_list.insert(0, 'joe budden')
guest_list.insert(4, 'lauryn hill')
guest_list.append('joel ortiz')

print(guest_list)
print(f"Hi {guest_list[0].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[1].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[2].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[3].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[4].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[5].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[6].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[7].title()}, I\'d like to invite you for a dinner.")
print(f"Hi {guest_list[8].title()}, I\'d like to invite you for a dinner.")

print("\nOh, I\'m sorry I can invite only two people to a dinner")
guest1 = guest_list.pop()
print(f"Hi {guest1.title()} I can\'t invite you to the dinner")
guest2 = guest_list.pop()
print(f"Hi {guest2.title()} I can\'t invite you to the dinner")
guest3 = guest_list.pop()
print(f"Hi {guest3.title()} I can\'t invite you to the dinner")
guest4 = guest_list.pop()
print(f"Hi {guest4.title()} I can\'t invite you to the dinner")
guest5 = guest_list.pop()
print(f"Hi {guest5.title()} I can\'t invite you to the dinner")
guest6 = guest_list.pop()
print(f"Hi {guest6.title()} I can\'t invite you to the dinner")
guest7 = guest_list.pop()
print(f"Hi {guest7.title()} I can\'t invite you to the dinner")

print(f"Hi {guest_list[0].title()}, you\'re still invited")
print(f"Hi {guest_list[1].title()}, you\'re still invited")

guest_no = len(guest_list)
print("\nThere will be {} guests invited".format(guest_no))

del guest_list[0]
del guest_list[0]
print(guest_list)
