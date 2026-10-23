import turtle
import math
import random

random.seed(7)

screen = turtle.Screen()
screen.setup(800,480)
screen.bgcolor("#12001c")

t = turtle.Turtle()
t.speed(0)

CX, CY = 0, 110   
K = 0.75  

def stars():
    t.penup()
    for _ in range(70):
        x = random.randint(-390, 390)
        y = random.randint(-230, 230)
        t.goto(x, y)
        t.dot(random.randint(2, 4), "white")

def stem():
    t.penup()        
    t.goto(CX, CY)
    t.setheading(-90)
    t.color("#2e9e5b")
    t.pensize(7)
    t.pendown()
    t.forward(CY + 200)
    


def leaf(x, y, angle, r=80):
    t.penup()    
    t.goto(x,y)
    t.setheading(angle)
    t.color("#7fe0a3", "#1f8a4c")
    t.pensize(2)
    t.pendown()
    t.begin_fill()
    t.circle(r, 60)
    t.left(120)
    t.circle(r, 60)
    t.end_fill()

def petal(size,edge,fill):
    t.color(edge, fill)
    t.begin_fill()
    t.circle(size, 80)
    t.left(100)   
    t.circle(size, 80)
    t.left(100)
    t.end_fill()

def bloom():
    rings =[
        (8,120, "#ff6fa8" , "#7d0a45"),
        (8,102, "#ff7fb4","#a8125c"),
        (7,84,"#ff9cc6", "#d81b78"),
        (6,66,"#ffb3d3", "#f2559a"),
        (5,50, "#ffd0e4", "#ff8cc0"),
        (4, 34, "#d6b2c7", "#ffc2dc"),
    ]
    for count, size, edge, fill in rings :    
        shift = random.randint(0, 40)
        for i in range (count):
            t.penup()
            t.goto(CX, CY)
            a = shift + i * 360 / count
            t.setheading(a + random.uniform(-4, 4))
            t.pendown()
            s = size * random.uniform(0.94, 1.04)
            petal(s, edge, fill)

def center():
    t.penup()
    t.goto(CX, CY)
    t.dot(26, "#ffd54a")
    for i in range (14):
        a = math.radians(i * 360 / 14)
        x =  CX + math.cos(a) * 20
        y = CY + math.sin(a) * 20 
        t.goto(x, y)
        t.dot(5, "#ff9f1c")

stars()
stem()
leaf(2 , -80 , 15)
leaf(-2 , -140 , 135)  
bloom()      
center()

t.hideturtle()
turtle.done()