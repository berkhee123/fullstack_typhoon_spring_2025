import turtle
import time
import random
import threading

# Тохиргоо
NUM_CIRCLES = 15
screen_width = 800
screen_height = 400
RADIUS = screen_width / (NUM_CIRCLES * 2)

# Цонх
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("lightgreen")
screen.title("SUPER CATERPILLAR 👀🔊")

# Төмөрлөг
worm_segments = []
colors = ["red", "green", "blue", "orange", "purple", "pink", "cyan", "magenta", "lime"]
positions = []

# Толгойн сегмент
head = turtle.Turtle()
head.penup()
head.shape("circle")
head.color("darkgreen")
head.shapesize(RADIUS / 10)
worm_segments.append(head)

# Толгойгоос бусад
for i in range(1, NUM_CIRCLES):
    seg = turtle.Turtle()
    seg.penup()
    seg.shape("circle")
    seg.shapesize(RADIUS / 10)
    seg.color(random.choice(colors))
    worm_segments.append(seg)

# Эхний байрлал
x = -screen_width / 2 + RADIUS
y = 0
for i in range(NUM_CIRCLES):
    pos = (x + i * 2 * RADIUS, y)
    positions.append(pos)
    worm_segments[i].goto(pos)

# 😳 Нүд нэмэх
eye_left = turtle.Turtle()
eye_right = turtle.Turtle()
for eye in [eye_left, eye_right]:
    eye.shape("circle")
    eye.color("white")
    eye.shapesize(0.3)
    eye.penup()

# 🔊 Дуу тоглуулах (background thread)
def play_sound():
    while True:
        playsound('chomp.mp3')  # энд өөрийн хүссэн mp3 оруулж болно
        time.sleep(3)  # 3 секунд тутамд тоглоно

threading.Thread(target=play_sound, daemon=True).start()

# 👁️ Анивчих эффект
def blink_eyes():
    eye_left.color("black")
    eye_right.color("black")
    screen.update()
    time.sleep(0.2)
    eye_left.color("white")
    eye_right.color("white")
    screen.update()

def animate():
    screen.ontimer(animate, 100)
    for i in range(NUM_CIRCLES):
        worm_segments[i].goto(positions[i])
    
    # 👁️ Нүдийг толгойн байрлалд байрлуулах
    hx, hy = positions[0]
    eye_left.goto(hx - RADIUS / 2.5, hy + RADIUS / 2)
    eye_right.goto(hx + RADIUS / 2.5, hy + RADIUS / 2)

    # Анивчих эффектийг санамсаргүй хугацаанд
    if random.random() < 0.02:
        blink_eyes()

# 🐭 Хулганаар толгойг удирдах
def move_head(x_mouse, y_mouse):
    positions.insert(0, (x_mouse, y_mouse))
    positions.pop()

# Хулгана бүртгэх
screen.onscreenclick(move_head)

# Анимэйшн эхлүүлэх
screen.ontimer(animate, 100)

turtle.done()
