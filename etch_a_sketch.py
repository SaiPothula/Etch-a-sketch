# Etch-A-Sketch drawing using turtle package
import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()


def fwd():
    my_turtle.forward(10)


def bkwd():
    my_turtle.backward(10)


def cckws():
    my_turtle.circle(20, 20)


def ckws():
    my_turtle.circle(20, -20)


def clr():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

my_screen.listen()
# action = {"w": fwd, "s": bkwd, "a": cckws, "d": ckws, "c": clr}
my_screen.onkey(fwd, "w")
my_screen.onkey(bkwd, "s")
my_screen.onkey(cckws, "a")
my_screen.onkey(ckws, "d")
my_screen.onkey(clr, "c")
my_screen.exitonclick()