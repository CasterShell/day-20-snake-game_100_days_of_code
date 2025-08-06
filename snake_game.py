import turtle
from turtle import Screen, Turtle
import time

from score_board import Score
from snake_class import Snake
from food import Food


user_score = Score()
snake = Snake()
food = Food()


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#x_position = [0,-20,-40]

#all_snakes = []



#create snake body



game_is_on = True
while game_is_on:
    user_score.show_score()
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        user_score.add_point()
    #detect collision with wall
    if snake.head.xcor() >  280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        user_score.game_over()
    #detects collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            user_score.game_over()


screen.exitonclick()


