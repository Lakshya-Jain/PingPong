import turtle
import winsound

#Creating a Window
wn = turtle.Screen()                        
wn.title ("Batman v/s Joker")
wn.bgpic(picname="bgimg.gif")
wn.setup(width=960, height=540)
wn.tracer(0)        

#Score
score_bat = 0
score_joker = 0

#Bat
bat = turtle.Turtle()
bat.speed(0)
wn.addshape("bat.gif")
bat.shape("bat.gif")
bat.penup()
bat.goto(-435,0)
#Move bat
def bat_up():
    y = bat.ycor()
    y +=50
    bat.sety(y)
def bat_down():
    y = bat.ycor()
    y -=50
    bat.sety(y)
#Assigning Keys
wn.listen()
wn.onkeypress(bat_up, "w")
wn.onkeypress(bat_down, "s")

#joker
joker = turtle.Turtle()
joker.speed(0)
wn.addshape("joker.gif")
joker.shape("joker.gif")
joker.penup()
joker.goto(415,0)
#Move Joker
def joker_up():
    y = joker.ycor()
    y +=50
    joker.sety(y)
def joker_down():
    y = joker.ycor()
    y -=50
    joker.sety(y)
#Assigning Keys
wn.listen()
wn.onkeypress(joker_up, "Up")
wn.onkeypress(joker_down, "Down")

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(2)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.5
ball.dy=0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto (15,-255)
pen.write("Bat: 0 v/s Joker: 0", align="center", font=("Courier", 19, "bold"))


#Loop
while True:
    wn.update()

    #Moving the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Defining Boundries
    if  ball.ycor() > 260:
        ball.sety(260)
        ball.dy *= -1
        winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)
    if  ball.ycor() < -260:
        ball.sety(-260)
        ball.dy *= -1
        winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)
    if ball.xcor() > 470:
       ball.goto(0,0)
       ball.dx *= -1
       score_bat +=5
       pen.clear()
       pen.write("Bat: {} v/s Joker: {}".format(score_bat,score_joker), align="center", font=("Courier", 19, "bold"))
    if ball.xcor() < -470:
       ball.goto(0,0)
       ball.dx *= -1
       score_joker +=5
       pen.clear()
       pen.write("Bat: {} v/s Joker: {}".format(score_bat,score_joker), align="center", font=("Courier", 19, "bold"))

    # Collosions
    if ball.xcor() > 345 and (ball.ycor() < joker.ycor() +62.5 and ball.ycor() > joker.ycor() -62.5):
        ball.dx *= -1 
        winsound.PlaySound("jokerlaugh.wav", winsound.SND_ASYNC)

    if ball.xcor() < -385 and (ball.ycor() < bat.ycor() +62.5 and ball.ycor() > bat.ycor() -62.5):
        ball.dx *= -1
        winsound.PlaySound("batman.wav", winsound.SND_ASYNC)
#end