import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(100)
    screen.fill((255,255,255))
    font = pygame.font.SysFont("Arial",36)
    text = font.render(f"{clock.get_fps():.2f} FPS",True,(0,0,0))
    screen.blit(text,(150,130))
    pygame.display.update()

pygame.quit()