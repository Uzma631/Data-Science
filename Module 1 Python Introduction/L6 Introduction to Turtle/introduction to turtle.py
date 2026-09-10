import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Graphics")
board=turtle.Turtle()
board.speed("fastest")
board.hideturtle()
colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(0,4):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(100)
    board.left(90)
    board.forward(100)
    board.left(90)
