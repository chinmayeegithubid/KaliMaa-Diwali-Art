import turtle
from math import pi, sin

def deg2rad(d):
    return d * pi / 180

def arc(turt, angle, radius, direction='r'):
    if direction not in ['r', 'l']:
        raise NameError("InvalidDirectionError: 'r' for right and 'l' for left")
    
    forw = deg2rad(radius)
    turt.forward(forw / 2)

    if direction == 'r':
        for _ in range(angle - 1):
            turt.right(1)
            turt.forward(forw)
        turt.right(1)
        turt.forward(forw / 2)

    if direction == 'l':
        for _ in range(angle - 1):
            turt.left(1)
            turt.forward(forw)
        turt.left(1)
        turt.forward(forw / 2)

def arcs(turt, direction, R1, a1, a2):
    if direction not in ['r', 'l']:
        raise NameError("InvalidDirectionError: 'r' for right and 'l' for left")
    
    # Compute R2 using circle geometry
    R2 = R1 * sin(deg2rad(a1 / 2)) / sin(deg2rad(a2 / 2))

    if direction == 'r':
        turt.begin_fill()
        turt.left(a1 / 2)
        arc(turt, a1, R1)
        turt.left(a1 / 2 + 90 + 90 - a2 / 2)
        arc(turt, a2, R2, 'l')
        turt.end_fill()

    if direction == 'l':
        turt.begin_fill()
        turt.right(a1 / 2)
        arc(turt, a1, R1, 'l')
        turt.right(a1 / 2 + 90 + 90 - a2 / 2)
        arc(turt, a2, R2)
        turt.end_fill()
