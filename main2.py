from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG GAME1')
screen.tracer(0)  # Απενεργοποιεί τα animations

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score1=Scoreboard()
score1.player_1_score()
score2=Scoreboard()
score2.player_2_score()





game_is_on=True
while game_is_on:
    screen.update()  # Animations ενεργα για να δείξει τα paddle
    time.sleep(ball.move_speed)

    ball.ball_move()
    screen.listen()
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')

    # Hit the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    # Hit the paddle
    if ball.xcor() > 330 and ball.distance(r_paddle)<50:
        ball.paddle_hit()

    if ball.xcor() <-330 and ball.distance(l_paddle)<50:
        ball.paddle_hit()

    # Right Paddle misses
    if ball.xcor()>400:
        ball.reset_position()
        score1.increase_score()

    #Left Paddle misses
    if ball.xcor()<-400:
        ball.reset_position()
        score2.increase_score()
