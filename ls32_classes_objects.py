"""Conceptual Introduction to Classes and Objects."""

# A data type communicates a value's attributes and capabilities
    # Ex: If you have a value of type int, you can do math with it

# A class is how you define a custom, composite data type
    # Conceptually similar to a template (a blank twitter profile)

# A value whose data type is composite is an object
    # Anything bound to an object (variables, items in list, etc)
    # holds a reference to the object itself; objects are mutuable
    
    # Different twitter profiles would be objects, since they have their own
    # custom values associated with them

# Classes vs Dictionaries

# Classes: 
# Attributes must be valid identifiers, are individually typed
# All objects of a class have the same attributes defined
# Useful when: attributes of model have different types & are known
# ahead of time

# Dictionaries: 
# Keys are any immutable type (str, float, int)
# All values associated with keys are of a single type
# No guarantee any two Dictionaries have the same keys
# Useful when: keys ("attributes") of model are unknown ahead
# of time and of the same type
