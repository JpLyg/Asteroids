from circleshape import *
from constants import *
import gamestate

class Shot(CircleShape):
    def __init__(self,x,y,radius,rotation):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
        self.duration = 0.5
        self.payload = 1

    def update(self, dt):
        self.position += self.velocity * dt
        if self.duration > 0:
             self.duration-= dt
        else: 
             gamestate.Score -=1
             print("score:",gamestate.Score)
             self.kill()
            

    def draw(self,screen):
                pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius)
    
    def shot_collision(self,target):
        if self.position.distance_to(target.position) <= (self.radius + target.radius):
            target.health -= self.payload
            gamestate.Score +=1
            print("score:",gamestate.Score)
            if self.payload != 0: self.payload = 0
            #print("health",target.health)
            self.kill()
            if target.radius >= ASTEROID_MIN_RADIUS and target.health <= 0:
                gamestate.Score += target.original_health
                print("score:",gamestate.Score)
                return True
            
            return False
