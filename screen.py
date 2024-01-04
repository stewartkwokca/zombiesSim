import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
LIGHT_GRAY = (211, 211, 211)

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

def screenSetup():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill(BLACK)

    pygame.display.set_caption('Zombie Infection Sim')
    pygame.display.flip()

    return screen

def renderText(text, font, text_col, x, y, window):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

