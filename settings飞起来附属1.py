class Settings:
    """存储游戏中所有设置的类"""
    
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (5, 5, 25)  # 深蓝色背景，像太空
        
        # 飞船设置
        self.ship_speed = 3.0  # 飞船速度
        
        # 子弹设置
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 215, 0)  # 金色子弹
        self.bullets_allowed = 10  # 允许更多子弹同时存在
        self.bullet_fire_delay = 150  # 子弹发射间隔（毫秒）
        
        # 外星人设置
        self.alien_speed_x = 0.5  # 降低水平移动速度
        self.alien_speed_y = 1.0  # 垂直移动速度
        self.fleet_drop_speed = 5  # 降低下降速度
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        
        # 减少外星人数量
        self.fleet_rows = 3  # 减少行数
        self.fleet_columns = 6  # 减少列数