import turtle
import pixart
#please press enter after copy pasting if drawing doesnt show up

row_color="0"
x=-400
y=400

#mechanism for creating the cubes based on input, and creating a new row when input is drawn
def input_row(r):
    try:
        if r[0]=="0":
            pixart.draw_black_pixel()
            input_row(r[1:])
        elif  r[0]=="1":
            pixart.draw_white_pixel()
            input_row(r[1:])
        elif  r[0]=="2":
            pixart.draw_red_pixel()
            input_row(r[1:])
        elif  r[0]=="3":
            pixart.draw_yellow_pixel()
            input_row(r[1:])
        elif  r[0]=="4":
            pixart.draw_orange_pixel()
            input_row(r[1:])
        elif  r[0]=="5":
            pixart.draw_green_pixel()
            input_row(r[1:])
        elif  r[0]=="6":
            pixart.draw_yellowgreen_pixel()
            input_row(r[1:])
        elif  r[0]=="7":
            pixart.draw_sienna_pixel()
            input_row(r[1:])
        elif  r[0]=="8":
            pixart.draw_tan_pixel()
            input_row(r[1:])
        elif  r[0]=="9":
            pixart.draw_gray_pixel()
            input_row(r[1:])
        elif  r[0]=="A":
            pixart.draw_darkgray_pixel()
            input_row(r[1:])
        else:
            input("press enter to close drawing")
    # new row code ,uses indexerror to know when row ends and new row input is needed      
    except IndexError:
        turtle.up()
        global y
        y=y-40
        turtle.goto(x,y)
        turtle.down()
        newstring=input("enter next string:")
        if newstring=="":
            input("press enter to close drawing")
        else:
            input_row(newstring)


#tweaker for turtle
def tweak(speed,tracer,outline_color="black"):
    turtle.speed(speed)
    turtle.tracer(tracer)
    turtle.color(outline_color)
    #centering the turtle
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

#please press enter after copy pasting if drawing doesnt show up
def main():
    tweak(0,False)
    global row_color 
    row_color=input("enter string:")
    input_row(row_color)
if __name__=="__main__":
    main()
