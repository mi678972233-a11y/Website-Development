import turtle
canvas = turtle.Screen().bgcolor("Orange")
sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome To The Turtle Window")
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1
turtle.done()
    