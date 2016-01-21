import time
import pygame
import random
from pygame.locals import *
pygame.init()
font=pygame.font.SysFont("arial",22) 
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,480))
screen.fill((0,0,0))
running=1

invaderc=0
x=[]
y=[]
exist=[]
ibx=[]
iby=[]
existc=0

pos=0
xpos=0
ypos=0
xm=1
px=320
bx=0
by=0
shoot=1
ishoot=0
invadersh=-1
score=0
lives=3
rst=0
rss=0
move=0
ibc=0
level=0
ld=301
hsd=300
def start(level):
    xpos=0
    ypos=0
    invaderc=0
    x=[]
    y=[]
    exist=[]
    ibx=[]
    iby=[]
    existc=0
    row=int(level*0.4)+15
    column=int(level*0.4)+5
    for i in range(0,column*row):
        if i>0:
            if i%row==0:
                xpos=0
                ypos=ypos+1
        x.append(xpos*27+10)
        y.append(ypos*25+100)
        exist.append(1)
        ibx.append(0)
        iby.append(0)
        invaderc=invaderc+1
        xpos=xpos+1
    return x,y,exist,ibx,iby,invaderc,xpos

def getText (screen,x,y,w,h,font,frontColour,backColour):
    """
    screen - the regular window variable you create
    x,y,w,h - the location and size of the input box
    font - the font/size you want it written in
    frontColour - the tuple of the foreground colour
    backColour - the background colour tuple
    """
    pygame.draw.rect(screen,frontColour,Rect((x,y),(w,h)),1)
    pygame.draw.rect(screen,backColour,Rect((x+2,y+2),(w-4,h-4)))
    pygame.display.update()
    typing=True
    returnText=""
    while typing:
        typeEvent=pygame.event.poll()
        if typeEvent.type == pygame.QUIT:
            pygame.quit()
        if typeEvent.type == pygame.KEYDOWN:
            
            
            if len(returnText)==3:
                typing=False
                
                
            #if return was hit, assume the user is finished entering text and return what's been entered
            #if backspace is hit, move the carat back one space and destroy the last letter
            
            elif typeEvent.key == pygame.K_BACKSPACE:
                #make sure there's something in the string first, don't want to kill what's not there
                if len(returnText)>0:
                    returnText=returnText[0:len(returnText)-1]
                    
            #just typing normally
            else:
                #add the typed letter to the string
                returnText=returnText+typeEvent.unicode
            pygame.draw.rect(screen,backColour,Rect((x+2,y+2),(w-4,h-4)))
            txtOut =font.render(returnText,True,frontColour)
            screen.blit(txtOut,(x+2,y+2))
            pygame.display.update()
            if not typing:
                #erase the input box
                pygame.draw.rect(screen,backColour,Rect((x,y),(w,h)))
                pygame.display.update()
    return returnText

def highscoref(name,score):
    
    f=open("sihighscore.txt",'r')
    hscore=[]
    fn=[]
    c=0
    s=-1
    for i in range(0,5):
        fn.append(f.readline().strip())
        hscore.append(int(f.readline().strip()))
        c=c+1
    f.close()
    for i in range(0,c):
        if score>hscore[i] and s==-1:         
            s=i
    d=c-1
    for i in range(s,c):
        fn[d]=fn[d-1]
        hscore[d]=hscore[d-1]
        if d==s:
            hscore[d]=score
            fn[d]=name
        d=d-1
    f=open("sihighscore.txt",'w')
    for i in range(0,5):
        f.write(fn[i]+"\n")
        f.write(str(hscore[i])+"\n")
    f.close()
    
def drawinvader(x,y,invaderc,exist):
    for i in range (0,invaderc):
        if exist[i]==1:
            pygame.draw.line(screen,(255,255,255),(x[i],y[i]),(x[i]+20,y[i]))
            pygame.draw.line(screen,(255,255,255),(x[i],y[i]),(x[i]+10,y[i]+20))
            pygame.draw.line(screen,(255,255,255),(x[i]+10,y[i]+20),(x[i]+20,y[i]))

def player(px):
    pygame.draw.rect(screen,(0,222,0),Rect((px,470),(50,10)))
    pygame.draw.rect(screen,(0,222,0),Rect((px+20,460),(10,10)))
    
def pbullet(bx,by):
    pygame.draw.rect(screen,(0,222,0),Rect((bx,by),(5,10)))

def ibullet(ibx,iby):
    for i in range(0,invaderc):
        if ibx[i]>0:
            pygame.draw.rect(screen,(255,255,255),Rect((ibx[i],iby[i]),(5,10)))

def movement(px,keys,shoot,bx,by):
    
    if keys[K_LEFT] and px>0:
        px=px-1
    if keys[K_RIGHT] and px<590:
        px=px+1
    if keys[K_SPACE] and shoot==1:
        bx=px+25
        by=460
    return px,bx,by

while running:
    levelc=level
    
    existc=0
    ibc=0
    for i in range (0,invaderc):
        
        if exist[i]==1:
            existc=existc+1
        if ibx[i]>1:
            ibc=ibc+1
    
    if existc==0 and ld==301:
        level=level+1
    
        
    keys=pygame.key.get_pressed()
    screen.fill((0,0,0))
    event = pygame.event.poll() 
    if event.type ==pygame.QUIT:
        running=0
    #print (float(existc)/(invaderc))*100    
    
    if by>0 and bx>0:
        shoot=0
        pbullet(bx,by)
        for i in range(0,invaderc):
            if by>y[i]-1 and by<y[i]+21 and bx>x[i]-1 and bx<x[i]+21 and exist[i]==1:
                exist[i]=0
                by=0
                bx=0
                shoot=1
                score=score+10
        by=by-1
        if by==0:
            bx=0
            by=0
            shoot=1
    if rst==0 and hsd==300:    
        player(px)
        px,bx,by=movement(px,keys,shoot,bx,by)
        ibullet(ibx,iby)
        drawinvader(x,y,invaderc,exist)  
        msg=font.render("lives "+str(lives),True,(0,255,0))
        screen.blit(msg,(10,10))
        msg=font.render("score: "+str(score),True,(0,255,0))
        screen.blit(msg,(500,10))
    if not levelc==level and ld==301:
        screen.fill((0,0,0))
        msg=font.render("level "+str(level),True,(0,255,0))
        screen.blit(msg,(320,195))
        ld=0
    if ld<301:
        screen.fill((0,0,0))
        msg=font.render("level "+str(level),True,(0,255,0))
        screen.blit(msg,(320,195))
        ld=ld+1
    if ld==300:
        x,y,exist,ibx,iby,invaderc,xpos=start(level)
                
    for i in range (0,invaderc):
        
        if exist[i]==1:
            existc=existc+1
        if ibx[i]>1:
            ibc=ibc+1
    ishoot=0
    ishoot=random.randint(0,100-level*5)
    if ishoot==1 and not (ibc==existc or ibc>existc):
        invadersh=random.randint(0,invaderc-1)
        while exist[invadersh]==0 or not ibx[invadersh]==0:
            invadersh=random.randint(0,invaderc-1)
        ibx[invadersh]=x[invadersh]
        iby[invadersh]=y[invadersh]
        #print invadersh
        #print x[invadersh]
        #print ibx[invadersh]
    if existc>0:
        if move>(float(existc)/(invaderc))*50:
            for i in range (0,invaderc):
        
                if (x[i]==620 or x[i]==0) and exist[i]==1:
                    xm=-xm
                    for i in range(0,invaderc):
                        y[i]=y[i]+5
                        x[i]=x[i]+xm    
                x[i]=x[i]+xm
            move=0
    move=move+1
    for i in range(0,invaderc):
        if ibx[i]>0:
            iby[i]=iby[i]+1
        if iby[i]==480:
            iby[i]=0
            ibx[i]=0
    #if rst==0:
    for i in range (0,invaderc):
        if ibx[i]>px-1 and ibx[i]+10<px+51 and iby[i]+10>469 and iby[i]+10<481:
            rst=1
        if ibx[i]>px+19 and ibx[i]+10<px+31 and iby[i]+10>459 and iby[i]+10<471 and rst==0:
            rst=1
    if rst==1 and lives-1>0:
        rss=rss+1
        screen.fill((0,0,0))
        msg=font.render("lives left "+str(lives-1),True,(0,255,0))
        screen.blit(msg,(320,195))
        msg=font.render("score: "+str(score),True,(0,255,0))
        screen.blit(msg,(320,230))
        
    if rst==1 and lives-1==0:
        f=open("sihighscore.txt",'r')
        hscore=[]
        fn=[]
        c=0
        s=-1
        for i in range(0,5):
            fn.append(f.readline().strip())
            hscore.append(int(f.readline().strip()))
            c=c+1
        f.close()
        for i in range(0,c):
            if score>hscore[i] and s==-1:         
                s=1
        rss=rss+1
        screen.fill((0,0,0))
        msg=font.render("HIGH SCORE",True,(0,255,0))
        screen.blit(msg,(320,210))
        msg=font.render("GAME OVER",True,(0,255,0))
        screen.blit(msg,(320,230))
        msg=font.render("Total score: "+str(score),True,(0,255,0))
        screen.blit(msg,(320,250))
    
    
    if rss==300 and lives-1>0:
        
        rst=0
        ibx=[]
        iby=[]
        for i in range(0,invaderc):
            ibx.append(0)
            iby.append(0)
        
        px=320
        bx=0
        by=0
        rss=0
        shoot=1
        lives=lives-1
        if rst==1:
            print rst
    if rss==300 and lives-1==0 or hsd<300:
        
            invaderc=0
            if s==1:
                arial=pygame.font.SysFont("arial",30)
                name=getText(screen,320,240,200,60,arial,(255,255,255),(0,0,0))
                highscoref(name,score)
                hsd=0
                s=-1
            if hsd<300:
                hsd=hsd+1
                f=open("sihighscore.txt",'r')
                for i in range(0,5):
                    name=str(f.readline().strip())
                    score=str(f.readline().strip())
                    msg=font.render("HIGH SCORES",True,(0,255,0))
                    screen.blit(msg,(320,10))
                    msg=font.render(name,True,(0,255,0))
                    screen.blit(msg,(100,i*20+100))
                    msg=font.render(score,True,(0,255,0))
                    screen.blit(msg,(400,i*20+100))
                f.close()
            level=1
            x=[]
            y=[]
            exist=[]
            ibx=[]
            iby=[]
            existc=0
            row=20
            column=5
            pos=0
            xpos=0
            ypos=0
            xm=1
            px=320
            bx=0
            by=0
            shoot=1
            ishoot=0
            invadersh=-1
            score=0
            lives=3
            rst=0
            rss=0
            move=0
            x,y,exist,ibx,iby,invaderc,xpos=start(1)
    #print px
    #for i in range(0,invaderc-5):
        #exist[i]=0
        #if i>0:
            #exist[i-1]=1
    #arial=pygame.font.SysFont("arial",30)
    #name=getText(screen,320,240,200,60,arial,(255,255,255),(0,0,0))
    clock.tick(500)
    pygame.display.update()
pygame.quit()