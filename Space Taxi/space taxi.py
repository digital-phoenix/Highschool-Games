import time
import pygame
import random
from pygame.locals import *
pygame.init()
font=pygame.font.SysFont("arial",25) 
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,480))
running=1
passd=0
tmoney=0
take=0
land=0
cb=(0,0,0)
cg=(0,222,0)
sx=0
sy=0
radius=10
load=0
place=0
money=20.00
ml=0
x=100
y=100
momentum=[]
tk=[]
press=[]
pd=201
collision=0
level=1
count=0
shape=[]
red=[]                      
green=[]                    
blue=[]                        
locx=[] 
locy=[]
sizex=[]
sizey=[]
t=[]
tcount=0
lc=1
win=0
for i in range(0,4):
      momentum.append(0)
      tk.append(0)
      press.append(0)
      
while running:
      screen.fill((0,0,0))
      front=x+70
      top=y-15
      back=x
      bottom=y+20
      keys=pygame.key.get_pressed()
      pygame.draw.rect(screen,(222,222,222),Rect((0,430),(640,50)))
      pygame.draw.rect(screen,(221,216,15),Rect((x+10,y-15),(40,15)))
      pygame.draw.rect(screen,(221,216,15),Rect((x,y),(70,20)))
      msg=font.render("$"+str(tmoney)+".00",True,(0,0,255))
      screen.blit(msg,(10,440))
      
      
      if not sx==0 and not sy==0:
            pygame.draw.line(screen,(cg),(sx-radius/2,sy),(sx-radius/2,sy))
            pygame.draw.line(screen,(cg),(sx+radius/2,sy),(sx+radius/2,sy))
            pygame.draw.line(screen,(cg),(sx-radius/2,sy+radius/2),(sx+radius/2,sy+radius/2))
            pygame.draw.circle(screen,(cg),(sx,sy),(radius),1)
            pygame.draw.line(screen,(cg),(sx,sy+radius),(sx,sy+3*radius))
            pygame.draw.line(screen,(cg),(sx-radius,sy+4*radius),(sx,sy+3*radius))
            pygame.draw.line(screen,(cg),(sx+radius,sy+4*radius),(sx,sy+3*radius))
            pygame.draw.line(screen,(cg),(sx,(sy+2*radius)+radius/2),(sx-radius,(sy+2*radius)))
            pygame.draw.line(screen,(cg),(sx,+((sy+2*radius))+radius/2),(sx+radius,sy+2*radius))
            
      if load==0 and sx==0 and sy==0 and place==0 and count>0:
            place=random.randint(1,count/9-tcount)
            
      pygame.draw.rect(screen,(0,255,0),Rect((0,10),(640,420)),1)      
      if bottom>420:
            collision=1
      if front>640:
            collision=1
            #print "4"
      if back<1:
            collision=1
            #print "5"
      if top<10 and front<150:
            collision=1
            #print "1"
      if top<10 and back>350:
            collision=1
            #print"2"
      if not passd==1+int(level):
            if top<10 and back<350 and front>150:
                  collision=1
                  #print "3"
      if passd==1+int(level) and load==1:
            pygame.draw.line(screen,(0,0,0),(150,10),(350,10))
            if top<10 and back<295 and front>195:
                  level=level+1
                  lc=1
      #print passd
      #print "level"+str(level)
      #print land
     
      #print pd
      #print "collision"+str(collision)
      #level 1
      #print load
      ex=0
      if "level 5"=="level "+str(level):
                        win=1
                  
      print win
      if lc==1 and win==0:
            money=20.00
            momentum=[0,0,0,0]
            f=open('spacetaxi.txt',"r")
            while ex==0:
                  line=f.readline().strip()
                  #print ex
                  if line=="level "+str(level):
                        count=0
                        shape=[]
                        red=[]                      
                        green=[]                    
                        blue=[]                        
                        locx=[] 
                        locy=[]
                        sizex=[]
                        sizey=[]
                        t=[]
                        passd=0
                        while not ex==1:
                              l=f.readline().strip()
                              count=count+1
                              if l=="level "+str(int(level)+1):
                                    ex=1
                                     
                              #print l      
                              if count%9==1 and not l=="level "+str(level+1):
                                    shape.append(int(l))
                                   
                              if count%9==2:
                                    red.append(int(l))
                              if count%9==3:
                                    green.append(int(l))
                              if count%9==4:
                                    blue.append(int(l))
                              if count%9==5:
                                    locx.append(int(l))
                              if count%9==6:
                                    locy.append(int(l))
                              if count%9==7:
                                    sizex.append(int(l))
                              if count%9==8:
                                    sizey.append(int(l))
                              if count%9==0:
                                    t.append(int(l))
                                    if 1==int(l):
                                          tcount=tcount+1
                  if not level==1:
                        x=320
                        y=380

      f.close()            
      if pd<201:
            place==0
            land==0
            take==0
      for i in range(0,count/9):
            
            if shape[i]==1:
                  pygame.draw.rect(screen,(red[i],green[i],blue[i]),Rect((locx[i],locy[i]),(sizex[i],sizey[i])))
            
            if shape[i]==2:
                  pygame.draw.circle(screen,(red[i],green[i],blue[i]),(locx[i],locy[i]),(sizex[i]))
            
            
            if bottom>locy[i]+4 and top<locy[i]+sizey[i] and (front<locx[i]+sizex[i] or back<locx[i]+sizex[i]) and (front>locx[i] or back>locx[i]):
                  collision=1
            if bottom>locy[i]-1 and bottom<locy[i]+3 and (front<locx[i]+sizex[i] or back<locx[i]+sizex[i]) and (front>locx[i] or back>locx[i]) and t[i]==0:
                  momentum=[0,0,0,0]
                  land=i+1
            if t[i]==0:
                  msg=font.render(str(i+1),True,(0,0,0))
                  screen.blit(msg,(sizex[i]/2+locx[i],locy[i]))   
                  
              
            #print lc    
            if place==i+1 and load==0 and t[i]==0:
                  if not land==i+1:
                        sx=locx[i]+radius
                        sy=locy[i]-4*radius
                  if not land==i+1:
                        msg=font.render("Hey Taxi",True,(0,0,255))
                        screen.blit(msg,(300,440))
                  if land==i+1: 
                        if take==0 and passd==int(level)+1:
                              msg=font.render("Take me up",True,(0,0,255))
                              screen.blit(msg,(250,440))
                        if take==0 and not passd==int(level)+1:
                              take=random.randint(1,count/9-tcount)
                              if take==i+1:
                                    take=0
                              if take>0:
                                    msg=font.render("Take me to platform "+str(take),True,(0,0,255))
                                    screen.blit(msg,(250,440))
                       
                        if sx<x:
                              sx=sx+1
                        if sx>x:
                              sx=sx-1
                        if sx==x:
                              load=1
                              sx=0
                              sy=0
     
      if land==place and not land==0 and t[i]==0: 
                  if take==0 and not passd==int(level)+1:
                        take=random.randint(1,(count/9)-tcount)
                        if take==place:
                              
                              take=0
                        if take>0:
                              msg=font.render("Take me to platform "+str(take),True,(0,0,255))
                              screen.blit(msg,(250,440))
                        if take==0 or passd==int(level)+1:
                              if sx<x:
                                    sx=sx+1
                              if sx>x:
                                    sx=sx-1
                              if sx==x:
                                    load=1
                                    sx=0
                                    sy=0
           
      #Delivery
      if take==0 and not passd==level+1 and load==1:
            take=random.randint(1,count/9-tcount)
      if take>0 and (land==place or load==1):
            msg=font.render("Take me to platform "+str(take),True,(0,0,255))
            screen.blit(msg,(250,440))
      if passd==int(level)+1 and ((land==place and land>0) or load==1):
            msg=font.render("Take me up",True,(0,0,255))
            screen.blit(msg,(250,440))
      if load==1 and take==land and take>0:
            sx=x
            sy=y+20-4*radius 
            pd=0
            tmoney=tmoney+5
            place=0
            take=0
            load=0
            passd=passd+1
      
      if pd<200:
            pd=pd+1
            msg=font.render("Thanks!",True,(0,0,255))
            screen.blit(msg,(250,440))
      if pd==200:
            sx=0
            sy=0
            pd=pd+1
      
      #movement
      
      press=[0,0,0,0]
      if keys[K_LEFT]:
            press[0]=1
            x=x-1
            tk[0]=tk[0]+1
            if tk[0]>10 and not momentum[1]==2:
                  momentum[1]=momentum[1]+1
                  momentum[0]=0
                  tk[0]=0
      if keys[K_RIGHT]:
            press[1]=1
            x=x+1
            tk[1]=tk[1]+1
            if tk[1]>10 and not momentum[0]==2:
                  momentum[0]=momentum[0]+1
                  momentum[1]=0
                  tk[1]=0
      if keys[K_DOWN]:
            press[2]=1
            y=y+1
            tk[2]=tk[2]+1
            if tk[2]>10 and not momentum[2]==2:
                  momentum[2]=momentum[2]+1
                  momentum[3]=0
                  tk[2]=0
      if keys[K_UP]:
            press[3]=1
            y=y-1
            tk[3]=tk[3]+1
            if tk[3]>10 and not momentum[3]==2:
                  momentum[3]=momentum[3]+1
                  if momentum[2]>0:
                        momentum[2]=0
                  tk[3]=0
      if momentum[0]>0:
            x=x+momentum[0]
      if momentum[1]>0:
            x=x-momentum[1]
      if momentum[2]>0:
            y=y+momentum[2]
      if momentum[3]>0:
            y=y-momentum[3]
      
      if not press[0]:
            tk[0]=0
      if not press[1]:
            tk[1]=0
      if not press[2]:
            tk[2]=0
      if not press[3]:
            tk[3]=0
      #money loss
      ml=ml+1      
      if ml==5:
            money=money-0.01
            ml=0
      #print locx 
      #print locy
      #print ""
      #print sizex
      #print  sizey
      #print tcount    
      #print momentum
      #print tk
      msg=font.render("Money "+str(money),True,(0,0,255))
      screen.blit(msg,(500,440))
      #if collision==1:
            #print level
      lc=0
      if collision==1 and lc==0:
            screen.fill((0,0,0))
            msg=font.render("GAME OVER",True,(255,0,0))
            screen.blit(msg,(250,180))
            msg=font.render("you crashed",True,(255,0,0))
            screen.blit(msg,(260,210))
            if keys[K_RETURN]:
            
                  shape=[]
                  red=[]                      
                  green=[]                    
                  blue=[]                        
                  locx=[] 
                  locy=[]
                  sizex=[]
                  sizey=[]
                  t=[]
                  level=1
                  lc=1
                  collision=0
                  passd=0
                  tmoney=0
                  take=0
                  land=0
                  sx=0
                  sy=0
                  load=0
                  place=0
                  money=20.00
                  ml=0
                  x=320
                  y=240
                  momentum=[0,0,0,0]
                  tk=[0,0,0,0]
                  press=[0,0,0,0]
                  pd=201
        
      land=0
      if win==1:
            screen.fill((0,0,0))
            msg=font.render("You Win",True,(255,0,0))
            screen.blit(msg,(250,180))
            msg=font.render("you score is "+"$"+str(tmoney),True,(255,0,0))
            screen.blit(msg,(260,210))
            msg=font.render("Press enter to restart",True,(255,0,0))
            screen.blit(msg,(250,240))
            if keys[K_RETURN]:
                  win=0
                  shape=[]
                  red=[]                      
                  green=[]                    
                  blue=[]                        
                  locx=[] 
                  locy=[]
                  sizex=[]
                  sizey=[]
                  t=[]
                  level=1
                  lc=1
                  collision=0
                  passd=0
                  tmoney=0
                  take=0
                  land=0
                  sx=0
                  sy=0
                  load=0
                  place=0
                  money=20.00
                  ml=0
                  x=320
                  y=240
                  momentum=[0,0,0,0]
                  tk=[0,0,0,0]
                  press=[0,0,0,0]
                  pd=201
      
      event = pygame.event.poll()
      if event.type==pygame.QUIT:
            running=0
      
      clock.tick(100)
      pygame.display.update()
pygame.quit()