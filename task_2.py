import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    corners = 6
    angle = 360/corners

    for i in range(6):
        koch_curve(t, order, size)
        t.left(angle)

    window.mainloop()

def parse_input(user_input: str) -> int:
    return int(user_input)

user_input = input("Enter recursion level: ")

draw_koch_curve(parse_input(user_input))