from random import choice
from turtle import Turtle, Screen

tinny = Turtle()
tinny.hideturtle()
colors = ["firebrick", "dark slate blue", "yellow", "dark green", "navy", "black", "magenta", "indian red", "dark gray"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tinny.forward(100)
        tinny.right(angle)

for shape_side_n in range(3,20):
    tinny.color(choice(colors))
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()
