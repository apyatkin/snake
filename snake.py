from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snack_body = []
        self.create_snake()
        self.head = self.snack_body[0]

    def create_snake(self):
        for segment in COORDINATES:
            snack_segment = Turtle(shape='square')
            snack_segment.penup()
            snack_segment.color('white')
            snack_segment.goto(segment)
            self.snack_body.append(snack_segment)

    def move(self):
        for seg in range(len(self.snack_body) - 1, 0, -1):
            new_x = self.snack_body[seg - 1].xcor()
            new_y = self.snack_body[seg - 1].ycor()
            self.snack_body[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


