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
