import turtle

def main():
    # declare a Turtle and Screen before drawing
    myTurtle = turtle.Turtle()
    myWindow = turtle.Screen()
    # points is a list of lists
    points = [[-100, -50], [0, 100], [100, -50]]

    myTurtle.shape("turtle")
    sierpinski_triangle(points, 5, myTurtle)
    myWindow.exitonclick()

def sierpinski_triangle(points, order, myTurtle):
    colorMap = ["yellow", "red", "violet", "green", "blue",]
    draw_triangle(points, colorMap[order-1], myTurtle) # order is some positive integer

    if order > 0:
        sierpinski_triangle([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], order - 1, myTurtle)
        sierpinski_triangle([points[1], get_mid(points[1], points[0]), get_mid(points[1], points[2])], order - 1, myTurtle)
        sierpinski_triangle([points[2], get_mid(points[2], points[1]), get_mid(points[2], points[0])], order - 1, myTurtle)

# point1 and point2 are lists
# get_mid() returns a list which contains x and y coordinates
def get_mid(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

def draw_triangle(points, color, myTurtle):
    myTurtle.up()   # pen up
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down() # pen down, ready to draw
    myTurtle.fillcolor(color)   # color to fill the shape
    myTurtle.begin_fill()   # called just before drawing the shape to be filled
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()
    
main()
