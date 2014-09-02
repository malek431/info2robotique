import math
import turtle
import random
boid =[]
pos =[]
N = 3
dmin = 50 #rayon de la zone de repultion
alpha =0.1
beta = 0.2
gamma =0.1
vcste=5
#creation des tortues
for  i in range ( N )  :
    boid.append(turtle.Turtle())
#initialisation des parametres
    boid[i].penup()
    boid[i].setposition(random.randint(-100,100),random.randint(-100,100))
    boid[i].setheading(random.randint(0,359))
    boid[i].color("blue")
    boid[i].pendown()

#moyenne des positions
def position_moyenne():
    sx,sy=0,0
    for i in range(N):
        x,y=boid[i].position()
        sx+=x
        sy+=y
    return sx / N, sy / N
def angle_moyenne():
    a = 0
    for i in range(N):
        a += boid[i].heading()
    return a / N 
#regle 2
def regle2():
    theta=angle_moyenne()/57.17
    return math.cos(theta), math.sin(theta)
#regle 1
def regle1(i):
    return position_moyenne() - boid[i].position()

def heading2speed(angle):
    return vcste*math.cos(angle/57.17),vcste*math.sin(angle/57.17)

def speed2heading(x,y):
    return math.atan2(y,x)*57.17
def bdistance(b,c):
    return b.distance(c)


def regle3(i):
    k = 0
    v= 0
    for j in range(N):
        if boid[i].distance(boid[j])<dmin:
            xi,yi=boid[i].position()
            xj,yj=boid[j].position()
            k+=1
            a=-(xj-xi)/k
            b=-(yj-yi)/k
            return a,b 
   
   

while 1 :
    pmx, pmy = position_moyenne()
    vx,vy =regle2()
    angle = angle_moyenne()
    for i in range(N):
        x,y=boid[i].position()
        r1x,r1y=pmx-x,pmy-y
        r3x,r3y=regle3(i)
       # entourage=mes_voisins(i)
       # if (len (entourage) > 0 ):
        #    ex,ey=position_moyenne(entourage)
        boid[i].setheading(speed2heading(alpha*vx+beta*r1x+gamma*r3x,alpha*vy+beta*r1y+gamma*r3y))
        boid[i].forward(vcste)

raw_input()
