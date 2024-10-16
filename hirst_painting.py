import turtle
from turtle import Turtle, Screen
from random import choice

# import colorgram
# colors = colorgram.extract('image.jpg', 91)
# color_in_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_in_rgb.append(new_color)

color_list = [(249, 228, 236), (224, 242, 230), (243, 236, 68), (183, 75, 21), (228, 154, 7), (234, 72, 134), (200, 163, 114), (216, 228, 238), (202, 131, 191), (116, 168, 241), (220, 231, 5), (76, 173, 37), (71, 103, 230), (125, 205, 126), (45, 111, 39), (75, 37, 30), (151, 74, 156), (60, 100, 153), (241, 162, 196), (244, 55, 28), (187, 28, 12), (203, 13, 78), (140, 216, 237), (248, 170, 166), (76, 67, 47), (148, 185, 244), (159, 212, 173), (253, 10, 4), (42, 90, 32), (98, 141, 146), (96, 15, 16), (46, 54, 199), (255, 5, 7)]
turtle.colormode(255)
toddy = Turtle()
toddy.hideturtle()
toddy.speed("fastest")
toddy.penup()

toddy.setheading(220)
toddy.forward(300)
toddy.setheading(0)

for dots in range(1, 101):
    toddy.dot(20, choice(color_list))
    toddy.forward(50)

    if dots % 10 == 0:
        toddy.setheading(90)
        toddy.forward(50)
        toddy.setheading(180)
        toddy.forward(500)
        toddy.setheading(360)


screen = Screen()
screen.exitonclick()