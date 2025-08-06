from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]  # Constant for initial positions
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []  # List to hold snake segments
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create initial three segments
        for x in STARTING_POSITIONS:
            self.add_segment(x, 0)  # Pass x, y coordinates for initial positions

    def add_segment(self, x, y):
        # Create and position a new segment
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(x, y)
        self.segments.append(snake)

    def extend(self):
        # Add a new segment at the position of the last segment
        last_segment = self.segments[-1]
        self.add_segment(last_segment.xcor(), last_segment.ycor())

    def move(self):
        # Move each segment to the position of the previous one
        for snake_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
