#!/opt/homebrew/bin/python3

# Personal message

name = "eric"
print(f"Hello {name.title()}, would you like to learn some Python today?\n")

# Name cases

name = "eric"
print(f"Hello {name.lower()}, would you like to learn some Python today?")
print(f"Hello {name.upper()}, would you like to learn some Python today?")
print(f"Hello {name.title()}, would you like to learn some Python today?\n")

# Famous quote and famous quote 2

famous_person = "blaise pascal"
quote = "In every man's heart is a God-shaped vacuum."
print(f"{famous_person.title()} said, {quote}")

# Stripping names

person =  " warren buffett "
print(f"{person}")
print(f"\t {person}")
print(f"\n\t {person}")
print(f"{person}".title().lstrip())
print(f"{person}".title().rstrip())
print(f"{person}".title().strip())

# File extensions

filename = 'python_notes.txt'
print(f"{filename}".removesuffix(".txt")) # rem: need to define the suffix

# Number eight

print(4 * 2)
print(5 + 3)
print((21 - 5) / 2)
print(64**(1/2))

# Favourite number

favourite_number = 5
print(f"My favourite number is {favourite_number}.")
