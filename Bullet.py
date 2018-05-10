from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, imageLocation, screenSize=(), direction=1):
        Sprite.__init__(self)
        self.image = pygame.image.load(imageLocation)
        self.dySpeed = 5
        self.dxSpeed = 5
        if(direction == 1):
            self.dySpeed *= -1
            self.dxSpeed = 0
        elif(direction == 2):
            self.dySpeed = 0
            self.image = pygame.transform.rotate(self.image, -90)
        elif(direction == 3):
            self.dxSpeed = 0
            self.image = pygame.transform.rotate(self.image, 180)
        else:
            self.dxSpeed *= -1
            self.dySpeed = 0
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.width = screenSize[0]
        self.height = screenSize[1]

    def update(self):
        self.rect.y += self.dySpeed
        self.rect.x += self.dxSpeed