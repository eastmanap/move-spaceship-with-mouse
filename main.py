import pygame
import sys
import colors
import config  # Import the config module
import math

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    player_image = pygame.image.load('player.png').convert_alpha()
    background_image = pygame.image.load('saturn_family1.jpg').convert()
    
    player_x, player_y = config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2
    last_angle = 0  # Store last rotation angle
    
    running = True
    while running:
        running = handle_events()
        screen.fill(colors.WHITE)
        screen.blit(background_image, [0, 0])
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx, dy = mouse_x - player_x, player_y - mouse_y  # Invert dy to correct rotation
        
        if dx != 0 or dy != 0:
            last_angle = math.degrees(math.atan2(dy, dx)) - 90  # Adjust rotation to face upward as front
        rotated_player = pygame.transform.rotate(player_image, last_angle)
        
        player_x, player_y = mouse_x, mouse_y
        screen.blit(rotated_player, (player_x - rotated_player.get_width() // 2, player_y - rotated_player.get_height() // 2))
        
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()