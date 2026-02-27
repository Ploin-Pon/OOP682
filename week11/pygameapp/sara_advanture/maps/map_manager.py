import pygame

class MapManager:
    """Manages multiple layers for a single map.
    Handles updating and drawing all layers in order.
    """
    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def update(self):
        for layer in self.layers:
            if hasattr(layer, 'update'):
                layer.update()

    def draw(self, surface: pygame.Surface):
        for layer in self.layers:
            layer.draw(surface)
