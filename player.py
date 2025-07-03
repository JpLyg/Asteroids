from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self,x,y,PLAYER_RADIUS):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.rof=0
        #self.color="white"
        self.timeout = 2
        self.score = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #print("player color:",self.color)
        pygame.draw.polygon(screen,self.color,self.triangle(),2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        if self.rof >0:
            self.rof -= dt
        if self.timeout > 0:
            self.timeout -= dt

        if self.health == 1: self.color="red"
        elif self.health == 2: self.color="yellow"
        elif self.health >= 3: self.color="white"


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:self.rotate(-dt)           #turn left
        if keys[pygame.K_d]:self.rotate(dt)            #turn right
        if keys[pygame.K_w]:self.move(dt)
        if keys[pygame.K_s]:self.move(-dt)
        #if keys[pygame.K_SPACE]:self.shoot(screen,dt)
        

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self,screen,dt):
        if self.rof <= 0:
            Shot(self.position.x,self.position.y,SHOT_RADIUS,self.rotation)
            self.rof = PLAYER_SHOOT_COOLDOWN
        #bullet.update(dt)
        #bullet.draw(screen)





    

    