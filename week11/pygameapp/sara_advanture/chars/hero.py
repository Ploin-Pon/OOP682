import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    def __init__(self, name, filename, x, y, rows=2, cols=3, width=34, height=56):
        super().__init__()
        self.name = name
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.rows = rows
        self.cols = cols
        self.rect = pygame.Rect(x, y, width, height)
        self.row = 0
        self.col = 0
        self.image = self.get_frame()

    def get_frame(self):
        return self.sheet.subsurface(
            self.col * self.rect.width, 
            self.row * self.rect.height, 
            self.rect.width, self.rect.height)

    def update(self, elapsed_time=100):
        if elapsed_time > 300: # This condition might need tweaking based on how it's called
            self.col = (self.col + 1) % self.cols
            if self.col == 0:
                self.row = (self.row + 1) % self.rows
        self.image = self.get_frame()

    def draw(self, surface):
        surface.blit(self.image, self.rect)