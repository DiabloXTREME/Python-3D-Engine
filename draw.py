import turtle


class draw:
    global t

    def __init__(self):
        t = turtle.Turtle
        t.speed(0)

    def point(self, x, y):
        if not isinstance(x, int) or isinstance(y, int):
            raise TypeError("The point function only takes integers")
