
import pygame, sys
from ejemploComplement import Button



pygame.init()

SCREEN = pygame.display.set_mode((1920, 1464))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Imagenes/fondo2.jpg")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Imagenes/font.ttf", size)





def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()



        SCREEN.fill("black")

        PLAY_BACK = Button(image=None, pos=(400, 1000),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        PLAY_CONTINUE = Button(image=None, pos=(510, 900),
                           text_input="CONTINUE", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_CONTINUE.changeColor(PLAY_MOUSE_POS)
        PLAY_CONTINUE.update(SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

                if PLAY_CONTINUE.checkForInput(PLAY_MOUSE_POS):
                    from Pantalladejuego import pantalla
                    pantalla()






        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 400))

        PLAY_BUTTON = Button(image=pygame.image.load("Imagenes/Play Rect.png"), pos=(433, 550),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Imagenes/Options Rect.png"), pos=(540, 750),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Imagenes/Quit Rect.png"), pos=(420, 950),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
