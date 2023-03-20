from turtle import Screen, Turtle

t = Turtle()


def kvadrat():
    for tall in range(4):
        t.forward(90)
        t.left(90)
    t.exitonclick()



#kvadrat()


def snokrystal():
    for i in range(10):
        t.goto(0, 0)
        t.left(45)
        t.forward(50)
        t.left(-90)
        t.forward(50)

#snokrystal()

screen = Screen()
screen.tracer(False)

for angle in range(720):
    t.reset()
    t.hideturtle()
    t.left(angle)
    snokrystal()
    screen.update()

screen.tracer(True)
screen.mainloop()




def sirkel():
    t.goto(0, 0)
    for i in range(360):
        t.forward(1)
        t.left(1)


def sirkel2():
    t.goto(0, 5)
    for i in range(360):
        t.forward(1)
        t.left(1)

# irkel()
# sirkel2()

