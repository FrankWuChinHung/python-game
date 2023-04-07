import sys
import pygame as pg

from settings import Settings
from player import Player
from bullet import Bullet

# 定義一個AlienInvasion類別
class AlienInvasion:
    
    # 初始化函數__init__()
    def __init__(self):
        
        pg.init()
        
        # self.clock = pg.time.Clock()
        self.settings = Settings()
        
        self.screen = pg.display.set_mode((self.settings.screen_width,self.settings.screen_width))   # 建立一個名為screen的Pygame視窗
        
        # self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)            # 建立全螢幕的Pygame視窗
        # self.settings.screen_width = self.screen.get_rect().width          # 更新設定值
        # self.settings.screen_height = self.screen.get_rect().height
        
        pg.display.set_caption("Alien Invasion")        # 透過pg.display.set_caption()函數設定視窗的標題為"Alien Invasion"
    
        self.player = Player(self)
        self.bullets = pg.sprite.Group()
        
        
    # 執行遊戲的函數run_game()    
    def run_game(self):
        while True:                              # 用while無窮迴圈，以等待用戶交互事件
            self._check_events()
            
            self.player.update()
            
            self._update_bullets()
            
            self._update_screen()
            # self.clock.tick(60)
    
    def _check_events(self):                     # Respond to keypresses and mouse events.
        for event in pg.event.get():             # 當用戶關閉視窗時，程式會呼叫sys.exit()函數終止遊戲
            if event.type == pg.QUIT:
                sys.exit()
                
            elif event.type == pg.KEYDOWN:       # 檢測到 KEYDOWN，玩家按下的是右箭頭鍵（K_RIGHT），則將玩家的太空船 moving_right 屬性設為 True，以表示玩家正在向右移動。
                self._check_keydown_events(event)
                
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):      # 如果檢測到 KEYDOWN，且玩家按下的是右箭頭鍵，則將玩家的太空船 moving_right 屬性設為 True，以表示玩家向右移動。    
        if event.key == pg.K_RIGHT:
            self.player.moving_right = True   
        elif event.key == pg.K_LEFT:
            self.player.moving_left = True        
        elif event.key == pg.K_UP:
            self.player.moving_up = True
        elif event.key == pg.K_DOWN:
            self.player.moving_down = True
            
        elif event.key == pg.K_q:                 # 當按q關閉視窗時，程式會呼叫sys.exit()函數終止遊戲
            sys.exit()
        
        elif event.key == pg.K_SPACE:
            
            self._fire_bullet()
    
    def _check_keyup_events(self, event):         # 如果檢測到 KEYUP，且玩家釋放的是右箭頭鍵，則將玩家的太空船 moving_right 屬性設為 False，以表示玩家停止了向右移動。                    
        if event.key == pg.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pg.K_LEFT:
            self.player.moving_left = False
        elif event.key == pg.K_UP:
            self.player.moving_up = False    
        elif event.key == pg.K_DOWN:
            self.player.moving_down = False            
    
    def _fire_bullet(self):
        # if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self, self.player)
        self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():       # 刪除已經消失的子彈
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    
    def _update_screen(self):                    # 更新遊戲螢幕狀態
        self.screen.fill(self.settings.bg_color)    
        self.player.blitme()                     # 用blitme()方法來繪製玩家的太空船。在遊戲的每個迭代中，這個方法都會被呼叫一次，以繪製最新的遊戲狀態。
        self._update_bullets()
        for bullet in self.bullets.sprites():    # 顯示所有子彈的圖像
            bullet.draw_bullet()
          
        
        pg.display.flip()                        # pg.display.flip()函數在每次迴圈迭代後更新視窗，讓視窗中的內容實際顯示
            
# 主程式            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()