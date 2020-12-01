import turtle

tyson = turtle.Turtle()
tyson.shape('turtle')
tyson.color('green')
drawArea = turtle.Screen()
drawArea.bgcolor('blue')
tyson.pensize(2)

for i in range (0,4):
    tyson.forward(100)
    tyson.left(90)

tyson.penup()
tyson.forward(150)
tyson.pendown()

for i in range (0,3):
    tyson.forward(50)
    tyson.left(120)

drawArea.mainloop()