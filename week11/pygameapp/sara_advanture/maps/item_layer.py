import pygame

class ItemLayer:
    """Layer for items (sprites) on the map.
    Manages a group of sprites that can be interacted with.
    """
    def __init__(self):
        self.items = pygame.sprite.Group()

    def add_item(self, item_sprite):
        self.items.add(item_sprite)

    def update(self):
        self.items.update()

    def draw(self, surface: pygame.Surface):
        self.items.draw(surface)
