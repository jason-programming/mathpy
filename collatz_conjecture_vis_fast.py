import turtle,random, math, colorsys, time
from turtle import Turtle, Screen

t=turtle.Pen()
t.speed(0)
t.clear()
t.width(3)

window = turtle.Screen()
window.screensize()
window.setup(width=1.0, height=1.0)

screen = Screen()
width = screen.window_width()
height = screen.window_height()

delta = 37
alpha = 110
r=10

dict_pos = dict()
dict_head = dict()

def inbounds(limit, value):
    'returns boolean answer to question "is turtle position within my axis limits"'
    return -limit < value * 2 < limit

def invisible():
    x, y = t.position()
    if not inbounds(height, y):
        return True

    if not inbounds(width, x):
        return True

    return False
    
def collatz_conjecture_visual(num):
    start = num
    collatz_list=[]
    step_count=[]
    while num>1:
        collatz_list.insert(len(collatz_list),int(num))
        step_count.insert(0,len(collatz_list))
        if num>1:
            if num%2==1:
                num=num*3+1
            else:
                num=num/2

        if num==1:
            collatz_list.insert(len(collatz_list),1)

    screen.tracer(0, 0)
    screen.title(str(start) + ", " + str(len(collatz_list)))

    t.up()
    t.home()
    t.goto(-650, -250)
    #print(collatz_list)

    step = 0
    last_pos = t.position()
    last_head = t.heading()

    for x in range(0, len(collatz_list)):
        d = len(collatz_list)-1 - x
        n = collatz_list[d]
        step = step + 1
        
        if ((step, n) in dict_pos):
            last_pos = dict_pos[step, n]
            last_head = dict_head[step, n]
        else:
            t.up()
            t.setposition(last_pos)
            t.setheading(last_head)
            h = math.log(step)/5.0
            if (h > 1.0):
                h = 1.0
            t.color(colorsys.hsv_to_rgb(h, 1.0, 1.0))
            
            if (n%2) == 0:
                t.right(alpha/4.0)
            else:
                t.right(alpha/2.0)

            last_head = t.heading()
            t.down()
            t.circle(r, min(180.0, 270/math.log(step+2)))
            
            t.up()
            t.setposition(last_pos)
            t.setheading(last_head)
            t.down()
            t.circle(r,delta)
                
            dict_pos[step, n] = last_pos = t.position()
            dict_head[step, n] = last_head = t.heading()

            if (invisible()):
                break

    screen.update()

for x in range(1,1000000):
    collatz_conjecture_visual(x)
