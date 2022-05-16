"""A demonstration of classes/objects."""
__author__ = "730321206"


class Pizza:
    """A simple model of a Pizza."""
    size: str = "medium"
    extra_cheese: bool = False
    toppings: int = 0


def price(pizza: Pizza) -> float:
    """Calculate the price of pizza(s) ordered."""
    final_price: float = 0.0
    topping: float = 0.75
    small: float = 7.0
    medium: float = 9.0
    large: float = 11.0
    extra_cheese: float = 1.0
    i: int = 0
    if pizza.size == "Small":
        final_price += small
    if pizza.size == "Medium":
        final_price += medium
    if pizza.size == "Large":
        final_price += large
    if pizza.extra_cheese == True:
        final_price += extra_cheese
    while i < pizza.toppings:
        final_price += topping
        i += 1
    return final_price
    

def main() -> None:
    """Entrypoint of program."""
    a_pizza: Pizza = Pizza()
    a_pizza.size = "Large"
    a_pizza.toppings = 3
    a_pizza.extra_cheese = True
    print("Size: " + a_pizza.size)
    print("Toppings: " + str(a_pizza.toppings))
    print("Price: " + str(price(a_pizza)))




if __name__ == "__main__":
    main()