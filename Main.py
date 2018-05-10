import pygame
from Spaceship import Spaceship
from random import randrange
from Asteroid import Asteroid
from Label import Label
pygame.init()

backgroundImage = pygame.transform.scale(pygame.image.load("images/stars.png"), (900, 600))
SCREEN_WIDTH = backgroundImage.get_width()
SCREEN_HEIGHT = backgroundImage.get_height()
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroid - CS301 - Jimenez")
screen.blit(backgroundImage, (0,0))

gameLoop = False
timer = pygame.time.Clock()
spaceshipSprite = Spaceship(["images/rocket2a.png", "images/rocket2b.png"], screen.get_size(), "images/rocket1.png")
instruction = Label("Press the arrow keys to move!", 30, (SCREEN_WIDTH//2, 30), (255,255,255))
collisionLabel = Label("Collisions: 0", 30, (80,SCREEN_HEIGHT-30), (255,255,255))
gameOverLabel = Label("GAME OVER!", 80, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (255,255,255))
spriteGroup = pygame.sprite.Group(spaceshipSprite, instruction,collisionLabel)
iteration = 0
asteroids = []
collisions = 0
gameOver = False

while not gameLoop:
    timer.tick(FPS)
    for asteroid in asteroids:
        if(asteroid.rect.top > SCREEN_HEIGHT):
            spriteGroup.remove(asteroid)
            asteroids.remove(asteroid)
        if(spaceshipSprite.smallerHitBox.colliderect(asteroid)):
            print(spaceshipSprite.rect)
            collisions += 1
            asteroids.remove(asteroid)
            asteroidRect = asteroid.rect
            asteroid.image = pygame.image.load("images/redasteroid.png")
            asteroidrect = asteroidRect
            collisionLabel.text = "Collisions: " + str(collisions)
        if(collisions == 5):
            spriteGroup.empty()
            gameOver = True
            spriteGroup.add(gameOverLabel)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameLoop = True

    if(not gameOver):
        if (randrange(1, 100) % 20 == 0):
            newAsteroid = Asteroid("images/asteroid.png", screen.get_size())
            asteroids.append(newAsteroid)
            spriteGroup.add(newAsteroid)
    spriteGroup.clear(screen, backgroundImage)
    spriteGroup.update()
    spriteGroup.draw(screen)
    pygame.display.update()

pygame.quit()