# kali.py
from KaliMaaArt.basics import arc, deg2rad
import turtle
from math import sin
from KaliMaaArt.face_feature import *
import random, time

turtle.colormode(255)
turtle.screensize(canvheight=1000, canvwidth=100)
turtle.bgcolor(60, 80, 110)
turtle.tracer(2)

def draw():
    eyebrow('r', R1=300, a1=60, a2=85, R2=260)
    eyebrow('l', R1=300, a1=60, a2=85, R2=260)
    eye('third', R11=160, a11=90, a12=105, a13=130,
        a21=90, a22=100, a23=115, offset=2, r=42)
    eye('left', R11=160, a11=90, a12=105, a13=130,
        a21=90, a22=100, a23=115, offset=2, r=42)
    eye('right', R11=160, a11=90, a12=105, a13=130,
        a21=90, a22=100, a23=115, offset=2, r=42)
    bindi2()
    nose(l=170, which='kali')
    mouth(l=170)

def diwali_effects():
    # Draw glowing stars left and right
    deco = turtle.Turtle()
    deco.hideturtle()
    deco.penup()
    deco.color("gold")
    deco.goto(-220, 400)
    deco.write("🌟✨🌟", align="center", font=("Comic Sans MS", 26, "bold"))
    deco.goto(220, 400)
    deco.write("🌟✨🌟", align="center", font=("Comic Sans MS", 26, "bold"))

    # Animated glowing "Happy Diwali"
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, 400)  # just above Maa Kali’s head
    msg.color("gold")

    text = "Happy Diwali"
    colors = ["gold", "yellow", "orange", "red", "white"]

    # Typewriter-style animation
    for i, ch in enumerate(text):
        msg.color(colors[i % len(colors)])
        msg.write(ch, align="center", font=("Comic Sans MS", 40, "bold"))
        time.sleep(0.18)
        msg.undo()
        msg.write(text[: i + 1], align="center", font=("Comic Sans MS", 40, "bold"))

    # Glow pulse effect
    def pulse():
        for c in colors:
            msg.color(c)
            msg.clear()
            msg.write(text, align="center", font=("Comic Sans MS", 40, "bold"))
            time.sleep(0.2)
        turtle.ontimer(pulse, 1000)

    pulse()

    # --- Firecracker animation ---
    cracker = turtle.Turtle()
    cracker.hideturtle()
    cracker.speed(0)
    fire_colors = ["red", "yellow", "orange", "white", "blue", "violet", "green", "gold"]

    def fire_burst():
        cracker.clear()
        for _ in range(5):
            x = random.randint(-350, 350)
            y = random.randint(-50, 350)
            cracker.penup()
            cracker.goto(x, y)
            cracker.pendown()
            cracker.color(random.choice(fire_colors))
            for i in range(20):
                cracker.forward(45)
                cracker.backward(45)
                cracker.right(18)
        turtle.ontimer(fire_burst, 800)

    fire_burst()



try:
    draw()
    diwali_effects()
    print("\n🎇 Drawing complete — Enjoy Happy Diwali! 🎆")
    print("Close the window manually when done.")
    turtle.mainloop()  # keeps window open
except Exception as e:
    print("Error:", e)
    input("Press Enter to exit…")

