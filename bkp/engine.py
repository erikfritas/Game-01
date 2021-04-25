import pygame as pyg
from pygame.locals import *
import random

desenv_mode = False

def spr_50(spr):
    return pyg.transform.scale((pyg.image.load(spr)), (50, 70))


def codes(opt):
    if opt == 'f3':
        global desenv_mode
        if desenv_mode:
            desenv_mode = False
        else:
            desenv_mode = True








