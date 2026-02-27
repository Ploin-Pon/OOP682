import pygame

def make_smart_transparent(surface, threshold=245):
    """
    เปลี่ยนพิกเซลที่เกือบขาว (RGB > threshold) ให้เป็นโปร่งใสทั้งหมด
    เหมาะสำหรับรูปภาพที่มีพื้นหลังเป็นสีขาวไม่บริสุทธิ์ (Noisy white)
    """
    # ต้องมั่นใจว่าเป็น Surface ที่รองรับ Alpha
    surface = surface.convert_alpha()
    
    # ใช้ PixelArray เพื่อแก้ไขค่าสีโดยตรง (เร็วกว่า get_at/set_at)
    pixels = pygame.PixelArray(surface)
    
    # วนลูปตรวจสอบพิกเซล (หรือใช้ระบบเปรียบเทียบ Array ถ้าต้องการความไวสูง)
    # แต่สำหรับ Spritesheet ขนาดไม่ใหญ่มาก วนลูปก็เพียงพอ
    w, h = surface.get_size()
    for y in range(h):
        for x in range(w):
            color = surface.unmap_rgb(pixels[x, y])
            # ถ้า R, G, B ทุกค่าสูงกว่า Threshold ให้ถือว่าเป็นสีขาวและทำเป็นโปร่งใส
            if color.r > threshold and color.g > threshold and color.b > threshold:
                pixels[x, y] = (0, 0, 0, 0) # โปร่งใส 100%
                
    pixels.close()
    return surface
