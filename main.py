import pygame
import pygame_gui
import time

# Initialization of pygame and the game window
pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clicker Game")
ui_manager = pygame_gui.UIManager((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


# Initialization of objects and widgets
button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((screen_width/2-50, screen_height/2-25), (100, 50)),
    text="Click Me!",
    manager=ui_manager
)

click_count = 0
font = pygame.font.Font(None, 36)
start_time = time.time()
best_score = 0

while running:
    time_delta = clock.tick(60) / 1000.0
    elapsed_time = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        ui_manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                click_count += 1

    if elapsed_time >= 10:
        best_score = max(best_score, click_count)
        click_count = 0
        start_time = time.time()

    # Rendering, screen update
    screen.fill((218, 247, 166))

    click_count_text = font.render(f"Clicks number: {click_count}", True, (199, 0, 57))
    timer_text = font.render(f"Time: {10 - int(elapsed_time)}s", True, (199, 0, 57))
    best_score_text = font.render(f"Best: {best_score}", True, (199, 0, 57))

    screen.blit(click_count_text, (screen_width/2 - click_count_text.get_width()/2, screen_height/2 - 75))
    screen.blit(timer_text, (10, screen_height - 40))
    screen.blit(best_score_text, (screen_width - best_score_text.get_width() - 10, 10))

    ui_manager.update(time_delta)
    ui_manager.draw_ui(screen)

    pygame.display.flip()
pygame.quit()