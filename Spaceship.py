from pygame.sprite import Sprite
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

        for imageLocation in imageLocations:
            self.imageNormal.append(pygame.image.load(imageLocation))
        for image in self.imageNormal:
            self.imageRight.append(pygame.transform.rotate(image, -90))
            self.imageLeft.append(pygame.transform.rotate(image, 90))
            self.imageBottom.append(pygame.transform.rotate(image, 180))

        self.imagesInUse = self.imageNormal

        self.idleImage = pygame.image.load(idleImageLocation)
        self.imageSize = self.imageNormal[0].get_size()
        self.rect = pygame.Rect((0,0), self.imageSize)
        self.rect.centerx = self.width//2
        self.rect.centery = self.height-60

        self.smallerHitBox = pygame.rect.Rect((0, 0), (120, 145))
        self.smallerHitBox.midbottom = self.rect.midbottom

        self.totalFrames = len(self.imageNormal)
        self.currentFrame = 0
        self.imageCurrentIndex = 0

        self.image = self.idleImage
        self.speedx = 5
        self.speedy = 5
        self.moving = False

    def update(self):

        self.dx = 0
        self.dy = 0
        self.moving = False

        keysPressed = pygame.key.get_pressed()
        if(keysPressed[pygame.K_RIGHT]):
            self.dx = self.speedx
            self.moving = True
            self.imagesInUse = self.imageRight
        elif(keysPressed[pygame.K_LEFT]):
            self.dx = -self.speedx
            self.moving = True
            self.imagesInUse = self.imageLeft
        elif(keysPressed[pygame.K_UP]):
            self.dy = -self.speedy
            self.moving = True
            self.imagesInUse = self.imageNormal
        elif(keysPressed[pygame.K_DOWN]):
            self.dy = self.speedy
            self.moving = True
            self.imagesInUse = self.imageBottom
        if(self.moving):
            self.music.play(-1)
            self.image = self.imagesInUse[self.imageCurrentIndex]
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
            self.image = self.idleImage
            self.music.stop()
        self.smallerHitBox.midbottom = self.rect.midbottom
