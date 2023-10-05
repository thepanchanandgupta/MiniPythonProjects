import turtle
from turtle import *
import random

timmy = Turtle()
tt_turtle_obj = Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]
turn = 15
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
timmy.shape("turtle")
sides = 3

for _ in range(sides):
    while sides <= 50:
        timmy.color(random.choice(colours))
        angles = 360 / sides
        timmy.forward(10)
        timmy.right(angles)
        sides += 1


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour: tuple[int, int, int] = (r, g, b)
    return colour


for i in range(turn):
    timmy.pensize(15)
    timmy.width(5)
    timmy.color(random_colour())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

timmy.pensize(1)
timmy.width(1)
timmy.speed("fastest")
my_screen = Screen()
my_screen.bgcolor()
my_screen.exitonclick()
