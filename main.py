import pygame
import os

from controller import Controller
from enemy import Enemy
from player import Player
from level import Level

pygame.init()
WIDTH = 1280
HEIGHT = 731
scr = pygame.display.set_mode((WIDTH, HEIGHT))
ground = 30
gravity = 1
player = Player()

image=pygame.image.load(os.path.join('pictures', 'enemy_1_0.png'))
collider = image.get_rect(topleft=(1000, 620))
collider.width = 50
collider.height = 30
enemy = Enemy(player,image,collider,y=670)

image1=pygame.image.load(os.path.join('pictures', 'enemy_1_0.51.png'))
collider1 = image1.get_rect(topleft=(1000, 670))
collider1.width = 24
collider1.height = 14


enemy1 = Enemy(player,image1,collider1,x = 800,y=670, speed = 5)


level = Level(player,enemy,enemy1)
controller = Controller(player,enemy,enemy1,level)
stop_fl = True
clock = pygame.time.Clock()
f_sys_50 = pygame.font.SysFont('arial', 50)
f_sys_40 = pygame.font.SysFont('monospace', 40)
timer = 500
sc_text = f_sys_50.render('Game over!', 1, (255, 0, 0), 230)
pos = sc_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
sc_text_3 = f_sys_40.render('R - начать заново ', 1, (0, 255, 0), 230)
pos_3 = sc_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
sc_text_0 = f_sys_40.render('* Влево  -     A *', 1, (0, 255, 0), (255, 255, 255))
sc_text_1 = f_sys_40.render('* Вправо -     D *', 1, (0, 255, 0), (255, 255, 255))
sc_text_2 = f_sys_40.render('* Вверх  - Space *', 1, (0, 255, 0), (255, 255, 255))
pos_0 = sc_text_0.get_rect(center=(WIDTH // 4, HEIGHT // 2 - 120))
pos_1 = sc_text_1.get_rect(center=(WIDTH // 4, HEIGHT // 2 - 80))
pos_2 = sc_text_2.get_rect(center=(WIDTH // 4, HEIGHT // 2 - 40))


def draw_text():
        scr.blit(sc_text_0, pos_0)
        scr.blit(sc_text_1, pos_1)
        scr.blit(sc_text_2, pos_2)


while stop_fl :
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            stop_fl = False

        keys = pygame.key.get_pressed()


        if keys[pygame.K_a]:
            player.move_left()


        elif keys[pygame.K_d]:
            player.move_right()


        else:
            player.is_running = False

        if keys[pygame.K_SPACE] and player.is_jumping == False:
            player.jump()

    if player.is_alive == False:
        scr.blit(sc_text, pos)
        scr.blit(sc_text_3, pos_3)

        if keys[pygame.K_r] :
            level.level=0
            player.is_alive = True
            player.x=10

    #pygame.display.update()

    else:
        player.update(gravity,ground,HEIGHT)
        level.update(WIDTH,scr)
        controller.update(WIDTH)
        if timer > 0 and level.level == 0:
            draw_text()

    if timer>0 :
        timer -= 1
    scr.blit(player.image,(player.x,player.y))
    pygame.display.update()
    #pygame.display.flip()
    clock.tick(60)
