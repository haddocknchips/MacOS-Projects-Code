#!/opt/homebrew/bin/python3

# If statement example

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# != example

print()
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Check is value is in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish.")

# 5-1 Conditional tests

print()
car = 'bmw'
print("Is car == 'bmw'? I predict True.")
print(car == 'bmw')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print()
fish = 'barracuda'
print("Is fish == 'barracuda'? I predict True.")
print(fish == 'barracuda')
print("Is fish == 'tuna'? I predict False.")
print(fish == 'tuna')

print()
sport = 'football'
print("Is sport == 'football'? I predict True.")
print(sport == 'football')
print("Is sport == 'baseball'? I predict False.")
print(sport == 'baseball')

print()
food = 'lasagna'
print("Is food == 'lasagna'? I predict True.")
print(food == 'lasagna')
print("Is food == 'chilli'? I predict False.")
print(food == 'chilli')

print()
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')
print("Is fruit == 'orange'? I predict False.")
print(fruit == 'orange')

print()
insect = 'beetle'
print("Is insect == 'beetle'? I predict True.")
print(insect == 'beetle')
print("Is insect == 'ant'? I predict False.")
print(insect == 'ant')

print()
movie_genre = 'sci-fi'
print("Is movie genre == 'sci-fi'? I suspect True.")
print(movie_genre == 'sci-fi')
print("Is movie genre == 'drama'? I suspect False.")
print(movie_genre == 'drama')

print()
weather = 'sunny'
print("Is weather == 'sunny'? I suspect True.")
print(weather == 'sunny')
print("Is weather == 'rainy'? I suspect False.")
print(weather == 'rainy')

# 5-2 More conditional tests

print()
participant = 'luis'
print(participant == 'luis')
print(participant == 'Luis'.lower())
print(participant == 'greg')

score = 88
print(score == 88)
print(score == 98)
print(score <= 100)
print(score >= 66) 
print(score <= 50)
print(score >= 33) 
print(score >= 50 and score <= 100)
print(score >= 50 and score <= 55)
print(score >= 50 or score <= 55)

print()
fruits = ['apple', 'orange', 'mango']
print('avocado' in fruits)
print('apple' in fruits)

# Conditional tests

print()
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# Amusement park

print()
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission costs is $40.")

## more flexibility, easier to modify
print()
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

## Python does not require an else in an elif chain
print()
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

# More than one condition could be true

print()
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")

# 5-3 Alien colors #1

print()
alien_color = 'blue'
if alien_color == 'blue':
    print("You just earned 5 points!")

print()
alien_color = 'blue'
if alien_color == 'green':
    print("You just earned 5 points!")

# 5-4 Alien colors #2

alien_color = 'green'
if alien_color == 'green':
    print("You just earned 10 points for shooting the alien!")
else:
    print("You just earned 5 points!")

alien_color = 'green'
if alien_color == 'blue':
    print("You just earned 10 points for shooting the alien!")
else:
    print("You just earned 5 points.")

# 5-5 Alien colors #3

print()

alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points.")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points.")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points.")

# 5-6 Stages of life

print()
age = 57
if age < 2:
    print("The person is a baby.")
if age >= 2 and age < 4:
    print("The person is a toddler.")
if age >= 4 and age < 13:
    print("The person is a kid.")
if age >= 13 and age < 20:
    print("The person is a teenager.")
if age >= 20 and age < 65:
    print("The person is an adult.")
if age >= 65:
    print("The person is an elder.")

# 5-7 Favorite fruit

print()
favorite_fruits = ['watermelon', 'durian', 'guyabano', 'apple', 'orange']
if 'apple' in favorite_fruits:
    print("That's a favorite!")
else:
    print("That's not a favorite.")
if 'mango' in favorite_fruits:
    print("That's a favorite!")
else:
    print("That's not a favorite.")
if 'strawberry' in favorite_fruits:
    print("That's a favorite!")
else:
    print("That's not a favorite.")
if 'orange' in favorite_fruits:
    print("That's a favorite!")
else:
    print("That's not a favorite.")

print()
favorite_fruits = ['macopa', 'avocado', 'lychee']
fruit = 'orange'
if fruit in favorite_fruits:
    print(f"You really like {fruit}s!")
fruit = 'macopa'
if fruit in favorite_fruits:
    print(f"You really like {fruit}s!")
fruit = 'rambutan'
if fruit in favorite_fruits:
    print(f"You really like {fruit}s!")
fruit = 'watermelon'
if fruit in favorite_fruits:
    print(f"You really like {fruit}s!")
fruit = 'avocado'
if fruit in favorite_fruits:
    print(f"You really like {fruit}s!")

# pizza toppings example

print()
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# Checking that a list is not empty.

print()
requested_toppings = ['olives']
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Using multiple lists

print()
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# 5-8 Hello admin

print()
usernames = ['admin', 'paolo', 'pauline', 'giulio', 'emilio', 'cj', 'ogi']
for user in usernames:
    if user == 'admin':
        print(f"Hello, {user.title()}. Would you like to see a status report?")
    elif user == 'cj':
        print(f"Hello, {user.upper()}. Thank you for logging in again.")
    else:
        print(f"Hello, {user.title()}. Thank you for logging in again.")

# 5-9 No users

print()
#usernames = ['admin', 'paolo', 'pauline', 'giulio', 'emilio', 'cj', 'ogi']
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello, {user.title()}. Would you like to see a status report?")
        elif user == 'cj':
            print(f"Hello, {user.upper()}. Thank you for logging in again.")
        else:
            print(f"Hello, {user.title()}. Thank you for logging in again.")
else: 
    print("We need to find some users!")

# 5-10 Checking usernames

print()
current_users = ['Paolo', 'Pauline', 'Giulio', 'Emilio', 'CJ', 'Ogi']
current_users_copy = [current_user.lower() for current_user in current_users]

new_users = ['Emilio', 'Ogi', 'Rudolph', 'Jim', 'Gregga']
new_users_copy = [new_user.lower() for new_user in new_users]

for new_user_copy in new_users_copy:
    if new_user_copy in current_users_copy:
        print("That username is taken. You will need to choose a new username.")
    else:
        print("That username is available.")

# 5-11 Ordinal numbers

print()
ordinals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal in ordinals:
    if ordinal == 1:
        print("1st")
    elif ordinal == 2:
        print("2nd")
    elif ordinal == 3:
        print("3rd")
    else:
        print(f"{ordinal}th")

# 5-12 Styling statements => checked

# Your ideas => transpose to separate notes
# - Horner's
# - Finance and investing tool
