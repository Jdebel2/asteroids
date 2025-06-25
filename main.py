import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        screen.fill(pygame.Color(0,0,0,255))

        for u in updateable:
            u.update(dt)

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            for s in shots:
                if a.collide(s):
                    a.split()
                    s.kill()

            if a.collide(player):
                print("Game Over!")
                sys.exit(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        
        pygame.display.flip()

if __name__ == "__main__":
    main()