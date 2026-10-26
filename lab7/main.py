import pygame 
from dog import Dog  # นำเข้าคลำส Dog จากไฟล์ dog.py
from space import Space  # นำเข้าคลำส Space จากไฟล์ space.py
import random

SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
FPS = 60
pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("space") 
clock = pygame.time.Clock() 

import os
BASE_DIR = os.path.dirname(__file__)

all_sprites = pygame.sprite.Group()
#dog = Dog(400, 500, 5, os.path.join(BASE_DIR, "images", "dog.png"))  # สร้างวัตถุ Dog
#all_sprites.add(dog)

space_image_path = os.path.join(BASE_DIR, "images", "space.png")
space = Space(400, 300, space_image_path)  # สร้างวัตถุ Space
all_sprites.add(space)


running = True 
time_steps = 0 

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    screen.fill(BLACK) 

    # อัปเดตการทำงานของสไปรต์
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip() 
    clock.tick(FPS)
pygame.quit()