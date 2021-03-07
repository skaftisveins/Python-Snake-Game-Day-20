from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.x_cordinates = [-20, 0, 20]
        self.snake_body = []

        for i in range(0, 3):
            snake = Turtle(shape='square')
            snake.color('white')
            snake.pu()
            snake.goto(x=self.x_cordinates[i], y=0)
            self.snake_body.append(snake)

    def move(self):
        for piece in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[piece - 1].xcor()
            new_y = self.snake_body[piece - 1].ycor()
            self.snake_body[piece].goto(new_x, new_y)
        self.snake_body[0].forward(20)

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
