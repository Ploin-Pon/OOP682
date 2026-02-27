import pygame
from utils.img_utils import make_smart_transparent

class MapLayer:
    """Base class for a map layer.
    Handles loading a tileset image and drawing tiles on a surface.
    Subclasses must implement `load_tiles` and `draw`.
    """
    def __init__(self, tileset_path: str, tile_width: int = 40, tile_height: int = 40):
        raw_tileset = pygame.image.load(tileset_path).convert_alpha()
        # ใช้ Smart Transparency เพื่อลบกล่องขาวที่ขอบของตกแต่ง
        self.tileset = make_smart_transparent(raw_tileset)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tiles = []  # list of subsurface tiles
        self.load_tiles()

    def load_tiles(self):
        # Split the tileset into individual tiles assuming a grid layout.
        sheet_width, sheet_height = self.tileset.get_size()
        cols = sheet_width // 32
        rows = sheet_height // 32
        for row in range(rows):
            for col in range(cols):
                rect = pygame.Rect(col * 32, row * 32, 32, 32)
                tile_surf = self.tileset.subsurface(rect)
                # Scale the tile to the target size (e.g., 40x40)
                scaled_tile = pygame.transform.scale(tile_surf, (self.tile_width, self.tile_height))
                self.tiles.append(scaled_tile)

    def draw(self, surface: pygame.Surface, map_grid):
        """Draw the layer.
        `map_grid` is a 2‑D list of tile indices.
        """
        for y, row in enumerate(map_grid):
            for x, tile_idx in enumerate(row):
                if tile_idx is None:
                    continue
                tile_image = self.tiles[tile_idx]
                surface.blit(tile_image, (x * self.tile_width, y * self.tile_height))
