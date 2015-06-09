import turtle

def draw_square(turtle_name,size):
    for i in range(1,5):
        turtle_name.forward(size)
        turtle_name.right(90)
        
def draw_triangle(turtle_name,size):
    for i in range(1,4):
        turtle_name.forward(size)
        turtle_name.right(120)

def draw_art():
    angle = int(raw_input("What is the angle? "))
    window = turtle.Screen()
    window.bgcolor("blue")

    # create turtle alpha
    alpha = turtle.Turtle()
    alpha.shape("square")
    alpha.color("green")
    alpha.speed(10)

    # define shape
    n = (360 / angle)
    while n > 0:
        alpha.right(angle)
        n = n - 1
        #draw_square(alpha,100)
        draw_triangle(alpha,100)

    # create turtle bravo
    bravo = turtle.Turtle()
    bravo.shape("circle")
    bravo.color("red")
    bravo.speed(10)
    bravo.right(90)
    bravo.color("green")
    bravo.forward(100)
    bravo.left(90)
    bravo.color("red")
    bravo.circle(100)
    
    window.exitonclick()

draw_art()
