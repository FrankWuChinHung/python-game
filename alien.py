import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        
        super().__init__()
        self.screen = ai_game.screen
        # self.settings = ai_game.settings

        # 載入 alien image
        self.image = pg.image.load('images/alien3.png')
        self.rect = self.image.get_rect()

        # 新的 alien 出現在螢幕左邊
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # self.rect是一個pygame中的Rect對象，代表 alien 矩形範圍。
        self.x = float(self.rect.x)


