#object creation file. Planned to be consisting of four types.
#Static, moveable, interactable, and mountable(?)
#I could probably cram these all into one object, but it helps debugging, at the expense
#of a pretty messy program. Oh well, its a seperate module.
import pygame, math

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

class newStatic:
    def __init__(self): #initiatialising
        self.height = 0;
        self.width = 0;
        self.x = 0;
        self.y = 0;
        self.lorr = 0; #lorr == set X Vel
        self.uord = 0;
        self.kupx = False;
        self.kupy = False;

    def setParams(self, height, width, x, y):
        self.height = height;
        self.width = width;
        self.x = x;
        self.y = y;

    def KUPX(self):
        self.kupx = True

    def KDPX(self):
        self.kupx = False;

    def KUPY(self):
        self.kupy = True;

    def KDPY(self):
        self.kupy = False

    def setColor(self, color):
        self.color = color;

    def drawChar(self, screen):#drawing the inital character
        self.screen = screen;
        self.rect = pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

    def setX(self, x):
        self.lorr = x;

    def setY(self, y):
        self.uord = y;

    def tick(self, screen):
        self.rect = self.rect.move(self.lorr,0)
        if self.rect.y + self.uord > self.y: #if the place you are trying to move to is above your original position
            self.rect = self.rect.move(0,self.uord)
        if (self.rect.x >= 1280 or self.rect.x <= self.width - (self.width*2)) or (self.rect.y <= 0+self.height or self.rect.y > 720): #if the object is off screen, stop rendering
            return
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.display.update(self.rect)
        if self.kupx == True:
            self.lorr *= 0.85

class newMoveable:
    def __init__(self): #initialising all the variables.
        self.height = 0;
        self.width = 0;
        self.x = 0;
        self.y = 0;
        self.velX = 0;
        self.velY = 0;
        self.kupy = False;
        self.lkupx = False;
        self.rkupx = False;
        self.Jump = False;
        self.crouching = False;
        self.groundY = 9999;

    def printCoords(self):
        return self.rect.x, self.rect.y #printing the x and y.

    def KUPY(self):
        self.kupy = True

    def LKUPX(self):
        self.lkupx = True;

    def LKDPX(self):
        self.lkupx = False;

    def RKUPX(self):
        self.rkupx = True
    def RKDPX(self):
        self.rkupx = False;
    def KDPY(self):
        self.kupy = False;

    def setParams(self, height, width, x, y): #setting the parameters for drawing
        self.height = height;
        self.width = width;
        self.x = x;
        self.y = y;

    def drawChar(self, screen):
        self.screen = screen;#initial character drawing.
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height)) #(x,y,width,height)

    def setColor(self, color):#self explanantory really \/
        self.color = color;

    def setVelX(self, velX):
        self.velX = velX;

    def setX(self, x):
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y

    def inJump(self): #end of self explanatory lmao /\
        if self.Jump != True:
            self.Jump = True;
            self.velY = -20
        else:
            return

    def tick(self, staticObjects):
        self.rect = self.rect.move(self.velX,self.velY)#assigning the new rect pos to self.rect
        pygame.draw.rect(self.screen, (0, 0, self.width, self.height), self.rect)#drawing the new rect
        pygame.display.update(self.rect)#updating the display
        groundY = self.groundY
        for j in range(len(staticObjects)): #lsiting all of the static objects
            xvalues = []
            for x in range(staticObjects[j].rect.x,staticObjects[j].rect.x +staticObjects[j].width): #finding all of their x values
                xvalues.append(x)
            yvalues = []
            for y in range(staticObjects[j].rect.y,staticObjects[j].rect.y +staticObjects[j].height): #finding all of their x values
                yvalues.append(y)
            for i in range(roundup(self.rect.y), 720, 10):
                if self.rect.x + self.width//2 in xvalues and i == staticObjects[j].rect.y: #so, if the middle of the player is over a platform, make the ground the platforms y pos
                        groundY = staticObjects[j].rect.y

        if roundup(self.rect.y) < groundY - self.height:
            self.velY +=1
        elif self.velY > 0:
            self.velY = 0
            self.rect.y = groundY - self.height
            self.Jump = False;

        if self.lkupx == True and self.rkupx == True: #kupx = Key Up X
            self.velX *= 0.85

        if self.rect.x >= 1180 - 50: #left wall side collision detection
            self.rect.x = 1180 - 50 #the -50 accounts for the players width
        if self.rect.x <= 100: #right wall side collision detection
            self.rect.x = 100
