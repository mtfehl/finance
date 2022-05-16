from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
i: int = 0
leo.color(135, 0, 223)
leo.penup()
leo.goto(-150, -50)
leo.pendown()
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
side_length: int = 300
bob.penup()
bob.goto(-150, -50)
bob.pendown()
bob.speed(100)
i: int = 0
while (i < 200):
    bob.forward(side_length)
    bob.left(120.5)
    i = i + 1
    side_length = side_length * 0.97


jon: Turtle = Turtle()

done()
