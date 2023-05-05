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
size_cursor = 20
current_color = 1
while True:

    # Ждем события (действия пользователя)
    for event in pg.event.get():
        # Если нажали на крестик,
        # то закрываем окно
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                size_cursor += 3
            elif event.key == pg.K_e:
                size_cursor -= 3

    keys_mouse = pg.mouse.get_pressed();
    keys_keyword = pg.key.get_pressed()
    if keys_mouse[0]:
        pg.draw.circle(
            display, array_colors[current_color], pg.mouse.get_pos(), size_cursor)
        pg.display.update()
    elif keys_mouse[1]:
        pg.draw.circle(
            display, array_colors[0], event.pos, size_cursor)
        pg.display.update()
    elif keys_mouse[2]:
        if (current_color == 8):
            current_color = 1
        else:
            current_color += 1


    # Обновляем поверхность игры
    # на каждом шаге основного цикла игры
    pg.display.update()
    clock.tick(FPS)
