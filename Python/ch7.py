### How input() works ###

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

### Greeter ### 

#name = input("Please enter your name: ")
#print(f"\nHello, {name}!")

#prompt = "If you can share your name, we can personalize the messages you see"
#prompt += "\nWhat is your first name? " # += adds a new string to the end
#
#name = input(prompt)
#print(f"\nHello, {name}!")

### Rollercoaster ###

#height = input("How wall are you, in inches? ")
#height = int(height)
#
#if height >= 48:
#    print("\nYou are all enough to ride!")
#else:
#    print("\nYou'll be able to ride when you're a little older.")

### Modulo operator ###

#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#
#if number % 2 == 0:
#    print(f"\nThe number {number} is even.")
#else:
#    print(f"\nThe number {number} is odd.")

# 7-1 Rental car

#car = input("What kind of car would you want to rent? ")
#print(f"\nLet me see if I can find a {car.title()}.")

# 7-2 Restaurant seating

#group_size = input("How many persons are in your group? ")
#
#if int(group_size) > 8:
#    print("Please wait for a table to be free.")
#else:
#    print("Let me show you to your table.")

# 7-3 Multiples of 10

number = input("Enter a number: ")
if int(number) % 10 == 0:
    print("That number is a multiple of 10.")
else:
    print("That number is not a multiple of 10.")

