import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle():
    "Draw Rectangle"
    for i in range(4):
        tao.fd(100)
        tao.left(90)

def Go(x,y):
    "Goto x,y"
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def Draw():
    for i in range(12):
        Rectangle()
        tao.left(30)

Draw()
