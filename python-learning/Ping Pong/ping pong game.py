#ping pong game
import turtle
import random
import time

# screen
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# player1
player1 = turtle.Turtle()
player1.speed(10)
player1.shape("square")
player1.color("green")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

# player2
player2 = turtle.Turtle()
player2.speed(10)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

# ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.randint(1, 5)
ball.dy = ball.dx

# ball movement
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# players movement
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)
    if player1.ycor() > 250:
        player1.sety(250)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)
    if player1.ycor() < -250:
        player1.sety(-250)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)
    if player2.ycor() > 250:
        player2.sety(250)

def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)
    if player2.ycor() < -250:
        player2.sety(-250)

# keyboard actions
wind.listen()
wind.onkeypress(player1_up, "w")
wind.onkeypress(player1_down, "s")
wind.onkeypress(player2_up, "Up")
wind.onkeypress(player2_down, "Down")

# main game loop
while True:
    wind.update()
    time.sleep(0.01)

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarder check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1