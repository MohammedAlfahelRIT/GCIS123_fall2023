import turtle
import sys

#drawing the table the cake will be ontop. Focus on positioning table and cake correctly.
def table(table_size,color):
    turtle.pencolor("black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.down()
    turtle.forward(table_size/2)
    turtle.back(table_size)
    turtle.left(90)
    turtle.forward(table_size/10)
    turtle.right(90)
    turtle.forward(table_size)
    turtle.right(90)
    turtle.forward(table_size/10)

    turtle.end_fill()
    turtle.up()
    turtle.goto(0,0+table_size/10)
    turtle.down()

#drawing the main body of the cake, based on cake size input.
def cake_base(cake_size,color):
    turtle.pencolor("white")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.down()
    turtle.forward(cake_size/2)
    turtle.back(cake_size)
    turtle.left(90)
    turtle.forward(cake_size)
    turtle.right(90)
    turtle.forward(cake_size)
    turtle.right(90)
    turtle.forward(cake_size)

    turtle.end_fill()

def cake_frosting(size):
    x=x
#drawing the cherry ontop of the cake, based cake size input.
def cake_cherry(size):
    x=x

#main function that requests input
def main():
    table_size=int(input("please enter table length: "))
    table_color=input("table color: ")
    table(table_size,table_color)
    cake_base(100,input("cake color: "))
    
    input("press any key to continue.. ")


if __name__=="__main__":
    main()
