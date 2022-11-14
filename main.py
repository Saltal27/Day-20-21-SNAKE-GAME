from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen. tracer(0)

snake = Snake()
food = Food()
food.create_food()
special_food = Food()
special_food.create_special_food()
timer = special_food.timer
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
there_is_special_food = False
did_eat_it = True
counter = 2

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.infinite_walls()
    timer.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        did_eat_it = True

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    if scoreboard.score % 5 == 0 and scoreboard.score > 0 and did_eat_it:
        if not there_is_special_food:
            special_food.refresh()
            timer.change_location(-280, -295, "LEFT")
            there_is_special_food = True

    if there_is_special_food:
        if snake.head.distance(special_food) < 25:
            scoreboard.increase_score(increase_amount=2)
            snake.extend(segments_num=2)
            special_food.goto(1000, 1000)
            timer.change_location(1000, 1000, "LEFT")
            there_is_special_food = False

        if timer.snake[len(timer.snake) - 1].xcor() < -280:
            special_food.goto(1000, 1000)
            timer.change_location(1000, 1000, "LEFT")
            there_is_special_food = False
            did_eat_it = False

        counter += 1

    if counter % 2 == 0:
        special_food.hideturtle()
    else:
        special_food.showturtle()

screen.exitonclick()
