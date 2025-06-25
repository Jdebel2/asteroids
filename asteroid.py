import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(
            screen, 
            pygame.Color(255,255,255,255), 
            self.position, 
            self.radius,
            2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        n_angle = random.uniform(20, 50)
        velocity_left = self.velocity.rotate(-n_angle)
        velocity_right = self.velocity.rotate(n_angle)
        asteroid_l = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_r = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_l.velocity = velocity_left * 1.2
        asteroid_r.velocity = velocity_right * 1.2