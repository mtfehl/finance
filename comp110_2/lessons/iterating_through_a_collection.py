"""Example of looping through all characters in a string"""

user_str: str = input("Give me a string! ")

# The variable i is a common counter variable name in programming
# i is short for iteration
i: int = 0

while i < len(user_str):
    print(user_str[i])
    if user_str[i] == "a":
        print("this is the letter a")
    else:
        print("this is not the letter a")
    i += 1

print("Done!")