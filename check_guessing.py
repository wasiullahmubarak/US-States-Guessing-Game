#



from turtle import Turtle, Screen
import pandas
SIZE=[200.0,200.0]
image="Table/New_file/map.gif"
screen = Screen()
turtle = Turtle()
screen.title("STATE NAMES")

screen.colormode(255)
screen.addshape(image)
turtle.shape(image)
screen.setup(900,600)