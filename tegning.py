from turtle import Screen, Turtle
from itertools import cycle

COLORS = ["orange", "blue", "red", "green", "purple"]

def draw_character():
    color = cycle(COLORS)

    for _ in range(36):
        for _ in range(3):
            tegne.color(next(color))
            tegne.forward(80)
            tegne.right(120)

        tegne.left(10)

    for _ in range(36):
        for _ in range(4):
            tegne.color(next(color))
            tegne.forward(70)
            tegne.right(90)

        tegne.left(10)

    for radius in range(10, 90, 10):
        tegne.color(next(color))
        tegne.circle(radius, 180)

screen = Screen()
screen.tracer(False)

tegne = Turtle()

x = 10000

while x > 1:
    for angle in range(720):
        tegne.reset()
        tegne.hideturtle()
        tegne.left(angle)
        draw_character()
        screen.update()
        x -= 1

screen.tracer(True)
screen.mainloop()