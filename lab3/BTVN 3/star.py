from turtle import *
color("red")
def draw_star(x, y, length): 
    penup()
    setpos(x,y)
    left(36)
    pendown()
    for i in range(5):
        forward(length)
        left(144)
draw_star(7, 8, 100)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)


mainloop()