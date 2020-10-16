#Main file, so just drawing the stages and intialising all the objects that'll be used.
#I can see a lot of rewriting potential in this code. Swag B)

###PLEASE ONLY PLACE OBJECTS WITH Y VALUES INCREMENTING IN TENS
import pygame, createObject, math, objectInventory

def roundup(x): #used in the jump detection
    return int(math.ceil(x / 10.0)) * 10


screen = pygame.display.set_mode((1280, 720)) #Setting Screen
pygame.display.set_caption('Game') #Window Name
screen.fill((255,255,255))#Fills white to screen
clock = pygame.time.Clock()
FPS = 60 #60FPS 4K Realtime RayTracing B)))))))))))))))

objects = objectInventory.init(screen)
staticObjects = objects.getStatic()
moveableObjects = objects.getMoveable()
player = moveableObjects[0] #this'll do for now, only one moveable and the player will be drawn before the rest anyway.

pygame.init() #intialising pygame
pygame.display.init()
pygame.display.update()
#Loop
running = True
while running: #main gameloop. Kinda stolen?
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #keydown event handling
            if event.key == pygame.K_w:
                player.inJump()
            elif event.key == pygame.K_a:
                if player.rect.x <= 100 and player.lkupx == False: #left side of page
                    for i in range(len(staticObjects)):
                        staticObjects[i].setX(5)
                        staticObjects[i].KDPX()
                    continue
                else:
                    player.setVelX(-5)
                    player.LKDPX()
            elif event.key == pygame.K_d:
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
            pygame.quit()

    screen.fill((255,255,255))
    clock.tick(FPS)

    for i in range(len(staticObjects)):
        staticObjects[i].tick(screen)
        if player.rect.x >= 1180-50 and player.rkupx == False: #if the player x is a certain number, move the land.
            staticObjects[i].setX(-5)
            staticObjects[i].KDPX()
        elif player.rect.x <= 100 and player.lkupx == False: #if the x value is smaller than 100 and the key ISNT up.
            staticObjects[i].setX(5)
            staticObjects[i].KDPX()
        if player.rect.y >= 720-player.height-1: #if the player x is a certain number, move the land.
            staticObjects[i].setY(-5)
        elif player.rect.y <= 0: #if the x value is smaller than 100 and the key ISNT up.
            staticObjects[i].setY(5)
        elif player.rect.y > 0 or player.rect.y <= 720-player.height-1: #if the x value is smaller than 100 and the key ISNT up.
            staticObjects[i].setY(0)

    player.tick(staticObjects)

    pygame.display.update()#fancy lil uhhh lil uhhhh display update for ya
