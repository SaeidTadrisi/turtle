from turtle import Turtle, Screen

screen = Screen()
winny = Turtle()

def forward():
    winny.forward(10)

def backward():
    winny.backward(10)

def counter_clockwise():
    new_heading = winny.heading() + 10
    winny.setheading(new_heading)

def clockwise():
    new_heading = winny.heading() - 10
    winny.setheading(new_heading)

def clear():
    winny.reset()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")


screen.exitonclick()