import pygame as pg
# Импортируем системную функцию exit
from sys import exit
import random
import time

# Инициализируем pygame
pg.init()
W, H = 800, 600
array_colors = [(255, 255, 255),
                (0, 0, 0),
                (156, 39, 176),
                (63, 81, 181),
                (33, 150, 243),
                (76, 175, 80),
                (255, 235, 59),
                (255, 152, 0),
                (158, 158, 158)]
# Создаем окошко 800 пикселей шириной
# и 600 пикселей высотой и записываем его
# в переменную display.
# Переменную display называют поверхностью.
display = pg.display.set_mode((W, H))
display.fill(array_colors[0])
# Основной цикл игры
FPS = 60  # Создаем переменную FPS
clock = pg.time.Clock()  # Создаем счетчик для FPS
startTime = time.perf_counter()
print(random.randint(0, 10))
array_rect = []

rect_count = 0
while True:

    # Ждем события (действия пользователя)
    for event in pg.event.get():
        # Если нажали на крестик,
        # то закрываем окно
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and len(array_rect) - 1 >= 0:

                for el in array_rect:
                    print(event.pos)
                    if el.x <= event.pos[0] <= (el.x + 20) and \
                            el.y <= event.pos[1] <= (el.y + 20):
                        pg.draw.rect(display, array_colors[0], el)
                        array_rect.pop(array_rect.index(el))
                        rect_count += 1
        if (time.perf_counter() - startTime) > 0.5:
            startTime = time.perf_counter()
            rect = pg.Rect(random.randint(1, 770), random.randint(1, 570), 20, 20)
            array_rect.append(rect);
            pg.draw.rect(display, array_colors[random.randint(1, 8)], rect)
        print(time.perf_counter())

        pg.display.update()
        clock.tick(FPS)
    if (rect_count == 3):
        break
font1 = pg.font.SysFont(None, 72)
img1 = font1.render('Победа', True, array_colors[5])
display.blit(img1, (20, 50))
pg.display.update()
pg.time.delay(1000)
pg.quit()
exit()
