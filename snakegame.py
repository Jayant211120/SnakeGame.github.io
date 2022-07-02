#We write some modules like turtle,random and time for using some functions
#turtle is used for making snake screen,head,food and some other things
import turtle

#random is used for generating food randomly
import random

#time is used for gap in snake game
import time

#we make some global variables for snake motions
delay=0.1
lowscore=0
high_score=0

#we make turtle screen properties
screen=turtle.Screen()
screen.title('Jayant Snake Game')
screen.bgcolor('grey')
screen.setup(width=600,height=600)
screen.tracer(0)

#we make Snake head
head=turtle.Turtle()
head.shape('circle')
head.color('white')
head.penup()
head.goto(0,0)
head.direction='stop'

#we make snake food
food=turtle.Turtle()
food.shape('circle')
food.color('purple')
food.penup()
food.goto(0,100)

#we make score board for snake game
score=turtle.Turtle()
score.shape('circle')
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,250)
score.write(f'Score:{lowscore} High_Score:{high_score}',align='center',font=("Lucida",20,'bold'))

#write functions for move snake
def goup():
    if head.direction!='down':
        head.direction='up'
def godown():
    if head.direction!='up':
        head.direction='down'
def goleft():
    if head.direction!='right':
        head.direction='left'
def goright():
    if head.direction!='left':
        head.direction='right'
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

#we use screen listen function and onkeypress function for control the snake using keys
screen.listen()
screen.onkeypress(goup,'Up')
screen.onkeypress(godown,'Down')
screen.onkeypress(goleft,'Left')
screen.onkeypress(goright,'Right')

#we make a list for increase the body of the snake
list=[]

#we write a loop for run infinite times for giving running game continuours
while True:
    #we use screen update for shown snake is moving
    screen.update()
    #Collision(snake cross the borders)with borders
    if head.xcor()>270 or head.xcor()<-270 or head.ycor()>270 or head.ycor()<-270:
        if head.xcor()>290:
           head.setx(-290)
        if head.xcor()<-290:
           head.setx(290)
        if head.ycor()>290:
           head.sety(-290)
        if head.ycor()<-290:
            head.sety(290)
    #Collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #we make snake body after eating food
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.color('skyblue')
        body.fillcolor('black')
        body.shape('circle')
        list.append(body)
        #increase the score
        lowscore+=10
        delay-=0.001
        if lowscore>high_score:
            high_score=lowscore
        score.clear()
        score.write(f'Score:{lowscore} High_Score:{high_score}',align='center',font=('Lucida',20,'bold'))
    #for increasing the snake body
    for index in range(len(list)-1,0,-1):
        x=list[index-1].xcor()
        y=list[index-1].ycor()
        list[index].goto(x,y)
    if len(list)>0:
        x=head.xcor()
        y=head.ycor()
        list[0].goto(x,y)
    move()
    #collision with snake body
    for lists in list:
        if lists.distance(head)<20:
            time.sleep(1)
            head.direction='stop'
            head.goto(0,0)
            for lists in list:
                lists.ht()
            list.clear()
            lowscore=0
            delay=0.1
            score.clear()
            score.write(f'Score:{lowscore} High_Score:{high_score}',align='center',font=('Lucida',20,'bold'))
    time.sleep(delay)       
#screen mainloop is used stable screen or window
screen.mainloop()
