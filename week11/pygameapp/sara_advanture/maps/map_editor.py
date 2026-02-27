import pygame
import sys
import os
from utils.img_utils import make_smart_transparent

# ตั้งค่าหน้าจอและขนาด
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 900
TILE_SIZE = 40
GRID_COLS = 25
GRID_ROWS = 20
MAP_WIDTH = GRID_COLS * TILE_SIZE
MAP_HEIGHT = GRID_ROWS * TILE_SIZE

# สี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
LIGHT_GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 100, 255)

class MapEditor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sara Adventure - Pro Multi-Map Editor")
        self.font = pygame.font.SysFont('leelawadeeui', 16)
        self.big_font = pygame.font.SysFont('leelawadeeui', 24)
        
        # ข้อมูลแมพ 1
        self.map1_tileset_path = r'map-img\forest_tileset.png'
        self.map1_floor = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.map1_decor = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.map1_trophy = (600, 300)
        self.map1_player = (100, 400)
        
        # ข้อมูลแมพ 2
        self.map2_tileset_path = r'map-img\space_tileset.png'
        self.map2_floor = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.map2_decor = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.map2_trophy = (600, 300)
        self.map2_player = (100, 400)

        self.current_map_idx = 1 # 1 หรือ 2
        self.load_map_data()
        
        self.selected_tile_idx = 0
        self.edit_mode = "FLOOR" # "FLOOR", "DECOR", "TROPHY", "SARA"
        self.palette_scroll = 0
        self.palette_cols = 10
        self.show_help = False
        self.is_drawing = False
        self.last_mouse_button = 0
        self.save_msg_timer = 0
        self.load_sara_preview()
        self.running = True

    def load_sara_preview(self):
        try:
            # พยายามโหลดภาพ Sara มาแสดงใน Editor เพื่อความสวยงาม
            path = r'sara\sara_spritesheet.png'
            raw_sheet = pygame.image.load(path).convert_alpha()
            sheet = make_smart_transparent(raw_sheet)
            
            # Slice frame 160x160
            self.sara_img = sheet.subsurface(0, 0, 160, 160)
            self.sara_img = pygame.transform.scale(self.sara_img, (40, 40))
        except:
            self.sara_img = None

    def load_map_data(self):
        """โหลด Tileset และตั้งค่าข้อมูลตาม Map Index ปัจจุบัน"""
        path = self.map1_tileset_path if self.current_map_idx == 1 else self.map2_tileset_path
        try:
            self.tileset = pygame.image.load(path).convert_alpha()
            self.tiles = self.load_tiles()
        except:
            print(f"Error loading tileset: {path}")
            self.tiles = []

    def load_tiles(self):
        tiles = []
        tw, th = self.tileset.get_size()
        cols = tw // TILE_SIZE
        rows = th // TILE_SIZE
        for r in range(rows):
            for c in range(cols):
                rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                tiles.append(self.tileset.subsurface(rect))
        return tiles

    def get_current_grids(self):
        if self.current_map_idx == 1:
            return self.map1_floor, self.map1_decor, self.map1_trophy, self.map1_player
        else:
            return self.map2_floor, self.map2_decor, self.map2_trophy, self.map2_player

    def set_current_grids(self, floor, decor, trophy, player):
        if self.current_map_idx == 1:
            self.map1_floor, self.map1_decor, self.map1_trophy, self.map1_player = floor, decor, trophy, player
        else:
            self.map2_floor, self.map2_decor, self.map2_trophy, self.map2_player = floor, decor, trophy, player

    def draw_grid(self):
        floor, decor, trophy, player = self.get_current_grids()
        
        # วาดพื้นและของตกแต่ง
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                f_idx = floor[r][c]
                if f_idx is not None:
                    self.screen.blit(self.tiles[f_idx], (c * TILE_SIZE, r * TILE_SIZE))
                d_idx = decor[r][c]
                if d_idx is not None:
                    self.screen.blit(self.tiles[d_idx], (c * TILE_SIZE, r * TILE_SIZE))

        # เส้นตาราง
        for r in range(GRID_ROWS + 1):
            pygame.draw.line(self.screen, (40, 40, 40), (0, r * TILE_SIZE), (MAP_WIDTH, r * TILE_SIZE))
        for c in range(GRID_COLS + 1):
            pygame.draw.line(self.screen, (40, 40, 40), (c * TILE_SIZE, 0), (c * TILE_SIZE, MAP_HEIGHT))

        # Markers
        if self.sara_img:
            self.screen.blit(self.sara_img, (player[0]-12, player[1]-20))
        else:
            pygame.draw.circle(self.screen, YELLOW, player, 8)
            label_p = self.font.render("P", True, BLACK)
            self.screen.blit(label_p, (player[0]-4, player[1]-8))
        
        # Trophy Marker (แสดงเป็นรูปเลย)
        try:
            trophy_img = pygame.image.load('sara/gold_trophy.png').convert_alpha()
            trophy_img = pygame.transform.scale(trophy_img, (30, 30))
            self.screen.blit(trophy_img, (trophy[0]-15, trophy[1]-15))
        except:
            pygame.draw.rect(self.screen, RED, (trophy[0]-10, trophy[1]-10, 20, 20))
            label_t = self.font.render("T", True, WHITE)
            self.screen.blit(label_t, (trophy[0]-4, trophy[1]-8))

    def draw_palette(self):
        start_x, start_y = MAP_WIDTH + 20, 60
        palette_width, palette_height = self.palette_cols * TILE_SIZE, SCREEN_HEIGHT - 120
        pygame.draw.rect(self.screen, (20, 20, 20), (start_x - 5, start_y - 5, palette_width + 10, palette_height + 10))
        
        clip_rect = pygame.Rect(start_x, start_y, palette_width, palette_height)
        self.screen.set_clip(clip_rect)
        for idx, tile in enumerate(self.tiles):
            c, r = idx % self.palette_cols, idx // self.palette_cols
            x, y = start_x + c * TILE_SIZE, start_y + r * TILE_SIZE - self.palette_scroll
            if -TILE_SIZE < y < palette_height:
                self.screen.blit(tile, (x, y))
                if idx == self.selected_tile_idx:
                    pygame.draw.rect(self.screen, YELLOW, (x, y, TILE_SIZE, TILE_SIZE), 2)
        self.screen.set_clip(None)
        
        label = self.font.render(f"Palette (Map {self.current_map_idx}) - Scroll Up/Down", True, WHITE)
        self.screen.blit(label, (start_x, start_y - 30))

    def draw_ui(self):
        pygame.draw.rect(self.screen, (30, 30, 30), (0, MAP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - MAP_HEIGHT))
        
        map_name = "Forest (Map 1)" if self.current_map_idx == 1 else "Space (Map 2)"
        status = f"Editing: {map_name} | Mode: {self.edit_mode} | Press 'H' for Help"
        self.screen.blit(self.big_font.render(status, True, GREEN if self.current_map_idx == 1 else BLUE), (20, MAP_HEIGHT + 15))
        
        hint = "Press '1' / '2' to Switch Maps | Left Click: Draw | Right Click: Delete | 'S' to Export"
        self.screen.blit(self.font.render(hint, True, LIGHT_GRAY), (20, MAP_HEIGHT + 50))

        # Save Message
        if self.save_msg_timer > 0:
            msg = self.font.render("--- DATA EXPORTED TO CONSOLE! ---", True, YELLOW)
            self.screen.blit(msg, (MAP_WIDTH + 20, MAP_HEIGHT - 30))
            self.save_msg_timer -= 1

    def draw_help(self):
        if not self.show_help: return
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 220))
        self.screen.blit(overlay, (0, 0))
        
        box = pygame.Rect(250, 80, 700, 520)
        pygame.draw.rect(self.screen, (40, 40, 40), box)
        pygame.draw.rect(self.screen, WHITE, box, 2)
        
        lines = [
            "Advanced Multi-Map Editor Pro Guide",
            "-------------------------------------",
            "[การจัดการแมพ]",
            "- กด '1': สลับไปแก้แมพป่า (Forest)",
            "- กด '2': สลับไปแก้แมพอวกาศ (Space)",
            "",
            "[การวาด]",
            "- คลิกซ้ายแช่แล้วลาก: วาดแผ่นกระเบื้อง หรือ วางพิกัดไอเท็ม",
            "- คลิกขวาแช่แล้วลาก: ลบกระเบื้อง (กลับเป็นค่าเริ่มต้น)",
            "- เมาส์กลาง (Scroll): เลื่อนดูแผ่นกระเบื้องใน Palette",
            "",
            "[โหมดแก้ไข]",
            "- F: โหมดพื้น (FLOOR) | D: โหมดของตกแต่ง (DECOR)",
            "- T: โหมดวางถ้วยรางวัล (TROPHY) | P: โหมดวางจุดเกิด SARA",
            "",
            "[การนำไปใช้]",
            "- S: พิมพ์โค้ดออกมาใน Console",
            "- นำโค้ดที่ได้ไปก๊อปปี้วางในไฟล์ 'maps/map_data.py'",
            "",
            "--- กด 'H' เพื่อปิดคู่มือวันนี้ ---"
        ]
        for i, line in enumerate(lines):
            self.screen.blit(self.font.render(line, True, WHITE if i > 0 else YELLOW), (box.x + 40, box.y + 30 + i * 23))

    def handle_click(self, mx, my, button):
        floor, decor, trophy, player = self.get_current_grids()
        
        if mx < MAP_WIDTH and my < MAP_HEIGHT:
            c, r = mx // TILE_SIZE, my // TILE_SIZE
            if button == 1: # Draw
                if self.edit_mode == "FLOOR": floor[r][c] = self.selected_tile_idx
                elif self.edit_mode == "DECOR": decor[r][c] = self.selected_tile_idx
                elif self.edit_mode == "TROPHY": trophy = (mx, my)
                elif self.edit_mode == "SARA": player = (mx, my)
            elif button == 3: # Delete
                if self.edit_mode == "FLOOR": floor[r][c] = 0
                elif self.edit_mode == "DECOR": decor[r][c] = None
                
            # สำคัญ: อัปเดตกลับไปยัง Instance Variable (สำหรับตัวแปรที่ไม่ใช่ List)
            self.set_current_grids(floor, decor, trophy, player)
        
        elif mx >= MAP_WIDTH + 20: # Palette
            start_x, start_y = MAP_WIDTH + 20, 60
            pc = (mx - start_x) // TILE_SIZE
            pr = (my - start_y + self.palette_scroll) // TILE_SIZE
            if 0 <= pc < self.palette_cols:
                idx = pr * self.palette_cols + pc
                if 0 <= idx < len(self.tiles):
                    self.selected_tile_idx = idx
                    if self.edit_mode not in ["FLOOR", "DECOR"]: self.edit_mode = "DECOR"

    def export_all(self):
        old_idx = self.current_map_idx
        data_str = "# ข้อมูลแผนที่ (25x20) เพื่อให้เต็มหน้าจอ 800x600 (32x32 ต่อช่อง)\n"
        data_str += "# 0 คือกระเบื้องแรกใน tileset\n\n"
        
        for idx in [1, 2]:
            self.current_map_idx = idx
            floor, decor, trophy, player = self.get_current_grids()
            prefix = f"MAP{idx}"
            
            data_str += f"# --- [ ข้อมูล {prefix} ] ---\n"
            data_str += f"{prefix}_PLAYER_START = {player}\n"
            data_str += f"{prefix}_TROPHY_POS = {trophy}\n"
            
            grass_var = "MAP1_GRASS" if idx == 1 else "MAP2_GRASS"
            data_str += f"{grass_var} = [\n"
            for row in floor:
                data_str += f"    {row},\n"
            data_str += "]\n\n"
            
            # เลเยอร์ตกแต่ง (Path/Decor)
            decor_var = "MAP1_DECOR" if idx == 1 else "MAP2_PATH"
            data_str += f"{decor_var} = [\n"
            for row in decor:
                data_str += f"    {row},\n"
            data_str += "]\n\n"
        
        # เขียนลงไฟล์โดยตรง
        try:
            with open('maps/map_data.py', 'w', encoding='utf-8') as f:
                f.write(data_str)
            print("\n" + "!" * 50)
            print("!!! AUTO-SAVE SUCCESSFUL: maps/map_data.py UPDATED !!!")
            print("!" * 50 + "\n")
        except Exception as e:
            print(f"Error saving file: {e}")
        
        # คืนค่าหน้าเดิมที่ผู้ใช้กำลังแต่งอยู่
        self.current_map_idx = old_idx
        self.load_map_data() 
        self.save_msg_timer = 180

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in [1, 3]:
                        self.is_drawing, self.last_mouse_button = True, event.button
                        self.handle_click(mx, my, event.button)
                    elif event.button == 4: self.palette_scroll = max(0, self.palette_scroll - 32)
                    elif event.button == 5: self.palette_scroll += 32
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button in [1, 3]: self.is_drawing = False
                
                if event.type == pygame.MOUSEMOTION:
                    if self.is_drawing: self.handle_click(mx, my, self.last_mouse_button)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s: self.export_all()
                    if event.key == pygame.K_h: self.show_help = not self.show_help
                    if event.key == pygame.K_f: self.edit_mode = "FLOOR"
                    if event.key == pygame.K_d: self.edit_mode = "DECOR"
                    if event.key == pygame.K_t: self.edit_mode = "TROPHY"
                    if event.key == pygame.K_p: self.edit_mode = "SARA"
                    if event.key == pygame.K_1:
                        self.current_map_idx = 1
                        self.load_map_data()
                    if event.key == pygame.K_2:
                        self.current_map_idx = 2
                        self.load_map_data()

            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_palette()
            self.draw_ui()
            self.draw_help()
            pygame.display.update()
            clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    editor = MapEditor()
    editor.run()
