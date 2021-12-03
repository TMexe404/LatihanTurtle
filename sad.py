import time
import turtle

turtle.title("sad")
t = turtle.Turtle()

t.color("black","yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

def rightEye():
    t.penup()
    t.goto(30, 135)
    t.pendown()
    t.dot(25)
def leftEye():
    t.penup()
    t.goto(-30, 135)
    t.pendown()
    t.dot(25)
def mouth():

    t.penup()
    t.goto(60, 60)
    t.pendown()
    t.setheading(120)
    t.circle(70, 120)

rightEye()
leftEye()
mouth()

time.sleep(1000)