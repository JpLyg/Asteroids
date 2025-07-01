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

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    pc1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,PLAYER_RADIUS)


    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
        screen.fill("black")


        updatable.update(dt) 
        for process in drawable:
            process.draw(screen)
        
        #the part above has been ultimiately perflexing. Why does the draw needs a loop and the update does not?
        # Turns out the .update() just happens to be a special method with build in auto loot inside pygame.sprite

        pygame.display.flip()

        clock.tick(30)
        dt = clock.tick(30)/1000
        #print(dt)

    exit()
if __name__ == "__main__":
    main()
    
