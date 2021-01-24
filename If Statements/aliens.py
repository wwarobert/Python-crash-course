alien_color = 'green'

print("\nAlien #1")
if alien_color == 'green':
    print('Hey, you just earned 5 points!')

if alien_color != 'green':
    print('Alien isn\'t green at all')

alien_color = 'red'
print("\nAlien #2a")
if alien_color == 'green':
    print('Hey, you just earned 5 points!')
elif alien_color != 'green':
    print('Hey, you just earned 10 points!')

alien_color = 'yellow'
print("\nAlien #2b")
if alien_color == 'green':
    print('Hey, you just earned 5 points!')
else:
    print('Hey, you just earned 10 points!')

alien_color = 'green'
print("\nAlien #3a")
if alien_color == 'green':
    print('Hey, you just earned 5 points!')
elif alien_color == 'yellow':
    print('Hey, you just earned 10 points!')
elif alien_color == 'red':
    print('Hey, you just earned 15 points!')

alien_color = 'yellow'
print("\nAlien #3b")
if alien_color == 'green':
    print('Hey, you just earned 5 points!')
elif alien_color == 'yellow':
    print('Hey, you just earned 10 points!')
elif alien_color == 'red':
    print('Hey, you just earend 15 points!')

alien_color = 'red'
print("\nAlien #3c")
if alien_color == 'green':
    print('Hey, you just earend 5 points!')
elif alien_color == 'yellow':
    print('Hey, you just earned 10 points!')
elif alien_color == 'red':
    print('Hey you just earend 15 points')
