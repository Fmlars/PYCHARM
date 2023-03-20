from turtle import Screen, Turtle

t = Turtle()

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
