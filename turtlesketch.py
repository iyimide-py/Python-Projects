from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


def move_forward():
    tim.forward(10)


def move_back():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

def draw_circle():
    tim.circle(100)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="o", fun=draw_circle)


screen.exitonclick()

