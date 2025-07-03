from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame
import random
import gamestate

gobal_score = 0

def main():
    
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    dt = 0
    score=0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroid_ = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #asteroid_updt = pygame.sprite.Group()
    asteroid_drw = pygame.sprite.Group()
    
    Asteroid.containers = (asteroid_,updatable,drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,drawable,updatable)
    pc1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,PLAYER_RADIUS)
    pc1.health= 3
    asteroid_f = AsteroidField()
    print (pc1.health)
    

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
             
        screen.fill("black")#background declaration

        updatable.update(dt) #whole update processes

        for ast in asteroid_:
            if ast.collision(pc1) and pc1.health <=0:
                print("game over, Total Score:",gamestate.Score)
                return
            
            for shots_ in shots:
               shot_collision(ast,shots_)

            #for ast2 in asteroid_:
             #   if ast != ast2:
              #       asteroid_collision(ast,ast2)           

            
                

        keys = pygame.key.get_pressed()            
        if keys[pygame.K_SPACE]:pc1.shoot(screen,dt)

        for process in drawable:
            process.draw(screen)
    

        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60)/1000

    exit()


def shot_collision(asteroid,shot):
    if shot.shot_collision(asteroid):
        # ddddddddddshot.kill()
        asteroid.split()   
        asteroid.kill()
        

def asteroid_collision(asteroid,asteroid2):
    if asteroid.self_collision(asteroid2):

        asteroid.split()
        asteroid2.split()
        asteroid.kill()
        asteroid2.kill()
    
    
if __name__ == "__main__":
    main()
    
