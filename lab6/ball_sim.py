import pygame 
import random
import os
import matplotlib.pyplot as plt 
from ball import Ball  # นำเข้าคลาส Ball จากไฟล์ ball.py
 
# กำหนดค่าต่าง ๆ 
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 
BALL_RADIUS = 30  # ขยายขนาดลูกบอลให้เห็นรูปชัดเจนขึ้น 
GRAVITY = 0.1 
BOUNCE_DAMPING = 0.9 
DAMPING_COEFFICIENT = 0.999 
FPS = 60 
FRAME_LIMIT = 600 
 
# สี 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
 
# เริ่มต้น Pygame 
pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("ลูกบอลเด้ง") 
clock = pygame.time.Clock() 

# โหลดรูปภาพลูกบอล
ball_img_path = os.path.join(os.path.dirname(__file__), "ball.png")
ball_img = pygame.image.load(ball_img_path).convert_alpha()
# ==============================================================
# จำนวนลูกบอล 50 ลูก
# ==============================================================
N = 50
BALL_RADIUS = 20  # ปรับขนาดลูกบอลให้พอดีกับ 50 ลูกบนหน้าจอ
ball_img = pygame.transform.smoothscale(ball_img, (BALL_RADIUS * 2, BALL_RADIUS * 2))

balls = []
for i in range(N):
    x = random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS)
    y = random.randint(BALL_RADIUS, SCREEN_HEIGHT // 2)
    vx = random.uniform(-5, 5)
    vy = random.uniform(-3, 3)
    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    balls.append(Ball(x, y, vx, vy, BALL_RADIUS, color))

positions = [[] for _ in range(N)]
angles = [0.0 for _ in range(N)]

# Simulation loop 
running = True 
time_steps = 0 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
    screen.fill(BLACK) 
    
    # อัปเดตและวาดลูกบอลทุกลูกในลิสต์
    for i, b in enumerate(balls):
        b.move()
        
        # หมุนตามความเร็วแกน X ของแต่ละลูก
        angles[i] -= b.vx * 3
        rotated_img = pygame.transform.rotate(ball_img, angles[i])
        
        rect = rotated_img.get_rect(center=(int(b.x), int(b.y)))
        screen.blit(rotated_img, rect)
        
        positions[i].append((b.x, b.y))
    
    pygame.display.flip() 
    clock.tick(FPS) 
    time_steps += 1 
    if time_steps > FRAME_LIMIT:  # จำกัดจำนวนเฟรม 
        running = False 
 
pygame.quit()

# แสดงข้อความใน Terminal หลังรันเสร็จ
print("\n" + "="*40)
print("Simulation Finished! Created by: Kanin")
print("="*40 + "\n")

# พล็อตกราฟเส้นทางลูกบอลทั้ง 50 ลูก
plt.figure(figsize=(9, 6))
for i in range(N):
    pos_x = [p[0] for p in positions[i]] 
    pos_y = [p[1] for p in positions[i]] 
    plt.plot(pos_x, pos_y, alpha=0.35, linewidth=0.8) 

plt.xlabel("X Position") 
plt.ylabel("Y Position") 
plt.title(f"Ball Trajectory ({N} balls) - Created by: Kanin", fontsize=13, fontweight='bold', color='navy') 
plt.grid(True) 
# Invert แกน y 
plt.gca().invert_yaxis() 
plt.show()