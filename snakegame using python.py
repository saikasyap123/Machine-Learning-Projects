import turtle
import time
import random
delay = 0.1
score = 0
high_score = 0
#setting up the screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('green')
wn.setup(width=600, height=600)
#turn off the animations on screenand also turns off the screen updates
wn.tracer(0)
#snake head
head = turtle.Turtle()
#speed is as fast as possible
head.speed(0)
head.shape('square')
head.color('Black')
#our turtle should not draw anything 
head.penup()
#start at center
head.goto(0,0)
head.direction = 'stop'
#snake prey
prey = turtle.Turtle()
#speed is as fast as possible
prey.speed(0)
prey.shape('circle')
prey.color('Red')
#our turtle should not draw anything 
prey.penup()
#start at center
prey.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("score: 0 High score: 0",align="center",font = ("Courier",24,"normal"))

segments = []


def go_up():
    head.direction = 'up'
def go_down():
    head.direction = 'down'
def go_left():
    head.direction = 'left'
def go_right():
    head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
#we need to update screen everytime
while True:
    wn.update()
    if (head.xcor())>290 or head.xcor()<(-290) or head.ycor()>290 or head.ycor()<(-290):
        head.goto(0,0)
        time.sleep(1)
        head.direction = 'strop'
        for segment in segments:
           segment.goto(1000,1000)
        segments.clear()
        score =0
        delay = 0.1
        pen.clear()
        pen.write("score :{} Highscore :{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    

    
    #default method to measure the distance between two turtles
    #each turtle is having default size 20 pixels
    if head.distance(prey) < 20:
        prey.goto(random.randint(-290,290),random.randint(-290,290))
        new_segment = turtle.Turtle()
        new_segment.penup()
        new_segment.color('grey')
        new_segment.shape('square')
        new_segment.speed(0)
        segments.append(new_segment)
        delay -=0.001
        score +=10
        if score>high_score:
            high_score = score
        pen.clear()
        pen.write("score :{} Highscore :{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    #moving every segment to previous segment coors except 1st segment
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #for the first segment 
    if len(segments)>0:
        segments[0].color('Black')
        segments[0].goto(head.xcor(),head.ycor())
    #to know the movement we need to introduce delay
    move()
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("score :{} Highscore :{}".format(score,high_score),align="center",font=("Courier",24,"normal"))



    time.sleep(delay)

wn.mainloop()
