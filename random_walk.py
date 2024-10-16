import turtle
from random import random, choice, randint
from turtle import Turtle, Screen
timmy = Turtle()
turtle.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b

walk_distance = 30
timmy.speed("fastest")
timmy.pensize(3)
angle_range = [0, 90, 180, 270]
for _ in range(100):
    timmy.forward(walk_distance)
    timmy.setheading(choice(angle_range))
    timmy.color(random_color())
















screen = Screen()
screen.exitonclick()