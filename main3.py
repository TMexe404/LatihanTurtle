import turtle

t = turtle.Turtle()
# t.penup()
# t.goto(30, 135)
# t.pendown()
# t.dot(25)
def Pola(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(10)

Pola(60,135)
Pola(60,90)
Pola(60,45)

Pola(5,135)
Pola(5,90)
Pola(5,45)

Pola(-50,135)
Pola(-50,90)
Pola(-50,45)

s =110
t.forward(s)  # Forward turtle by s units
t.left(90)  # Turn turtle by 90 degree

# drawing second side
t.forward(s-20)  # Forward turtle by s units
t.left(90)  # Turn turtle by 90 degree

#drawing third side
t.forward(s)  # Forward turtle by s units
t.left(90)  # Turn turtle by 90 degree

# drawing fourth side
t.forward(s)  # Forward turtle by s units
t.left(90)  # Turn

t.write("pass Succes", font=(
        "Verdana", 16, "bold"))

turtle.done()