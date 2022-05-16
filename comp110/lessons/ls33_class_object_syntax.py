"""Syntax for Classes & Objects."""

# ClassNames being with uppercase letters, instead of _ we use capitals
# Attributes are declared in the class body
# A [ClassName] object will have a [name] attribute of type [type]
    # A 'TwitterProfile' object will have a 'followers' attribute of type 'int'

# ex:
class TwitterProfile:
    # Every object of type TwitterProfile will have three attributes:
        # handle, followers, is_private
    handle: str
    followers: int = 0
    is_private: bool = True

# After defining a class, you can now use it as a type (ex: in variable declarations)
a_profile: TwitterProfile

# Initializing a composite data type value requires Constructing a new object.
a_profile: TwitterProfile = TwitterProfile()
a_profile = TwitterProfile()
# To establish an object whose type is custom, you must "construct" it
# Constructor is a special function responsible for initializing an object from a class
    # Every Python class has a default constructor
    # ex: str(5), int("5")

# When the TwitterProfile() expression is evaluated, the processor constructs
# a new object in heap memory w/ space allocated for each attribute
# Any default values of an attribute are bound to the class' defaults
# If a custom constructor is defined, it is evaluated 

print(a_profile.handle)
# By referencing the variable's name followed by the dot operator, followed by an attribute
# name, we are saying:
# "Hey a_profile, what's your handle attribute's value?"
# General form: [object].[attribute]

a_profile.handle = "UNC"
# Change an object's property value using the assignment operator
# General form: <object>.<property> = <value>

# Pythons attributes are:
    # Java's instance variables
    # C++ data members
    # JavaScript's object properties
#Objects are often referred to as instances of a class