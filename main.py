from turtle import Turtle, Screen
import random

scr = Screen()
scr.setup(width=800, height = 600)

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtles = []

for i in range(7):
    current_turtle = Turtle(shape='turtle')
    current_turtle.color(rainbow[i])
    current_turtle.penup()
    current_turtle.goto(x = -350, y = -225 + 75 * i)
    turtles.append(current_turtle)
    
user_bet = scr.textinput(title="Place a bet", prompt="Which turtle will win? Enter a ROYGBIV color: ").lower()
if user_bet not in rainbow:
    user_bet = scr.textinput(title="Place a bet", prompt="Error: Please enter a ROYGBIV color: ").lower()

if user_bet:
    race_going = True

while race_going:
    if any(t.xcor() >= 300 for t in turtles):
        race_going = False
    for t in turtles:
        t.forward(random.randint(5, 25))

winning_coordinate = 0

for t in turtles:
    if t.xcor() > winning_coordinate:
        winning_coordinate = t.xcor()

winning_turtles = [t.pencolor().title() for t in turtles if t.xcor() == winning_coordinate]

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, -150)

if user_bet in winning_turtles:
    if len(winning_turtles) == 1:
        msg = f"You bet correctly on {user_bet.title()}."
    else:
        msg =f"Tie between {', '.join(winning_turtles)}.\nYou bet correctly on {user_bet.title()}."
else:
    msg = f"You bet on {user_bet.title()}, who didn't win.\nWinner was {winning_turtles[0].title()}."

writer.write(arg = msg, move = False, align="center", font = ('Impact', 36, 'bold'))

scr.exitonclick()