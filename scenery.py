import turtle
import sys

#drawing the table the cake will be ontop. Focus on positioning table and cake correctly.
def table(table_size,color):
    print("Your cake is loading!!")
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
    #table right leg
    turtle.up()
    turtle.goto(table_size/2-table_size/10,0)
    turtle.down()
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.forward(table_size/2)
    turtle.back(table_size/2)
    turtle.setheading(0)
    turtle.forward(table_size/10)
    turtle.right(90)
    turtle.forward(table_size/2)
    turtle.right(90)
    turtle.forward(table_size/10)
    turtle.end_fill()
    #turtle left leg
    turtle.up()
    turtle.goto(-table_size/2,0)
    turtle.down()
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.forward(table_size/2)
    turtle.back(table_size/2)
    turtle.setheading(0)
    turtle.forward(table_size/10)
    turtle.right(90)
    turtle.forward(table_size/2)
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
    #prepares turtle position to draw decoration
    turtle.up()
    turtle.setheading(90)
    turtle.forward(cake_size)
    turtle.left(90)
    turtle.forward(cake_size/2)
    turtle.setheading(0)
    
    


#drawing the candle ontop of the cake.
def cake_cherry(radius):
    turtle.up()
    #turtle.setheading(90)
    #turtle.forward(radius)
    turtle.down()
    turtle.pencolor("white")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    turtle.goto(0,0)


#main function that requests input
def main():
    table_size=int(input("please enter table length: "))
    table_color=input("table color: ")
    #keeping cake smaller than table as per doc requirments
    while True:
        cake_size=int(input("cake size: "))
        if table_size>=cake_size:
            break
        else:
            print("cake size must be less than table size")
    cake_color=input("cake color: ")
    table(table_size,table_color)
    cake_base(cake_size,cake_color)
    cake_cherry(cake_size/10)
    
    
    input("press any key to continue.. ")


if __name__=="__main__":
    main()
