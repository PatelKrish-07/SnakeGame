from snake import Snake
from turtle import Screen,Turtle
from food import Food
from scoreboard import Score
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")   #arrow keys start with capital letter
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food)<15:
        score.latest()
        food.refresh()
        snake.extend()

    #detect collision with wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()

    #detect collision with tail
    for item in snake.squares[1:]:

        if snake.head.distance(item)<10:

            score.reset()
            snake.reset()

screen.exitonclick()

