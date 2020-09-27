import pygame
import time
import random
 
pygame.init()

crash_sound = pygame.mixer.Sound("h.ogg")

global num

display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
car_width = 73
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
 
carImg = pygame.image.load('cat.gif')
gameIcon = pygame.image.load('cat.gif')

pygame.display.set_icon(gameIcon)

pause = False

file=open("C:\\Python\\test1.txt","r+")
global highscore
file_num=file.read()
ss=0
for i in range(len(file_num)):
    if file_num[i]=="1" or file_num[i]=="2" or file_num[i]=="3" or file_num[i]=="4" or file_num[i]=="5" or file_num[i]=="6" or file_num[i]=="7" \
       or file_num[i]=="8" or file_num[i]=="9" or file_num[i]=="0":
        ss = file_num[i:]
        break
highscore=int(ss)
#print("file---->",highscore)
file.close()


def things_dodged(count):
    font = pygame.font.SysFont("TimesNewRoman", 25)
    text = font.render("Score : {0}                                                                     high Score is : {1}".format(str(count),highscore), True, black)
    gameDisplay.blit(text,(0,0))    
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

 
def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("TimesNewRoman",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    global num
    #print(">>>>>>>",num)
    final_num=num
    #print("finallyyyy",final_num)
    if final_num > highscore:
        file.truncate(0)
        file.write(str(final_num))
    file.close()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,green,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
    num=dodged

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("TimesNewRoman",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("TimesNewRoman",100)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("TimesNewRoman",115)
        TextSurf, TextRect = text_objects("GAME", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,green,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause
    pygame.mixer.music.load("s.wav")
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
    global dodged
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
 
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        car(x,y)
        global num
        num=0
        num=dodged 
        things_dodged(dodged)

        
        #print("-->",num)
        if x > display_width - car_width or x < 0:
            crash()
 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
 
        if y < thing_starty+thing_height:
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
