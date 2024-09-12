import turtle as t
import random
# import colorgram as cg

# rgb_colors = []
# colors = cg.extract("turtleHirst_image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

hirst = t.Turtle()
t.colormode(255)
hirst.speed('fastest')
hirst.penup()
hirst.hideturtle()
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
              (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165),
              (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9),
              (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167),
              (77, 234, 202), (52, 234, 243), (3, 67, 40)]

hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    hirst.dot(20, random.choice(color_list))
    hirst.forward(50)

    if dot_count % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)

Hirst = t.Screen()
Hirst.exitonclick()
