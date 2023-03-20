from turtle import Turtle,Screen

t = Turtle()
s = Screen()

def hexa():
    for i in range(0,(int(360/45))):
        t.forward(100)
        t.right(45)

def sirkel():
    t.goto(0,0)
    for i in range(360):
        t.forward(1)
        t.left(1)
    for i in range(360):
        t.forward(1)
        t.left(1)
    s.exitonclick()

#sirkel()

def juksesirkler():
    t.circle(50)
    t.penup()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.pendown()
    t.circle(100)
    s.exitonclick()

#juksesirkler()


def snokrystal(size, x, y):
    t.goto(x, y)
    t.pendown()
    t.pensize(10)
    for i in range(6):
        t.forward(size)
        t.goto(x, y)
        t.left(60)

    for i in range(6):
        t.forward(size / 4 * 3)
        t.left(45)
        t.forward(size / 3)
        t.right(45)
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.forward(size / 4 * 3)
        t.right(45)
        t.forward(size / 3)
        t.left(45)
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.left(60)

    t.penup()
    s.exitonclick()

snokrystal(100, 0, 0)