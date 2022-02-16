import pygame

from settings import Settings
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.settings = Settings()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Images/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.x < self.settings.screen_width-100:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed_factor

        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)