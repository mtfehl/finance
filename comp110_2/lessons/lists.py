"""Lists and their basic functions."""


from random import randint

rolls: list[int] = list() # similar to str(10)
rolls.append(randint(1, 6)) # add items to a list
rolls.append(randint(1, 6))
print(rolls)

# Access an individual item
print(rolls[0])
print(rolls[1])

# Access the length of a list (number of items)
print(len(rolls))

# Access the last item of a list
last_index: int = len(rolls) - 1
print(rolls[last_index])