import turtle 

wn=turtle.Screen()
wn.title('PingPong')
wn.bgcolor('black')                #Creating window
wn.setup(800,600)
wn.tracer(0)

#Creating paddle for left side
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Creating paddle for right side
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')           #Creates a 20pixelx20pixel paddle by default
paddle_b.color('white')
paddle_b.shapesize(5,1)            #Straches 5 times along height, 1 times(constant) along width
paddle_b.penup()
paddle_b.goto(350,0)

#Creating paddle for ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)

ball.dx=0.3                        
ball.dy=0.3

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0,260)
pen.write('Player Left: 0   Player Right: 0', True, 'center', ('Courier', 24, 'normal'))

#Creating functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')
while True:
    wn.update()
    
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        
    #Paddle and Ball collosions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1