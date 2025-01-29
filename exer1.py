from turtle import Turtle , Screen

vaidik = Turtle()


def shapes(angle , sides):
    for i in range(sides):
        vaidik.forward(100)
        vaidik.right(angle)

for i in range(3 , 11):
    angle = 180 - ((i-2)*180)/i
    shapes(angle , i)

    
    


ApniScreen  = Screen()
ApniScreen.exitonclick()