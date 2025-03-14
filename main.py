import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        
        #old player update and draw
        #player.update(dt)
        #player.draw(screen)

        #group update and draw
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for roid in asteroids:
            if roid.check_collision(player):
                print("Game over!")
                sys.exit()            
            for shot in shots:
                if shot.check_collision(roid):
                    shot.kill()
                    roid.split()

        pygame.display.flip()
        dt = (clock.tick(60)/1000)
        

if __name__ == "__main__":
    main()
