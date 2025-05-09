import turtle
import time
import random

# Тохиргоо
NUM_CIRCLES = 15
screen_width = 800
screen_height = 400
RADIUS = screen_width / (NUM_CIRCLES * 2)

# Цонх тохиргоо
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("lightyellow")
screen.title("Caterpillar Animation!")

# Worm тохируулга
worm_segments = []
colors = ["red", "green", "blue", "orange", "purple", "pink", "cyan", "magenta", "lime"]

for i in range(NUM_CIRCLES):
    seg = turtle.Turtle()
    seg.penup()
    seg.shape("circle")
    seg.shapesize(RADIUS / 10)  # хэмжээ тохируулах
    seg.color(random.choice(colors))  # random өнгө
    worm_segments.append(seg)

# Эхний байрлал
x = -screen_width / 2 + RADIUS
y = 0
positions = []

for i in range(NUM_CIRCLES):
    pos = (x + i * 2 * RADIUS, y)
    positions.append(pos)
    worm_segments[i].goto(pos)

# Хулганаар толгойг удирдах
def move_head(x_mouse, y_mouse):
    # Толгойг хулгана руу зөөх
    positions.insert(0, (x_mouse, y_mouse))  # шинэ байрлал жагсаалтад нэмнэ
    positions.pop()  # хамгийн сүүлийнг хаяна (тасралтгүй урт хадгалахгүй)

    for i in range(NUM_CIRCLES):
        worm_segments[i].goto(positions[i])

# Хулгана хөдөлсөн үед дуудах
screen.ontimer(lambda: screen.onscreenclick(move_head), 100)

# Давтамжтайгоор байнга update хийж байх
def animate():
    screen.ontimer(animate, 100)  # 100ms тутамд өөрийгөө дахин дуудах
    for i in range(NUM_CIRCLES):
        worm_segments[i].goto(positions[i])

screen.ontimer(animate, 100)

# Үзэгчийн цонх нээгдэхийг хүлээнэ
turtle.done()
