import turtle
from turtle import Turtle, Screen
from random import Random, random, randint

tonny = Turtle()
turtle.colormode(255)
tonny.speed("fastest")

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b

def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tonny.color(random_color())
        tonny.setheading(tonny.heading() + size)
        tonny.circle(50)

draw_spirograph(2)


screen = Screen()
screen.exitonclick()
