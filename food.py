from turtle import Turtle
from snake import Snake
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.timer = 0

    def create_food(self, food_stretch_wid=0.5, food_stretch_len=0.5, food_color="SteelBlue"):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=food_stretch_wid, stretch_len=food_stretch_len)
        self.color(food_color)
        self.refresh()

    def refresh(self):
        food_x = random.randint(-270, 270)
        food_y = random.randint(-270, 270)
        self.goto(food_x, food_y)

    def create_special_food(self):
        self.create_food(food_stretch_wid=1, food_stretch_len=1, food_color="Crimson")
        self.goto(1000, 1000)
        self.timer = Snake(segments_num=30, initial_x=1000, initial_y=1000, snake_color="Crimson", snake_heading="LEFT")
