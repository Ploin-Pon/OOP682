import os
import pygame
from chars.hero import Hero

class Sara(Hero):
    def __init__(self, position):
        # Sara spritesheet is at c:\Users\SciLab\Downloads\OOP682\week11\pygameapp\sara_advanture\sara\sara_spritesheet.png
        # Base Hero expects: name, filename, x, y, rows=2, cols=3, width=34, height=56
        current_dir = os.path.dirname(__file__)
        spritesheet_path = os.path.join(current_dir, 'sara_spritesheet.png')
        
        super().__init__(
            name="Sara",
            filename=spritesheet_path,
            x=position[0],
            y=position[1],
            rows=4,
            cols=3,
            width=160,
            height=160
        )

    def update(self, elapsed_time=100):
        # Using the base Hero update logic for animation
        super().update(elapsed_time)
