import pygame

# 定義了一個名為Player的類別，用於表示玩家的太空船。


class Player():

    def __init__(self, ai_game):

        # 遊戲的屏幕，是由Pygame函數pygame.display.set_mode()創建的屏幕對象。
        self.screen = ai_game.screen
        # 遊戲屏幕的矩形區域，使用get_rect()方法從self.screen中獲取。
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings                   # 連接settings物件

        # 太空船的圖像，使用pygame.image.load()方法從圖像文件中載入。
        self.image = pygame.image.load('images/ship1.jpg')
        # 太空船圖像的矩形區域，使用get_rect()方法從self.image中獲取。
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom   # 太空船圖像的底部中心點，初始化為遊戲屏幕底部的中心點。
        # self.rect.x = width // 2
        # self.rect.y = height - 100

        # self.rect是一個pygame中的Rect對象，它代表了火箭的矩形範圍。
        self.x = float(self.rect.x)
        # self.x和self.y則是火箭的實際位置，是用浮點數類型來儲存的。
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # 自定義的方法，用於更新玩家的太空船的位置。
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:    # 若 moving_right 為 True，表示玩家正在向右移動，
            # < self.screen_rect.right不會超出遊戲螢幕範圍。
            self.x += self.settings.player_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed                              # 左右

        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.player_speed                              # 上下

        # 這個方法需要在主遊戲迴圈中被定期呼叫，以確保太空船在遊戲中移動。
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # blitme()方法將太空船圖像顯示在屏幕上，使用blit()方法將圖像貼到指定的矩形位置（即self.rect）。
        self.screen.blit(self.image, self.rect)

    # def fire_bullet(self):
    #     new_bullet = Bullet(self.settings, self.screen, self.rect)
    #     ai_game.bullets.add(new_bullet)
