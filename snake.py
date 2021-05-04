import turtle
import tkinter
import time
import random
delay=0.1
score=0
highestscore=0

# Snake Body
bodies=[]

#Getting a Screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("#dbdee5")
s.setup(width=600,height=600)

#Create Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#Score Board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("#0f1b48")
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score : 0    | Heighest Score : 0")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
        
def moveright():
    if head.direction!="left":
        head.direction="right"

def moveleft():
    if head.direction!="right":
        head.direction="left"

def movestop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
# Event Handling - Key Mapping
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

#Main loop
while True:
    s.update() #This is for update the screen
    #Check Collision With Border
    if(head.xcor()>290):
        head.setx(-290)
    if(head.xcor()<-290):
        head.setx(290)
    if(head.ycor()>290):
        head.sety(-290)
    if(head.ycor()<-290):
        head.sety(290)

    #Check Collision With Food
    if(head.distance(food)<20):
        #Move the food to new random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #Increase the lenght of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.ht()
        body.shape("square")
        body.color("red")
        body.fillcolor("#0f1b48")
        bodies.append(body) #Append New Body
        body.st()
        #Increase The Score
        score+=10

        #Change Delay
        delay-=0.001

        #Update The Highest Score
        if score>highestscore:
            highestscore=score
        sb.clear()
        sb.write("Score : {}    |    Highest Score : {}".format(score,highestscore))
    # Move The Snake Body
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if(len(bodies)>0):
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    #Check Collision With Snake Body
    for body in bodies:
        if(body.distance(head)<20):
            #popup=turtle.getscreen()
            #popup.textshow("Game Over","Your score is {}".format(score))
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            tkinter.messagebox.showinfo("Game Over","Your Score is : {}".format(score))
            # Hide Bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            score=0
            delay=0.1

            # Update Score Board
            sb.clear()
            sb.write("Score : {}    |    Highest Score : {}".format(score,highestscore))
    time.sleep(delay)
s.mainloop()
            
