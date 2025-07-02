from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame

def main():
    
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    dt = 0
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
    asteroid_f = AsteroidField()
    

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
             
        screen.fill("black")#background declaration

        updatable.update(dt) #whole update processes

        for ast in asteroid_:
            if ast.collision(pc1):
                print("game over")
                return
            for shots_ in shots:
                shots_.shot_collision(ast)     
            
                

        keys = pygame.key.get_pressed()            
        if keys[pygame.K_SPACE]:pc1.shoot(screen,dt)


    
        for process in drawable:
            process.draw(screen)
    

        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60)/1000


    exit()
if __name__ == "__main__":
    main()
    
