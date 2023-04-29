import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加載外星人圖像並設定其rect屬性
        self.image = pg.image.load('images/alien3.png')
        self.rect = self.image.get_rect()

        # 將每個新外星人放在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 儲存外星人的精確水平位置
        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
        return False  

    def update(self):
        """Move the alien to the right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

        # Check if the alien has reached the edge of the screen.
        if self.check_edges():
            # Change fleet direction and move aliens down.
            self.settings.fleet_direction *= -1
            self.rect.y += self.settings.fleet_drop_speed


