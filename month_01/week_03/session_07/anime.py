import turtle
import time

# Тохиргоо
NUM_CIRCLES = 15
screen_width = 800
screen_height = 400
RADIUS = screen_width / (NUM_CIRCLES * 2)

# Цонхны тохиргоо
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("lightblue")

# Тохируулга
worm = turtle.Turtle()
worm.penup()
worm.speed(0)  # Хурдан

# Эхний байрлал
x = -screen_width / 2 + RADIUS
y = 0

# Давталт
for i in range(NUM_CIRCLES):
    worm.goto(x, y)
    
    if i % 2 == 0:
        worm.color("red")
    else:
        worm.color("green")
        
    worm.begin_fill()
    worm.circle(RADIUS)
    worm.end_fill()
    
    x += 2 * RADIUS  # Дараагийн тойргийн байрлал
    
    time.sleep(0.1)  # Анимэйшн мэт харагдуулахын тулд бага зэрэг хүлээлт

# Дууссан хойно turtle-г нуух
worm.hideturtle()
turtle.done()

