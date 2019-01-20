import pygame,random,math,os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (250,100)

pygame.init()
pygame.mixer.init()

soundpt=pygame.mixer.Sound("assets/sounds/point.wav")
soundlose=pygame.mixer.Sound("assets/sounds/gameover.wav")
soundflap=pygame.mixer.Sound("assets/sounds/swoosh.wav")

app_exit=False

black=(0,0,0)
white=(255,255,255)
grey=(150,150,150)
green=(0,255,100)
blue=(0,0,255)
cyan=(0,255,255)

display=pygame.display.set_mode((1000,700))
pygame.display.set_caption("FLAPPY BIRD")
display.fill(white)

bird_vel=0

grav=1
gravsub=1

pipe_width=70

pipe_vel=3

setup=1

clock=pygame.time.Clock()

def menu(cyan):

    imag=pygame.image.load("assets/images/Menubackground.png")
    imag=pygame.transform.scale(imag,(1000,700))
    display.fill(white)
    display.blit(imag,(0,0))

    fonts=pygame.font.SysFont("Comic Sans",40)
    
    label=fonts.render("MENU",True,cyan)
    label2=fonts.render("CHERRY BLOSSOMS",True,cyan)
    label3=fonts.render("GREENERY",True,cyan)
    label4=fonts.render("INSTRUCTIONS",True,cyan)
    
    pygame.draw.rect(display,(255,0,0),(350,70,300,60))
    pygame.draw.rect(display,(255,0,0),(350,220,300,60))
    pygame.draw.rect(display,(255,0,0),(350,370,300,60))
    pygame.draw.rect(display,(255,0,0),(350,520,300,60))

    display.blit(label,[500-label.get_width()/ 2,85])
    display.blit(label2,[500-label2.get_width()/ 2,235])
    display.blit(label3,[500-label3.get_width()/ 2,385])
    display.blit(label4,[500-label4.get_width()/ 2,535])
    
    pygame.display.update()

    cond=True

    while cond:

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos

                if pos[0] in range(335,686) and pos[1] in range(210,291):
                    return 2

                elif pos[0] in range(335,686) and pos[1] in range(360,441):
                    return 1

                elif pos[0] in range(335,686) and pos[1] in range(510,591):
                    instructions(cyan)

            if event.type==pygame.QUIT:
                return 0

def instructions(cyan):

    imag=pygame.image.load("assets/images/Menubackground.png")
    imag=pygame.transform.scale(imag,(1000,700))
    display.fill(white)
    display.blit(imag,(0,0))

    font=pygame.font.SysFont("Copperplate Gothic Bold",50)
    text("Welcome to Flappy bird",50,font)
    text("The objective is to fly through the gaps between the pipes",100,font)
    text("Controls:",170,font)
    text("Click the mouse to fly",220,font)
    text("Press SPACE to pause and unpause",270,font)
    text("There are two backgrounds to choose from",320,font)
    text("So sit back and enjoy",370,font)

    back=pygame.image.load("assets/images/back.png")
    back=pygame.transform.scale(back,(100,50))
    display.blit(back,(0,0))

    pygame.display.update()

    while True:

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos

                if pos[0] in range(105) and pos[1] in range(55):

                    fonts=pygame.font.SysFont("Comic Sans",40)

                    display.fill(white)
                    display.blit(imag,(0,0))

                    label=fonts.render("MENU",True,cyan)
                    label2=fonts.render("CHERRY BLOSSOMS",True,cyan)
                    label3=fonts.render("GREENERY",True,cyan)
                    label4=fonts.render("INSTRUCTIONS",True,cyan)
                    
                    pygame.draw.rect(display,(255,0,0),(350,70,300,60))
                    pygame.draw.rect(display,(255,0,0),(350,220,300,60))
                    pygame.draw.rect(display,(255,0,0),(350,370,300,60))
                    pygame.draw.rect(display,(255,0,0),(350,520,300,60))

                    display.blit(label,[500-label.get_width()/ 2,85])
                    display.blit(label2,[500-label2.get_width()/ 2,235])
                    display.blit(label3,[500-label3.get_width()/ 2,385])
                    display.blit(label4,[500-label4.get_width()/ 2,535])
                    
                    pygame.display.update()

                    return
    
def text(msg,pos,fonts):
    
    lbl=fonts.render(msg,True,(255,0,0))
    display.blit(lbl,[500-lbl.get_width()/ 2,pos])            

def pause():
    
    loopvar=True
    while loopvar:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                loopvar=False 

def leap():
    global bird_vel
    bird_vel=-7

def gravity():
    global grav,gravsub,bird_vel
    if gravsub==5:
        bird_vel+=grav
        gravsub=1
    else:
        gravsub+=1

def pipes():

    pipe_height=random.randint(100,420)

    return pipe_height

def draw(x,h,p1,p2,p3,p4,p1in,p2in,p3in,p4in,background):

    if p1!=None:
        display.blit(p1,(x[0],700-h[0]))
        display.blit(p1in,(x[0],0))        
        display.blit(background,(x[0]+69,0),(x[0]+69,0,3,700))
    if p2!=None:
        display.blit(p2,(x[1],700-h[1]))
        display.blit(p2in,(x[1],0))
        display.blit(background,(x[1]+69,0),(x[1]+69,0,3,700))
    if p3!=None:
        display.blit(p3,(x[2],700-h[2]))
        display.blit(p3in,(x[2],0))
        display.blit(background,(x[2]+69,0),(x[2]+69,0,3,700))
    if p4!=None:
        display.blit(p4,(x[3],700-h[3]))
        display.blit(p4in,(x[3],0))
        display.blit(background,(x[3]+69,0),(x[3]+69,0,3,700))

def collision(y,x,h):
    for i in range(len(x)):
        if x[i]==346:
            if y <700-25-gap-h[i] or y>660+25-h[i]:# 
                return True
        if x[i] in range(234,346):
            if y in range(684-gap-h[i],694-gap-h[i]) or y in range(666-h[i],674-h[i]):
                return True
            
    if y>700:#651
        return True
                
    return False

def score(pts):

    rendering="Score: "+str(pts)
    pygame.draw.rect(display,(255,0,0),(10,10,120,40))
    fonts1=pygame.font.SysFont("Copperplate Gothic Bold",35)
    label5=fonts1.render(rendering,True,cyan)
    display.blit(label5,(15,5+label5.get_height()/ 2))

def bird(bird_y,background):
    
    if  bird_y<651 and bird_y>-1:
        display.blit(background.subsurface(300,bird_y,50,50),(300,bird_y))
    elif bird_y>650:
        display.blit(background.subsurface(300,bird_y,50,700-bird_y),(300,bird_y))
    elif bird_y<0:
        display.blit(background.subsurface(300,0,50,bird_y+50),(300,bird_y))        

while not app_exit:#loop to control entry and exit from application

    game_exit=False

    soundlose.stop()

    if setup==1:
        back=menu(cyan)

    bird_vel=0

    grav=1
    gravsub=1

    pipe_width=70

    pipe_vel=3

    display.fill(white)

    if back==1:
        background=pygame.image.load("assets/images/Birdbackground.png")
        display.blit(background,(0,0))

    elif back==2:
        background=pygame.image.load("assets/images/CherryBlossom.png")
        background=pygame.transform.scale(background,(1000,700))
        display.blit(background,(0,0))

    elif back==0:
        break

    img=pygame.image.load("assets/images/bird2.gif")
    img=pygame.transform.scale(img,(50,50))
    img=img.subsurface(0,3,50,44)
    img=pygame.transform.scale(img,(50,50))

    bird_y=300

    pipe_x=[1000,1000,1000,1000]

    pipe_height=[0,0,0,0]
    
    vel2,vel3,vel4=0,0,0

    detervar=0

    pipe1,pipe2,pipe3,pipe4=None,None,None,None
    p1in,p2in,p3in,p4in=None,None,None,None

    gap=220

    points=0

    pygame.time.wait(500)

    while  not game_exit:

        jump=0
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                jump=1

            if event.type==pygame.QUIT:
                game_exit=True
                app_exit=True

            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                pause()
                jump=1
                

        if jump==1 and bird_y >= 0:
            soundflap.play()
            leap()

        if app_exit==True:
            break

        gravity()
        
        if bird_y <= 0:
            bird_vel=1

        if pipe_x[0]==1000:
            pipe_height[0]=pipes()
            pipe1=pygame.image.load("assets/images/Warp Pipe.png")
            pipe1=pygame.transform.scale(pipe1,(pipe_width,pipe_height[0]))
            p1in=pygame.transform.scale(pipe1,(pipe_width,700-(pipe_height[0]+gap)))
            p1in=pygame.transform.rotate(p1in,180)
            
        elif pipe_x[0]==667:
            pipe_height[1]=pipes()
            pipe2=pygame.image.load("assets/images/Warp Pipe.png")
            pipe2=pygame.transform.scale(pipe2,(pipe_width,pipe_height[1]))
            p2in=pygame.transform.scale(pipe2,(pipe_width,700-(pipe_height[1]+gap)))
            p2in=pygame.transform.rotate(p2in,180)
            vel2=1
            
            
        elif pipe_x[0]==334:
            pipe_height[2]=pipes()
            pipe3=pygame.image.load("assets/images/Warp Pipe.png")
            pipe3=pygame.transform.scale(pipe3,(pipe_width,pipe_height[2]))
            p3in=pygame.transform.scale(pipe3,(pipe_width,700-(pipe_height[2]+gap)))
            p3in=pygame.transform.rotate(p3in,180)
            vel3=1
            
        elif pipe_x[0]==1:
            pipe_height[3]=pipes()
            pipe4=pygame.image.load("assets/images/Warp Pipe.png")
            pipe4=pygame.transform.scale(pipe4,(pipe_width,pipe_height[3]))
            p4in=pygame.transform.scale(pipe4,(pipe_width,700-(pipe_height[3]+gap)))
            p4in=pygame.transform.rotate(p4in,180)
            vel4=1
            
        draw(pipe_x,pipe_height,pipe1,pipe2,pipe3,pipe4,p1in,p2in,p3in,p4in,background)

        bird(bird_y,background) ##

        display.blit(img,(300,bird_y))

        bird_y+=bird_vel

        if bird_vel<0:
            display.blit(background,(300,bird_y+50),(300,bird_y+50,50,int(math.fabs(bird_vel))))
        else:
            display.blit(background,(300,bird_y-bird_vel),(300,bird_y-bird_vel,50,int(math.fabs(bird_vel))))
    

        pipe_x[0]-=pipe_vel
        if vel2==1:
            pipe_x[1]-=pipe_vel
        if vel3==1:
            pipe_x[2]-=pipe_vel
        if vel4==1:
            pipe_x[3]-=pipe_vel

        if pipe_x[0]<=-335:
          pipe_x[0]=1000
        elif pipe_x[1]<=-335:
          pipe_x[1]=1000
        elif pipe_x[2]<=-335:
          pipe_x[2]=1000
        elif pipe_x[3]<=-335:
          pipe_x[3]=1000

        game_exit=collision(bird_y,pipe_x,pipe_height)

        for i in pipe_x:
            if i==226:
                points+=1
                break
            if i ==244:
                soundpt.play()
            
        score(points)

        if game_exit==True:
            
            soundpt.stop()
            soundlose.play()

            pygame.time.wait(500)
            
            imag=pygame.image.load("assets/images/Menubackground.png")
            imag=pygame.transform.scale(imag,(1000,700))
            display.fill(white)
            display.blit(imag,(0,0))

            pygame.draw.rect(display,(255,0,0),(300,140,400,80))

            rendering="Score: "+str(points)
            fonts1=pygame.font.SysFont("Copperplate Gothic Bold",90)
            label6=fonts1.render(rendering,True,cyan)
            display.blit(label6,(500-label6.get_width()/2,150))

            pygame.draw.rect(display,(255,0,0),(50,450,250,70))
            pygame.draw.rect(display,(255,0,0),(380,450,250,70))
            pygame.draw.rect(display,(255,0,0),(710,450,250,70))
            
            rendering="Menu"
            fonts1=pygame.font.SysFont("Copperplate Gothic Bold",70)
            label6=fonts1.render(rendering,True,cyan)
            display.blit(label6,(175-label6.get_width()/2,460))

            rendering="Retry"
            fonts1=pygame.font.SysFont("Copperplate Gothic Bold",70)
            label6=fonts1.render(rendering,True,cyan)
            display.blit(label6,(505-label6.get_width()/2,460))

            rendering="Quit"
            fonts1=pygame.font.SysFont("Copperplate Gothic Bold",70)
            label6=fonts1.render(rendering,True,cyan)
            display.blit(label6,(825-label6.get_width()/2,460))

            
            pygame.display.update()
            
            condit=True
            
            while condit==True:
               for event in pygame.event.get():
                   if event.type==pygame.QUIT:
                        app_exit=True
                        condit=False

                   elif event.type==pygame.MOUSEBUTTONDOWN:
                        pos=event.pos

                        if pos[0] in range(45,306) and pos[1] in range(445,525):
                            setup=1
                            condit=False

                        if pos[0] in range(375,636) and pos[1] in range(445,525):
                            setup=0
                            condit=False

                        if pos[0] in range(705,966) and pos[1] in range(445,525):
                            app_exit=True
                            condit=False

        pygame.display.update()   
        
        clock.tick(100)


pygame.quit()
quit()


