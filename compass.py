import turtle
import time
import math


def setup_screen():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor("#F0F0F0")
    screen.title("Enhanced Animated Compass")
    return screen


def create_compass(t):
    # Outer circle
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.color("#FF1493")
    t.begin_fill()
    t.circle(180)
    t.end_fill()

    # Inner circle
    t.penup()
    t.goto(0, -160)
    t.pendown()
    t.color("#FF69B4")
    t.begin_fill()
    t.circle(160)
    t.end_fill()

    # Center point
    t.penup()
    t.goto(0, 0)
    t.dot(10, "white")

    # Draw compass points
    main_points = [("N", 90), ("E", 0), ("S", 270), ("W", 180)]
    sub_points = [("NE", 45), ("SE", 315), ("SW", 225), ("NW", 135)]

    for label, angle in main_points:
        draw_compass_point(t, label, angle, 140, ("Arial", 20, "bold"))

    for label, angle in sub_points:
        draw_compass_point(t, label, angle, 130, ("Arial", 14, "normal"))


def draw_compass_point(t, label, angle, distance, font):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(distance)
    t.color("white")
    t.write(label, align="center", font=font)


def create_needle(t):
    t.penup()
    t.goto(0, 0)
    t.color("white")
    t.shape("triangle")
    t.shapesize(0.8, 4)
    t.setheading(90)
    return t


def animate_needle(needle):
    angles = list(range(0, 361, 5))
    for angle in angles:
        needle.setheading(angle)
        time.sleep(0.05)


def draw_tick_marks(t):
    for angle in range(0, 360, 6):
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(155)
        t.pendown()
        t.forward(5)


def main():
    screen = setup_screen()

    compass_turtle = turtle.Turtle()
    compass_turtle.hideturtle()
    compass_turtle.speed(0)

    create_compass(compass_turtle)
    draw_tick_marks(compass_turtle)

    needle = create_needle(turtle.Turtle())

    while True:
        animate_needle(needle)


if __name__ == "__main__":
    main()
