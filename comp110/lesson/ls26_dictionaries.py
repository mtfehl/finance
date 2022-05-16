"""Some reference examples of using dictionaries."""
__author__ = "730321206"

from typing import Dict
team: Dict[int, str] = {}
# Declare Dict[key_type, value_type]
# In this example, key is an int, value is a str.
# I.e., we're mapping integers -> strings
# Dictionaries are mapped in order they were introduced, not in any order
team[91] = "Rodman"
team[23] = "James"
# when called up, "team[23]," jordan will be returned
team[33] = "Pippen"
team[23] = "Jordan"
# overwrites the previous value of 23 to become James; can't have duplicate keys
team
# calling on this shows all the keys and their associated values that appear

# Iterate through the keys of a dictionary
for key in team:
    print(key)
    # Access values by giving their key
    print(team[key])

# Remove a key value pair by its key
booted_player: str = team.pop(91)
print(booted_player)
print(team)
# Mutable data structures similar to lists

# To look up if your dictionary has a key, we use the 'in' keyword
if 23 in team:
    print("You have Jordan!")

if 91 in team:
    print("You have Rodman!")

### Change Examples to DNA Base Pairs

def count_pairs(dna: str) -> Dict[str, int]:
    counts: Dict[str, int] = {
    # Our keys will be the base pair letters (actg)
    # Our values will be the count of each base pair in our input str
        "a": 0,
        "c": 0,
        "g": 0,
        "t": 0,
    }
    for letter in dna:
        counts[letter] += 1
    return counts