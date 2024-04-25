# import modules
import turtle

# create game window
window = turtle.Screen()
# set a title to the window
window.title("Ping Pong by Elalfee")
# set a background color for the window
window.bgcolor("black")
# set the dimensions of the window
window.setup(width=800, height=600)
# stop self update of the window
window.tracer(0)

# create first paddle
left_paddle = turtle.Turtle()
# maximum spped
left_paddle.speed(0)
# set the shape of the paddle
left_paddle.shape("square")
# set the color of the paddle
left_paddle.color("blue")
# stretch the dimension of the paddle
left_paddle.shapesize(stretch_wid=5, stretch_len=0.5)
# remove the movement traces of the paddle
left_paddle.penup()
# set the position of the paddle
left_paddle.goto(-350, 0)

# create second paddle
right_paddle = turtle.Turtle()
# maximum spped
right_paddle.speed(0)
# set the shape of the paddle
right_paddle.shape("square")
# set the color of the paddle
right_paddle.color("red")
# stretch the dimension of the paddle
right_paddle.shapesize(stretch_wid=5, stretch_len=0.5)
# remove the movement traces of the paddle
right_paddle.penup()
# set the position of the paddle
right_paddle.goto(350, 0)

# create ball
ball = turtle.Turtle()
# maximum spped
ball.speed(0)
# set the shape of the ball
ball.shape("circle")
# set the color of the ball
ball.color("white")
# remove the movement traces of the ball
ball.penup()
# set the position of the ball
ball.goto(0, 0)
# set delta x of the ball
ball.dx = 2.5
# set delta y of the ball
ball.dy = 2.5

# each player initial score
blue = 0
red = 0

# create score
score = turtle.Turtle()
# maximum spped
score.speed(0)
# set the color
score.color("white")
# remove the movement traces
score.penup()
# hide the score to only show the text
score.hideturtle()
# set the position
score.goto(0, 260)
# write the score
score.write("Blue Player: {} Red Player: {}".format(blue, red), align="center", font=("Courier", 24, "bold"))

def left_paddle_up():
    # get the y coordinate of the paddle
    y = left_paddle.ycor()
    # increase the y coordinate by 20
    y += 20
    # limit the movement of the paddle to the top and bottom border
    if(y > 250):
        return
    # set the coordinate to the paddle
    left_paddle.sety(y)
    
def left_paddle_down():
    # get the y coordinate of the paddle
    y = left_paddle.ycor()
    # decrease the y coordinate by 20
    y -= 20
    # limit the movement of the paddle to the top and bottom border
    if(y < -250):
        return
    # set the coordinate to the paddle
    left_paddle.sety(y)

def right_paddle_up():
    # get the y coordinate of the paddle
    y = right_paddle.ycor()
    # increase the y coordinate by 20
    y += 20
    # limit the movement of the paddle to the top and bottom border
    if(y > 250):
        return
    right_paddle.sety(y)
    
def right_paddle_down():
    # get the y coordinate of the paddle
    y = right_paddle.ycor()
    # decrease the y coordinate by 20
    y -= 20
    # limit the movement of the paddle to the top and bottom border
    if(y < -250):
        return
    # set the coordinate to the paddle
    right_paddle.sety(y)

# tell the window to expect keyboard input
window.listen()
# func left_paddle_up will invoke on pressing on w
window.onkeypress(left_paddle_up, "w")
# func left_paddle_down will invoke on pressing on s
window.onkeypress(left_paddle_down, "s")
# func right_paddle_up will invoke on pressing on Up arrow
window.onkeypress(right_paddle_up, "Up")
# func right_paddle_down will invoke on pressing on Down arrow
window.onkeypress(right_paddle_down, "Down")

# Game loop that stay true untill a player lose or quit
while True:
    # update window on each cycle of the loop
    window.update()
    
    # move the ball
    ball.setx(ball.xcor() + ball.dx) # +2.5 in x-axis everytime the loop runs.
    ball.sety(ball.ycor() + ball.dy) # +2.5 in y-axis everytime the loop runs.
    
    # if ball collides with the top and bottom, reverse direction.
    if ball.ycor() > 290:
        ball.sety(290) # set the y-axis position
        ball.dy *= -1 # reverse the direction
    
    if ball.ycor() < -290:
        ball.sety(-290) # set the y-axis position
        ball.dy *= -1 # reverse the direction
    
    # if the ball pass the left or right the ball go to the center again.
    if ball.xcor() > 390:
        ball.goto(0, 0) # back to the starting position
        ball.dx *= -1 # reverse the direction
        blue += 1 # blue wins
        # clear then show the new score
        score.clear()
        score.write("Blue Player: {} Red Player: {}".format(blue, red), align="center", font=("Courier", 24, "bold"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0) # back to the starting position
        ball.dx *= -1 # reverse the direction
        red += 1 # red wins
        # clear then show the new score
        score.clear()
        score.write("Blue Player: {} Red Player: {}".format(blue, red), align="center", font=("Courier", 24, "bold"))
        
    # if ball collides with the paddles, reverse direction
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340) # set the x-axis position
        ball.dx *= -1 # reverse the direction
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340) # set the x-axis position
        ball.dx *= -1 # reverse the direction