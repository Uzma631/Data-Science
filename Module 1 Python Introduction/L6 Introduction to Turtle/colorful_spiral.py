
import turtle

pen = turtle.Turtle()
pen.speed(0)

colors = ["red", "blue", "green", "yellow"]

for i in range(50):
    pen.color(colors[i % 4])
    pen.forward(i * 3)
    pen.right(90)

turtle.done()
