import random
from turtle import Turtle, Screen
race_is_on = False
screen = Screen()
screen.title("Turtle Race")
screen.bgcolor('black')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Put your bet on a color")
color = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
y_coordinates = [-75, -45, -15, 15, 45, 75]
my_turtles = []
for turtle_index in range(0, 6):
    a = Turtle(shape="turtle")
    a.color(color[turtle_index])
    a.penup()
    a.goto(x=-230, y=y_coordinates[turtle_index])
    my_turtles.append(a)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win. The winner is {winner}")
            else:
                print(f"You loose. The winner is {winner}")
            race_is_on = False
        distance = random.randint(0, 10)
        turtle.forward(distance)
screen.exitonclick()