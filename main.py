from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food
import time

GAME_SPEED = 0.08

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # Detect collision with food.
    if snake.snake_body[0].distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()

screen.exitonclick()
