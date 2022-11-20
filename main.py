from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_mode = screen.textinput(title="Game mode", prompt="Which mode would you like to choose?"
                                                       "\ntype 'i' for Infinite mode"
                                                       " / 'c' for 'Closed box mode'").lower()

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


def refresh_game():
    global snake
    global scoreboard
    global food

    snake.change_location(-1000, -1000, "right")
    snake = Snake()
    scoreboard.refresh_highest_score()
    scoreboard.score = 0
    scoreboard.refresh_scoreboard()
    
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    return snake


def hide_special_food():
    global special_food
    global there_is_special_food
    global timer

    there_is_special_food = False
    special_food.goto(1000, 1000)
    timer.change_location(1000, 1000, "LEFT")


game_is_on = True
there_is_special_food = False
did_eat_it = True
counter = 3
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    if game_mode == "i":
        snake.infinite_walls()
    elif game_mode == "c":
        if snake.closed_box():
            snake = refresh_game()
            food.refresh_position()
            if there_is_special_food:
                hide_special_food()
    timer.move()

    if snake.head.distance(food) < 15:
        food.refresh_position()
        scoreboard.increase_score()
        snake.extend()
        did_eat_it = True

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            snake = refresh_game()
            food.refresh_position()
            if there_is_special_food:
                hide_special_food()

    if scoreboard.score % 5 == 0 and scoreboard.score > 0 and did_eat_it:
        if not there_is_special_food:
            special_food.refresh_position()
            timer.change_location(-280, -295, "LEFT")
            there_is_special_food = True

    if there_is_special_food:
        if snake.head.distance(special_food) < 25:
            scoreboard.increase_score(increase_amount=2)
            snake.extend(segments_num=2)
            hide_special_food()

        if timer.snake[len(timer.snake) - 1].xcor() < -280:
            hide_special_food()
            did_eat_it = False

        counter += 1

    if counter % 3 == 0:
        special_food.hideturtle()
    else:
        special_food.showturtle()

screen.exitonclick()
