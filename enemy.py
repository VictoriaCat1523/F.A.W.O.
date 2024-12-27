import pygame
import os
class Enemy:
    def __init__(self, player, image, collider, x = 1000, y = 620, speed = 3):
        self.width = 50
        self.height = 50
        self.image = image
        self.speed = speed
        self.x = x
        self.y = y
        self.right = False
        self.move = 0
        self.collider = collider
        self.collider.y=self.y
        self.player = player
    def move_left(self):
        self.move = -self.speed
    def update(self):
        self.x += self.move
        self.collider.x = self.x
        self.collision()
    def collision(self):

        if self.player.rect.colliderect(self.collider):
            self.player.is_alive = False
        if self.player.rect1.colliderect(self.collider):
            pass


