#multi colored lines with python turtle


import turtle
import random

screen = turtle.Screen()
turtle.setup(1024, 768)
screen.bgcolor("#FFFFE0")

# the number of turtles to create and what color to create them with
colors = ["black", "red", "orange", "green"]

# create a new turtle with a certain color
def create_turtle(color):
        t = turtle.Turtle()
        t.speed(0)
        t.width(3)
        t.shape("turtle")
        t.color(color)
        return t

# create a list of turtles from a list of colors
def create_turtles(colors):
        turtles = []
        for color in colors:
                t = create_turtle(color)
                turtles.append(t)
        return turtles

def move_turtle(t):
        t.stamp()
        angle = random.randint(-90, 90)
        t.right(angle)
        distance = random.randint(50, 100)
        t.forward(distance)

turtles = create_turtles(colors)

for move in range(100):
        for a_turtle in turtles:
                move_turtle(a_turtle)
                
