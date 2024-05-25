import turtle
from turtle import Turtle, Screen
import random

color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57)]

tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)


def draw_dot():
    for i in range(11):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.penup()
        tim.forward(50)


def new_position(height, x_cor):
    tim.sety(height)
    tim.setx(x_cor)


coordinates = tim.pos()
new_height = coordinates[1]
x_cor = coordinates[0]
for i in range(11):
    draw_dot()
    new_height += 50
    new_position(new_height, x_cor)

screen = Screen()
screen.exitonclick()