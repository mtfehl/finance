"""An example of methods and method calls."""


class Person:
    """A model of a person."""
    name: str
    age: int = 0

    def __init__(self, name: str):
        """Constructor of Person initializes name."""
        self.name = name


    def say_hello(self) -> None:
        """Greet the user!"""
        print(f"Hello, I'm {self.name}!")
        # Example of a method: once defined, can call a method on 
        # any object of that class using the dot operator

    
def main() -> None:
    """Entrypoint."""
    person_a = Person("Joe")
    person_a.say_hello()
    person_b = Person("Michael")
    person_b.say_hello()
    # Example of calling a method


if __name__ == "__main__":
    main()