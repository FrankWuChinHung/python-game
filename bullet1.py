import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):                             # 建立Bullet物件
    def __init__(self, ai_game):
        super().__init__()                    # 先使用super()調用父類別Sprite的初始化方法，再將screen、settings、color等屬性保存下來。
        self.screen = ai_game.screen              # 連接遊戲螢幕
        self.settings = ai_game.settings          # 連接settings物件
        self.color = self.settings.bullet_color   # 子彈顏色
        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)  # 子彈位置
        self.rect.midtop = ai_game.player.rect.midtop                                          # 子彈圖像的頂部中心點，初始化為玩家頂部的中心點。
                
        self.y = float(self.rect.y)            # self.y 變數存儲了矩形的 y 坐標，並轉換為浮點數型態。
        
    def update(self):                          # update() 方法是每個遊戲循環中，子彈需要執行的操作。
        self.y -= self.settings.bullet_speed   # 在這個方法中，每次更新 self.y 的值，使其向上移動一個設置值 settings.bullet_speed。
        self.rect.y = self.y                   # 接著，更新 self.rect.y 的值，將矩形的位置向上移動。
       
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)   #使用 pygame.draw.rect() 函數，在屏幕上繪製一個矩形，矩形的顏色、位置和大小等屬性從之前定義的變數中讀取。
        
# 請檢查 bullet.update() 方法是否在遊戲迴圈中被正確地呼叫。如果是，請確認 bullet.y 是否在更新時有被增加，以讓子彈在畫面上向上移動。您也可以在bullet.draw_bullet() 方法中加入一個 print 來檢查是否被正確呼叫。
