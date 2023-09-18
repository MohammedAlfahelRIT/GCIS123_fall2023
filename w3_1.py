import turtle

def my_turtle():
    turtle.circle(25)
    turtle.setheading(270)
    turtle.forward(100)
    turtle.setheading(315)
    turtle.forward(50)
    turtle.up()
    turtle.back(50)
    turtle.setheading(225)
    turtle.down()
    turtle.setheading(225)
    turtle.forward(50)
    turtle.up()
    turtle.goto(0,0)

def draw_circle(x,y,radius,fillcolor):
    turtle.up()
    turtle.goto(x,y)
    #drawing centered circle
    turtle.forward(radius)
    turtle.left(90)
    #
    turtle.pencolor("black")
    turtle.fillcolor(fillcolor)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    #return turtle to center
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(180)

    
def square(my_size):
    print(my_size)
    angle=90
    turtle.color("red")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(my_size)
        turtle.left(angle)

    turtle.end_fill()

def tweak(speed,tracer):
    turtle.speed(speed)

    turtle.tracer(tracer)

def draw_eye(x,y,radius,eye_color):
    draw_circle(x,y,radius,"white")
    draw_circle(x,y,radius/2,eye_color)
    draw_circle(x,y,radius/4,"black")

def draw_nose(size,color):
    draw_circle(0,0,size,color)

def draw_mouth(x,y,size):
    turtle.fillcolor("black")
    turtle.goto(x,y-size/1.5)
    turtle.back(size)
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.circle(size,180)
    turtle.end_fill()


def draw_smiley(x,y,size,smileycolor,eyecolor):
    draw_circle(x,y,size,smileycolor)
    draw_circle(x,y,size/8,"pink")
    draw_eye(x+size/3,y+size/3,size/4,"blue")
    draw_eye(x-size/3,y+size/3,size/4,eyecolor)
    draw_mouth(x,y,size/3)
    

def main():
    tweak(10,False)
    #size =int(input("enter a size:"))
    #square(size)
    #my_turtle()
    draw_smiley(0,0,100,"yellow","blue")
    input("press any key to continue.. ")
main()    