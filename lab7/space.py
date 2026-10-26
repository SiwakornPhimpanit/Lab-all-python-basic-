import pygame
import sys
import math

class Space(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (100, 100))  # ปรับ
        self.image = pygame.transform.scale(self.original_image, (100, 100))

        # สร้างสี่เหลี่ยม (rect) เพื่อใช้กำหนดตำแหน่งและเช็คการชน
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.angle = 0
        self.rotation_speed = 3
        self.rotation_smoothness = 0.15

        self.thrust = 0.5       # อัตราเร่งเมื่อกดเดินหน้า
        self.friction = 0.97    # แรงเสียดทาน (1.0 = ไม่หยุดเลย, ยิ่งน้อยยิ่งเบรคไว)
        self.max_speed = 5     # ล็อกความเร็วสูงสุด
        self.velocity = pygame.math.Vector2(0, 0)  # เวกเตอร์ความเร็ว
        self.pos = pygame.math.Vector2(x, y)  # เวกเตอร์ตำแหน่ง (ใช้ float เพื่อความแม่นยำ)

    def update(self):
        keys = pygame.key.get_pressed()

        # --- 1. รับค่าเวกเตอร์ทิศทางจากปุ่มกด ---
        input_dir = pygame.math.Vector2(0, 0)
        if keys[pygame.K_LEFT]:
            input_dir.x -= 1
        if keys[pygame.K_RIGHT]:
            input_dir.x += 1
        if keys[pygame.K_UP]:
            input_dir.y -= 1
        if keys[pygame.K_DOWN]:
            input_dir.y += 1

        # ถ้ามีการกดปุ่มทิศทาง (ไม่ว่าจะตรงหรือเฉียง)
        if input_dir.length() > 0:
            # ปรับเวกเตอร์ให้ความยาวเท่ากับ 1 เสมอ (เพื่อไม่ให้เดินเฉียงเร็วกว่าเดินตรง)
            input_dir = input_dir.normalize()
            
            # --- 2. คำนวณมุมเป้าหมาย (Target Angle) ---
            # ใช้ atan2 หามุมจากเวกเตอร์ (ใส่ -y เพราะแกน Y ของจอคอมกลับหัวกับกราฟคณิตศาสตร์)
            # ลบ 90 องศา เพื่อให้สอดคล้องกับภาพยานที่หันหน้าขึ้นบนเสมอที่มุม 0 องศา
            target_angle = math.degrees(math.atan2(-input_dir.y, input_dir.x)) - 90
            
            # --- 3. การหมุนแบบสมูท (Lerp & Shortest Path) ---
            # หระยะห่างของมุมเป้าหมายกับมุมปัจจุบัน
            angle_diff = (target_angle - self.angle) % 360
            
            # บังคับให้หมุนไปทางที่ใกล้ที่สุด (ไม่เกิน 180 องศา)
            if angle_diff > 180:
                angle_diff -= 360
                
            # ค่อยๆ ปรับมุมปัจจุบันเข้าหามุมเป้าหมายทีละนิด (สมูท)
            self.angle += angle_diff * self.rotation_smoothness

            # --- 4. การขับเคลื่อน (ตามทิศที่กำลังหันหน้า) ---
            angle_rad = math.radians(self.angle + 90)
            accel_x = math.cos(angle_rad) * self.thrust
            accel_y = -math.sin(angle_rad) * self.thrust
            
            self.velocity.x += accel_x
            self.velocity.y += accel_y
            
        else:
            # --- 5. การลดความเร็วเมื่อปล่อยปุ่ม (แรงเสียดทาน) ---
            self.velocity *= self.friction
            if self.velocity.length() < 0.1:
                self.velocity.update(0, 0)

        # จำกัดความเร็วสูงสุด
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        # --- 6. อัปเดตตำแหน่งและภาพ ---
        self.pos += self.velocity
        
        # หมุนภาพตามมุมล่าสุด
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        # นำศูนย์กลางของภาพใหม่ไปวางทับตำแหน่ง pos ล่าสุด
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))


# สำหรับทดสอบรันไฟล์นี้โดยตรง (Run File)
if __name__ == '__main__':
    import os
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Flight Simulation")
    clock = pygame.time.Clock()

    image_path = os.path.join(os.path.dirname(__file__), "images", "space.png")
    space = Space(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, image_path)
    all_sprites = pygame.sprite.Group(space)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()