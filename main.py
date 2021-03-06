#Main file, so just drawing the stages and intialising all the objects that'll be used.
#I can see a lot of rewriting potential in this code. Swag B)

import pygame, createObject, math, objectInventory, threading, time, sys
from pygame import *

def roundup(x): #used in the jump detection
    return int(math.ceil(x / 10.0)) * 10


screen = pygame.display.set_mode((1280, 720), vsync=1) #Setting Screen
pygame.display.set_caption('Test 1234567890') #Window Name
screen.fill((255,255,255))#Fills white to screen
clock = pygame.time.Clock()
FPS = 60 #60FPS 4K Realtime RayTracing B)))))))))))))))


background = pygame.Surface((1280, 720))

objects = objectInventory.init(background)
staticObjects = objects.getStatic()
moveableObjects = objects.getMoveable()
player = moveableObjects[0] #this'll do for now, only one moveable and the player will be drawn before the rest anyway.

pygame.init() #intialising pygame
pygame.display.init()
pygame.display.update()
#pygame.display.toggle_fullscreen()
game_x = 0
game_y = 0


chunk_width = objectInventory.chunk_width




def Render(threadName, counter): #needs to tick x times per second
    while running:
        screen.fill((255,255,255))
        background.fill((255,255,255))
        player.render(background)
        for i in range(screen.get_width()):
            staticObjects[i].render(screen)
            background.blit(staticObjects[i].image, (staticObjects[i].rect.x, staticObjects[i].rect.y))
        background.blit(player.image, (player.rect.x, player.rect.y))
        screen.blit(background,(0,0))
    
        pygame.display.update()#fancy lil uhhh lil uhhhh display update for ya

threadLock = threading.Lock()

class thread (threading.Thread):
    def __init__(self,threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self): #initiating the thread
        print("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        Render(self.name, 15) #max 25tps.
        # Free lock to release next thread
        threadLock.release()


#Loop
running = True
gameTick = thread(1, "Render")
gameTick.start()
#pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #keydown event handling
            if event.key == pygame.K_w:
                player.inJump()
            elif event.key == pygame.K_a:
                player.gameX -=5
                game_x = 5
                if player.rect.x <= 100 and player.lkupx == False: #left side of page
                    for i in range(len(staticObjects)):
                        staticObjects[i].setX(5)
                        staticObjects[i].KDPX()
                    continue
                else:
                    player.setVelX(-5)
                    player.LKDPX()
            elif event.key == pygame.K_d:
                game_x = 5
                if player.rect.x >= 1180-50 and player.rkupx == False: #if the x value is smaller than 1180-50 and the key ISNT up.: #if the players coords are bigger than 1080, then move land instead of player.
                    for i in range(len(staticObjects)):
                        staticObjects[i].setX(-5)
                        staticObjects[i].KDPX()
                    continue
                else:
                    player.setVelX(5)
                    player.RKDPX() #have to do the right and left versions, as otherwise the variable gets confused.
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.KUPY()
            elif event.key == pygame.K_a:
                player.LKUPX()
                for i in range(len(staticObjects)):
                    staticObjects[i].setX(0)
                    staticObjects[i].KUPX()
            elif event.key == pygame.K_d:
                player.RKUPX()
                for i in range(len(staticObjects)):
                    staticObjects[i].setX(0)
                    staticObjects[i].KUPX()
        elif event.type == pygame.QUIT:
            running = False
            gameTick.join
            pygame.quit()
            sys.exit()

    for i in range(-screen.get_width(), screen.get_width()*2, chunk_width): #static objects tick
        staticObjects[i].tick(screen)
        if player.rect.x >= 1180-50 and player.rkupx == False: #if the player x is on the right side of the screen and trying to move across
            staticObjects[i].setX(-5)
            staticObjects[i].KDPX()
        elif player.rect.x <= 100 and player.lkupx == False: #if the x value is if the player is on the left of the screen and trying to move left
            staticObjects[i].setX(5)
            staticObjects[i].KDPX()
        if player.rect.y >= 720-player.rect.height-1: #if the player is above the top of the screen, pan all objects down
            staticObjects[i].setY(-5)
        elif player.rect.y <= 0+player.rect.height: #if the player is below the bottom of the screen, pan all objects up
            staticObjects[i].setY(5)
        elif player.rect.y > 0 or player.rect.y <= 720-player.rect.height-1: #if the x value is smaller than 100 and the key ISNT up.
            staticObjects[i].setY(0)

    player.tick(staticObjects)
    clock.tick(60)
#    print(round(player.gameX, 0), player.gameY, staticObjects[0].game_x)
