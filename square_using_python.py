import turtle
utsav=turtle.Turtle()
utsav.color("#2b9c02","#92f56e")
for i in range(2):
    utsav.begin_fill()
    utsav.forward(100)
    utsav.left(90)
    utsav.forward(100)
    utsav.left(90)
    utsav.forward(100)
    utsav.left(90)
    utsav.forward(100)

    utsav.penup()
    utsav.forward(70)
    utsav.pendown()
    
    utsav.end_fill()


turtle.done()
