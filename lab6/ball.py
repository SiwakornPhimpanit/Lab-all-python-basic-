import pygame

# กำหนดค่าคงที่
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 15
GRAVITY = 0.1
BOUNCE_DAMPING = 0.9
DAMPING_COEFFICIENT = 0.999
FPS = 60
FRAME_LIMIT = 600


class Ball:
    def __init__(self, x, y, vx, vy, radius, color=None):
        if color is None:
            color = radius
            radius = BALL_RADIUS
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY
        self.vx *= DAMPING_COEFFICIENT
        self.vy *= DAMPING_COEFFICIENT

        # การชนกับขอบจอ
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.vx = -self.vx * BOUNCE_DAMPING
        if self.y + self.radius >= SCREEN_HEIGHT:
            self.vy = -self.vy * BOUNCE_DAMPING
            self.y = SCREEN_HEIGHT - self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)