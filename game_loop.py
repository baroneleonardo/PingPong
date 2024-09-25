import pygame
import random
from utils import draw_text, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BLACK, COLOR_WHITE


def reset_ball(ball_rect):
    ball_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    return ball_accel_x, ball_accel_y

def game_loop(screen, mode, difficulty, music_on, sound_effects_on):

    pygame.init()
    paddle_hit_sound = pygame.mixer.Sound('sounds/paddle_hit.wav')
    score_sound = pygame.mixer.Sound('sounds/score.wav')
    # set the window's title
    pygame.display.set_caption('Pong')

    # create the clock object to keep track of the time
    clock = pygame.time.Clock()

    started = False
    
    # paddles
    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)
    paddle_1_move = 0
    paddle_2_move = 0

    # ball
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
    ball_accel_x, ball_accel_y = reset_ball(ball_rect)

    # difficulty-based ball speed scaling
    if difficulty == "Easy":
        speed_multiplier = 0.8
    elif difficulty == "Medium":
        speed_multiplier = 1.0
    elif difficulty == "Hard":
        speed_multiplier = 1.5

    # scores
    score_1 = 0
    score_2 = 0

    # GAME LOOP
    while True:
        screen.fill(COLOR_BLACK)

        if not started:
            font = pygame.font.SysFont('Consolas', 30)
            draw_text(screen, 'Press Space to Start', font, COLOR_WHITE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
            continue

        delta_time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5
                if mode == "2 Players":
                    if event.key == pygame.K_UP:
                        paddle_2_move = -0.5
                    if event.key == pygame.K_DOWN:
                        paddle_2_move = 0.5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1_move = 0.0
                if mode == "2 Players":
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        paddle_2_move = 0.0

        # Move paddles
        paddle_1_rect.top += paddle_1_move * delta_time
        if mode == "2 Players":
            paddle_2_rect.top += paddle_2_move * delta_time

        # AI movement for single player mode
        if mode == "1 Player vs AI":
            if ball_rect.centery > paddle_2_rect.centery:
                paddle_2_rect.centery += 0.4 * delta_time
            elif ball_rect.centery < paddle_2_rect.centery:
                paddle_2_rect.centery -= 0.4 * delta_time

        # Limit paddle movement
        if paddle_1_rect.top < 0:
            paddle_1_rect.top = 0
        if paddle_1_rect.bottom > SCREEN_HEIGHT:
            paddle_1_rect.bottom = SCREEN_HEIGHT

        if paddle_2_rect.top < 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom > SCREEN_HEIGHT:
            paddle_2_rect.bottom = SCREEN_HEIGHT

        # Ball movement
        ball_rect.left += ball_accel_x * delta_time * speed_multiplier
        ball_rect.top += ball_accel_y * delta_time * speed_multiplier

        # Ball collision with top/bottom
        if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
            ball_accel_y *= -1

        # Ball goes off screen
        if ball_rect.left <= 0:
            score_2 += 1
            ball_accel_x, ball_accel_y = reset_ball(ball_rect)
            started = False
            if sound_effects_on:
                score_sound.play()

        if ball_rect.right >= SCREEN_WIDTH:
            score_1 += 1
            ball_accel_x, ball_accel_y = reset_ball(ball_rect)
            started = False
            if sound_effects_on:
                score_sound.play()

        # Paddle collision
        if paddle_1_rect.colliderect(ball_rect) and ball_rect.left < paddle_1_rect.right:
            ball_accel_x *= -1
            ball_rect.left += 5
            if sound_effects_on:
                paddle_hit_sound.play()

        if paddle_2_rect.colliderect(ball_rect) and ball_rect.right > paddle_2_rect.left:
            ball_accel_x *= -1
            ball_rect.right -= 5
            if sound_effects_on:
                paddle_hit_sound.play()

        # Draw paddles and ball
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        # Display score
        font = pygame.font.SysFont('Consolas', 30)
        score_text = font.render(f"{score_1} - {score_2}", True, COLOR_WHITE)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 50))

        pygame.display.update()

