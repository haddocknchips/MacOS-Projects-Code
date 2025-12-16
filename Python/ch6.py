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
person = {'first_name': 'giuliano', 'surname': 'sison', 'age': 34, 
          'city': 'london'}
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

# 6-3 Glossary

print()
glossary = {
    'if': 'conditional operation',
    'and': 'requirement for both conditions to be True',
    'or': 'requirement for either condition to be True',
    'else': 'alternative operation if initial condition is not met',
    'print': 'show output on screen or file',
}

for word in glossary:  # This is not yet in book; found thorugh research; iterating in dictionaries
    print(word, ":", glossary[word])

# Looping through dictionary

print()
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print()
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print()
for name in favorite_languages.keys():
    print(name.title())

print()
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

## To check for polling

print()
if 'erin' not in favorite_languages.keys():
    print(f"Erin, please take our poll!")

## Looping in a sorted order

print()
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

## using the values() method

print()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print()
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # set() for unique values, avoided repeats
    print(language.title())

# 6-4 Glossary

glossary = {
    'if': 'conditional operation',
    'and': 'requirement for both conditions to be True',
    'or': 'requirement for either condition to be True',
    'else': 'alternative operation if initial condition is not met',
    'print': 'show output on screen or file',
    'dictionary': 'a list of paired items, comprising a key and a value',
    'loop': 'a repeating sequence of operations on a list, dictionary, set or series of data, bounded by specific conditions',
    'set': 'a group of unique pieces of information',
    'method': 'an operation performed on a variable',
    'elif': 'an alternative condition to "if", assumes an "else" at the end',
}

print()
for key, value in glossary.items():
    print(f"{key}: {value}")

# 6-5 Rivers

rivers = {
    'nile': 'egypt',
    'zambezi': 'zimbabwe',
    'euphrates': 'iraq',
}

print()
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

# 6-6 Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',  
}

poll_targets = ['jen', 'emilio', 'giulio', 'edward', 'pauline']

print()
for respondent in poll_targets:
    if respondent in favorite_languages:
        print(f"Thank you, {respondent.title()}, for taking our poll.")
    else:
        print(f"Hi, {respondent.title()}. Please take our poll.")

# Nesting

print()
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

## Using code to generate aliens: range() function

print()
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print()
print(f"Total number of aliens: {len(aliens)}")

# Change first 3 aliens to yellow, medium, 10 points
print()
for alien in aliens [0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens [:10]:
    print(alien)

# Lists in dictionaries

# Store information about a pizza being ordered.
print()
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following"
      " toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# Another list within dictionary

print()
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
    else:
        print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Nested dictionaries

print()
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
   
# 6-7 People

people = {
    'giulio': {
        'first_name': 'giuliano', 
        'surname': 'sison', 
        'age': 34, 
    },
    'emilio': {
        'first_name': 'emilio', 
        'surname': 'sison', 
        'age': 27,
    },
    'pauline': {
        'first_name': 'pauline', 
        'surname': 'sison', 
        'age': 58,
    },
}

for name, details in people.items():
    print(f"{name.title()}")
    full_name = f"{details['first_name']} {details['surname']}" # converts values to a variable; quite cool
    age = details['age']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age}")

# 6-8 Pets

print()

archie = {
    'name': 'archie',
    'animal': 'goldfish',
    'age': 2,
    'owner': 'john',
}

pepper = {
    'name': 'pepper',
    'animal': 'dog',
    'age': 5,
    'owner': 'paolo',
}

buxley = {
    'name': 'buxley',
    'animal': 'cat',
    'age': 8,
    'owner': 'pauline',
}

pets = [archie, pepper, buxley]

for pet in pets:
    print(f"\nName: {pet['name'].title()}")
    print(f"Animal: {pet['animal']}")
    print(f"Age: {pet['age']}")
    print(f"Owner: {pet['owner'].title()}")

# 6-9 Favorite places

print()

favorite_places = {
    'paolo': ['cape town', 'snowbird', 'chesapeake'],
    'pauline': ['chobe', 'winter park', 'tubbataha'],
    'albert': ['princeton'],
}

for name, favorites in favorite_places.items():
    if len(favorites) == 1:
        print(f"{name.title()}'s favorite place is:")
    else:
        print(f"{name.title()}'s favorite places are:")
    for place in favorites:
        print(f"\t{place.title()}")
