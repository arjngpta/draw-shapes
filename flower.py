import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
    alpha = turtle.Turtle()
    alpha.shape("circle")
    alpha.color("green")
    alpha.speed(5)
    alpha.right(90)
    alpha.forward(500)
    alpha.backward(500)
    alpha.color("red")
    alpha.circle(50)
    alpha.right(90)
    alpha.circle(50)
    alpha.right(90)
    alpha.circle(50)
    alpha.right(90)
    alpha.circle(50)
    alpha.right(90)
    alpha.color("pink")
    
    window.exitonclick()

draw_flower()
