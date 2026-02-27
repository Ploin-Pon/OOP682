import pygame

class Trophy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # Load and scale the trophy image
        original_image = pygame.image.load('sara/gold_trophy.png').convert_alpha()
        self.image = pygame.transform.scale(original_image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
