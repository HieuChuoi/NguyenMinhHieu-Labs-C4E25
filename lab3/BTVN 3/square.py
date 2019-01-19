from turtle import *
def draw_square(dai, mau):
    color(mau)
    for i in range(4):
        forward(dai)
        left(90)
draw_square(100, "red")
# speed(0)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()