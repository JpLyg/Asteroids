from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__self(x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.position,self.radius,1)

    def update(self, dt):
        self.position += self.velocity*dt
        if self.health <= 1: self.color="red"
        if self.health == 2: self.color="yellow"

    def split(self):
        ran = random.uniform(20,50)
        new_angle_1 = self.velocity.rotate(ran)
        new_angle_2 = self.velocity.rotate(-ran)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        cas1=Asteroid(self.position.x,self.position.y,new_rad)
        cas1.velocity=new_angle_1
        cas1.health=self.original_health -1
        cas1.original_health=self.original_health -1
        cas2=Asteroid(self.position.x,self.position.y,new_rad)
        cas2.velocity=new_angle_2
        cas2.health=self.original_health -1
        cas2.original_health=self.original_health -1

    def self_collision(self,oas):
        if self.position.distance_to(oas.position) <= (self.radius + oas.radius):
            if oas.radius >= ASTEROID_MIN_RADIUS: return True
        return False