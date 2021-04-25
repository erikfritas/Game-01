import pygame as pyg
from pygame.locals import *

clock = pyg.time.Clock()

pyg.init()

screen = pyg.display.set_mode([800, 600], RESIZABLE)

mouse0 = pyg.image.load('./res/mouse/mouse_0.png')
mouse = pyg.transform.scale(mouse0, (100, 100))

# Angulo
angle = 0
mx = 350
my = 250
mxs = []
mys = []


def update():
    global angle, my, mx
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            exit()
    mx = pyg.mouse.get_pos()[0]
    my = pyg.mouse.get_pos()[1]
    try:
        if mx > mxs[1]:
            angle += 1
        else:
            if angle > 0:
                angle = 0
            angle -= 1
    except:
        mxs.append(mx)
        mys.append(my)
    try:
        t = mxs[2]
        mxs.pop(0)
    except:
        pass


def render():
    global angle
    screen.fill((0, 0, 10))
    mouse_copy = pyg.transform.rotate(mouse, angle)
    screen.blit(mouse_copy, (mx - int(mouse_copy.get_width()/2), my - int(mouse_copy.get_height()/2)))


while True:
    clock.tick()
    update()
    render()

    pyg.display.update()

