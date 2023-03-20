import turtle

def draw_square(length, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.penup()

def draw_divided_square(length, x, y):
    draw_square(length, x, y)
    draw_square(length/2, x+length/4, y+length/4)
    draw_square(length/2, x-length/4, y+length/4)
    draw_square(length/2, x+length/4, y-length/4)
    draw_square(length/2, x-length/4, y-length/4)

draw_divided_square(100, 0, 0)
turtle.exitonclick()
