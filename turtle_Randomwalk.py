import turtle
from turtle import Turtle, Screen
import random
walk = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


directions = [0, 90, 180, 270]
walk.pensize(15)

for _ in range(200):
    walk.color(random_color())
    walk.forward(30)
    walk.setheading(random.choice(directions))
    walk.speed('fastest')

wait = Screen()
wait.exitonclick()
