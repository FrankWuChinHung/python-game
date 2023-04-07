import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):                             # 建立Bullet物件
    
    def __init__(self, ai_game, player):
        super().__init__()                         # 先使用super()調用父類別Sprite的初始化方法，再將screen、settings、color等屬性保存下來。
        self.screen = ai_game.screen              # 連接遊戲螢幕
        self.settings = ai_game.settings          # 連接settings物件
        self.player = player
        
        self.image = pygame.image.load('images/bullet.jpg')    # 子彈的圖像，使用pygame.image.load()方法從圖像文件中載入。
        self.rect = self.image.get_rect()
        
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        
        self.speed = self.settings.bullet_speed

        self.color = self.settings.bullet_color
        
#         self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        
#         self.rect.midtop = player.rect.midtop                        # 子彈圖像的頂部中心點，初始化為玩家頂部的中心點。
        
        self.y = float(self.rect.y)            # self.y 變數存儲了矩形的 y 坐標，並轉換為浮點數型態。
        
    def update(self):                          # update() 方法是每個遊戲循環中，子彈需要執行的操作。
        self.y -= self.settings.bullet_speed   # 在這個方法中，每次更新 self.y 的值，使其向上移動一個設置值 settings.bullet_speed。
        self.rect.y = self.y                   # 接著，更新 self.rect.y 的值，將矩形的位置向上移動。
       
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)   #使用 blitme()方法將子彈圖像顯示在屏幕上，使用blit()方法將圖像貼到指定的矩形位置（即self.rect）。

        
        
        
       
        