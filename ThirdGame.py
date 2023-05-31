import random

import pygame as pg

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pg.init()
dis_W = 800
dis_H = 600
dis = pg.display.set_mode((dis_W, dis_H))  # Задаём размер игрового поля.

pg.display.update()
pg.display.set_caption("Змейка");
snake_block = 10
x1 = dis_W / 2
y1 = dis_H / 2
v_x1 = 0
v_y1 = 0
game_over = False
clock = pg.time.Clock()
foodx = round(random.randrange(0, dis_W - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_H - snake_block) / 10.0) * 10.0

length_of_snake =1
while not game_over:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game_over = True
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_LEFT:
                v_x1 = -snake_block
                v_y1 = 0
            elif e.key == pg.K_RIGHT:
                v_x1 = snake_block
                v_y1 = 0
            elif e.key == pg.K_UP:
                v_x1 = 0
                v_y1 = -snake_block
            elif e.key == pg.K_DOWN:
                v_x1 = 0
                v_y1 = snake_block
    if x1 >= dis_W or x1 <= 0 or y1 >= dis_H or y1 <= 0:
        game_over = True
    if x1 == foodx and y1 == foody:  # Указываем, что в случаях,

        foodx = round(random.randrange(0, dis_W - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_H - snake_block) / 10.0) * 10.0
    length_of_snake += 1
    dis.fill(white)
    x1 += v_x1
    y1 += v_y1
    v_x1 = 0
    v_y1 = 0
    pg.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
    pg.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pg.display.update()
    clock.tick(30)

pg.quit()
quit()
