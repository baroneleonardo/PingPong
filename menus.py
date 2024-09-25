import pygame
from utils import draw_text, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BLACK, COLOR_WHITE


def main_menu(screen):
    pygame.init()
    font = pygame.font.SysFont('Consolas', 40)
    menu_options = ["Play", "Options", "Exit"]
    selected_option = 0
    music_on = True
    sound_effects_on = True
    
    while True:
        screen.fill(COLOR_BLACK)
        
        # Display the title
        draw_text(screen, "Pong Menu", font, COLOR_WHITE, (SCREEN_WIDTH // 2, 100))

        # Display menu options
        for index, option in enumerate(menu_options):
            color = COLOR_WHITE if index == selected_option else (100, 100, 100)
            draw_text(screen, option, font, color, (SCREEN_WIDTH // 2, 250 + index * 80))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None, None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if selected_option == 0:  # Play
                        return "play", game_mode_selection(screen)
                    elif selected_option == 1:  # Options
                        music_on, sound_effects_on = options_menu(screen)
                        return "options", None
                    elif selected_option == 2:  # Exit
                        pygame.quit()
                        return None, None

def game_mode_selection(screen):
    font = pygame.font.SysFont('Consolas', 40)
    game_modes = ["1 Player vs AI", "2 Players"]
    selected_mode = 0
    
    while True:
        screen.fill(COLOR_BLACK)
        
        # Display title
        draw_text(screen, "Select Game Mode", font, COLOR_WHITE, (SCREEN_WIDTH // 2, 100))

        # Display game mode options
        for index, mode in enumerate(game_modes):
            color = COLOR_WHITE if index == selected_mode else (100, 100, 100)
            draw_text(screen, mode, font, color, (SCREEN_WIDTH // 2, 250 + index * 80))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_mode = (selected_mode - 1) % len(game_modes)
                elif event.key == pygame.K_DOWN:
                    selected_mode = (selected_mode + 1) % len(game_modes)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return game_modes[selected_mode]
                
def options_menu(screen):
    font = pygame.font.SysFont('Consolas', 40)
    options = ["Toggle Music", "Toggle Sound Effects", "Back"]
    selected_option = 0
    music_on = True
    sound_effects_on = True

    while True:
        screen.fill(COLOR_BLACK)
        
        # Display title
        draw_text(screen, "Options", font, COLOR_WHITE, (SCREEN_WIDTH // 2, 100))

        # Display options menu
        for index, option in enumerate(options):
            color = COLOR_WHITE if index == selected_option else (100, 100, 100)
            draw_text(screen, option, font, color, (SCREEN_WIDTH // 2, 250 + index * 80))
        
        # Show current status for music and sound effects
        draw_text(screen, f"Music: {'On' if music_on else 'Off'}", font, COLOR_WHITE, (SCREEN_WIDTH // 2, 500))
        draw_text(screen, f"Sound Effects: {'On' if sound_effects_on else 'Off'}", font, COLOR_WHITE, (SCREEN_WIDTH // 2, 550))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if selected_option == 0:  # Toggle Music
                        if music_on:
                            music_on = False
                            pygame.mixer.music.stop()
                        else:
                            music_on = True
                            pygame.mixer.music.play(-1) 

                    elif selected_option == 1: 
                        if sound_effects_on:
                            sound_effects_on = False
                        else:
                            sound_effects_on = True

                    elif selected_option == 2:  # Back
                        return music_on, sound_effects_on


def difficulty_selection(screen):
    font = pygame.font.SysFont('Consolas', 40)
    difficulties = ["Easy", "Medium", "Hard"]
    selected_difficulty = 0
    
    while True:
        screen.fill(COLOR_BLACK)
        
        # Display title
        draw_text(screen, "Select Difficulty", font, COLOR_WHITE, (SCREEN_WIDTH // 2, 100))

        # Display difficulty options
        for index, difficulty in enumerate(difficulties):
            color = COLOR_WHITE if index == selected_difficulty else (100, 100, 100)
            draw_text(screen, difficulty, font, color, (SCREEN_WIDTH // 2, 250 + index * 80))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_difficulty = (selected_difficulty - 1) % len(difficulties)
                elif event.key == pygame.K_DOWN:
                    selected_difficulty = (selected_difficulty + 1) % len(difficulties)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return difficulties[selected_difficulty]