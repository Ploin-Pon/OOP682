import pygame
from pygame.sprite import Sprite
from utils.img_utils import make_smart_transparent

class Hero(Sprite):
    def __init__(self, name, filename, x, y, rows=4, cols=3, width=160, height=160):
        super().__init__()
        self.name = name
        # Fix: ใช้ Smart Transparency เพื่อล้างขาวที่เป็น Noise ออกให้หมด
        raw_sheet = pygame.image.load(filename).convert_alpha()
        self.sheet = make_smart_transparent(raw_sheet)
        
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, 50, 50) # ขนาดที่จะแสดงผลในเกม (ย่อลงมา)
        self.row = 0
        self.col = 0
        self.image = self.get_frame()
        self.animation_timer = 0
        self.frame_duration = 100 # ms
        self.is_moving = False

    def get_frame(self):
        # ดึงภาพดิบจาก Spritesheet
        raw_frame = self.sheet.subsurface(
            self.col * self.width, 
            self.row * self.height, 
            self.width, self.height)
        # ย่อขนาดให้เหมาะสมกับช่อง 40x40 (แต่ตัวละครอาจะสูงกว่าช่องนิดหน่อยเพื่อให้สวย)
        return pygame.transform.scale(raw_frame, (50, 50))

    def move(self, dx, dy, screen_width, screen_height):
        if dx != 0 or dy != 0:
            self.is_moving = True
            self.rect.x += dx
            self.rect.y += dy
            
            # Keep within screen boundaries
            if self.rect.left < 0: self.rect.left = 0
            if self.rect.right > screen_width: self.rect.right = screen_width
            if self.rect.top < 0: self.rect.top = 0
            if self.rect.bottom > screen_height: self.rect.bottom = screen_height
            
            # Simple directional row mapping
            # Row 0: Down, Row 1: Up, Row 2: Right, Row 3: Left
            if dy > 0:
                self.row = 0
            elif dy < 0:
                self.row = 1
            elif dx > 0:
                self.row = 2
            elif dx < 0:
                self.row = 3
        else:
            self.is_moving = False

    def update(self, dt):
        # Handle animation
        if self.is_moving:
            self.animation_timer += dt
            if self.animation_timer >= self.frame_duration:
                self.animation_timer = 0
                self.col = (self.col + 1) % self.cols
        else:
            # Optionally reset to first frame when idle
            self.col = 0
            self.animation_timer = 0
            
        self.image = self.get_frame()

    def draw(self, surface):
        surface.blit(self.image, self.rect)