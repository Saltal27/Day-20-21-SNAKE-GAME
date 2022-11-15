from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, snake_color="white", segments_num=3, initial_x=0, initial_y=0, snake_heading="RIGHT"):

        """When creating an object using this class, the object will have these default attributes:
        snake color: white, number of snake segments: 3, coordinates of the first segment / head (of the snake): (0, 0),
         snake heading towards: Right
        However, you can change any of these attributes (when creating the object) using the key parameters:
        snake_color, segments_num, initial_x, initial_y, snake_heading"""

        self.segments_positions = []
        self.segment_x = initial_x
        self.segment_y = initial_y
        self.snake = []
        self.create_snake(snake_color, segments_num, snake_heading)
        self.head = self.snake[0]

    def create_snake(self, snake_color, segments_num, snake_heading):
        for _ in range(segments_num - 1):
            self.segments_positions.append((self.segment_x, self.segment_y))
            if snake_heading == "RIGHT":
                self.segment_x -= 20
            elif snake_heading == "LEFT":
                self.segment_x += 20

        for position in self.segments_positions:
            self.add_new_segment(position[0], position[1], snake_color, snake_heading)

    def add_new_segment(self, new_segment_x, new_segment_y, snake_color, snake_heading="RIGHT"):
        new_segment = Turtle(shape="square")
        new_segment.color(f"{snake_color}")
        new_segment.penup()
        new_segment.setposition(new_segment_x, new_segment_y)
        if snake_heading == "LEFT":
            new_segment.setheading(LEFT)
        self.snake.append(new_segment)

    def extend(self, segment_color="white", segments_num=1):
        for _ in range(segments_num):
            last_segment = self.snake[len(self.snake) - 1]
            added_segment_x = last_segment.xcor()
            added_segment_y = last_segment.ycor()
            self.segments_positions.append((added_segment_x, added_segment_y))
            self.add_new_segment(added_segment_x, added_segment_y, segment_color)

    def move(self):
        for segment_num in range(len(self.snake) - 1, 0, -1):
            previous_segment = self.snake[segment_num - 1]
            new_x = previous_segment.xcor()
            new_y = previous_segment.ycor()
            self.snake[segment_num].setposition(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def infinite_walls(self):
        for segment_num in range(len(self.snake) - 1):
            if self.snake[segment_num].xcor() > 280:
                self.snake[segment_num].setx(-280)

        for segment_num in range(len(self.snake) - 1):
            if self.snake[segment_num].xcor() < -280:
                self.snake[segment_num].setx(280)

        for segment_num in range(len(self.snake) - 1):
            if self.snake[segment_num].ycor() > 280:
                self.snake[segment_num].sety(-280)

        for segment_num in range(len(self.snake) - 1):
            if self.snake[segment_num].ycor() < -280:
                self.snake[segment_num].sety(280)

    def closed_box(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True

    def change_location(self, location_x, location_y, snake_heading):
        for segment in self.snake:
            segment.goto(location_x, location_y)
            if snake_heading == "RIGHT":
                location_x -= 20
            elif snake_heading == "LEFT":
                location_x += 20
                segment.setheading(LEFT)

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
