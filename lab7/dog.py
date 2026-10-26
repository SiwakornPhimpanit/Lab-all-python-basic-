import pygame
import sys
SCREEN_WIDTH = 800 
# สร้าง Class Dog
class Dog(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, image_path):
        super().__init__()
        
        # โหลดรูปภาพและทำให้พื้นหลังโปร่งใส (ถ้าไฟล์รูปมี alpha channel)
        self.image = pygame.image.load(image_path).convert_alpha()
        
        # ทางเลือก: ปรับขนาดรูปภาพถ้าใหญ่เกินไป
        self.image = pygame.transform.scale(self.image, (100, 100))

        # ปรับขนาดรูปภาพ (สามารถแก้ตัวเลข 150, 150 ให้เข้ากับขนาดเกมได้)
        self.image_right = pygame.transform.scale(self.image, (100, 100))
        
        # สร้างรูปสำหรับหันซ้าย โดยการ Flip แกน X (แนวนอน=True, แนวตั้ง=False)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        
        # สร้างสี่เหลี่ยม (rect) เพื่อใช้กำหนดตำแหน่งและเช็คการชน
        self.rect = self.image_right.get_rect()
        self.rect.center = (x, y)

# ความเร็วในการเดินแนวนอน
        self.vx = vx
        
        # ตั้งค่าเริ่มต้นให้รูปหันไปตามทิศทางที่เดิน
        if self.vx >= 0:
            self.image = self.image_right
        else:
            self.image = self.image_left
            
        # สร้างกล่องสี่เหลี่ยมสำหรับจัดการตำแหน่งและการชน
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # 1. ให้หมาเดินไปตามแนวแกน X
        self.rect.x += self.vx

        # 2. ตรวจสอบการชนขอบจอ (กำแพง)
        # ถ้าเดินชนขอบขวาของจอ
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH # จัดให้อยู่พอดีขอบจอ
            self.vx = -self.vx             # กลับทิศทางการเดิน (บวกเป็นลบ)
            self.image = self.image_left   # สลับรูปให้หมาหันซ้าย
            
        # ถ้าเดินชนขอบซ้ายของจอ
        elif self.rect.left <= 0:
            self.rect.left = 0             # จัดให้อยู่พอดีขอบจอ
            self.vx = -self.vx             # กลับทิศทางการเดิน (ลบเป็นบวก)
            self.image = self.image_right  # สลับรูปให้หมาหันขวา