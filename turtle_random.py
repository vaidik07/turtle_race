from turtle import Turtle , Screen
import random

screen = Screen()
screen.setup(width=500 , height=400)

user_bet = screen.textinput(title="Make your bet" , prompt="Which turtle will win the race ? Enter the colour:")
colors = ["red" , "orange" , "yellow"  , "green" , "blue" , "purple"]
y_positions = [-70 , -40 , -10 , 20 , 50 , 80]
all_turtle = []
is_race_on = False


for i in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x= -230 , y = y_positions[i])
    all_turtle.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtle:
        if t.xcor()>230:
            is_race_on = False
            winning_colour = t.pencolor()
            if winning_colour == user_bet:
                print(f"You have won !!! The winning colour is {winning_colour}")
            
            else:
                print(f"You lost !!!! The winning colour is {winning_colour}")
        rand_distance = random.randint(0 , 10)
        t.forward(rand_distance)

        







ApniScreen  = Screen()
ApniScreen.exitonclick()