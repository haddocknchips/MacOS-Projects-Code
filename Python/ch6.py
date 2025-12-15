#!/opt/homebrew/bin/python3

# Simple dictionary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Start with an empty dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values

print()
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

#alien_0 = {'color': 'yellow'}
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# Different speeds

print()
#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Originial position: {alien_0['x_position']}")

## Move the alien to the right.
## Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

## The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

## Removing key-value pairs

print()
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Favorite languages example

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',  # comma so one can just add lines
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Using get()

alien_0 = {'color': 'green', 'speed': 'slow'}
#point_value = alien_0.get('points', 'No point value assigned.')
point_value = alien_0.get('points') # No second key => Python returns 'None'; this is not an error.
print(point_value)

# 6-1 Person

print()
person = {'first_name': 'giuliano', 'surname': 'sison', 'age': 34, 'city': 'london'}
#for element in person:
print(person['first_name'].title())
print(person['surname'].title())
print(person['age'])
print(person['city'].title())

# 6-2 Favorite numbers

print()
favorite_numbers = {
    'paolo': 5,
    'pauline': 7,
    'giuliano': 11,
    'emilio': 8,
}
print(favorite_numbers)
