import turtle

pen = turtle.Turtle()
pen.speed(0)

colors = ["pink", "cyan", "yellow", "violet"]

for i in range(12):

    pen.color(colors[i % 4])
    pen.begin_fill()

    # Draw one square
    for j in range(4):
        pen.forward(50)
        pen.right(90)

    pen.end_fill()
    pen.right(30)

turtle.done()
