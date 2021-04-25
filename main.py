import pygame as pyg
from pygame.locals import *
import os, random
from spritesheet.Sprites import *

clock = pyg.time.Clock()
FPS = 120

os.environ['SDL_VIDEO_CENTERED'] = '1'

pyg.init()

info = pyg.display.Info()

WINDOW_SIZE2 = [2000, 2000]
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width-10, screen_height-50
WINDOW_SIZE = [(window_width+4)*2, (window_height+50)*2]
SURF_SIZE = [window_width+4, window_height+50]

display = pyg.display.set_mode(WINDOW_SIZE, FULLSCREEN)  # FULLSCREEN padrao, RESIZABLE dev_mode
# time.sleep(0.5)
# display = pyg.display.set_mode(WINDOW_SIZE2, RESIZABLE)  # FULLSCREEN padrao, RESIZABLE dev_mode
screen = pyg.Surface(SURF_SIZE)
pyg.display.update()

cor = {"preto": [0, 0, 10],
       "branco": [200, 200, 210],
       "amarelo": [180, 180, 0],
       "azul": [2, 2, 250],
       "agua_es": [40, 200, 184],
       "vermelho": [225, 40, 10],
       "cinza": [150, 150, 150]}

icons = {'dev_bar': pyg.transform.scale(pyg.image.load('./res/menus/dev_bar.png'), (240, 100))}

ctrl = {'up': False,
        'down': False,
        'left': False,
        'right': False,
        'speed': 8}

colide = {'cup': False,
          'cdown': False,
          'cleft': False,
          'cright': False}

pos = {'x': WINDOW_SIZE[0]/2-90,
       'y': WINDOW_SIZE[1]/2-50,
       'w': 30,
       'h': 50}

poss = {'x': 50,
        'y': 50,
        'w': 50,
        'h': 70}

equiped = {'power': False}

anim = {'idle': False,
        'walk': False,
        'fall': False,
        'zwalk': False}

c_anim = {'climb_L': False,
          'climb_R': False}

anms = ['idle', 'walk', 'fall', 'climb']

fonte = pyg.font.SysFont("consolas", 20, True, False)
fonte_50 = pyg.font.SysFont("consolas", 40, True, False)

# =============================================


def spr_20(spr):
    return pyg.transform.scale((pyg.image.load(spr)), (25, 20))


def spr_50(spr):
    return pyg.transform.scale((pyg.image.load(spr)), (30, 50))


def spr_80(spr):
    return pyg.transform.scale((pyg.image.load(spr)), (50, 80))


def sp(spr, x, y):
    return pyg.transform.scale(spr.image_at([x, y, 50, 50]), (100, 100))


# Images / Sprites

pr = "./res/player/"
zr = "./res/enemies/zombies/"
sr = "./res/spritesheet/"
bar = "./res/recursos/madeiras/"
bpr = "./res/recursos/pedras/"

mouses = pyg.image.load('./res/mouse/mouse_0.png')
seletor = pyg.image.load('./res/mouse/mouse_1.png')

allAnims = {'p_fall0': spr_50(f'{pr}fall/player_0.png'),
            'p_fall1': spr_50(f'{pr}fall/player_1.png'),
            'p_walkL0': spr_50(f'{pr}walk/left_0.png'),
            'p_walkL1': spr_50(f'{pr}walk/left_1.png'),
            'p_walkR0': spr_50(f'{pr}walk/right_0.png'),
            'p_walkR1': spr_50(f'{pr}walk/right_1.png'),
            'p_idleL0': spr_50(f'{pr}idle/left_0.png'),
            'p_idleL1': spr_50(f'{pr}idle/left_1.png'),
            'p_idleR0': spr_50(f'{pr}idle/right_0.png'),
            'p_idleR1': spr_50(f'{pr}idle/right_1.png'),
            'z_walkL0': spr_80(f'{zr}left_0.png'),
            'z_walkR0': spr_80(f'{zr}right_0.png'),
            'z_walkL1': spr_80(f'{zr}left_1.png'),
            'z_walkR1': spr_80(f'{zr}right_1.png')}

sprs = SpriteSheet(f'{sr}spritesheet.png')

b_grama0 = sprs.image_at([0, 0, 50, 50])
b_grama1 = sprs.image_at([0, 50, 50, 50])
b_grama2 = sprs.image_at([0, 100, 50, 50])
b_agua0 = sp(sprs, 200, 0)
b_agua1 = sp(sprs, 250, 0)
b_agua2 = sp(sprs, 300, 0)
b_agua3 = sp(sprs, 200, 50)
b_agua4 = sp(sprs, 250, 50)
b_agua5 = sp(sprs, 300, 50)
b_agua6 = sp(sprs, 200, 100)
b_agua7 = sp(sprs, 250, 100)
b_agua8 = sp(sprs, 300, 100)
v_arvore = spr_80(f'{bar}verao_arvore.png')
i_arvore = spr_80(f'{bar}inverno_arvore.png')
s_arvore = spr_80(f'{bar}sangue_arvore.png')
r_arvore = spr_80(f'{bar}raio_arvore.png')
v_pedra = spr_20(f'{bpr}verao_pedra.png')
i_pedra = spr_20(f'{bpr}inverno_pedra.png')
s_pedra = spr_20(f'{bpr}sangue_pedra.png')
r_pedra = spr_20(f'{bpr}raio_pedra.png')

hr = {'dia': True,
      'noite': False}

climb = False
if climb:
    climbAnims = {'p_climb_L0': spr_50(f'{pr}climb/left_0.png'),
                  'p_climb_L1': spr_50(f'{pr}climb/left_1.png'),
                  'p_climb_R0': spr_50(f'{pr}climb/right_0.png'),
                  'p_climb_R1': spr_50(f'{pr}climb/right_1.png')}

# Padrao
player_image = allAnims[f'p_idleL0']

# =============================================

dev_mode = False

tm = 10
tcbx = 10
tcby = -5
tml = 15
tcbl = 20
tmh = 20

# =============================================

cont = 0
contmedio = 15
contmax = contmedio*2
walk = False

zwalkl = False
zwalkr = False

# =============================================

true_scroll = [0, 0]
scroll = true_scroll.copy()

# =============================================

objs = []
pisaveis = []

b_pos = []

botoes = {}
hover = False
click = False
btn1 = False

# =============================================

mr_ver = False
freepos = {}


def str_scr(str_, color, position, opt='padrao'):
    if opt.lower() == 'padrao':
        fstr_ = fonte.render(str_, True, color)
        screen.blit(fstr_, position)
    elif opt.lower() == 'maior':
        fstr_ = fonte_50.render(str_, True, color)
        screen.blit(fstr_, position)


class Botao:
        def __init__(self, color, local, nome, mouse):
            self.mouse = mouse
            pyg.mouse.set_visible(False)
            x, y = self.mouse
            pyg.Rect(x, y, 10, 10)
            if hover:
                self.color = cor['branco']
            else:
                self.color = color
            self.local = local
            self.nome = nome

        def draw(self):
            global hover
            self.btn = pyg.draw.rect(screen, self.color, self.local)
            if self.btn.collidepoint(self.mouse):
                str_scr(self.nome, cor['preto'], [self.btn.x + 4.5, self.btn.y - 1.5], 'maior')
                hover = True
            else:
                hover = False
                str_scr(self.nome, cor['branco'], [self.btn.x + 4.5, self.btn.y - 1.5], 'maior')
            return self.btn

        def is_clicked(self):
            return pyg.mouse.get_pressed()[0] and self.btn.collidepoint(pyg.mouse.get_pos())


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
        mapa.append(f'2{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                    f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}'
                    f'{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}{ra()}2')
    mapa.pop(0)
    mapa.insert(0, '222222222222222222222222222222222222222')
    mapa.pop(-1)
    mapa.append('222222222222222222222222222222222222222')

    with open('./res/mapas/mapa1.txt', 'w') as m1:
        for m in mapa:
            m1.writelines(m+'\n')
    return mapa


newm = generate(game_map)
i = 0


def colision_obj(img, x, y, w, h):
    global i
    screen.blit(img, (x - scroll[0], y - scroll[1]))
    x -= scroll[0]
    y -= scroll[1]
    obj = pyg.Rect(x, y, w, h)
    try:
        objs.pop(i)
        objs.append(obj)
    except:
        objs.append(obj)
    if dev_mode:
        pyg.draw.rect(screen, cor["azul"], (x, y, w, h))
    i += 1


def chao(img, x, y):
    global pisaveis
    screen.blit(img, (x - scroll[0], y - scroll[1]))
    pisaveis.append(pyg.Rect(x-scroll[0], y-scroll[1], 50, 50))


def agua(psx, psy, opt='quad'):
    if opt == 'quad':
        colision_obj(b_agua0, psx, psy, 100, 100)
        colision_obj(b_agua1, psx + 100, psy, 100, 100)
        colision_obj(b_agua2, psx + 200, psy, 100, 100)
        colision_obj(b_agua3, psx, psy + 100, 100, 100)
        colision_obj(b_agua4, psx + 100, psy + 100, 100, 100)
        colision_obj(b_agua5, psx + 200, psy + 100, 100, 100)
        colision_obj(b_agua6, psx, psy + 200, 100, 100)
        colision_obj(b_agua7, psx + 100, psy + 200, 100, 100)
        colision_obj(b_agua8, psx + 200, psy + 200, 100, 100)


def arvore(asx, asy, biome, full=True):
    if full:
        if biome == 'v':
            colision_obj(v_arvore, asx, asy, 50, 50)
    else:
        pass


def pedra(pdx, pdy, biome, full=True):
    if full:
        if biome == 'v':
            colision_obj(v_pedra, pdx, pdy, 30, 20)
    else:
        pass


conx = 200
cony = 50
testC = False


def flatmap():
    global conx, cony, i, objs, newm, b_grama0

    i = 0
    objs = []
    y = 0
    for layer in newm:
        x = 0
        for tile in layer:
            # grama
            if tile == '1':
                chao(b_grama0, x * 50, y * 50)
            # agua
            elif tile == '2':
                chao(b_grama0, x * 50, y * 50)
                colision_obj(b_agua4, x * 50, y * 50, 50, 50)
            # pedra
            elif tile == '3':
                chao(b_grama0, x * 50, y * 50)
                pedra(x * 50, y * 50, 'v', True)
            # arvore
            elif tile == '4':
                chao(b_grama0, x * 50, y * 50)
                arvore(x * 50, y * 50, 'v', True)
            x += 1
        y += 1


def codes(opt):
    if opt == 'f3':
        global dev_mode
        if dev_mode:
            dev_mode = False
        else:
            dev_mode = True
    if opt == 'f4':
        global testC
        if testC:
            testC = False
        else:
            testC = True


def slice(lista, opt):
    if opt == 'primeiro':  # so o primeiro fica True e o resto fica False
        lista['idle'] = True
        lista['fall'] = False
        lista['walk'] = False
    elif opt == 'walk':  # o idle e o fall fica False, o walk fica verdadeiro
        lista['idle'] = False
        lista['fall'] = False
        lista['walk'] = True


blpos = {'x': pos['x'],
         'y': pos['y'],
         'w': 10,
         'h': 10,
         's': 10.5,
         'vr': False,
         'vl': False,
         'vt': False,
         'vb': False}


bclick = False


def getplpos():
    global blpos
    blpos = {'x': pos['x'],
             'y': pos['y'],
             'w': 10,
             'h': 10,
             's': 10.5,
             'vr': False,
             'vl': False,
             'vt': False,
             'vb': False}
    return blpos


mpos = []


class Bullet:
    def __init__(self, enemies):
        self.enemies = enemies
        self.mx = mpos[0][0]
        self.my = mpos[0][1]
        self.brect = pyg.Rect(blpos['x'] - scroll[0], blpos['y'] - scroll[1], blpos['w'], blpos['h'])

    def atira(self):
        global bclick
        screen.blit(pyg.transform.scale(mouses, (50, 50)), (self.brect.x, self.brect.y))
        if blpos['x'] - scroll[0] < self.mx:
            blpos['x'] += blpos['s']

        elif blpos['x'] - scroll[0] > self.mx:
            blpos['x'] -= blpos['s']

        if blpos['y'] - scroll[1] < self.my:
            blpos['y'] += blpos['s']
        if blpos['y'] - scroll[1] > self.my:
            blpos['y'] -= blpos['s']

        if self.mx + 5 > blpos['x'] - scroll[0] > self.mx - 10 \
                and self.mx - 10 < blpos['x'] - scroll[0] < self.mx + 5 \
                and self.my + 5 > blpos['y'] - scroll[1] > self.my - 10\
                and self.my - 10 < blpos['y'] - scroll[1] < self.my + 5\
                or self.brect.collidelistall(self.enemies):
            bclick = False

    def getrect(self):
        return self.brect

    def bpos(self, opt):
        if opt == 'x':
            return self.brect.x
        else:
            return self.brect.y


def controls(event):
    global btn1, bclick, blpos, mpos
    if event.type == KEYDOWN:
        if event.key == K_w:
            ctrl['up'] = True
        elif event.key == K_s:
            ctrl['down'] = True
        if event.key == K_a:
            ctrl['left'] = True
        if event.key == K_d:
            ctrl['right'] = True
        if event.key == K_F3:
            codes('f3')
        if event.key == K_F4:
            codes('f4')

    if event.type == KEYUP:
        if event.key == K_w:
            ctrl['up'] = False
        elif event.key == K_s:
            ctrl['down'] = False
        if event.key == K_a:
            ctrl['left'] = False
        elif event.key == K_d:
            ctrl['right'] = False

    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1 and equiped['power']:
            if blpos != getplpos():
                blpos = getplpos()
            mpos = []
            mpos.append(pyg.mouse.get_pos())
            bclick = True

    if pyg.mouse.get_pressed()[2]:
        btn1 = True
    else:
        btn1 = False


def colisores(um, dois, tres, quatro, optx, opty):
    rect = [(optx-scroll[0])+um, (opty-scroll[1])+dois, tres, quatro]
    if not dev_mode:
        colisor = pyg.Rect(rect)
    else:
        colisor = pyg.draw.rect(screen, cor['azul'], rect)
    return colisor


class Players:
    def __init__(self, objcs):
        global player_image, dev_mode, cont
        screen.blit(player_image, (pos['x']-scroll[0], pos['y']-scroll[1]))
        for i in anim:
            if anim[i]:
                if ctrl['left']:
                    if cont <= contmedio:
                        player_image = allAnims[f'p_{i}L0']
                        cont += 1
                    elif cont <= contmax:
                        player_image = allAnims[f'p_{i}L1']
                        cont += 1
                    else:
                        cont = 0
                elif ctrl['right']:
                    if cont <= contmedio:
                        player_image = allAnims[f'p_{i}R0']
                        cont += 1
                    elif cont <= contmax:
                        player_image = allAnims[f'p_{i}R1']
                        cont += 1
                    else:
                        cont = 0

        self.player = pyg.Rect(pos['x'], pos['y'], 30, 50)
        pup = colisores(tcbx-3, tcby, pos['w'] - tcbl+6, tm, optx=pos['x'], opty=pos['y'])
        pdown = colisores(tcbx-3, pos['h'] + tm-13, pos['w'] - tcbl+6, tm, optx=pos['x'], opty=pos['y'])
        pleft = colisores(-5, tml-10, tm, pos['h'] - tmh+14, optx=pos['x'], opty=pos['y'])
        pright = colisores(pos['w'] + tm-15, tml-10, tm, pos['h'] - tmh+14, optx=pos['x'], opty=pos['y'])

        if ctrl['up'] and not pup.collidelistall(objcs) and not self.player.y <= 3:
            pos['y'] -= ctrl['speed']
        elif ctrl['down'] and not pdown.collidelistall(objcs) and not self.player.y >= 1947:
            pos['y'] += ctrl['speed']
        if ctrl['left'] and not pleft.collidelistall(objcs) and not self.player.x <= 3:
            pos['x'] -= ctrl['speed']
        elif ctrl['right'] and not pright.collidelistall(objcs) and not self.player.x >= 1917:
            pos['x'] += ctrl['speed']

    def pos(self, opt):
        if opt == 'x':
            return self.player.x
        else:
            return self.player.y


epos = {'w': 30,
        'h': 50,
        'left': True,
        'right': False
        }

epx = []
epy = []
dis = 10000
esps = []

zcont = 0
enemies = []


class Enemy:
    def __init__(self, objcs, i):
        global epos, zcont
        self.i = i
        try:
            fakeX = epx[i]
            fakeY = epy[i]
        except:
            epx.append(random.randint(0, 1000))
            epy.append(random.randint(0, 1000))
        if dev_mode:
            self.enemy = pyg.draw.rect(screen, cor["cinza"], (epx[i]-scroll[0], epy[i]-scroll[1], 30, 50))
            try:
                a = enemies[i]
            except:
                enemies.append(self.enemy)
        else:
            self.enemy = pyg.Rect(epx[i]-scroll[0], epy[i]-scroll[1], 30, 50)
            try:
                a = enemies[i]
            except:
                enemies.append(self.enemy)
            if epos['left']:
                if zcont < 40:
                    screen.blit(allAnims['z_walkL0'], (epx[i]-scroll[0], epy[i]-scroll[1]))
                    zcont += 1
                elif zcont < 80:
                    screen.blit(allAnims['z_walkL1'], (epx[i] - scroll[0], epy[i] - scroll[1]))
                    zcont += 1
                else:
                    zcont = 0
            elif epos['right']:
                if zcont < 40:
                    screen.blit(allAnims['z_walkR0'], (epx[i]-scroll[0], epy[i]-scroll[1]))
                    zcont += 1
                elif zcont < 80:
                    screen.blit(allAnims['z_walkR1'], (epx[i] - scroll[0], epy[i] - scroll[1]))
                    zcont += 1
                else:
                    zcont = 0
        self.eup = colisores(tcbx - 3, tcby, epos['w'] - tcbl + 6, tm, optx=epx[i], opty=epy[i])
        self.edown = colisores(tcbx - 3, epos['h'] + tm - 13, epos['w'] - tcbl + 6, tm, optx=epx[i], opty=epy[i])
        self.eleft = colisores(-5, tml - 10, tm, epos['h'] - tmh + 14, optx=epx[i], opty=epy[i])
        self.eright = colisores(epos['w'] + tm - 15, tml - 10, tm, epos['h'] - tmh + 14, optx=epx[i], opty=epy[i])
        try:
            fakeESP = esps[i]
        except:
            esps.append(random.randint(2, 6))
        if pos['y'] + dis > epy[i] > pos['y'] and not self.eup.collidelistall(objcs) and not epy[i] <= 3:
            epy[i] -= esps[i]
            epos['left'] = True
            epos['right'] = False
        elif pos['y'] - dis < epy[i] < pos['y'] and not self.edown.collidelistall(objcs) and not epy[i] >= 1947:
            epy[i] += esps[i]
            epos['right'] = True
            epos['left'] = False
        if pos['x'] + dis > epx[i] > pos['x'] and not self.eleft.collidelistall(objcs) and not epx[i] <= 3:
            epx[i] -= esps[i]
            epos['left'] = True
            epos['right'] = False
        elif pos['x'] - dis < epx[i] < pos['x'] and not self.eright.collidelistall(objcs) and not epx[i] >= 1917:
            epx[i] += esps[i]
            epos['right'] = True
            epos['left'] = False

    def eposs(self, opt):
        if opt == 'x':
            return epx[self.i]
        else:
            return epy[self.i]


def update():
    global display, screen, walk, blpos
    clock.tick(FPS)

    for event in pyg.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pyg.quit()
            exit()

        controls(event)

    if ctrl['up'] \
            or ctrl['down'] \
            or ctrl['left'] \
            or ctrl['right']:
        walk = True
    else:
        walk = False

    if not walk:
        slice(anim, 'primeiro')
    elif walk:
        slice(anim, 'walk')


ob = [0, 0]
wmax = 1950


def render():
    global scroll, btn1, mr_ver, ob, bclick, mpos
    screen.fill(cor["preto"])

    flatmap()
    mouse = pyg.mouse.get_pos()
    mr = pyg.Rect(mouse[0] + scroll[0], mouse[1] + scroll[1], 20, 20)
    objo = pisaveis
    for obj in objo:
        if obj.colliderect(mr)\
                and obj.x < wmax:
            screen.blit(seletor, (obj.x - scroll[0], obj.y - scroll[1]))
            break
        elif obj.x >= wmax:
            break

    p1 = Players(objs)
    if hr['noite']:
        for e in range(0, 10):
            Enemy(objs, e)

    if bclick:
        b = Bullet(enemies)
        if b.getrect().collidelistall(objs):
            bclick = False
        else:
            b.atira()

    if 1250 > p1.pos('x') > 698:
        true_scroll[0] += (p1.pos('x') - true_scroll[0] - (SURF_SIZE[0]/2 + 15))
    if 1626 > p1.pos('y') > 406:
        true_scroll[1] += (p1.pos('y') - true_scroll[1] - (SURF_SIZE[1]/2 + 25))

    screen.blit(icons['dev_bar'], (5, SURF_SIZE[1] - 115))
    str_scr(f"mx: {mouse[0]}  my: {mouse[1]}", cor['branco'], (10, SURF_SIZE[1] - 105))
    str_scr(f"px: {p1.pos('x')}  py: {p1.pos('y')}", cor['branco'], (10, SURF_SIZE[1] - 85))
    str_scr(f'cx: {true_scroll[0]}  cy: {true_scroll[1]}', cor['branco'], (10, SURF_SIZE[1] - 65))
    str_scr(f"FPS: {clock.get_fps():.1f}", cor['branco'], (10, SURF_SIZE[1] - 45))

    scroll = true_scroll.copy()

    btn_exit = Botao(cor['vermelho'], [SURF_SIZE[0] - 45, 10, 30, 30], 'X', mouse)
    btn_exit.draw()
    if btn_exit.is_clicked():
        pyg.quit()
        exit()

    screen.blit(pyg.transform.scale(mouses, (20, 20)), mouse)


while True:
    update()
    render()

    display.blit(pyg.transform.scale(screen, SURF_SIZE), (0, 0))
    pyg.display.update()
