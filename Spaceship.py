from pygame.sprite import Sprite
from Bullet import Bullet
import pygame

# +90 left
class Spaceship(Sprite):
    def __init__(self, imageLocations=[], screenSize=(), idleImageLocation=""):
        Sprite.__init__(self)
        pygame.mixer.init()
        self.music = pygame.mixer.Sound("images/rocketSound.wav")
        self.width = screenSize[0]
        self.height = screenSize[1]

        self.imageNormal = []
        self.imageRight = []
        self.imageLeft = []
        self.imageBottom = []

        self.imageNormal.append(pygame.image.load(idleImageLocation))
        for imageLocation in imageLocations:
            self.imageNormal.append(pygame.image.load(imageLocation))
        for image in self.imageNormal:
            self.imageRight.append(pygame.transform.rotate(image, -90))
            self.imageLeft.append(pygame.transform.rotate(image, 90))
            self.imageBottom.append(pygame.transform.rotate(image, 180))

        self.imagesInUse = self.imageNormal

        #self.idleImage = pygame.image.load(idleImageLocation)
        self.imageSize = self.imageNormal[0].get_size()
        self.rect = pygame.Rect((0,0), self.imageSize)
        self.rect.centerx = self.width//2
        self.rect.centery = self.height-60

        self.smallerHitBox = pygame.rect.Rect((0, 0), (120, 145))
        self.smallerHitBox.midbottom = self.rect.midbottom

        self.totalFrames = len(self.imageNormal)
        self.currentFrame = 0
        self.imageCurrentIndex = 0

        self.image = self.imagesInUse[self.imageCurrentIndex]
        self.speedx = 5
        self.speedy = 5
        self.moving = False
        self.maxInterval = 50
        # 1 up 2 right 3 bottom 4 left
        self.direction = 1
        self.perFrameIncrement = 5
        self.currentInterval = 0
        self.beams = []

    def update(self):

        self.dx = 0
        self.dy = 0
        self.moving = False

        keysPressed = pygame.key.get_pressed()
        if (keysPressed[pygame.K_SPACE]):
            if (self.currentInterval == 0):
                newBeam = Bullet("images/laserBlue01.png", (self.width, self.height), self.direction)
                if(self.direction == 1):
                    newBeam.rect.x = self.smallerHitBox.centerx
                    newBeam.rect.y = self.smallerHitBox.midtop[1] - 50
                elif(self.direction == 2):
                    newBeam.rect.x = self.smallerHitBox.midright[0] + 5
                    newBeam.rect.y = self.smallerHitBox.midright[1] - 25
                elif(self.direction == 3):
                    newBeam.rect.x = self.smallerHitBox.midbottom[0] - 10
                    newBeam.rect.y = self.smallerHitBox.midbottom[1] - 30
                elif(self.direction == 4):
                    newBeam.rect.x = self.smallerHitBox.midleft[0] - 35
                    newBeam.rect.y = self.smallerHitBox.midleft[1] - 35
                self.beams.append(newBeam)
                self.currentInterval += self.perFrameIncrement
            elif (self.currentInterval == self.maxInterval):
                self.currentInterval = 0
            else:
                self.currentInterval += self.perFrameIncrement
        if(keysPressed[pygame.K_RIGHT]):
            self.dx = self.speedx
            self.moving = True
            self.direction = 2
            self.imagesInUse = self.imageRight
        elif(keysPressed[pygame.K_LEFT]):
            self.dx = -self.speedx
            self.moving = True
            self.direction = 4
            self.imagesInUse = self.imageLeft
        elif(keysPressed[pygame.K_UP]):
            self.dy = -self.speedy
            self.moving = True
            self.direction = 1
            self.imagesInUse = self.imageNormal
        elif(keysPressed[pygame.K_DOWN]):
            self.dy = self.speedy
            self.moving = True
            self.direction = 3
            self.imagesInUse = self.imageBottom

        if(self.moving):
            self.music.play(-1)
            #self.image = self.imagesInUse[self.imageCurrentIndex]
            self.currentFrame += 1
            if(self.currentFrame >= self.totalFrames):
                self.currentFrame = 0
                self.imageCurrentIndex = (self.imageCurrentIndex + 1) % (len(self.imageNormal))
                self.image = self.imagesInUse[self.imageCurrentIndex]

            if (self.rect.right > self.width):
                self.rect.right = self.width
            elif (self.rect.left < 0):
                self.rect.left = 0
            elif(self.rect.top < 0):
                self.rect.top = 0
            elif(self.rect.bottom > self.height):
                self.rect.bottom = self.height
            else:
                self.rect.move_ip(self.dx, self.dy)
        else:
            self.music.stop()
            self.image = self.imagesInUse[0]
        self.smallerHitBox.midbottom = self.rect.midbottom
