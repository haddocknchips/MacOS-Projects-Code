#!/opt/homebrew/bin/python3

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])

message = f"My first bicycle was a {bicycles[0].title()}. "
print(message)

# Names

friends = ['fred', 'yuriko', 'dave', 'becky', 'eric', 'cheryl']

print("\n")
print(f"{friends[0].title()} is a friend of ours. ")
print(f"{friends[1].title()} is a friend of ours. ")
print(f"{friends[2].title()} is a friend of ours. ")
print(f"{friends[3].title()} is a friend of ours. ")
print(f"{friends[4].title()} is a friend of ours. ")

# Greetings

print("\n")
print(f"hi {friends[0].title()}! how are you? ")
print(f"hi {friends[1].title()}! how are you? ")
print(f"hi {friends[2].title()}! how are you? ")
print(f"hi {friends[3].title()}! how are you? ")
print(f"hi {friends[4].title()}! how are you? ")

# Own list

vehicles = ['porsche', 'bmw', 'ferrari', 'lamborghini']
print("\n")
print(f"I would like to own a {vehicles[0]} car. ")
print(f"I would like to own a {vehicles[1]} car. ")
print(f"I would like to own a {vehicles[2]} car. ")
print(f"I would like to own a {vehicles[3]} car. ")
print("\n")

# Adding elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# Deleting

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] # why is the format different from append?
print(motorcycles)

# Guest list

guests = ['albert einstein', 'nelson mandela', 'abraham lincoln']
print("\n")
print(f"Dear {guests[0].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[1].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[2].title()}, I would be most grateful if you could join me for dinner. ")

# Changing guest list
regrets = guests.pop(0)
print(f"\n{regrets.title()} can't make it, unfortunately. ")
guests.append('jose rizal')
print(f"\nDear {guests[0].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[1].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[2].title()}, I would be most grateful if you could join me for dinner. ")

print("\nDear guests, we were able to secure a larger venue and will be joined by other distinguished guests! ")

guests.insert(0, 'andres bonifacio')
guests.insert(2, 'warren buffett')
guests.append('blaise pascal')

print(f"\nDear {guests[0].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[1].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[2].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[3].title()}, I would be most grateful if you could join me for dinner. ")
print(f"Dear {guests[4].title()}, I would be most grateful if you could join me for dinner. ")

# Shrinking guest list

print("\nDear esteemed guests, I am very sorry that I will only be able to invite two persons on this occasion. ")

apologies = guests.pop(0)
print(f"\nDear {apologies.title()}, I'm sorry that I won't be able to invite you to dinner this time. ")
apologies = guests.pop(0)
print(f"\nDear {apologies.title()}, I'm sorry that I won't be able to invite you to dinner this time. ")
apologies = guests.pop(0)
print(f"\nDear {apologies.title()}, I'm sorry that I won't be able to invite you to dinner this time. ")
apologies = guests.pop(0)
print(f"\nDear {apologies.title()}, I'm sorry that I won't be able to invite you to dinner this time. ")

print(f"\nDear {guests[0].title()}, I would be most grateful if you could join me for dinner. ")
print(f"\nDear {guests[1].title()}, I would be most grateful if you could join me for dinner. ")

del guests[0]
del guests[0]
print(guests)
