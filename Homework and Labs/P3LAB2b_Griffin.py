import turtle

tyson = turtle.Turtle()
tyson.pensize(4)
tyson.color('Purple')
draw = turtle.Screen()
draw.bgcolor('Cyan')

tyson.penup()
tyson.backward(100)
tyson.pendown()

# draw K
for i in range (0,1):
    tyson.right(90)
    tyson.forward(100)
    tyson.right(180)
    tyson.forward(200)
    tyson.backward(120)
    tyson.right(40)
    tyson.forward(145)
    tyson.backward(120)
    tyson.right(110)
    tyson.forward(115)

# undo the angle and move back
tyson.penup()
tyson.left(150)
tyson.forward(100)
tyson.right(90)
tyson.forward (120)
tyson.right(90)
tyson.forward(25)
tyson.left(90)
tyson.pendown()

for i in range (0,1):
    tyson.right(90)
    tyson.forward(10)
    tyson.backward(20)
    tyson.forward(10)
    tyson.left(90)
    tyson.forward(50)
    tyson.right(90)
    tyson.forward(75)
    tyson.right(90)
    tyson.forward(100)
    tyson.right(90)
    tyson.forward(200)
    tyson.right(90)
    tyson.forward(90)




draw.mainloop()