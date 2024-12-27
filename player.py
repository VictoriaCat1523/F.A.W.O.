
import pygame
import os
class Player:
    def __init__(self, x = 100, y = 701):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join('pictures','cat_1.png'))
        self.speed = 5
        self.jump_speed = 15
        self.move = 0
        self.jump_velocity = 0
        self.is_jumping = False
        self.is_running = False
        self.rect = self.image.get_rect(topleft=(100, 701))
        self.rect.width = 30
        self.rect1 = self.image.get_rect(topleft=(100, 701))
        self.is_alive = True
    def move_left(self):
        self.move = -self.speed
        self.is_running = True

    def move_right(self):
        self.move = self.speed
        self.is_running = True

    def jump(self):
        self.jump_velocity = -self.jump_speed
        self.is_jumping = True
    def gety(self):
        return  str(self.rect.y)

    def update(self,gravity,ground,HEIGHT):
        self.y += self.jump_velocity
        self.rect.y = self.y
        self.rect1.y = self.y



        self.jump_velocity += gravity
        self.x += self.move
        self.rect.x = self.x+10
        self.rect1.x = self.x
        if self.y + self.height + ground >= HEIGHT:
            self.y = HEIGHT - self.height - ground
            self.is_jumping = False
            self.jump_velocity = 0
        if self.is_running == False:
            self.move = 0
