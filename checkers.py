import turtle
#setup to make drawing instant
wn= turtle.Screen()
#x and y values to specify where the drawing starts, help at centering the drawing
X=-400
Y=400
#P value used later for sitching the color from red to black in checkerboard
P=True

# function to create a square
def square(my_size,color):
    turtle.down()
    angle=90
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(my_size)
        turtle.right(angle)

    turtle.end_fill()
    turtle.up()
    turtle.forward(my_size)

#function to craete a row of squares using the square function
def row(startx=0,starty=0,):
    turtle.up()
    turtle.goto(startx,starty)
    turtle.down()
    if P==True:
        for i in range(10):
            square(40,"red")
            square(40,"black")
    else:
        for i in range(10):
            square(40,"black")
            square(40,"red")

# a function that creates a grid using the row function
def grid(n):
    if n<0:
        return None
    elif n==0 or n==1:
        return None
    else:
        global Y
        Y=Y-40
        row(X,Y)
        global P
        P= not P
        return grid(n-1)


def tweak(speed,tracer,outline_color="black"):
    turtle.speed(speed)
    turtle.color(outline_color)

def main():
    wn.tracer(0)
    tweak(0,False)
    grid(20)
    wn.update()
    input("")

if __name__=="__main__":
    main()