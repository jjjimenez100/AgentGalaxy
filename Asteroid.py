from pygame.sprite import Sprite
from random import randrange, uniform
import pygame

class Asteroid(Sprite):
    def __init__(self, imageLocation, screenSize=()):
        Sprite.__init__(self)
        self.width = screenSize[0]
        self.height = screenSize[1]
        self.image = pygame.transform.scale(pygame.image.load(imageLocation), (50,50))
        self.rect = self.image.get_rect()
        self.spawnOnTop = randrange(1,100) % 2 == 0
        #if(spawnOnTop):
        self.rect.x = randrange(10, self.width-self.image.get_width()) # Para di sagad sa side
        self.rect.y = uniform(-40, 0)
        #self.speedx = randrange(5,10)
        self.speedy = randrange(1, 5)
    def update(self):
        #self.rect.x += self.speedx
        self.rect.y += self.speedy