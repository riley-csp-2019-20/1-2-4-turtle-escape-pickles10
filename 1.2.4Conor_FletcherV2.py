import turtle as trtl
import random
wn = trtl.Screen()
wn.bgcolor("black")


#           Variables           #

#wall_width = random.randint(1,100)
bump = 1
wall_width = 15

squares = 10
angles = 90.1
door_width = 30
length = 30
#angles = random.randint(30,200)
playerColor = input("What color do you want your player?")
player = trtl.Turtle()
player.pencolor(playerColor)






#          Maze Maker            #
drawer = trtl.Turtle()
drawer.speed(0)
drawer.ht()


#           Functions           #
def up():
    player.setheading(95)
    player.forward(10)
def down():
    player.setheading(272)
    player.forward(10)
def right():
    player.setheading(7)
    player.forward(10)
def left():
    player.setheading(174)
    player.forward(10)
def drawBarrier():
    drawer.left(90)
    drawer.forward(wall_width*2)
    drawer.backward(wall_width*2)
    drawer.right(90)
def hulk():
    global bump
    bump += 1
    drawer.shapesize(2*bump)
    
def drawDoor():
    drawer.penup()
    drawer.forward(door_width)
    drawer.pendown()


# makes walls, gaps, and walls in maze
counter1 = 1
while counter1 < (squares*4):
    drawer.pensize(12)
    drawer.color("green")
    if counter1 > 4:
        

        door = random.randint(door_width, length - 2*door_width)
        barrier = random.randint(wall_width*2, length - 2*door_width)

        if door < barrier :
            drawer.forward(door)
            drawDoor()
            drawer.forward(barrier-door-door_width)
            drawBarrier()
            drawer.forward(length-barrier)
        else:
            drawer.forward(barrier)
            drawBarrier()
            drawer.forward(door-barrier)
            drawDoor()
            drawer.forward(length-door-door_width)

        drawer.left(angles)
        
    counter1 += 1
    length += wall_width
 
wn.onkeypress(hulk,"space")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.listen()

wn.mainloop()