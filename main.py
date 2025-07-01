from constants import *
from player import *
import pygame

def main():
    
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    dt = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pc1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,PLAYER_RADIUS)
    
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
        screen.fill("black")

        pc1.update(dt,PLAYER_TURN_SPEED)


        pc1.draw(screen)

        pygame.display.flip()

        clock.tick(30)
        dt = clock.tick(30)/1000
        #print(dt)

    exit()
if __name__ == "__main__":
    main()
    
