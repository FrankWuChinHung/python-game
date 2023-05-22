class Settings():
    
    def __init__(self):
        
        self.screen_width = 1000         # 遊戲視窗的寬度，其值為800。
        self.screen_height = 1000       # 遊戲視窗的高度，其值為800。
        self.bg_color = (0,0,0)   # 遊戲背景顏色，其值為(230,230,230)，淺灰色。
        
        # Player
        self.player_speed = 0.5         # player移動速度
        
        # Bullet
        self.bullet_speed = 1.0          # 子彈移動速度
        self.bullet_width = 3            # 子彈寬度
        self.bullet_height = 10          # 子彈高度
        self.bullet_color = (255,0,0)    # 子彈顏色
        # self.bullets_allowed = 3
        
       
        
