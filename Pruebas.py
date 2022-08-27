import pygame, sys
from pygame.locals import *

pygame.init()
#Implementación de la pantalla
PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption("Ahorcadito")

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

Colorcito_asi_bien_ricolino = (12,178,73)

PANTALLA.fill(Colorcito_asi_bien_ricolino)
#Bucle del jeugo: Mantiene el juego abierto
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()