import pygame
import os
os.chdir('D:\python stuff\Game_maker')

pygame.init()
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
leftie= pygame.image.load('L1.png')
Rightie= pygame.image.load('R1.png')
bg = pygame.image.load('background.jpg')
bg2=pygame.transform.scale(bg,(1400,720))
platform = pygame.image.load('platform.jpg')
plat2= pygame.transform.scale(platform,(300,20))
score = 0
bullet_sound= pygame.mixer.Sound("bullet.mp3")
background_music= pygame.mixer.music.load("tekken3.mp3")
hit_sound= pygame.mixer.Sound("hit.mp3")
pygame.mixer.music.play(-1)


class hero :
    def __init__(self,x,y,width,height):
        self.x,self.y,self.width,self.height=x,y,width,height
        self.value = 10
        self.runner = True
        self.jumping=False
        self.jump_height=10
        self.left, self.right = False, False
        self.walkCount = 0 
        self.hitbox= (self.x+20 ,self.y + 28 , 60)
    def drawing(self):
        if self.walkCount + 1 >= 27 :
            self.walkCount = 0 
        if self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1 
        elif self.right:
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        else:
            if self.left:
                win.blit(leftie,(self.x,self.y))
            elif self.right:
                win.blit(Rightie,(self.x,self.y))
            else:    
                win.blit(char,(self.x,self.y))
        self.hitbox= (self.x+ 17 ,self.y +11 , 28 , 60)        
        #pygame.draw.rect(win,(0,0,0),self.hitbox,2)  

    def hit(self):
        self.x,self.y=50,490
        self.walkCount=0
        font1= pygame.font.SysFont('Times New Roman',100,True)
        text=font1.render('Died!!',1,(255,0,0))
        win.blit(text,(screen_x//2,screen_y//2-200))
        pygame.display.update()
        i=0
        while i < 100:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=100
                    pygame.quit()




class Villain :
    count=0
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    def __init__(self,x,y,width,height,end,value):
        self.x,self.y,self.width,self.height,self.end=x,y,width,height,end
        self.walkCount = 0
        self.value = value
        self.hitbox= (self.x+20 ,self.y , 28 , 60)
        self.health= 10
        Villain.count+=1 
        self.visible = True


    def draw(self,win):
        self.move()
        if self.visible==True:
            if self.walkCount +1 >= 33:
                self.walkCount=0
            if self.value>0:
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.value<0:
                win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            self.hitbox= (self.x+15,self.y , 28 , 60)        
            #pygame.draw.rect(win,(0,0,0),self.hitbox,2)        
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20, 50 , 10 ))
            pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-20, 50 -( 5*  (10 - self.health) ), 10) )
    def move(self):    
        if self.value>0:  
            if self.x < 1400:
                self.x+= self.value
            else:
                self.value*= -1
                self.walkCount=0        
        else:     
            if self.x > 0 :
                self.x+= self.value
            else:
                self.value= 5   
                self.walkCount=0

    def  hit(self):
        hit_sound.play()
        if self.health !=0 :
            self.health-=1
        else:
            self.visible=False
        
class projectile:
    def __init__(self,x,y,color,radius,side):
        self.x,self.y,self.color,self.radius,self.side=x,y,color,radius,side
        self.value=6 * side
    def drawing(self,win): 
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius) 
          


screen_x,screen_y=1280,720
win = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption('First game of blueee')
#fpsbuild
clock = pygame.time.Clock()


def More_Drawing():
    win.blit(bg2,(-60,0)) 
    text = Score_Font.render('SCORE: ' + str(score), 1 , (0,0,0) )
    win.blit(text,(1000,10))
    win.blit(plat2,(100, 400))
    win.blit(plat2,(950, 400))     
    trevor.drawing()    
    sayandeep.draw(win)   
    kaiser.draw(win)
    for bullet in bullets:
        bullet.drawing(win)
    pygame.display.update()

#main runner
trevor = hero(50,490,64,64)
sayandeep = Villain(1000,490,64,64,720,5)
kaiser= Villain(500,490,64,64,720,8)
bullets=[]
shooter= 0
Score_Font = pygame.font.SysFont('comicsans',40 , True , True)

while trevor.runner:
    More_Drawing()
    clock.tick(60) #fps
    if sayandeep.visible==True:
        if trevor.hitbox[1] < sayandeep.hitbox[1] + sayandeep.hitbox[3] and trevor.hitbox[1]  > sayandeep.hitbox[1]:
            if trevor.hitbox[0] > sayandeep.hitbox[0] and trevor.hitbox[0] < sayandeep.hitbox[0]+ sayandeep.hitbox[2]:
                trevor.hit()     
                score-=5
                sayandeep.x=1000
    if kaiser.visible==True:                    
        if trevor.hitbox[1] < kaiser.hitbox[1] + kaiser.hitbox[3] and trevor.hitbox[1]  > kaiser.hitbox[1]:
            if trevor.hitbox[0] > kaiser.hitbox[0] and trevor.hitbox[0] < kaiser.hitbox[0]+ kaiser.hitbox[2]:
                trevor.hit()     
                score-=5
                kaiser.x=1000        
        

    if shooter>0:
        shooter+=1
    if shooter>3:
        shooter=0    

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            trevor.runner=False
            
    for bullet in bullets:
        if sayandeep.visible==True :
            if bullet.y - bullet.radius < sayandeep.hitbox[1] + sayandeep.hitbox[3] and bullet.y + bullet.radius > sayandeep.hitbox[1]:
                if bullet.x + bullet.radius > sayandeep.hitbox[0] and bullet.x - bullet.radius < sayandeep.hitbox[0]+ sayandeep.hitbox[2]:
                    sayandeep.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet))     
        if kaiser.visible==True :
            if bullet.y - bullet.radius < kaiser.hitbox[1] + kaiser.hitbox[3] and bullet.y + bullet.radius > kaiser.hitbox[1]:
                if bullet.x + bullet.radius > kaiser.hitbox[0] and bullet.x - bullet.radius < kaiser.hitbox[0]+ kaiser.hitbox[2]:
                    kaiser.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet))     
        

        if 0<bullet.x < 1280 :
            bullet.x+=bullet.value  
        else:
            bullets.pop(bullets.index(bullet))      
    
    
    #buttons
    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and trevor.x!=0:
        trevor.left, trevor.right = True , False
        trevor.x-=trevor.value 
    elif keys[pygame.K_RIGHT] and trevor.x!=(screen_x+trevor.width):
        trevor.right, trevor.left = True , False
        trevor.x+=trevor.value
    else:
        trevor.walkCount = 0

    if keys[pygame.K_UP] and  trevor.jumping == False:
        trevor.jumping=True
        trevor.right, trevor.left = False,False
        trevor.walkCount = 0
    if keys[pygame.K_SPACE] and shooter==0:  # make a key with x to shoot bullets
        bullet_sound.play()
        if trevor.left:
            side= -1
        else:
            side =  1    
        if len(bullets)< 30 :
            bullets.append(projectile((trevor.x+trevor.width-10),(trevor.y+30),(0,0,0),5,side))
        shooter=1

    if trevor.jumping == True:
        if trevor.jump_height>=-10:
            neg = 1
            if trevor.jump_height<0:
                neg = -1
            trevor.y -= (trevor.jump_height**2) * 0.5 * neg 
            trevor.jump_height-=1
        else:
            trevor.jump_height=10
            trevor.jumping=False

        
pygame.quit()            