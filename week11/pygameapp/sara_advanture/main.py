import sys, os
import pygame
from sara import Sara # นำเข้าคลาส Sara

class SaraAdventure(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.caption = 'Sara Adventure'
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        pygame.display.set_caption(self.caption)

        # สร้างกลุ่ม Sprite และตัวละคร
        self.all_sprites = pygame.sprite.Group()
        self.hero = Sara((100, self.screen_height - 100)) # สร้าง Sara และกำหนดตำแหน่งเริ่มต้น
        self.all_sprites.add(self.hero)

        # โหลดเสียง (ต้องมีไฟล์ wave_sound.wav ในโฟลเดอร์)
        self.wave_sound = None
        try:
            sound_path = os.path.join(os.path.dirname(__file__), 'wave_sound.wav')
            self.wave_sound = pygame.mixer.Sound(sound_path)
        except pygame.error as e:
            print(f"Cannot load sound: {sound_path} - {e}")
    
    def handle_close(self):
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.wave_sound:
                        self.wave_sound.play()

    def draw_text(self , text ,position ,color=(0,0,0)):
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, position)
    def start(self):
        while True:
            # 1. จัดการ Event
            self.handle_events()

            # 2. อัปเดตสถานะเกม
            self.all_sprites.update()

    def start(self):
        while True:
            self.handle_close()
            # 3. วาดทุกอย่างลงบนหน้าจอ
            self.screen.fill((255,255,255))
            self.draw_text('Sara Adventure', (100,100))
            self.hero.
            self.all_sprites.draw(self.screen) # วาด Sprite ทั้งหมดในกลุ่ม

            # 4. อัปเดตหน้าจอ
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()


if __name__ == '__main__':
    game = SaraAdventure()
    game.start()


    