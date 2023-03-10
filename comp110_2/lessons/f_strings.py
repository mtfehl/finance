"""Quick examples of using F-strings to concatenate"""

name: str = "Michael"
age_turning: int = 23
print("Hello " + name + ", you're almost " + str(age_turning) + "!")

print(f"Hello {name}, you're almost {age_turning}!")
# easier way to concatenate without typing so damn much


__author__ = "Michael Fehl"