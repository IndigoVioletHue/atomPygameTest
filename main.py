#Main file, so just drawing the stages and intialising all the objects that'll be used.
#I can see a lot of rewriting potential in this code. Swag B)

###PLEASE ONLY PLACE OBJECTS WITH Y VALUES INCREMENTING IN TENS
import pygame, createObject, math

def roundup(x): #used in the jump detection
    return int(math.ceil(x / 10.0)) * 10

BLACK = (0,0,0)
WHITE = (255,255,255) #defining it because currently, during the only build, these are most of the colours to be used.
screen = pygame.display.set_mode((1280, 720)) #Setting Screen
pygame.display.set_caption('Game') #Window Name
screen.fill(WHITE)#Fills white to screen
clock = pygame.time.Clock()
FPS = 60 #60FPS 4K Realtime RayTracing B)))))))))))))))

player = createObject.newMoveable() #player object creation
player.setParams(75, 50, 615, 450)
player.setColor(BLACK)
player.drawChar(screen)

land = createObject.newStatic() #land object in the middle, might ditch this idea.
land.setParams(120, 1280, 0, 650)
land.setColor((124,124,124))
land.isGround()

land2 = createObject.newStatic() #right land
land2.setParams(120, 1280, 1280, 650)
land2.setColor((200,124,200))
land2.isGround()

leftLand = createObject.newStatic() #left land
leftLand.setParams(120, 1280, -1280, 650)
leftLand.setColor((124,200,124))
leftLand.isGround()

platform = createObject.newStatic() #platform
platform.setParams(50, 300, 50, 580)
platform.setColor((124,124,124))

platform2 = createObject.newStatic() #another platform2
platform2.setParams(50, 300, 250, 280)
platform2.setColor((124,124,124))

platform3 = createObject.newStatic() #another platform2
platform3.setParams(50, 300, 450, 80)
platform3.setColor((124,124,124))

land.drawChar(screen) #drawing all of the land characters, as originally it was done every gametick,
land2.drawChar(screen)#before the newStatic class had a tick function
leftLand.drawChar(screen)
platform.drawChar(screen)
platform2.drawChar(screen)
platform3.drawChar(screen)

staticObjects = [land, land2, leftLand, platform, platform2, platform3] #another reason to do the land differently, i'd have to have a long as heck list.

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

    screen.fill(WHITE)
    clock.tick(FPS)

    for i in range(len(staticObjects)):
        staticObjects[i].tick(screen)
        if player.rect.x >= 1180-50 and player.rkupx == False: #if the player x is a certain number, move the land.
            staticObjects[i].setX(-5)
            staticObjects[i].KDPX()
        elif player.rect.x <= 100 and player.lkupx == False: #if the x value is smaller than 100 and the key ISNT up.
            staticObjects[i].setX(5)
            staticObjects[i].KDPX()
        if player.rect.y >= 720: #if the player x is a certain number, move the land.
            staticObjects[i].setY(-5)
        elif player.rect.y <= 0: #if the x value is smaller than 100 and the key ISNT up.
            staticObjects[i].setY(5)
        elif player.rect.y > 0 or player.rect.y <= 720: #if the x value is smaller than 100 and the key ISNT up.
            staticObjects[i].setY(0)

    player.tick(staticObjects)

    pygame.display.update()#fancy lil uhhh lil uhhhh display update for ya
