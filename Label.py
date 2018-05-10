from pygame.sprite import Sprite
import pygame

class Label(Sprite):
    def __init__(self, text, size, coordinates, color):
        Sprite.__init__(self)
        self.text = text
        self.size = size
        self.coordinates = coordinates
        self.color = color

    def update(self):
        label = pygame.font.SysFont("freesansbold.ttf", self.size).render(self.text, True, self.color)
        labelPos = label.get_rect()
        labelPos.centerx = self.coordinates[0]
        labelPos.centery = self.coordinates[1]
        self.image = label
        self.rect = labelPos
