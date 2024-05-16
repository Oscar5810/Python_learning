from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.dot()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    num_color = shape_side_n-3
    tim.color(colours[num_color])
    draw_shape(shape_side_n)


display = Screen()
display.exitonclick()
