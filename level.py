import pygame
import os
class Level:
    def __init__(self, player, enemy,enemy1):
        self.level_0 = pygame.image.load(os.path.join('pictures', 'backgraund_0.jpg'))
        self.level_1 = pygame.image.load(os.path.join('pictures', 'backgraund_1.jpg'))
        self.level_2 = pygame.image.load(os.path.join('pictures', 'backgraund_2.jpg'))
        self.level = 0
        self.player = player
        self.enemy = enemy
        self.enemy1 = enemy1


    def update(self,WIDTH,scr):
        self.draw(WIDTH, scr)
        if self.level == 1:
            pass



    def draw(self, WIDTH, scr):


        if self.level==0:
            if self.player.x + self.player.width >= WIDTH:
                scr.blit(self.level_1, (0, 0))
                scr.blit(self.enemy.image, (self.enemy.x, self.enemy.y))
                self.player.x = 100
                self.level = 1

            else:
                scr.blit(self.level_0, (0, 0))
        elif self.level == 1:
            if self.player.x - self.player.width <= 0:
                scr.blit(self.level_0, (0, 0))
                self.player.x = WIDTH - 200
                self.level = 0
            elif self.player.x + self.player.width >= WIDTH:
                scr.blit(self.level_2, (0, 0))
                self.player.x = 100
                self.level = 2
            else:
                scr.blit(self.level_1, (0, 0))
                scr.blit(self.enemy.image, (self.enemy.x, self.enemy.y))
        elif self.level== 2:
            if self.player.x - self.player.width <= 0:
                scr.blit(self.level_1, (0, 0))
                self.player.x = WIDTH - 200
                self.level= 1

            else:
                scr.blit(self.level_2, (0, 0))
                scr.blit( self.enemy.image, (self.enemy.x, self.enemy.y))
                scr.blit(self.enemy1.image, (self.enemy1.x, self.enemy1.y))
        # отрисовка коллайдеров, для отладки
        #pygame.draw.rect(scr, (255,255,10), self.player.rect)
        #pygame.draw.rect(scr, (255, 205, 50), self.enemy.collider)
        #pygame.draw.rect(scr, (255, 105, 50), self.enemy1.collider)
        #scr.blit(self.enemy1.image, (self.enemy1.x, self.enemy1.y))
        #scr.blit(self.enemy.image, (self.enemy.x, self.enemy.y))


