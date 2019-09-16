import turtle as t
from time import sleep


length_between_consecutive_elements = 200


def draw_a_star(N):
    if N % 2:
        center_angle = (N // 2) / N * 360
    else:
        center_angle = (N // 2 - 1) / N * 360
    
    angle_of_rotation = center_angle    
    t.right(center_angle / 2)


    for i in range(N):
        t.forward(length_between_consecutive_elements)
        t.right(angle_of_rotation)
    
    t.left(center_angle / 2)
    

t.penup()
t.goto(-120, 100)
t.pendown()
draw_a_star(5)

t.penup()
t.goto(120, 100)
t.pendown()
draw_a_star(11)

pause = 5
sleep(pause)



