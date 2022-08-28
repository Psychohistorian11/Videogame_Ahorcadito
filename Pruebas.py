import pygame, sys
from pygame.locals import *

pygame.init()
#Implementación de la pantalla
W,H = 1920,1464
PANTALLA = pygame.display.set_mode((W,H))
FPS = 60
RELOJ = pygame.time.Clock()

pygame.displawy.set_caption("Ahorcadito")

#icono del juego
icono = pygame.image.load("Imagenes/img.png")
pygame.display.set_icon(icono)

#fondo del juego
fondo = pygame.image.load("Imagenes/fondo1.jpg").convert()
x = 0


BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

Colorcito_asi_bien_ricolino = (12,178,73)

#PANTALLA.fill(Colorcito_asi_bien_ricolino)

#Rectangulo1 = pygame.draw.rect(PANTALLA,NEGRO,(100,50,100,50))

#pygame.draw.line(PANTALLA,VERDE, (100,104), (199,104), 10)

#pygame.draw.circle(PANTALLA,ROJO, (122,130), 20, 10)

#pygame.draw.ellipse(PANTALLA,BLANCO,(300,200,40,80))


#Bucle del jeugo: Mantiene el juego abierto
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo,(x_relativa,0))
    x -= 1

    pygame.display.update()
    RELOJ.tick(FPS)