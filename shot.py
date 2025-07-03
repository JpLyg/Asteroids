from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self,x,y,radius,rotation):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
        self.duration = 0.5

    def update(self, dt):
        self.position += self.velocity * dt
        if self.duration > 0:
             self.duration-= dt
        else: self.kill()

    def draw(self,screen):
                pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius)
    
    def shot_collision(self,target):
        if self.position.distance_to(target.position) <= (self.radius + target.radius):
            if target.radius >= ASTEROID_MIN_RADIUS:
                 #work here
                 
                return True
            
            #target.kill()    
            #self.kill()
            return False
