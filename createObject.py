#object creation file. Planned to be consisting of four types.
#Static, moveable, interactable, and mountable(?)
#I could probably cram these all into one object, but it helps debugging, at the expense
#of a pretty messy program. Oh well, its a seperate module.
import pygame


class newStatic:
    def __init__(self): #initiatialising
        self.height = 0;
        self.width = 0;
        self.x = 0;
        self.y = 0;
        self.lorr = 0; #lorr == set X Vel
        self.kupx = False;

    def setParams(self, height, width, x, y):
        self.height = height;
        self.width = width;
        self.x = x;
        self.y = y;

    def KUPX(self):
        self.kupx = True

    def KDPX(self):
        self.kupx = False;

    def setColor(self, color):
        self.color = color;

    def drawChar(self, screen):#drawing the inital character
        self.screen = screen;
        self.rect = pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

    def setX(self, x):
        self.lorr = x;

    def tick(self, screen):
        self.rect = self.rect.move(self.lorr,0)
        if self.rect.x >= 1280 or self.rect.x <= -1280:
            return
        print("Rendered" + str(self.rect.x))
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

    def tick(self):
        self.rect = self.rect.move(self.velX,self.velY)#assigning the new rect pos to self.rect
        pygame.draw.rect(self.screen, (0, 0, self.width, self.height), self.rect)#drawing the new rect
        pygame.display.update(self.rect)#updating the display
        groundY = 600;
        if self.Jump == True: #code for jumping, basically keeps moving it up by less and less uuntil it decreases and reaches 600(floor)
            if self.rect.y >= groundY - 25:
                self.velY = 0
                self.rect.y = groundY - 25
                self.Jump = False;
            else:
                self.velY +=1

        if self.lkupx == True and self.rkupx == True: #kupx = Key Up X
            self.velX *= 0.85

        if self.rect.x >= 1180 - 50: #left wall side collision detection
            self.rect.x = 1180 - 50 #the -50 accounts for the players width
        if self.rect.x <= 100: #right wall side collision detection
            self.rect.x = 100
