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

numbers = [number for number in range (1, 1000001)]
print(numbers)
