from KaliMaaArt.basics import arc, deg2rad, arcs
import turtle
from math import sin,sqrt,cos,tan

def eyebrow(which, R1=370, a1=50, a2=78, R2=290):
    turt = turtle.Turtle()

    if which not in ['r', 'l']:
        raise NameError("InvalidDirectionError: 'r' for right and 'l' for left")

    turt.hideturtle()
    turt.fillcolor(0, 0, 0)
    turt.color(0, 0, 0)

    if which == 'l':
        turt.penup()
        turt.left(10)
        turt.goto(65, 100)
        turt.pendown()

        turt.begin_fill()
        turt.left(a1/2)
        arc(turt, a1, R1)
        turt.left(a1/2 +90 +90-a2/2)
        arc(turt,a2-12,R2,'l')
        arc(turt,80,20,'l')
        turt.end_fill()

    if which == 'r':
        turt.penup()
        turt.left(170)
        turt.goto(-65,100)
        turt.pendown()

        turt.begin_fill()
        turt.right(a1/2)
        arc(turt, a1, R1,'l')
        turt.right(a1/2+90+90-a2/2)
        arc(turt,a2-12,R2)
        arc(turt, 80, 20)
        turt.end_fill()


def eye(which,R11=180,a11=80,a12=105,a13=125,
        a21=80,a22=90,a23=100,r=45,offset=5):

    if which == 'third':
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.penup()
        turt.goto(0, 150)
        turt.pendown()
        turt.seth(90)
        turt.width(1)
        turt.fillcolor(255, 0, 0)  # red fill
        turt.color(255, 0, 0)      # red outline

        # First arcs
        R12 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a12/2))
        arcs(turt, 'r', R12, a12, a13)

        # Second arcs
        R21 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a21/2))

        turt.seth(90)
        R22 = R21 * sin(deg2rad(a21/2))/sin(deg2rad(a22/2))
        arcs(turt, 'l', R22, a22, a23)

        # Reset for inner details
        turt.penup()
        turt.goto(0, 150)
        turt.left(90)
        turt.pendown()
        turt.seth(90)

        # Black outline of eye
        turt.fillcolor(0, 0, 0)
        turt.color(0, 0, 0)
        turt.width(5)
        arcs(turt, 'r',R11,a11,a12)

        turt.left(180-a12/2)
        turt.fillcolor(0, 0, 0)
        turt.color(0, 0, 0)
        arcs(turt,'l',R21,a21,a22)
        turt.width(1)

        # White fill for eyeball
        turt.fillcolor(255, 255, 255)
        turt.begin_fill()
        turt.seth(90)
        turt.left(a11/2)
        arc(turt,a11,R11)
        turt.seth(-90)
        turt.left(a21/2)
        arc(turt,a21,R21)
        turt.end_fill()

        turt.fillcolor(0, 0, 0)
        turt.penup()
        turt.seth(90+offset)
        turt.forward(70)
        turt.pendown()
        turt.seth(0)
        turt.begin_fill()
        turt.circle(r)
        turt.end_fill()
        turt.seth(90)
        turt.forward(r-10)
        turt.pendown()
        turt.seth(0)
        turt.fillcolor(255, 255, 255)
        turt.begin_fill()
        turt.circle(10)
        turt.end_fill()

    elif which == 'left':
        turt = turtle.Turtle()
        turt.hideturtle()

        R12 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a12/2))  # ✅ define R12
       ## R21 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a12/2))
        turt.penup()
        turt.goto(95, 45)
        turt.seth(10)
        turt.width(1)
        turt.fillcolor(255, 0, 0)
        turt.color(255, 0, 0)
        arcs(turt,'r',R12,a12,a13)

        R21 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a21/2))
        turt.seth(10)
        R22 = R21*sin(deg2rad(a21/2))/sin(deg2rad(a22/2))
        arcs(turt,'l',R22,a22,a23)

        turt.width(5)
        turt.penup()
        turt.goto(95, 45)
        turt.seth(10)
        turt.fillcolor(0, 0, 0)
        turt.color(0, 0, 0)
        turt.pendown()
        arcs(turt,'r',R11,a11,a12)
        turt.left(180-a12/2)

        R21 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a21/2))
        arcs(turt,'l',R21,a21,a22)
        turt.width(1)
        turt.fillcolor(255, 255, 255)
        turt.begin_fill()
        turt.seth(10)
        turt.left(a11/2)
        arc(turt,a11,R11)
        turt.seth(190)
        turt.left(a21/2)
        arc(turt,a21,R21)
        turt.end_fill()

        turt.fillcolor(0, 0, 0)
        turt.penup()
        turt.seth(10+offset)
        turt.forward(70)
        turt.pendown()
        turt.seth(-80)
        turt.begin_fill()
        turt.circle(r)
        turt.end_fill()
        turt.seth(10)
        turt.forward(r-10)
        turt.pendown()
        turt.seth(-80)
        turt.fillcolor(255, 255, 255)
        turt.begin_fill()
        turt.circle(10)
        turt.end_fill()

    elif which == 'right':
        turt = turtle.Turtle()
        turt.hideturtle()
        R12 = R11 * sin(deg2rad(a11/2))/sin(deg2rad(a12/2))
        turt.penup()
        turt.goto(-95, 45)
        turt.seth(180-10)
        turt.width(1)
        turt.fillcolor(255,0,0)
        arcs(turt, 'l',R12,a12,a13)
        R21 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a21/2))
        turt.seth(170)
        R22 = R21*sin(deg2rad(a21/2))/sin(deg2rad(a22/2))
        arcs(turt, 'r', R22, a22, a23)

        turt.width(5)
        turt.penup()
        turt.goto(-95, 45)
        turt.seth(170)
        turt.fillcolor(0, 0, 0)
        turt.color(0, 0, 0)
        turt.pendown()
        arcs(turt,'l',R11,a11,a12)
        turt.right(180-a12/2)

        R21 = R11*sin(deg2rad(a11/2))/sin(deg2rad(a21/2))
        arcs(turt, 'r', R21, a21, a22)
        turt.width(1)

        turt.fillcolor(255, 255, 255)
        turt.begin_fill()
        turt.seth(170)
        turt.right(a11/2)
        arc(turt,a11,R11,'l')   # ✅ Correct
        turt.seth(-10)
        turt.right(a21/2)
        arc(turt,a21,R21,'l')   # ✅ Added missing a22
        turt.end_fill()


        turt.fillcolor(0, 0, 0)
        turt.penup()
        turt.seth(170-offset)
        turt.forward(70)
        turt.pendown()
        turt.seth(-100)
        turt.begin_fill()
        arc(turt,360,r,'r') 
        turt.end_fill()
        turt.seth(170)
        turt.forward(r-10)
        turt.pendown()
        turt.seth(-100)
        turt.fillcolor(255, 255, 255)
        turt.begin_fill()
        arc(turt,360,10,'r')
        turt.end_fill()

    else:
        raise NameError("InvalidChoiceError: accepted values are 'third', 'left', 'right'")


def bindi(width=70, a1=200, a2=220):
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.width(2)

    R1 = width/sin(deg2rad(a1/2))
    turt.penup()
    turt.goto(-width, 220)
    turt.fillcolor(200,0,0)
    arcs(turt,'l',R1,a1,a2)

    turt.goto(0,75)
    turt.seth(0)
    turt.pendown()
    turt.width(8)
    turt.color(175,0,0)
    turt.fillcolor(255,0,0)
    turt.begin_fill()
    turt.circle(18)
    turt.end_fill()

def bindi2(width=50, a1=190, a2=210):
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.width(2)

    R1 = width/sin(deg2rad(a1/2))
    turt.penup()
    turt.goto(-width,180)
    turt.fillcolor(240,240,240)
    arcs(turt,'l',R1,a1,a2)

    turt.goto(0, 80)
    turt.seth(0)
    turt.pendown()
    turt.width(5)
    turt.color(255,0,0)
    turt.fillcolor(255,50,0)
    turt.begin_fill()
    turt.circle(12)
    turt.end_fill()


def nose(width=40,a1=200,a2=210,l=220,r=65,a=49,R2=30,
         a21=195,a22=205,which='kali'):
    turt = turtle.Turtle()
    turt.hideturtle()

    if which == 'kali':
        turt.fillcolor(30,40,55)
        turt.color(30,40,55)

    turt.penup()
    turt.goto(65, 100)
    turt.pendown()
    turt.seth(220)
    arc(turt,a,r,'l')
    turt.forward(l)

    turt.penup()
    turt.goto(-65, 100)
    turt.pendown()
    turt.seth(-40)
    arc(turt,a,r,'r')
    turt.forward(l)

    R1 = width/sin(deg2rad(a1/2))
    turt.penup()
    turt.goto(-width,-l+45)
    turt.seth(0)
    turt.pendown()
    arcs(turt,'l',R1,a1,a2)

    turt.width(2)
    turt.penup()
    turt.goto(-width,-l + 30)
    turt.pendown()
    turt.seth(120)
    arcs(turt,'r',R2,a21,a22)

    turt.penup()
    turt.goto(width,-l + 30)
    turt.pendown()
    turt.seth(60)
    arcs(turt,'l',R2,a21,a22)

    def nosering(R=70, arc1=335):
        turt.penup()
        turt.goto(width+25,-l+50)
        turt.pendown()
        turt.width(3)

        if which == 'kali':
            turt.color(30,40,55)
            turt.dot()
            turt.width(1)
            turt.seth(269)
            turt.fillcolor(200,200,200)
            turt.color(200,200,200)
        arcs(turt,'r',R,arc1, arc1+1)
        turt.penup()
        turt.seth(-20)
        turt.forward(2*R+5)
        if which == 'kali':
            turt.color(170, 0, 0)
            turt.fillcolor(170, 0, 0)

        turt.pendown()
        turt.begin_fill()
        turt.circle(20)
        turt.end_fill()
        turt.left(85)
        turt.forward(27)
        turt.fillcolor(255,255,255)
        turt.begin_fill()
        turt.circle(5)
        turt.end_fill()

    nosering()


def smile(R1=450,R2=400,l=220,a1=12,a2=8,th1=20,th2=40):
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.width(7)
    turt.color(160,0,0)
    turt.fillcolor(255,51,35)

    w = 2*R1*sin(deg2rad(a1/2))*cos(deg2rad(th1))+2*R2*sin(deg2rad(a2/2))*cos(deg2rad(th2))
    turt.penup()
    turt.goto(-w,-l-80)
    turt.pendown()

    turt.begin_fill()
    turt.seth(th1-a1/2)
    arc(turt,a1,R1,'l')
    turt.right(th1+th2+a1/2+a2/2)
    arc(turt,a2,R2,'l')
    turt.right(th1+th2+a1/2+a2/2)
    arc(turt,a1,R1,'l')
    turt.seth(10)

    turt.width(5)
    l = 20
    a = 20
    move = l/cos(deg2rad(a/2))
    r = l*tan(deg2rad(a/2))

    turt.forward(move)
    turt.left(a/2)

    arc(turt,180,r,'l')
    turt.left(a/2)
    turt.forward(move)
    turt.width(7)
    turt.right(20)

    L = w/cos(deg2rad(a/2))
    turt.forward(L)
    turt.right(20)
    turt.forward(L)

    turt.seth(170)
    l = 20
    a = 20
    move = l/cos(deg2rad(a/2))
    r = l*tan(deg2rad(a/2))

    turt.width(5)
    turt.forward(move)
    turt.right(a/2)

    arc(turt,180, r,'r')
    turt.right(a/2)
    turt.forward(move)
    turt.width(7)
    turt.left(20)

    turt.end_fill()
    turt.forward(25)
    turt.right(70)
    turt.begin_fill()
    angle = 110
    tilt = 90 - angle / 2-10
    w2 =-turt.xcor()
    R = w2/(2*sin(deg2rad(angle / 2))*cos(deg2rad(tilt)))

    arc(turt, angle, R, 'l')

    turt.seth(-turt.heading())

    arc(turt,angle,R,'l')
    turt.seth(90)
    turt.forward(L-25)
    turt.right(20)
    turt.forward(L-25)
    turt.end_fill()


def mouth(R1=450,R2=400,l=220,a1=12,a2=8,th1=20,th2=30):
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.width(7)
    turt.color(160,0,0)
    turt.fillcolor(220,0,0)

    w = 2*R1*sin(deg2rad(a1/2))*cos(deg2rad(th1)) + 2*R2*sin(deg2rad(a2/2))*cos(deg2rad(th2))
    turt.penup()
    turt.goto(-w,-l-80)
    turt.pendown()

    turt.begin_fill()
    turt.seth(th1 - a1/2)
    arc(turt,a1,R1,'l')
    turt.right(th1+th2+a1/2+a2/2)
    arc(turt,a2,R2,'l')
    turt.seth(th2 - a2/2)
    arc(turt,a2,R2,'l')
    turt.right(th1+th2+a1/2+a2/2)
    arc(turt,a1,R1,'l')
    L = w/cos(deg2rad(3))
    turt.seth(183)
    turt.forward(L)
    turt.seth(177)
    turt.forward(L)
    turt.end_fill()
    turt.right(180)
    turt.forward(60)
    turt.fillcolor(255,25,0)

    turt.begin_fill()
    turt.seth(-87)
    turt.forward(165)
    angle = 174
    w2 = -turt.xcor()
    R = w2/sin(deg2rad(angle/2))
    turt.seth(-angle/2)
    arc(turt,angle,R,'l')
    turt.forward(165)

    turt.seth(183)
    turt.forward(L-60)
    turt.seth(177)
    turt.forward(L-60)
    turt.end_fill()


def face():
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.penup()
    turt.goto(0,400)
    turt.pendown()
    turt.color(254,222,0)
    turt.fillcolor(254,222,0)
    turt.begin_fill()
    turt.goto(-420,170)

    turt.seth(-85)
    angle = 50
    tilt = 90-angle/2-5
    w2 = -turt.xcor()
    R = w2/(2*sin(deg2rad(angle/2))*cos(deg2rad(tilt)))
    arc(turt,angle-20,R,'l')
    head = -turt.heading()

    chin = 120
    radius = -turt.xcor()/sin(deg2rad(chin/2))
    turt.seth(-chin/2)
    arc(turt,chin,radius,'l')
    turt.seth(head)
    arc(turt,angle-20,R,'l')
    turt.goto(0,400)
    turt.end_fill()

