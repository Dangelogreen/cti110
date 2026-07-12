# D'Angelo Green
# 7/12/2026
# P4LAB1
# Draw a house with turtle graphics.

import turtle

wn = turtle.Screen()
wn.bgcolor("gray")

t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.pensize(3)
t.speed(5)

count = 0

while count < 4:
    t.forward(67)
    t.left(90)
    count = count + 1

t.left(90)
t.forward(67)
t.right(90)

t.color("gold")

for i in range(3):
    t.forward(67)
    t.left(120)

wn.mainloop()