from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape('turtle')

colors = ['black', 'gold', 'green', 'red', 'purple', 'brown', 'pink', 'blue']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_sides)


timmy = Screen()
timmy.exitonclick()
