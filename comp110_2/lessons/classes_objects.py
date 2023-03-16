"""Example of a class and object instantiation."""

__author__ = "Michael Fehl"


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Defitions
    size: str
    toppings: int
    extra_cheese: bool = False

    # This is called a constructor -- it initalizes the attributes to a new object being constructed (a_pizza in this example)
    def __init__(self, size: str, toppings: int): 
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings

    # This is a part of the pizza class now it is indented -- this is a method!
    def price(self, tax: float) -> float:
        """Calculate price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        elif self.size == "medium":
            total += 8.0
        else:
            total += 6.0
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total *= tax
        
        return total


a_pizza: Pizza = Pizza("large", 3)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
# This is a method call: class_variable.method_call()
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")