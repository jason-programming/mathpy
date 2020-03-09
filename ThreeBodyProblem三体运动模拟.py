'''
作品名称：三体运动模拟
作者：朱既同
学校：深圳外国语学校
班级：初一一班
学号：201910129
Python3.7
'''
import turtle
import math

Tnow = 0
Tstep = 300 #每300s计算一次
G=6.6726e-11 #万有引力常数
scale=0.5e9 #绘图比例尺
State = True
lastpos_x = {}
lastpos_y = {}

t=turtle.Pen()
s=turtle.Pen()
m=turtle.Pen()
t.speed(0)
s.speed(0)
m.speed(0)
t.shape('circle')
s.shape('circle')
m.shape('circle')
t.shapesize(0.3)
s.shapesize(0.3)
m.shapesize(0.3)
t.color('blue')
s.color('red')
t.up()
s.up()
m.up()


class star:
    '''创建星类'''
    global Tstep
    def __init__(self,m,x=0,y=0,z=0,vx=0,vy=0,vz=0):#注：单位一律使用国际通用单位（m:质量  x,y,z:星初始坐标  vx,vy,vz:星初始速度）
        self.m = m
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
    
    def calc(self,f):#f：x,y,z三个方向上的力组成的列表
        '''
        计算星位置
        '''
        fx = f[0]
        fy = f[1]
        fz = f[2]
        self.vx = self.vx + (fx / self.m * Tstep)
        self.x = self.x + self.vx * Tstep
        
        self.vy = self.vy + (fy / self.m * Tstep)
        self.y = self.y + self.vy * Tstep
        
        self.vz = self.vz + (fz / self.m * Tstep)
        self.z = self.z + self.vz * Tstep


def gravity(star1, star2):#star1,star2：两个星对象
    '''
    计算星之间的引力
    注：返回值是作用于star1（传进来的第一个参数）x,y,z三个方向上的力组成的列表
    '''
    r2 = (star2.x-star1.x)**2 + (star2.y-star1.y)**2 + (star2.z-star1.z)**2
    f  = G*(star1.m*star2.m) / r2
    fx = (star2.x-star1.x)*f / math.sqrt(r2)
    fy = (star2.y-star1.y)*f / math.sqrt(r2)
    fz = (star2.z-star1.z)*f / math.sqrt(r2)

    return fx,fy,fz

def cf3(star1, star2, star3):#star1,star2,star3：三个星对象
    '''
    计算合力
    注：返回值是作用于star1（传进来的第一个参数）x,y,z三个方向上的合力组成的列表
    '''
    f2=gravity(star1,star2)
    f3=gravity(star1,star3)
    fx=f2[0]+f3[0]
    fy=f2[1]+f3[1]
    fz=f2[2]+f3[2]

    return fx,fy,fz

def distance(x1, y1, x2, y2):#x1,y1：第一个物体的坐标  x2,y2：第二个物体的坐标
    '''
    计算距离
    注：只有x,y坐标是因为此函数用于绘图（平面图）
    '''
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def fastdraw(Tt, htkey, x, y):#Tt：海龟对象  htkey：字典索引  x,y：星当前位置
    '''
    绘图函数
    注：正常情况下每天更新一次星位置以提高绘图速度，当两次星距离（图上）大于3像素，每次计算都更新星位置以提高绘图精度
    '''
    global Tnow
    global lastpos_x
    global lastpos_y
    
    if (htkey not in lastpos_x):
        lastpos_x[htkey] = Tt.pos()[0]
        lastpos_y[htkey] = Tt.pos()[1]

    if ((Tnow % 86400 == 0) or (distance(lastpos_x[htkey], lastpos_y[htkey], x, y) > 3.0)):
        Tt.goto(x, y)
        lastpos_x[htkey] = x
        lastpos_y[htkey] = y


#创建三体
star1=star(2e31,1e11,0,0,-7e4,-7e4,0)
star2=star(2e31)
star3=star(2e31,-2e11,0,0,7e4,7e4,0)


#主程序
while (True):
    star1.calc(cf3(star1,star2,star3))
    star2.calc(cf3(star2,star1,star3))
    star3.calc(cf3(star3,star1,star2))

    if (State and (Tnow > 0)):
        t.down()
        s.down()
        m.down()
        State = False

    fastdraw(t, id(t), star1.x//scale, star1.y//scale)
    fastdraw(s, id(s), star2.x//scale, star2.y//scale)
    fastdraw(m, id(m), star3.x//scale, star3.y//scale)
    if Tnow%86400 == 0:
        print("Day",int(Tnow//86400))

    Tnow = Tnow + Tstep
    
    
        

