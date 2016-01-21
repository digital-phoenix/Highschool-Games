import time
import pygame
import random
pygame.init()


        
def border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md):
    
    pygame.draw.rect(screen,(0,255,0),Rect((30,30), (600,420)),1)
    
    if xnp>29 and xnp<31:
        left=0
    
        
    if (bx>30 and bx<35) and shot==1:   
        exite=1
        exitn=0
        mn=0
        me=1
    if (by>450 and by<455)and shot==1:
        exitn=-1
        exite=0
        mn=-1
        me=0
    if (bx>630 and bx<635)and shot==1:
        exite=-1
        exitn=0
        mn=0
        me=-1
    if (by>30 and by<35)and shot==1:
        exitn=1
        exite=0
        mn=1
        me=0
    if (bx>30 and bx<35) and shot==2:   
        exite2=1
        exitn2=0
        mn2=0
        me2=1
    if (by>450 and by<455)and shot==2:
        exitn2=-1
        exite2=0
        me2=0
        mn2=-1
    if (bx>630 and bx<635)and shot==2:
        exite2=-1
        exitn2=0
        mn2=0
        me2=-1
    if (by>30 and by<35)and shot==2:
        exitn2=1
        exite2=0
        mn2=1
        me2=0
    if (bx>30 and bx<35) or (by>450 and by<455) or (bx>630 and bx<635) or (by>30 and by<35):
        if shot==1:
           
            portalx=bx
            portaly=by
           
        if shot==2:
         
            portalx2=bx
            portaly2=by
         
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
        
        
    if y-radius>30 and y-radius<35:
        fall=1
        md=0
    if xpp>629 and xpp<631:
        right=0
        
    if y+4*radius<451 and y+4*radius>449:
        fall=0
        md=0
    return fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md

def border3(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md):
    
    pygame.draw.rect(screen,(0,0,0),Rect((30,30), (600,420)),1)
    pygame.draw.line(screen,(0,255,0),(30,30), (130,30))
    pygame.draw.line(screen,(0,255,0),(30,450), (130,450))
    if xnp>29 and xnp<31:
        left=0
    if bx<130 and bx>29 and by<31 and by>29 and shot==2:
        exitn2=1
        exite2=0
        mn2=1
        me2=0
        portalx2=bx
        portaly2=by
    if bx<130 and by>29 and by<31 and bx>29 and shot==1:
        exitn=1
        exite=0
        mn=1
        me=0
        portalx=bx
        portaly=by
    
    if bx<130 and bx>29 and by>449 and by<451 and shot==2:
        exitn2=1
        exite2=0
        mn2=1
        me2=0
        portalx2=bx
        portaly2=by
    if bx<130 and by>29 and by<449 and bx>451 and shot==1:
        exitn=1
        exite=0
        mn=1
        me=0
        portalx=bx
        portaly=by

    if (bx>30 and bx<31) or (by>450 and by<451) or (bx>630 and bx<631) or (by>30 and by<31):
        
           
      
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
        
        
    if y-radius>30 and y-radius<35:
        fall=1
        md=0
    if xpp>629 and xpp<631:
        right=0
        
    if y+4*radius<451 and y+4*radius>449:
        fall=0
        md=0
    return fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md

def cliff3(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md):
    
    pygame.draw.rect(screen,(0,0,0),Rect((cliffx,cliffy), (cliffw,450-cliffy)),1)
    
    if xnp>cliffx+cliffw-2 and xnp<cliffx+cliffw+2 and y>cliffy :
        left=0
        
      
    if bx>cliffx-1 and bx<cliffx+cliffw+5 and by>cliffy and by<450:
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
        
        
    if y+4*radius>cliffy-1 and y+4*radius<cliffy+2 and xpp>cliffx-1 and xnp<cliffx+cliffw+5:
        fall=0
    if xpp<cliffx+2 and xpp>cliffx-2 and y+4*radius>cliffy:
        right=0
        
    
    return fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md

def cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md):
    
    pygame.draw.rect(screen,(0,255,0),Rect((cliffx,cliffy), (cliffw,450-cliffy)),1)
    
    if xnp>cliffx+cliffw-2 and xnp<cliffx+cliffw+2 and y>cliffy :
        left=0
    
        
    if (bx>cliffx-1 and bx<cliffx+5) and by>cliffy and shot==1:   
        exite=-1
        exitn=0
        mn=0
        me=-1
    if (bx>cliffx+cliffw-1 and bx<cliffx+cliffw+5) and by<cliffy and shot==1:
        exite=1
        exitn=0
        mn=0
        me=1
    if (by<cliffy+5 and by>cliffy-1)and x>cliffx-1 and x<cliffx+cliffw and shot==1:
        exitn==-1
        exite=0
        mn=-1
        me=0
    if (bx>cliffx-1 and bx<cliffx+5) and by>cliffy and shot==2:   
        exite2=-1
        exitn2=0
        me2=-1
        mn2=0
    if (bx>cliffx+cliffw-1 and bx<cliffx+cliffw+5) and by>cliffy and shot==2:
        exite2=1
        exitn2=0
        mn2=0
        me2=1
    if (by<cliffy+5 and by>cliffy-1)and x>cliffx-1 and x<cliffx+cliffw and shot==2:
        exitn2=-1
        exite2=0
        me2=0
        mn2=-1
    if bx>cliffx-1 and bx<cliffx+cliffw+5 and by>cliffy and by<450:
        if shot==1:
           
            portalx=bx
            portaly=by
           
        if shot==2:
         
            portalx2=bx
            portaly2=by
         
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
        
        
    if y+4*radius>cliffy-1 and y+4*radius<cliffy+2 and xpp>cliffx-1 and xnp<cliffx+cliffw+5:
        fall=0
    if xpp<cliffx+2 and xpp>cliffx-2 and y+4*radius>cliffy:
        right=0
        
    
    return fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md

def cliff2(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md):
    
    pygame.draw.rect(screen,(0,255,0),Rect((cliffx,cliffy), (cliffw,450-cliffy)),1)
    
    if xnp>cliffx2+cliffw2-2 and xnp<cliffx2+cliffw2+2 and y>cliffy2 :
        left=0
    
        
    if (bx>cliffx2-1 and bx<cliffx2+5) and by>cliffy2 and shot==1:   
        exite=-1
        exitn=0
        mn=0
        me=-1
    if (bx>cliffx2+cliffw2-1 and bx<cliffx2+cliffw2+5) and by<cliffy2 and shot==1:
        exite=1
        exitn=0
        mn=0
        me=1
    if (by<cliffy2+5 and by>cliffy2-1)and x>cliffx2-1 and x<cliffx2+cliffw2 and shot==1:
        exitn==-1
        exite=0
        mn=-1
        me=0
    if (bx>cliffx2-1 and bx<cliffx2+5) and by>cliffy2 and shot==2:   
        exite2=-1
        exitn2=0
        me2=-1
        mn2=0
    if (bx>cliffx2+cliffw2-1 and bx<cliffx2+cliffw2+5) and by>cliffy2 and shot==2:
        exite2=1
        exitn2=0
        mn2=0
        me2=1
    if (by<cliffy2+5 and by>cliffy2-1)and x>cliffx2-1 and x<cliffx2+cliffw2 and shot==2:
        exitn2=-1
        exite2=0
        me2=0
        mn2=-1
    if bx>cliffx2-1 and bx<cliffx2+cliffw2+5 and by>cliffy2 and by<450:
        if shot==1:
           
            portalx=bx
            portaly=by
           
        if shot==2:
         
            portalx2=bx
            portaly2=by
         
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
        
        
    if y+4*radius>cliffy2-1 and y+4*radius<cliffy2+2 and xpp>cliffx2-1 and xnp<cliffx2+cliffw2+5:
        fall=0
    if xpp<cliffx2+2 and xpp>cliffx2-2 and y+4*radius>cliffy2:
        right=0
        
    
    return fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md

def roof(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md):
    
    pygame.draw.rect(screen,(0,255,0), Rect((roofx,30),(roofw,roofy,)),1)
    
    if xnp>roofx+roofw-2 and xnp<roofx+roofw+2 and y<roofy+30 :
        left=0
    
        
    if (bx>roofx-1 and bx<roofx+5) and by<roofy+30 and shot==1:   
        exite=-1
        exitn=0
        mn=0
        me=-1
    if (bx>roofx+roofw-1 and bx<roofx+roofw+5) and by<roofy+30 and shot==1:
        exite=1
        exitn=0
        mn=0
        me=1
    if (by>roofy+35 and by<roofy+29)and x>roofx-1 and x<roofx+roofw and shot==1:
        exitn=1
        exite=0
        mn=1
        me=0
        
    if (bx>roofx-1 and bx<roofx+5) and by<roofy+30 and shot==2:   
        exite2=-1
        exitn2=0
        mn2=0
        me2=-1
    if (bx>roofx+roofw-1 and bx<roofx+roofw+5) and by<roofy+30 and shot==2:
        exite2=1
        exitn2=0
        mn2=0
        me2=1
    if (by>roofy+30 and by<roofy-1)and x>roofx-1 and x<roofx+roofw and shot==2:
        exitn2=1
        exite2=0
        mn2=1
        me2=0
    if bx>roofx-1 and bx<roofx+roofw+5 and by<roofy+30 and by>29:
        if shot==1:
           
            portalx=bx
            portaly=by
           
        if shot==2:
         
            portalx2=bx
            portaly2=by
         
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
        
        
    
    if xpp<roofx+2 and xpp>roofx-2 and y+4*radius<roofy+30:
        right=0
    return fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md
def enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n):
    pygame.draw.rect(screen,(0,0,0),Rect((doorx,doory),(50,100)))
    if x>doorx-1 and x<doorx+50 and y>doory:
        level=level+1
        x=50
        y=400
        portalx=0
        portaly=0
        portalx2=0
        portaly2=0
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
        
    return level,x,y,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n 
def stickman(x,y,radius,screen,cb):
    x=int(x)
    y=int(y)
    pygame.draw.line(screen,(cb),(x-radius/2,y),(x-radius/2,y))
    pygame.draw.line(screen,(cb),(x+radius/2,y),(x+radius/2,y))
    pygame.draw.line(screen,(cb),(x-radius/2,y+radius/2),(x+radius/2,y+radius/2))
    pygame.draw.circle(screen,(cb),(x,y),(radius),1)
    pygame.draw.line(screen,(cb),(x,y+radius),(x,y+3*radius))
    pygame.draw.line(screen,(cb),(x-radius,y+4*radius),(x,y+3*radius))
    pygame.draw.line(screen,(cb),(x+radius,y+4*radius),(x,y+3*radius))
    pygame.draw.line(screen,(cb),(x,(y+2*radius)+radius/2),(x-radius,(y+2*radius)))
    pygame.draw.line(screen,(cb),(x,+((y+2*radius))+radius/2),(x+radius,y+2*radius))
    
def gpos(xpp,xy,xnp,cb,y,x,radius,screen):
    if xpp<xy[0]:
        pygame.draw.line(screen,(cb),(x+radius,y+2*radius),(x+radius+10,y+2*radius))
    if xnp>xy[0]:
        pygame.draw.line(screen,(cb),(x+radius,y+2*radius),(x-radius-10,y+2*radius))

   

def linecalc(m,y,radius,xy,x,b,bx,by,mouse,dx,e,n,dy):
       
  
    if  m==0 and shoot>0 and not xy[1]==y and not xy[0]==x and n==0 and e==0: 
       
        m=(float(xy[1])-float(y))/(float(xy[0])-float(x))
       
        b=-m*x+(y)
        if xy[0]<x:
            dx=-1
        if xy[1]>y:
            dy=1
        if xy[1]<y:
            dy=-1
        if xy[0]>x:
            dx=1
    if xy[0]==x:
        if xy[1]>y:
            n=1
        if xy[1]>y:
            n=-1
    if xy[1]==y:
        if xy[0]>x:
            e=1
        if xy[0]>x:
            e=-1
        
    if not e==0 or not n==0:
        if bx==0:
            bx=x
        if by==0:
            by=y
        bx=bx+e
        by=by+n
        
    if not m==0:
        
       
        
        if bx==0:
            bx=x
        if by==0:
            by=y
        if m>1 or m<-1 :
            by=by+dy
            bx=(by/m)-(b/m)
        if m<1 and m>-1:
            bx=bx+dx
            by=m*bx+b
        print "m="+str(m)
        print dy
        #pygame.draw.rect(screen,(0,255,0),Rect((bx,by),(5,5)))
        
        #if not m==0: 
        #print "m="+str(m)
        #print "b"+str(b)
        #print "by"+str(by)
        #print "bx"+str(bx)
    
    return bx,by,m,dx,b,e,n,shoot,dy
from pygame.locals import *


clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,480))
running=1
cb=(0,0,0)
white=(255,255,255)
x=200
y=400
radius=10
b=0
m=0
gposy=0
gposx=0
xpp=x+radius
xnp=x-radius
fall=0
left=1
right=1
bx=0
by=0
dx=0
e=0
n=0
portal=0 
portalx=0
portaly=0
portalx2=0
portaly2=0
shoot=0
shot=0
exite=0
exitn=0
exitn2=0
exite2=0
momentum=0
refresh=momentum
xportal=0
cliffx=0
cliffy=0
cliffw=0
mn=0
me=0
mn2=0
me2=0
md=0
come=0
checkx=portalx
checky=portaly
checkx2=portalx2
checky2=portaly2
ml=2
level=1
doorx=0
dorry=0
cliffx2=0
cliffy2=0
cliffw2=0
dy=0
while running:
    
    
    if not xportal==0:
            xportal=xportal-1
    if by>480 or by<1 or bx>640 or bx<1:
        bx=0
        dx=0
        by=0
        m=0 
        e=0
        n=0
    mouse=pygame.mouse.get_pressed()
    keys=pygame.key.get_pressed()
    if mouse[0]:
        shoot=shoot+1
    if keys[K_e]:
        shoot=1
        shot=1
    if keys[K_r]:
        portalx=0 
        portaly=0
        portalx2=0
        portaly2=0
    if keys[K_w]:
        shoot=1
        shot=2
    if xnp==0:
        left=0
    if xpp==640:
        right=0
    if  keys[K_LEFT]  and left==1:
        x=x-1
    if  keys[K_RIGHT] and right==1:
        x=x+1
    
    screen.fill((255,255,255))
   
    xy=pygame.mouse.get_pos()
    xpp=x+radius
    xnp=x-radius
    left=1
    right=1
    if shot==0:
        shot=shoot
    
    stickman(x,y,radius,screen,cb)
    gpos(xpp,xy,xnp,cb,y,x,radius,screen)
    
    bx,by,m,dx,b,e,n,shoot,dy=linecalc(m,y,radius,xy,x,b,bx,by,mouse,dx,e,n,dy)
    #level 1
    if level==1:
        border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md=border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
        cliffx=300
        cliffw=100
        cliffy=200
        cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md=cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
        doorx=610
        doory=380
        enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
        level,x,y,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n=enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
        #level 2
    if level==2:
        border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md=border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
        cliffx=128
        cliffw=128
        cliffy=350
        cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md=cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
        cliffx2=384
        cliffw2=148
        cliffy2=150
        cliff2(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md=cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md)
        roofx=128
        roofw=128
        roofy=200
        roof(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md= roof(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md)
        doorx=610
        doory=380
        enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
        level,x,y,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n=enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
       #level 3
    if level==3:
        border3(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md=border3(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
        cliffx=100
        cliffy=200
        cliffw=100
        cliff3(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
        fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md=cliff3(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
        doorx=610
        doory=380
        enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
        level,x,y,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n=enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
    if not portalx==0:
        pygame.draw.circle(screen,(0,0,255),(int (portalx), int(portaly)),(20))
    if not portalx2==0:
        
        pygame.draw.circle(screen,(0,255,0),(int (portalx2),int (portaly2)),(20))
    
    if fall==1:
        y=y+1
   
        #print md
    if not portalx==0 and not portalx2==0 and x<portalx+20 and x>portalx-20 and y+3*radius>portaly-20 and y+3*radius<portaly+20 and xportal==0:
        if exite2==1:
            x=portalx2+(2*radius)
            
            if portaly2>250:
                y=portaly2-4*radius
            if portaly2<250:
                y=portaly2
        if exite2==-1:
            x=portalx2-(2*radius)
            
            if portaly2>250:
                y=portaly2-4*radius
            if portaly2<250:
                y=portaly2
        if exitn2==-1:
            y=portaly2-(4*radius)-30 
            x=portalx2
        if exitn2==1:
            y=portaly2+50
            x=portalx2
        if momentum<249:
            momentum=momentum+40
        if momentum>249:
            momentum=250
        
        come=1
        xportal=1
        #print x   
        #print y
        
    if not portalx==0 and not portalx2==0 and x<portalx2+20 and x>portalx2-20 and y+3*radius>portaly2-20 and y+3*radius<portaly2+20 and xportal==0:
        if exite==1:
            x=portalx+(2*radius)
            if portaly>250:
                y=portaly-4*radius
            if portaly<250:
                y=portaly
        if exite==-1:
            x=portalx-(2*radius)
            if portaly>250:
                y=portaly-4*radius
            if portaly<250:
                y=portaly
        if exitn==-1:
            y=portaly-(4*radius)-30
            x=portalx
        if exitn==1:
            y=portaly+50
            x=portalx
       
       
        come=2
        xportal=1
        if momentum<249:
            momentum=momentum+40
        if momentum>249:
            momentum=250
        #print x
        #print y
    
           
    
        
    if momentum>0:
        if fall==0:
            momentum=0
        #print mn
        
       
        #print mn2    
        if momentum<249:
            md=momentum 
        if momentum>249:
            md=250
            
        print momentum
        print ml
       #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
        while not md==0 and momentum>10: 
            xpp=x+radius
            xnp=x-radius
            screen.fill((255,255,255))
           
            refresh=momentum
            if come==1:
                if (right==1 and me2==1) or (left==1 and me2==-1):  
                    x=x+me2
                y=y+mn2
            if come==2:
                if (right==1 and me2==1) or (left==1 and me2==-1):  
                    x=x+me
                    
                y=y+mn
            if come==0 or (mn==-1 and not me2==0) or (mn2==-1 and not me==0):
                y=y+2
            md=md-1
            #print x
            #print y
            if not portalx==0 and not portalx2==0 and x<portalx+20 and x>portalx-20 and y+3*radius>portaly-20 and y+3*radius<portaly+20 and xportal==0:
                if me2==1:
                    x=portalx2+(2*radius)
                
                    if portaly2>250:
                        y=portaly2-4*radius
                    if portaly2<250:
                        y=portaly2
                if me2==-1:
                    x=portalx2-(2*radius)
                
                    if portaly2>250:
                        y=portaly2-4*radius
                    if portaly2<250:
                        y=portaly2
                if mn2==-1:
                    y=portaly2-(4*radius)-50 
                    x=portalx2
                if mn2==1:
                    y=portaly2+50
                    x=portalx2
                if momentum<249:
                    momentum=momentum+40
                if momentum>249:
                    momentum=250
           
                come=1
                xportal=1
                #print x   
                #print y
        
            if not portalx==0 and not portalx2==0 and x<portalx2+20 and x>portalx2-20 and y+3*radius>portaly2-20 and y+3*radius<portaly2+20 and xportal==0:
                    if me==1:
                        x=portalx+(2*radius)
                        if portaly>250:
                            y=portaly-4*radius
                        if portaly<250:
                            y=portaly
                    if me==-1:
                        x=portalx-(2*radius)
                        if portaly>250:
                            y=portaly-4*radius
                        if portaly<250:
                            y=portaly
                    if mn==-1:
                        y=portaly-(4*radius)-50
                        x=portalx
                    if mn==1:
                        y=portaly+50
                        x=portalx
                    
                    come=2
                    xportal=1
                    if momentum<249:
                        momentum=momentum+40
                    if momentum>249:
                        momentum=250
        
            checkx=portalx
            checky=portaly
            checkx2=portalx2
            checky2=portaly2
            if level==1:
                border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
                fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md=border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
                cliffx=300
                cliffw=100
                cliffy=200
                cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
                fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md=cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
                doorx=610
                doory=380
                enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
                level,x,y,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n=enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
                #level 2
            if level==2:
                border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
                fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md=border(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,mn,me,mn2,me2,md)
                cliffx=128
                cliffw=128
                cliffy=350
                cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
                fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md=cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx,cliffy,cliffw,mn,me,mn2,me2,md)
                cliffx2=384
                cliffw2=148
                cliffy2=150
                cliff2(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md)
                fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md=cliff(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,cliffx2,cliffy2,cliffw2,mn,me,mn2,me2,md)
                roofx=128
                roofw=128
                roofy=200
                roof(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md)
                fall,left,right,portal,portalx,portaly,portalx2,portaly2,bx,by,m,e,n,shot,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md= roof(xpp,xnp,y,radius,fall,left,right,portal,portalx,portaly,bx,by,shot,portalx2,portaly2,m,e,n,exite,exitn,exite2,exitn2,roofx,roofy,roofw,mn,me,mn2,me2,md)
                doorx=610
                doory=380
                enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
                level,x,y,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n=enddoor(x,y,doorx,doory,level,portalx,portaly,portalx2,portaly2,bx,dx,by,m,e,n)
                      
            stickman(x,y,radius,screen,cb)
            gpos(xpp,xy,xnp,cb,y,x,radius,screen)
           
            bx,by,m,dx,b,e,n,shoot,dy=linecalc(m,y,radius,xy,x,b,bx,by,mouse,dx,e,n,dy)
            if keys[K_r]:
                portalx=0
                portaly=0
                portalx2=0
                portaly2=0
    
            if not portalx==checkx or not portaly==checky or not portalx2==checkx2 or not portaly2==checky2:
                come=0
            if not portalx==0:
                pygame.draw.circle(screen,(0,0,255),(int(portalx),int(portaly)),(20))
            if not portalx2==0:
                pygame.draw.circle(screen,(0,255,0),(int(portalx2),int(portaly2)),(20))
                
            if  keys[K_LEFT]  and left==1:
                    x=x-1
            if  keys[K_RIGHT] and right==1:
                    x=x+1
            clock.tick(refresh**100+300)
            pygame.display.update()
    if  mn==-1 and mn2==-1 and come>0:
        ml=ml-1
    if (not me==0 and come==2) or( not me2==0 and come==1):
        ml=ml-1
    if ml<1:
        momentum=0
        ml=2
    
    event = pygame.event.poll()
    #print x
    #print y
    if event.type ==pygame.QUIT:
        running=0
    
        
    fall=1
    clock.tick(300)
    shoot=0
    pygame.display.update()
    
pygame.quit()