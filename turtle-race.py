import time
import turtle
import random
from turtle import Turtle
from random import randint

# Window Setup
window = turtle.Screen()
window.title("TURTLE RACE - MAULANA ID")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("TURTLE RACE", font=("Arial", 30, "bold"))
turtle.penup()

# Dirt
turtle.setpos(-400, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

# Finish Lane
def white():
    stamp_size = 20
    square_size = 15
    finish_lane = 200

    turtle.color("white")
    turtle.shape("square")
    turtle.shapesize(square_size / stamp_size)
    turtle.penup()

    for x in range(10):
        turtle.setpos(finish_lane, (150 - (x * square_size * 2)))
        turtle.stamp()

    for y in range(10):
        turtle.setpos(finish_lane + square_size, ((150 - square_size) - (y * square_size * 2)))
        turtle.stamp()
white()

def black():
    stamp_size = 20
    square_size = 15
    finish_lane = 200

    turtle.color("black")
    turtle.shape("square")
    turtle.shapesize(square_size / stamp_size)
    turtle.penup()

    for a in range(10):
        turtle.setpos(finish_lane + square_size, ((165 - square_size) - (a * square_size * 2)))
        turtle.stamp()

    for z in range(10):
        turtle.setpos(finish_lane, (135 - (z * square_size * 2)))
        turtle.stamp()
black()
        
turtle.hideturtle()

# Turtle 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("red")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

# Turtle 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("orange")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

# Turtle 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("yellow")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

# Turtle 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("blue")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

time.sleep(1)

# Moving Turtle
for b in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))
    
turtle.exitonclick()

