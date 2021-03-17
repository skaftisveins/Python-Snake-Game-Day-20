from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_piece(position)

    def add_piece(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def reset(self):
        for piece in self.snake_body:
            piece.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_piece(self.snake_body[-1].position())

    def move(self):
        for piece in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[piece - 1].xcor()
            new_y = self.snake_body[piece - 1].ycor()
            self.snake_body[piece].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)


# nr1 = (25 ** 0.5)
# print(nr1)
# print(nr1 % 1)

# n = [1,2,3,4,5,6,7,8,9]

# m = ''.join(map(str, n))
# print(m)
