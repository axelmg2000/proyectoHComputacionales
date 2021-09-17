"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
vel = 1000 #Add variable that controls speed (ms)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global vel #Created a global variable named vel  
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    randNum = random.randint(0,6)
    if(randNum == 1):
    #El 25% de las veces aproximadamente se cambiará la posición de la comida cuando la serpiente de acerque
        x = head.x
        y = head.y
        if ((x == food.x - 10 or x == food.x + 10) and y == head.y) or ((y == food.y - 10 or y == food.y + 10) and x == head.x):
                food.x = randrange(-15, 15) * 10
                food.y = randrange(-15, 15) * 10

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, vel) #Added variable that contains the snake´s speed 

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Change the snakes arrow keys
onkey(lambda: change(10, 0), 's')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 'z')

move()
done()
