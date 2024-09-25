import pygame
import random

from utils import draw_text, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BLACK, COLOR_WHITE
from menus import main_menu, options_menu, difficulty_selection
from game_loop import game_loop




if __name__ == '__main__':
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    music_on = True
    sound_effect_on = True
    while True:
        choice, mode = main_menu(screen)
        if choice == "play" and mode:
            difficulty = difficulty_selection(screen)
            if difficulty:
                game_loop(screen, mode, difficulty, music_on, sound_effect_on)
        elif choice == "options":
            music_on, sound_effect_on = options_menu(screen)
        else:
            break

