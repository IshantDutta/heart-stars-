import turtle as t
import math as m
import random as r
import time


# Screen setup

s = t.Screen()
s.setup(800, 800)
s.bgcolor("black")
s.tracer(0)

# Neon pink
NEON_PINK = "#ff1493"

N = 500
stars = []


# Create heart-shaped targets

for i in range(N):

    a = 2 * m.pi * (i / N)

    # Heart equation
    heart_x = 16 * m.sin(a) ** 3

    heart_y = (
        13 * m.cos(a)
        - 5 * m.cos(2 * a)
        - 2 * m.cos(3 * a)
        - m.cos(4 * a)
    )

    # Scale heart
    tx = heart_x * 15 + r.uniform(-12, 12)
    ty = heart_y * 15 + r.uniform(-12, 12)

    # Random starting position
    sx = r.randint(-350, 350)
    sy = r.randint(-350, 350)

    # Random star size
    size = r.uniform(2.5, 5.5)

    stars.append((sx, sy, tx, ty, size))



# Turtle setup

p = t.Turtle()
p.hideturtle()
p.speed(0)
p.penup()



# Draw a star

def draw_star(x, y, size):

    p.pencolor(NEON_PINK)
    p.width(1)

    for angle in (0, 45, 90, 135):

        rad = m.radians(angle)

        dx = m.sin(rad) * size
        dy = m.cos(rad) * size

        p.goto(x - dx, y - dy)
        p.pendown()

        p.goto(x + dx, y + dy)

        p.penup()



# Smooth easing function

def smooth_step(x):

    return x * x * x * (x * (x * 6 - 15) + 10)



# Animation

steps = 180

for frame in range(steps + 1):

    p.clear()

    progress = frame / steps

    # Smooth acceleration and deceleration
    eased = smooth_step(progress)

    for sx, sy, tx, ty, size in stars:

        cx = sx + (tx - sx) * eased
        cy = sy + (ty - sy) * eased

        draw_star(cx, cy, size)

    s.update()

    # Smaller delay = smoother animation
    time.sleep(0.015)


# Keep window open
t.done()