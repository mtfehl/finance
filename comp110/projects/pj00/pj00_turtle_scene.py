"""Space and its planetary orbits. Challenge points in 'earth_land' function.""" 

__author__ = "720321206"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """Entrypoint of the scene."""
    turtie: Turtle = Turtle()
    background(turtie, -1000, 1000, 2000.0)
    sun(100)
    asteroid_belt(200.0, -70.0, 5.0)
    orbit(0, -25, 125.0)
    planet("mercury", 125, 75, 10.5)
    orbit(0, -50, 150.0)
    planet("venus", 125, 175, 12.5)
    orbit(0, -75, 175.0)
    planet("earth", -175, 100, 13.0)
    orbit(0, -100, 200.0)
    planet("mars", -75, -100, 11.5)
    earth_land()
    spaceship(turtie, -350, 50)
    stars(400, 300, 40)
    stars(-300, -300, 20)
    stars(-400, 200, 10)
    stars(200, 350, 20)
    stars(300, 300, 15)
    stars(-250, -100, 20)
    stars(450, -50, 5)
    stars(500, -350, 25)
    stars(600, -400, 35)
    stars(-600, -300, 50)
    stars(-500, 400, 24)
    stars(-525, 80, 10)
    stars(560, 200, 13)
    done()


def background(turtie: Turtle, x: int, y: int, width: float) -> None:
    """A black background to represent empty space."""
    turtie.speed(0)
    turtie.hideturtle()
    if (x, y) == (-350, 50):
        turtie.color("green")
    else:
        turtie.color("black")
    turtie.penup()
    turtie.goto(x, y)
    turtie.pendown()
    turtie.begin_fill()
    i: int = 0
    while (i < 4):
        turtie.forward(width)
        turtie.right(90)
        i += 1
    turtie.end_fill()


def sun(radius: int) -> None:
    """The sun, the center of our solar system."""
    turt: Turtle = Turtle()
    turt.speed(10)
    turt.hideturtle()
    turt.color("yellow")
    turt.begin_fill()
    turt.circle(radius) 
    turt.end_fill()


def orbit(x: int, y: int, radius: float) -> None:
    """The orbit path of each planet."""
    tortle: Turtle = Turtle()
    tortle.speed(10)
    tortle.hideturtle()
    tortle.color("white")
    tortle.penup()
    tortle.goto(x, y)
    tortle.pendown()
    if radius == 10:
        tortle.begin_fill()
        tortle.circle(radius)
        tortle.end_fill()
    else:
        tortle.circle(radius)


def planet(which: str, x: float, y: float, radius: float) -> None:
    """The basic structure & color of each planet."""
    king_turtle_III: Turtle = Turtle()
    king_turtle_III.speed(7)
    king_turtle_III.hideturtle()
    king_turtle_III.penup()
    king_turtle_III.goto(x, y)
    king_turtle_III.pendown()
    if which == "mercury":
        king_turtle_III.color(214, 208, 192)
    if which == "venus":
        king_turtle_III.color(225, 167, 0)
    if which == "earth":
        king_turtle_III.color(9, 63, 220)
    if which == "mars":
        king_turtle_III.color(220, 140, 9)
    king_turtle_III.begin_fill()
    king_turtle_III.circle(radius)
    king_turtle_III.end_fill()


def earth_land() -> None:
    """Here, I'm attempting to creating a perception of land on my Earth planet, and I feel pretty content with it."""
    tort: Turtle = Turtle()
    tort.hideturtle()
    tort.speed(5)
    tort.penup()
    tort.goto(-175, 105)
    tort.pendown()
    tort.color(0, 154, 5)
    i: int = 0
    radius: float = 10.0
    while (i < 5):
        """By creating a while loop here, 
        I was able to continuously make smaller circles to take up a larger surface area of Earth."""
        tort.circle(radius)
        radius *= 0.8
        i += 1


def asteroid_belt(x: float, y: float, radius: float) -> None:
    """The belt of asteroids surrounding the four innermost planets."""
    asturtle: Turtle = Turtle()
    asturtle.speed(0)
    asturtle.color(100, 100, 100)
    asturtle.penup()
    asturtle.goto(x, y)
    asturtle.pendown()
    i: int = 0
    left: float = 90.0
    forward: float = 350.0
    while (i < 70):
        asturtle.begin_fill()
        asturtle.circle(radius)
        asturtle.end_fill()
        asturtle.penup()
        asturtle.left(left)
        asturtle.forward(forward)
        asturtle.pendown()
        left *= 0.9987
        forward *= 0.99995
        i += 1


def stars(x: int, y: int, size: int) -> None:
    """The other stars and suns in the galaxy."""
    kurt_the_turt: Turtle = Turtle()
    kurt_the_turt.penup()
    kurt_the_turt.speed(10)
    kurt_the_turt.goto(x, y)
    kurt_the_turt.pendown()
    kurt_the_turt.color(255, 255, 255)
    kurt_the_turt.left(80)
    i: int = 0
    kurt_the_turt.begin_fill()
    while (i < 4):
        kurt_the_turt.forward(size)
        kurt_the_turt.right(165)
        kurt_the_turt.forward(size)
        kurt_the_turt.left(120)
        kurt_the_turt.forward(10)
        kurt_the_turt.right(165)
        kurt_the_turt.forward(10)
        kurt_the_turt.left(120)
        i += 1
    kurt_the_turt.end_fill()


def triangle(x: int, y: int, length: int) -> None:
    """Base shape of a triangle."""
    tart: Turtle = Turtle()
    tart.hideturtle()
    tart.penup()
    tart.goto(x, y)
    tart.pendown()
    tart.color("green")
    tart.begin_fill()
    i: int = 0
    while (i < 3):
        tart.forward(length)
        tart.left(120)
        i += 1
    tart.end_fill()
    

def spaceship(turtie: Turtle, x: int, y: int) -> None:
    """A lil spaceship going off to explore the universe for aliens!"""
    toot: Turtle = Turtle()
    toot.hideturtle()
    triangle(x, y, 40)
    background(turtie, x, y, 40)
    triangle((x - 10), (y - 50), 15)
    triangle((x + 32), (y - 50), 15)
    orbit((x + 20), (y - 7), 10)


if __name__ == "__main__":
    main()