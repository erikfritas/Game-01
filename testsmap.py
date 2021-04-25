import pygame as pyg
from pygame.locals import *
import random, time
from spritesheet.Sprites import *

clock = pyg.time.Clock()
FPS = 60

pyg.init()

screen = pyg.display.set_mode([800, 600], RESIZABLE)

mouse = pyg.transform.scale(pyg.image.load('./res/mouse/mouse_0.png'), (16, 16))
seletor = pyg.transform.scale(pyg.image.load('./res/mouse/mouse_1.png'), (16, 16))

with open('./res/mapas/mapa1.txt') as m1:
    game_map = m1.readlines()


def po():
    r = random.randint(0, 300)
    # pedra
    if r < 20:
        return '3'
    # arvore
    elif r < 40:
        return '4'
    # grama
    else:
        return '1'


def ra():
    return po()


def generate(gm):
    mapa = []
    for num in gm:
        if num != '1\\n':
            mapa.append(f'22222222222222222222222222222222222222222222222222222222222222222')
        else:
            mapa.append(f'222222222222222222222222222222222222222222222222222222222222222222\\n')
        break
    for num in gm:
        if num != '1\\n':
            mapa.append(f'2{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}2')
        else:
            mapa.append(f'2{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                        f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}2\\n')
    for num in gm:
        if num != '1\\n':
            mapa.append(f'22222222222222222222222222222222222222222222222222222222222222222')
        else:
            mapa.append(f'2222222222222222222222222222222222222222222222222222222222222222222\\n')
        break

    with open('./res/mapas/mapa1.txt', 'w') as m1:
        for m in mapa:
            m1.writelines(m+'\n')
    return mapa


newm = generate(game_map)

auto = False

while True:
    clock.tick(FPS)
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_e:
                if not auto:
                    auto = True
                else:
                    auto = False

    screen.fill((0, 0, 10))

    if auto:
        newm = generate(game_map)
        time.sleep(.5)

    tile_rects = []
    y = 0
    for layer in newm:
        x = 0
        for tile in layer:
            # grama
            if tile == '1':
                pyg.draw.rect(screen, (0, 180, 0), (x * 16, y * 16, 16, 16))
            # agua
            if tile == '2':
                pyg.draw.rect(screen, (0, 0, 180), (x * 16, y * 16, 16, 16))
            # pedra
            if tile == '3':
                pyg.draw.rect(screen, (180, 180, 180), (x * 16, y * 16, 16, 16))
            # arvore
            if tile == '4':
                pyg.draw.rect(screen, (107, 29, 5), (x * 16, y * 16, 16, 16))
            # areia
            if tile == '5':
                pyg.draw.rect(screen, (230, 201, 14), (x * 16, y * 16, 16, 16))
            # buraco
            if tile == '6':
                pyg.draw.rect(screen, (31, 8, 1), (x * 16, y * 16, 16, 16))
            x += 1
        y += 1
    screen.blit(mouse, (100, 100))

    pyg.display.update()
