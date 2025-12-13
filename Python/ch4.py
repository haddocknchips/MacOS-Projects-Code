# Magicians list

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick! ")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!\n")

# 4-1 Pizzas

pizzas = ['pepperoni', 'quatro formaggi', 'diavola']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("As you can see, I really love pizza!\n")

# 4-2 Animals

animals = ['dog', 'cat', 'horse']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("All of these animals are domesticated.\n")

# Numbers

for number in range(1, 6):
    print(number)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Squares

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

## more concise:

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# List comprehension

squares = [value**2 for value in range (1, 11)]
print(squares)

# 4-3 Counting to twenty

numbers = [number for number in range(1, 21)]
print(numbers)

numbers = []
for number in range(1, 21):
    numbers.append(number)
print(numbers)

# 4-4 One million

# suppressing below to save time
# numbers = [number for number in range (1, 1000001)]
# print(numbers)

# 4-5 Summing a million

numbers = [number for number in range (1, 1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6 Odd numbers

odd_numbers = [number for number in range(1, 21, 2)]
print(odd_numbers)

odd_numbers = []
for number in range(1, 21, 2):
    odd_numbers.append(number)
print(odd_numbers)

# 4-7 Threes

multiples_3 = [three for three in range(3, 31, 3)]
print(multiples_3)

multiples_3 = []
for three in range(3, 31, 3):
    multiples_3.append(three)
print(multiples_3)

# 4-8, 4-9 Cubes

cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(cubes)

cubes = [cube**3 for cube in range(1, 11)]
print(cubes)

# Slices of list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3]) # first to third
print(players[:3]) # ditto
print(players[2:]) # third to end
print(players[-3:]) # ditto

# Looping through a slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the last three players on my team:")
for player in players[-3:]: # using list vs range in previous examples
    print(player.title())

# Copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 4-10 Slices

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print("The first three names in the list are:")
for player in players[:3]:
    print(player.title())
print("The last three names in the list are:")
for player in players[-3:]:
    print(player.title())

# 4-11 My pizzas, your pizzas

my_pizzas = ['pepperoni', 'quatro formaggi', 'diavola']
friend_pizzas = pizzas[:]

my_pizzas.append('garlic and olives')
friend_pizzas.append('hawaiian')

print("\nMy favorite pizzas are:")
print(my_pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

# 4-12 More loops
print("\nMy favorite pizzas are:")
for my_pizza in my_pizzas[:]:
    print(my_pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza)

# Tuples ******

# Dimensions

print()

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Can't change tuples => use when storing set of values that should 
# not be changed throughout the program

# these don't work:
# dimensions = (200, 50)
# dimensions[0] = 250
# print(dimensions[0])
# print(dimensions[1])

# Looping thorugh values in a tuple

print()
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Writing over a tuple

dimensions = (200, 50)
print("\nOriginial dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 4-13 Buffet

print()
buffet_menu = ('salad', 'cream of mushroom soup', 'spaghetti', 'hamburger', 'fish fingers')
for food in buffet_menu:
    print(food)

print()
buffet_menu = ('salad', 'chicken noodle soup', 'lamb curry', 'hamburger', 'fish fingers')
for food in buffet_menu:
    print(food)

# 4-14 look through PEP 8 code

# 4-15 code review
