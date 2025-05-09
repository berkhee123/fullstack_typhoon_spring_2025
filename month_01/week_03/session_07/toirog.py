import turtle

NUM_CIRCLES = 15
screen_width = 800

# Радиусыг дэлгэцийн өргөнөөс хамааруулна
RADIUS = screen_width / (NUM_CIRCLES * 2)

turtle.speed(0)
turtle.penup()
turtle.goto(-screen_width/2 + RADIUS, 0)

for i in range(NUM_CIRCLES):
    if i % 2 == 0:
        turtle.color("red")
    else:
        turtle.color("green")
        
    turtle.begin_fill()
    turtle.circle(RADIUS)
    turtle.end_fill()
    
    turtle.forward(2 * RADIUS)

turtle.hideturtle()
turtle.done()

