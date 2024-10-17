from random import randint, choice
from turtle import Turtle, Screen

race_start = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-60, -30, 0, 30, 60, 90]
all_turtles =[]

def random_forward(turtle_to_move):
    turtle_to_move.forward(randint(0,10))

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_start = True

while race_start:
    for turtle in all_turtles:
        random_forward(turtle)
        if turtle.xcor() >= 220:
            race_start = False
            if turtle.color()[0] == user_bet:
                print("You Win!")
            else:
                print(f"You lost, {turtle.color()[0]} Won")

screen.exitonclick()