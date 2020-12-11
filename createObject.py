#object creation file. Planned to be consisting of four types.
#Static, moveable, interactable, and mountable(?)
#I could probably cram these all into one object, but it helps debugging, at the expense
#of a pretty messy program. Oh well, its a seperate module.
import pygame, math, random

pygame.init()

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

class newText(pygame.font.Font):
    def __init__(self, text, size, color):
        content = pygame.font.Font(None, size)
        self = content.render(text, 1, color)
    
class newChunk(pygame.sprite.Sprite):
    def __init__(self, width):
        pygame.sprite.Sprite.__init__(self)


class newStatic(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, screen): #initialising all the variables.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(screen, color, (x,y,width,height))
        self.screen = screen
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.lorr = 0 #lorr == set X Vel
        self.uord = 0
        self.blittable = None
        self.kupx = False
        self.kupy = False
        self.isground = False

    def setParams(self, height, width, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def isGround(self):
        self.isground = True

    def KUPX(self):
        self.kupx = True

    def KDPX(self):
        self.kupx = False

    def KUPY(self):
        self.kupy = True

    def KDPY(self):
        self.kupy = False

    def setColor(self, color):
        self.color = color

    def drawChar(self, screen):#drawing the initial character
        self.screen = screen
        self.rect = pygame.draw.rect(screen, self.color, (self.rect.x,self.rect.y,self.width,self.height))

    def isGround(self):
        self.isground = True

    def setX(self, x):
        self.lorr = x

    def setY(self, y):
        self.uord = y

    def render(self, screen):
#        if (self.rect.x >= 1280 or self.rect.x <= self.width - (self.width*2)) or (self.rect.y <= 0+self.height or self.rect.y > 720): #if the object is off screen, stop rendering
#            pass
        if self.isground and (self.rect.x > 1280):
            self.rect.x = 0
        if self.isground and (self.rect.x < 0):
            self.rect.x = 1280-self.width
            
        self.rect = pygame.draw.rect(screen, self.color, (self.rect.x,self.rect.y,self.width,self.height))#drawing the new rect

    def tick(self, screen):
        self.screen = screen
        self.rect.move_ip(self.lorr,0)

        if self.rect.y + self.uord > self.y: #if the place you are trying to move to is above your original position
            self.rect.move_ip(0,self.uord)
 
        if self.kupx == True:
            self.lorr *= 0.85

class newMoveable(pygame.sprite.Sprite):
    def __init__(self, color, width, height): #initialising all the variables.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
#        self.image = pygame.image.load("8219_cheems.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.width//2, self.rect.height//2
        self.gameX = 0
        self.gameY = 0
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.velX = 0
        self.velY = 0
        self.kupy = False
        self.lkupx = False
        self.rkupx = False
        self.Jump = False
        self.crouching = False
        self.groundY = 720 
        self.blittable = None

    def printCoords(self):
        return self.rect.x, self.rect.y #printing the x and y.

    def KUPY(self):
        self.kupy = True

    def LKUPX(self):
        self.lkupx = True

    def LKDPX(self):
        self.lkupx = False

    def RKUPX(self):
        self.rkupx = True
    def RKDPX(self):
        self.rkupx = False
    def KDPY(self):
        self.kupy = False

    def setParams(self, x, y): #setting the parameters for drawing
        self.rect.x = x
        self.rect.y = y

    def setColor(self, color):#self explanantory really \/
        self.color = color

    def setVelX(self, velX):
        self.velX = velX

    def setX(self, x):
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y

    def inJump(self): #end of self explanatory lmao /\
        if self.Jump != True:
            self.Jump = True
            self.velY = -20
        else:
            return

    def render(self, screen):
        self.rect = pygame.draw.rect(screen, self.color, self.rect)#drawing the new rect

    def tick(self, staticObjects): #i need the list of all of the land objects for the collision detection mechanism.
        self.rect = self.rect.move(self.velX,self.velY)#assigning the new rect pos to self.rect
        self.gameX = self.rect.x + -(staticObjects[0].rect.x)
        self.gameY = self.rect.y + -(staticObjects[0].rect.y)

        for i in range(len(staticObjects)): #collision detection
            if not self.rect.colliderect(staticObjects[i]) and not self.rect.y == staticObjects[i].rect.y - self.rect.height:
                self.Jump = True
            elif self.rect.colliderect(staticObjects[i]) and self.velY >=0:
                self.velY = 0
                self.rect.y = staticObjects[i].rect.y - self.rect.height + 1
                self.Jump = False
                break


        if self.Jump == True: #if jumping (in air.)
            self.velY +=1

        #momentum decrease only when the player is not moving
        if self.lkupx == True and self.rkupx == True: #kupx = Key Up X
            self.velX *= 0.85


        if self.rect.x >= 1180 - self.rect.width: #left wall side collision detection
            self.rect.x = 1180 - self.rect.width #the - accounts for the players width
        elif self.rect.x <= 100: #right wall side collision detection
            self.rect.x = 100
        
        if self.rect.y > 1000:
            for i in range(len(staticObjects)):
                staticObjects[i].rect.x, staticObjects[i].rect.y = staticObjects[i].x, staticObjects[i].y
            self.rect.x, self.rect.y = 1280//2,720//2
            self.velY, self.velX = 0, 0

