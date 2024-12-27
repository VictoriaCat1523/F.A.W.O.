import pygame
import os
class Controller:
    def __init__(self, player, enemy,enemy1, level):
        self.level = level
        self.player = player
        self.enemy = enemy
        self.enemy1 = enemy1
    def update(self,WIDTH):
        if self.level.level == 0:
            self.player.x = max(0, self.player.x)
        elif self.level.level > 0:
            if self.enemy.x - self.enemy.width > - 100:
                self.enemy.move_left()
            else:
                self.enemy.x = 1500
            self.enemy.update()

        if self.level.level > 1:
            if self.enemy1.x - self.enemy1.width > - 100:
                self.enemy1.move_left()
            else:
                self.enemy1.x = 1500
            self.enemy1.update()
        if self.level.level == 2:
            if self.player.x + self.player.width > WIDTH:
                self.player.x = WIDTH - self.player.width