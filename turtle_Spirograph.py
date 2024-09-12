import turtle as t
import random
spi = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


spi.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spi.color(random_color())
        spi.circle(100)
        spi.setheading(spi.heading() + 10)


draw_spirograph(5)
spiro = t.Screen()
spiro.exitonclick()

