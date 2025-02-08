" Ping Pong game simulate turns and simulate scores"
import turtle
# Creating window
window=turtle.Screen()
window.title("Ping Pong by zack")
window.setup(width=800,height=600)
window.tracer(0)
window.bgcolor(0.1,0.1,0.1)


# Creating ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.goto(x=0,y=0)
ball_dx=1
ball_dy=1
#ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball_speed=0.5
# Creat first player
player1=turtle.Turtle()
player1.shape("square")
player1.speed(0)
player1.shapesize(stretch_len=1,stretch_wid=6)
player1.color("blue")
player1.penup()
player1.goto(x=-350,y=0)

# Creating player2
player2=turtle.Turtle()
player2.shape("square")
player2.speed(0)
player2.shapesize(stretch_len=1,stretch_wid=6)
player2.color("red")
player2.penup()
player2.goto(x=+350,y=0)

# Creat text
text=turtle.Turtle()
text.color("white")
text.speed(0)
text.penup()
text.goto(x=0,y=260)
text.write("Player 1 : 0 Player 2 : 0",align="center" , font=("Courier", 14, "normal"))
text.hideturtle()
player_speed=20
score_p1,score_p2=0,0

# Creating player movements

def player1_move_up():
    player1.sety(player1.ycor()+player_speed)
def player1_move_down():
    player1.sety(player1.ycor()-player_speed)
def player2_move_up():
    player2.sety(player2.ycor()+player_speed)
def player2_move_down():
    player2.sety(player2.ycor()-player_speed)


# Key boundings

window.listen()
window.onkeypress(player1_move_up,"w")
window.onkeypress(player1_move_down,"s")
window.onkeypress(player2_move_up,"Up")
window.onkeypress(player2_move_down,"Down")

while True:
    window.update()
    ball.setx(ball.xcor()+(ball_dx*ball_speed))
    ball.sety(ball.ycor()+(ball_dy*ball_speed))

    # ball and boreder collisions
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *=-1

    # collision with player 1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    # collision with player 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1
    # Score Simulation
    if ball.xcor() > 390:
        ball.goto(x=0,y=0)
        text.clear()
        score_p1+=1
        text.write(f"Player 1 : {score_p1} Player 2 : {score_p2}",align="center" , font=("Courier", 14, "normal"))
    if ball.xcor() <- 390:
        ball.goto(x=0,y=0)
        text.clear()
        score_p2+=1
        text.write(f"Player 1 : {score_p1} Player 2 : {score_p2}",align="center" , font=("Courier", 14, "normal"))
