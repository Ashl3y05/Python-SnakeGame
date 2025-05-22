from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard

from snake import Snake




screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Bland Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.randomize_location()
        snake.extend_snake()
        scoreboard.increase_score()
        scoreboard.refresh_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.reset_game()
        snake.reset_snake()
        scoreboard.game_over()


    for box in snake.bob_the_snake[1:]:  # Slicing
        if snake.head.distance(box) < 15:
            is_game_on = False
            scoreboard.reset_game()
            snake.reset_snake()


screen.exitonclick()
