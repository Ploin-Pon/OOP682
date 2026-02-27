import sys, os
import pygame
from sara import Sara 
from maps import MapManager, GrassLayer, PathLayer, ItemLayer
from maps.map_data import (
    MAP1_GRASS, MAP1_DECOR, MAP1_PLAYER_START, MAP1_TROPHY_POS,
    MAP2_GRASS, MAP2_PATH, MAP2_PLAYER_START, MAP2_TROPHY_POS
)
from chars.trophy import Trophy

class SaraAdventure(object):
    def __init__(self):
        pygame.init()
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Mixer init failed: {e}")

        self.screen_width = 1000
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.caption = 'Sara Adventure'
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('leelawadeeui', 24)
        self.big_font = pygame.font.SysFont('leelawadeeui', 48)
        pygame.display.set_caption(self.caption)

        # Map setup
        self.map1 = self._init_map1()
        self.map2 = self._init_map2()
        self.current_map = self.map1 # เริ่มที่แมพป่า (Forest)
        
        # Sprite Groups
        self.all_sprites = pygame.sprite.Group()
        self.hero = Sara(MAP1_PLAYER_START)
        self.trophy = self.map1_trophy # เริ่มด้วยถ้วยแมพ 1
        self.all_sprites.add(self.hero)
        
        # Game state
        self.win = False

        # Sound setup
        self.wave_sound = None
        try:
            sound_path = os.path.join(os.path.dirname(__file__), 'wave_sound.wav')
            if os.path.exists(sound_path):
                self.wave_sound = pygame.mixer.Sound(sound_path)
        except pygame.error as e:
            print(f"Cannot load sound: {e}")

    def _init_map1(self):
        m = MapManager()
        # แผนที่ป่า 
        grass = GrassLayer('map-img/forest_tileset.png', MAP1_GRASS)
        m.add_layer(grass)
        
        decor = PathLayer('map-img/forest_tileset.png', MAP1_DECOR)
        m.add_layer(decor)
        
        items = ItemLayer()
        self.map1_trophy = Trophy(MAP1_TROPHY_POS)
        items.add_item(self.map1_trophy)
        m.add_layer(items)
        return m

    def _init_map2(self):
        m = MapManager()
        # แผนที่อวกาศ
        grass = GrassLayer('map-img/space_tileset.png', MAP2_GRASS)
        m.add_layer(grass)
        
        path = PathLayer('map-img/space_tileset.png', MAP2_PATH)
        m.add_layer(path)
        
        items = ItemLayer()
        self.map2_trophy = Trophy(MAP2_TROPHY_POS)
        items.add_item(self.map2_trophy)
        m.add_layer(items)
        return m

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not self.win:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.wave_sound:
                            self.wave_sound.play()

    def update(self, dt):
        if self.win:
            return

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        speed = 5
        if keys[pygame.K_LEFT]: dx = -speed
        if keys[pygame.K_RIGHT]: dx = speed
        if keys[pygame.K_UP]: dy = -speed
        if keys[pygame.K_DOWN]: dy = speed
        
        self.hero.move(dx, dy, self.screen_width, self.screen_height)
        self.hero.update(dt)
        
        # Check collision with trophy
        if pygame.sprite.collide_rect(self.hero, self.trophy):
            if self.current_map == self.map1:
                # วาร์ปไปแมพอวกาศ (Space)
                self.current_map = self.map2
                self.hero.rect.center = MAP2_PLAYER_START
                self.trophy = self.map2_trophy # เปลี่ยนตัวเช็คเป็นถ้วยในแมพ 2
            else:
                # ชนะในแมพอวกาศ
                self.win = True

    def draw_text(self, text, position, color=(255, 255, 0), big=False):
        surf = self.big_font if big else self.font
        surface = surf.render(text, True, color)
        rect = surface.get_rect(center=position) if big else surface.get_rect(topleft=position)
        self.screen.blit(surface, rect)

    def start(self):
        while True:
            dt = self.clock.tick(60) # Get delta time in ms
            self.handle_events()
            self.update(dt)

            # Drawing
            self.screen.fill((0, 0, 0))
            
            # Draw Map
            self.current_map.draw(self.screen)
            
            # Draw Sprites
            self.all_sprites.draw(self.screen)

            if self.win:
                self.draw_text('ยินดีด้วย! คุณเก็บถ้วยรางวัลสำเร็จ', (400, 300), color=(0, 255, 0), big=True)

            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = SaraAdventure()
    game.start()