import pygame
import sys
import os

def run_helper(tileset_path):
    pygame.init()
    tile_size = 32
    
    try:
        tileset = pygame.image.load(tileset_path).convert_alpha()
    except:
        print(f"Cannot load {tileset_path}")
        return

    tw, th = tileset.get_size()
    cols = tw // tile_size
    rows = th // tile_size
    
    # Create a large enough screen
    screen = pygame.display.set_mode((tw + 100, th + 100))
    pygame.display.set_caption(f"Tileset Helper: {os.path.basename(tileset_path)}")
    font = pygame.font.SysFont('tahoma', 12)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill((50, 50, 50))
        screen.blit(tileset, (10, 10))
        
        # Draw grid and IDs
        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                x = 10 + c * tile_size
                y = 10 + r * tile_size
                pygame.draw.rect(screen, (255, 255, 255), (x, y, tile_size, tile_size), 1)
                
                # Draw ID text
                txt = font.render(str(idx), True, (255, 255, 0))
                screen.blit(txt, (x + 2, y + 2))
                
        pygame.display.update()

if __name__ == "__main__":
    # Default to space tileset as requested for map 2
    path = r'c:\Users\SciLab\Downloads\OOP682\week11\pygameapp\sara_advanture\map-img\space_tileset.png'
    print("Opening Tileset Helper... Close the window to exit.")
    run_helper(path)
