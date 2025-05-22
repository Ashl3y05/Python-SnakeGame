from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.bob_the_snake = []
        self.create_snake()
        self.head = self.bob_the_snake[0]

    def create_snake(self):
         for position in STARTING_POS:
            self.add_box_to_bob(position)

    def reset_snake(self):
        for seg in self.bob_the_snake:
            seg.goto(800,800)
        self.bob_the_snake.clear()
        self.create_snake()
        self.head = self.bob_the_snake[0]

    def add_box_to_bob(self, position):
        bob = Turtle(shape="square")
        bob.color("white")
        bob.penup()
        bob.goto(position)
        self.bob_the_snake.append(bob)

    def extend_snake(self):
        self.add_box_to_bob(self.bob_the_snake[-1].position())

    def move_snake(self):
        for box in range(len(self.bob_the_snake) - 1, 0, -1):
            next_x = self.bob_the_snake[box - 1].xcor()
            next_y = self.bob_the_snake[box - 1].ycor()
            self.bob_the_snake[box].goto(next_x, next_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
