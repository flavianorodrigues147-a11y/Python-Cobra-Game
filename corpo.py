# jogo da cobrinha em python usando pygame

# Para poder aparecer a janela do jogo é necessário instalar o pygame e estabelecer o ambiente virtual

import pygame
from pygame.locals import *
import random

WINDOW_WIDTH = 600  # largura da janela
WINDOW_HEIGHT = 600  # altura da janela
POS_INCIAL_X = WINDOW_WIDTH / 2  # posição inicial x da cobra
POS_INCIAL_Y = WINDOW_HEIGHT / 2  # posição inicial y da cobra
BLOCK = 10  # tamanho do pixel da cobra
direcao = K_RIGHT  # direção inicial da cobra


def verificar_margens(pos):
    if 0 <= pos[0] < WINDOW_WIDTH and 0 <= pos[1] < WINDOW_HEIGHT:
        return False
    else:
        return True


def gera_pos_aleatoria():
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    return x // BLOCK * BLOCK, y // BLOCK * BLOCK


def game_over():
    pygame.quit()
    quit()


def colisao_cobra_maca(cobra_pos, maca_pos):
    if cobra_pos[0] == maca_pos:
        return True
    return False


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

cobra_pos = [(POS_INCIAL_X, POS_INCIAL_Y), (POS_INCIAL_X + BLOCK,
                                            POS_INCIAL_Y), (POS_INCIAL_X + 2 * BLOCK, POS_INCIAL_Y)]
cobra_surface = pygame.Surface((BLOCK, BLOCK))  # cria a superfície da cobra
cobra_surface.fill((53, 59, 72))  # define a cor da cobra

maca_surface = pygame.Surface((BLOCK, BLOCK))
maca_surface.fill((255, 0, 0))
maca_pos = gera_pos_aleatoria()


while True:
    pygame.time.Clock().tick(10)
    # aqui definimos a cor de fundo que é verde por conta dos condigos RGB
    window.fill((68, 189, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_RIGHT, K_LEFT, K_DOWN, K_UP]:
                direcao = event.key

    window.blit(maca_surface, maca_pos)

    for item in range(len(cobra_pos) - 1, 0, -1):
        cobra_pos[item] = cobra_pos[item - 1]

    if colisao_cobra_maca(cobra_pos, maca_pos):
        cobra_pos.append((-1, -1))
        maca_pos = gera_pos_aleatoria()

    for pos in cobra_pos:
        window.blit(cobra_surface, pos)  # desenha a cobra na janela

    if verificar_margens(cobra_pos[0]):
        game_over()

    if direcao == K_RIGHT:
        cobra_pos[0] = (cobra_pos[0][0] + BLOCK, cobra_pos[0]
                        [1])  # move a cobra para a direita

    elif direcao == K_LEFT:
        cobra_pos[0] = (cobra_pos[0][0] - BLOCK, cobra_pos[0]
                        [1])  # move a cobra para a esquerda

    elif direcao == K_DOWN:
        cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] +
                        BLOCK)  # move a cobra para baixo

    elif direcao == K_UP:
        cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] -
                        BLOCK)  # move a cobra para cima

    pygame.display.update()
