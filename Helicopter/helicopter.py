import time
import pygame
import random
from pygame.locals import *
pygame.init()
font=pygame.font.SysFont("arial",30) 
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,480))
running=1
x=40
y=210
level=1
up=1
down=1
left=1
right=1
wall=(random.randint(1,210),random.randint(1,210))
length=640
wall2=(random.randint(240,480),random.randint(240,480))
cwall=wall
cwall2=wall2
length2=length+640
m=0
b=0
m2=0
b2=0
wy=0
wy2=0
score=0
lc=0
cx=40
col=0
intx=0
intx2=0
intx3=0
intc=0
intc2=0
intc3=0
mc=0
mc2=0
mc3=0
while running:
    mouse=pygame.mouse.get_pressed()
    length2=length+640
    if x<length+1 and x>length-641 and level==1:
        if mc==0:
            m=(float(cwall[0])-float(cwall[1]))/(float(length-640)-length)   
            b=(-m*length)+cwall[1]
            m2=(float(cwall2[0])-float(cwall2[1]))/(float(length-640)-length)
            b2=(-m2*length)+cwall2[1]
            mc=1
            mc2=0
            mc3=0
        if intc==0:
            intx=length-640
            intx2=0
            intx3=0
            intc=1
            intc2=0
            intc3=0
        cx=(x-(length-640))+intx
        
    if x>length2-589 and x<length2+1 and level==1:
        if mc2==0:
            m=(float(wall[0])-wall[1])/(float(length2-590)-length2)
            b=(-m*length)+wall[1]
            m2=(float(wall2[0])-wall2[1])/(float(length2-590)-length2)
            b2=(-m2*length2)+wall2[1]
            mc=0
            mc2=1
            mc3=0
        if intc2==0:
            intx=0
            intx2=length2-590
            intx3=0
            intc2=1
            intc=0
            intc3=0
        cx=(x-(length2-590))+intx2
        
    if x>length2-640 and x<length2-590 and level==1:
        if mc3==1:
            m=(float(cwall[1])-float(wall[0]))/(float(length2-640)-float(length2-590))
            b=(-m*float(length2-640))+cwall[1]
            m2=(float(cwall2[1])-float(wall2[0]))/(float(length2-640)-float(length2-590))
            b2=(-m2*(length2-640))+cwall2[1]
            mc=0
            mc2=0
            mc3=1
        if intc3==0:
            intx=0
            intx2=0
            intx3=length2-640
            intc2=0
            intc=0
            intc3=1
        cx=(x-(length2-640))+intx3
    keys=pygame.key.get_pressed()
    screen.fill((255,255,255))
    if length+50<0 and level==1:
        col=1
        length=length2
        length2=length+640
        cwall=wall
        cwall2=wall2
        wall2=(random.randint(240,480),random.randint(240,480))
        wall=(random.randint(1,210),random.randint(1,210))
        
    if x==0:
        left=0
    if x==640:
        right=0
    print "score="+str(score)
    print intx
    print intx2
    print intx3
    
    if mouse[0] and level==1:
        y=y-1
    if not mouse[0] and level==1:
        y=y+1
    msgs=font.render(str(y),True,(0,0,0))
    screen.blit(msgs,(10,20))
    print "mouse0 = " + str(mouse[0])
    
    wy=m*cx+b
    wy2=m2*cx+b2
    if b==0:
        if y>480 or y<0:
            level=2
    print "b= "+str(b)
    
    print "b2= "+str(b2)
    print "m= "+str(m)
    print "m2= "+str(m2)
    print "wy "+str(wy)
    print "wy2 "+str(wy2)
    print "x " +str(x)
    print "y " +str(y)
    if not b==0:
        if (y<wy) or (y+30>wy2):
            level=2
    
    print "length" +str(length)
    print cx
    if level==1:
        length=length-1
        lc=10
        pygame.draw.rect(screen,(255,0,0),Rect((x,y),(30,30)))
       
        if keys[K_LEFT] and left==1:
            x=x-1
        if keys[K_RIGHT] and right==1:
            x=x+1
        pygame.draw.line(screen,(0,255,0),(length-640,cwall[0]),(length,cwall[1]))
        pygame.draw.line(screen,(0,255,0),(length-640,cwall2[0]),(length,cwall2[1]))
        pygame.draw.line(screen,(0,255,0),(length2-590,wall[0]),(length2,wall[1]))
        pygame.draw.line(screen,(0,255,0),(length2-590,wall2[0]),(length2,wall2[1]))
        pygame.draw.line(screen,(0,255,0),(length2-640,cwall[1]),(length2-590,wall[0]))
        pygame.draw.line(screen,(0,255,0),(length2-640,cwall2[1]),(length2-590,wall2[0]))
        
        
        score=score+1
    if level==2:
        msg=font.render("GAME OVER",True,(0,0,0))
        screen.blit(msg,(250,190))
        msg=font.render("You score is "+str(score),True,(0,255,0))
        screen.blit(msg,(250,230))
        if keys[K_RETURN]:
            level=1
            lc=10
            wall=(random.randint(1,210),random.randint(1,210))
            length=640
            wall2=(random.randint(240,480),random.randint(240,480))
            x=40
            y=210
            score=0
            intx=0
            intx2=0
            intx3=0

        lc=lc-1
    event = pygame.event.poll()
    if event.type ==pygame.QUIT:
        running=0
    clock.tick(300)
    pygame.display.update()
pygame.quit()