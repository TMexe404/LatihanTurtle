
import turtle
from turtle import *
import time

turtle.title("LOVE")
ttl = turtle.Turtle()

def curve():
    for i in range(200):
        ttl.right(1)
        ttl.forward(1)
        print(i)

def heart():
    ttl.fillcolor('red')
    ttl.begin_fill()
    ttl.left(140)
    ttl.forward(113)
    curve()
    ttl.left(120)
    curve()
    ttl.forward(112)
    ttl.end_fill()

def txt():
    ttl.up()
    ttl.setpos(-75, 78)
    ttl.down()
    ttl.color('white')
    ttl.write("SAD     Happy", font=(
        "Verdana", 16, "bold"))

heart()
txt()

ttl.penup()
ttl.goto(50, 150)
ttl.pendown()

def drawing_rose(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)
for _ in range(9):
    ttl.color("black", "white")
    ttl.begin_fill()
    drawing_rose(ttl, 60)
    ttl.left(360 / 9)
    ttl.end_fill()


time.sleep(1000)

# To hide turtle
# ttl.ht()