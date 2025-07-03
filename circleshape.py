import pygame
from  constants import *
import gamestate

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.health = 0
        self.color= "white"
        self.original_health = 0

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self,target):
        if self.position.distance_to(target.position) <= (self.radius + target.radius) and target.timeout <=0: 
            target.health -=1
            target.timeout= 2
            gamestate.Score -= 10
            print("score:",gamestate.Score)
            
            print("ship health:",target.health)
            return True
        return False

