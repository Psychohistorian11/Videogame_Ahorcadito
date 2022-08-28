import pygame
import sys
from pygame.locals import *

pygame.init()
# Implementación de la pantalla

W, H = 1920, 1464
PANTALLA = pygame.display.set_mode((W, H))
FPS = 60
RELOJ = pygame.time.Clock()

pygame.display.set_caption("Ahorcadito")

# icono del juego
icono = pygame.image.load("Imagenes/img.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("Imagenes/fondo1.jpg").convert()
x = 0
y = 0
PANTALLA.blit(fondo, (x, y))
image_sprite = [pygame.image.load("Imagenes/skins/skin1/Skin1paso1.png"),
             pygame.image.load("Imagenes/skins/skin1/Skin1paso2.png"),
             pygame.image.load("Imagenes/skins/skin1/Skin1paso3.png"),
             pygame.image.load("Imagenes/skins/skin1/Skin1paso4.png"),
             pygame.image.load("Imagenes/skins/skin1/Skin1paso5.png"),
             pygame.image.load("Imagenes/skins/skin1/Skin1paso6.png"),
             pygame.image.load("Imagenes/skins/skin1/Skin1paso7.png"),
             pygame.image.load("Imagenes/skins/skin1/Skin1paso8.png")]

image_sprite2 = [pygame.image.load("Imagenes/skins/skin2/Skin2paso1.png"),
                pygame.image.load("Imagenes/skins/skin2/Skin2paso2.png"),
                pygame.image.load("Imagenes/skins/skin2/Skin2paso3.png"),
                pygame.image.load("Imagenes/skins/skin2/Skin2paso4.png"),
                pygame.image.load("Imagenes/skins/skin2/Skin2paso5.png"),
                pygame.image.load("Imagenes/skins/skin2/Skin2paso6.png"),
                pygame.image.load("Imagenes/skins/skin2/Skin2paso7.png"),
                pygame.image.load("Imagenes/skins/skin2/Skin2paso8.png")]

clock = pygame.time.Clock()

value = 0
value2 = 0

run = True

class pantalla:
   while run:
        if value >= len(image_sprite):
          value = 0

        image = image_sprite[value]

        x = 100

        if value == 0:
          y = 500
        else:
          y = 500

        PANTALLA.blit(image, (x, y))

        pygame.display.update()

        PANTALLA.fill((0, 0, 0))

        value += 1
        fondo = pygame.image.load("Imagenes/fondo1.jpg").convert()
        x = 0
        y = 0
        PANTALLA.blit(fondo, (x, y))



        clock.tick(8)

        if value2 >= len(image_sprite2):
                value2 = 0

        image2 = image_sprite2[value2]

        x = 1250

        if value == 0:
            y = 500
        else:
            y = 500

        PANTALLA.blit(image2, (x, y))

        pygame.display.update()

        value2 += 1













































