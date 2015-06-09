import turtle

def draw_square(turtle_name,size):
    for i in range(1,5):
        turtle_name.forward(size)
        turtle_name.right(90)
        
def draw_triangle(turtle_name,size):
    for i in range(1,4):
        turtle_name.forward(size)
        turtle_name.right(120)

def draw_rhombus(turtle_name,size,shape_angle):
    for i in range(1,5):
        if i % 2 == 0:
            turtle_name.forward(size)
            turtle_name.right(180 - shape_angle)
        else:
            turtle_name.forward(size)
            turtle_name.right(shape_angle)


def draw_art():
    shape_angle = int(raw_input("What is the shape angle? "))
    angle = int(raw_input("What is the space angle? "))
    window = turtle.Screen()
    window.bgcolor("white")

    # create turtle alpha
    alpha = turtle.Turtle()
    alpha.shape("turtle")
    alpha.color("blue")
    alpha.speed(100)

    # define shape
    n = (360 / angle)
    while n > 0:
        alpha.right(angle)
        n = n - 1
        #draw_square(alpha,100)
        #draw_triangle(alpha,100)
        draw_rhombus(alpha,100,shape_angle)
    alpha.right(90)
    alpha.forward(200)

    # create turtle bravo
    #bravo = turtle.Turtle()
    #bravo.shape("circle")
    #bravo.color("red")
    #bravo.speed(10)
    #bravo.right(90)
    #bravo.color("green")
    #bravo.forward(100)
    #bravo.left(90)
    #bravo.color("red")
    #bravo.circle(100)
    
    window.exitonclick()

draw_art()
