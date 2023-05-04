import pygame as pg
# Импортируем системную функцию exit
from sys import exit

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

current_color = 1
while True:

    # Ждем события (действия пользователя)
    for event in pg.event.get():
        # Если нажали на крестик,
        # то закрываем окно
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pg.draw.circle(
                    display, array_colors[current_color], event.pos, 20)
                pg.display.update()
            elif event.button == 3:
                if (current_color == 8):
                    current_color = 1
                else:
                    current_color += 1
                pg.display.update()
            elif event.button == 2:
                pg.draw.circle(
                    display, array_colors[0], event.pos, 20)
                pg.display.update()

    # Обновляем поверхность игры
    # на каждом шаге основного цикла игры
    pg.display.update()
    clock.tick(FPS)
