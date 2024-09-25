import pygame

# Screen dimensions
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# Colors (RGB)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def draw_text(screen, text, font, color, center):
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=center)
    screen.blit(rendered_text, text_rect)
