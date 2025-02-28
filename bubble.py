import pygame
import random

class Bubble(pygame.sprite.Sprite):
    def __init__(self, screen, game_settings):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bubble_radius = random.randint(game_settings.bubble_min_r, game_settings.bubble_max_r)
        self.image = pygame.Surface((self.bubble_radius * 2, self.bubble_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 182, 193), (self.bubble_radius, self.bubble_radius), self.bubble_radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_rect.height - self.rect.height)
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0 or self.rect.right > self.screen_rect.width:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.height:
            self.speed_y = -self.speed_y

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
