import pygame
from .layer import MapLayer

class GrassLayer(MapLayer):
    """เลเยอร์พื้นหญ้าหรือพื้นหลังหลัก
    """
    def __init__(self, tileset_path: str, map_grid, tile_width: int = 40, tile_height: int = 40):
        super().__init__(tileset_path, tile_width, tile_height)
        self.map_grid = map_grid

    def draw(self, surface: pygame.Surface):
        super().draw(surface, self.map_grid)
