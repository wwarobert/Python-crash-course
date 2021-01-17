players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:2])
print(players[1:3])
print(players[0:4])
print(players[3:4])
print(players[:4])
print(players[:2])
print(players[:1])
print(players[2:])
print(players[3:])
print(players[0:])
print(players[-3:])
print(players[-1:])
print(players[-2:])
print(players[-5:])
print(players[-9:])

print("\nHere are the first three players in my team:")
for player in players[:3]:
    print(player.title())

print("\nHere are the last three players in my team:")
for player in players[2:]:
    print(player.title())
