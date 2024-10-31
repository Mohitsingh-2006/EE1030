import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=200, height=400)
screen.title("Arrows Pattern")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.width(2)

# Draw the curved left edge
pen.penup()
pen.goto(-50, 150)
pen.pendown()
pen.setheading(-90)
pen.circle(50, 180)  # Half-circle for the left edge

# Draw the arrows pointing to the right
arrow_length = 100
spacing = 30

for y in range(150, -150, -spacing):
    pen.penup()
    pen.goto(-50, y)
    pen.setheading(0)
    pen.pendown()
    pen.forward(arrow_length)  # Draw the main arrow line
    
    # Draw the arrowhead
    pen.left(150)
    pen.forward(10)
    pen.backward(10)
    pen.right(300)
    pen.forward(10)
    pen.backward(10)
    pen.setheading(0)

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()

