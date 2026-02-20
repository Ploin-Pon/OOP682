import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
running = True
sara = pygame.image.load("image/sara-cal1.png")
sara_flipped = pygame.transform.flip(sara, True, False) # สร้างรูปที่กลับด้านในแนวนอน
clock = pygame.time.Clock()

# --- เพิ่มโค้ดส่วนนี้สำหรับอนิเมชัน ---
NUM_FRAMES_PER_ROW = 3
NUM_ROWS = 2

# คำนวณขนาดของเฟรมเดียว (มี 3 รูปต่อแถว, 2 แถว)
frame_width = sara.get_width() / NUM_FRAMES_PER_ROW
frame_height = sara.get_height() / NUM_ROWS

# สร้างลิสต์ของ Rect สำหรับแต่ละเฟรมของอนิเมชัน
walk_frames = []
for row in range(NUM_ROWS):
    for col in range(NUM_FRAMES_PER_ROW):
        frame_rect = pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height)
        walk_frames.append(frame_rect)

current_frame = 0
last_update_time = pygame.time.get_ticks()
animation_speed_ms = 120 # ความเร็วในการเปลี่ยนเฟรม (มิลลิวินาที)

# --- เพิ่มโค้ดส่วนนี้สำหรับควบคุมตัวละคร ---
char_x = 50
char_y = 50
char_speed = 3
facing_right = True # ตัวแปรเพื่อเช็คทิศทางที่ตัวละครหันหน้า
# ------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # --- เพิ่มโค้ดส่วนนี้สำหรับรับอินพุตและเคลื่อนที่ ---
    # ใช้ get_pressed() เพื่อให้เคลื่อนที่ได้อย่างต่อเนื่องเมื่อกดปุ่มค้าง
    keys = pygame.key.get_pressed()
    is_moving = False
    if keys[pygame.K_a]: # ซ้าย
        char_x -= char_speed
        is_moving = True
        facing_right = True
    if keys[pygame.K_d]: # ขวา
        char_x += char_speed
        is_moving = True
        facing_right = False
    if keys[pygame.K_w]: # ขึ้น (หลัง)
        char_y -= char_speed
        is_moving = True
    if keys[pygame.K_s]: # ลง (หน้า)
        char_y += char_speed
        is_moving = False

    clock.tick(60) # ปรับ tick ให้เหมาะสมกับเกมมากขึ้น
    screen.fill((255,255,255))

    # --- อัปเดตเฟรมอนิเมชัน (เฉพาะตอนที่เคลื่อนที่) ---
    if is_moving:
        now = pygame.time.get_ticks()
        if now - last_update_time > animation_speed_ms:
            last_update_time = now
            current_frame = (current_frame + 1) % len(walk_frames)
 
    # --- วาดตัวละครตามทิศทางที่หันหน้า ---
    if facing_right:
        screen.blit(sara, (char_x, char_y), walk_frames[current_frame])
    else:
        screen.blit(sara_flipped, (char_x, char_y), walk_frames[current_frame])

    pygame.display.update()

pygame.quit()