import pygame

class newStatic:
    def __init__(self):
        self.height = 0;
        self.width = 0;
        self.x = 0;
        self.y = 0;
        self.lorr = 0;
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

    def drawChar(self, screen):
        self.screen = screen;
        self.rect = pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

    def setX(self, x):
        self.lorr = x;

    def tick(self):
        self.rect = self.rect.move(self.lorr,0)
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.display.update(self.rect)
        if self.kupx == True:
            self.lorr *= 0.9

class newMoveable:
    def __init__(self):
        self.height = 0;
        self.width = 0;
        self.x = 0;
        self.y = 0;
        self.velX = 0;
        self.velY = 0;
        self.kupy = False;
        self.kupx = False;
        self.Jump = False;
        self.crouching = False;

    def printCoords(self):
        return self.rect.x, self.rect.y

    def KUPY(self):
        self.kupy = True

    def KUPX(self):
        self.kupx = True

    def KDPX(self):
        self.kupx = False;

    def KDPY(self):
        self.kupy = False;

    def setParams(self, height, width, x, y):
        self.height = height;
        self.width = width;
        self.x = x;
        self.y = y;

    def drawChar(self, screen):
        self.screen = screen;
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height)) #(x,y,width,height)

    def setColor(self, color):
        self.color = color;

    def setVelX(self, velX):
        self.velX = velX;

    def setX(self, x):
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y


    def crouch(self):
        self.crouching = True;

    def inJump(self):
        if self.Jump != True:
            self.Jump = True;
            self.velY = -20
        else:
            return

    def tick(self):
        self.rect = self.rect.move(self.velX,self.velY)
        pygame.draw.rect(self.screen, (0, 0, self.width, self.height), self.rect)
        pygame.display.update(self.rect)
        if self.Jump == True:
            if self.rect.y >= 600:
                self.velY = 0
                self.rect.y = 600
                self.Jump = False;
            else:
                self.velY +=1

        if self.kupx == True:
            self.velX *= 0.9

        if self.rect.x >= 1080:
            self.rect.x = 1080
        if self.rect.x <= 100:
            self.rect.x = 100
