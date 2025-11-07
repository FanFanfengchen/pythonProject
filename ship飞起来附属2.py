import pygame

class Ship:
    """管理飞船的类"""
    
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # 加载飞船图像并获取其外接矩形
        try:
            self.image = pygame.image.load('images/ship.bmp')
        except (pygame.error, FileNotFoundError):
            # 如果没有找到图片，创建一个更酷的飞船图形
            self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
            # 绘制飞船主体（银色三角形）
            pygame.draw.polygon(self.image, (192, 192, 192), [
                (30, 0),    # 顶部
                (0, 50),    # 左下
                (60, 50)    # 右下
            ])
            # 绘制飞船尾翼
            pygame.draw.polygon(self.image, (105, 105, 105), [
                (10, 50),
                (0, 60),
                (25, 60)
            ])
            pygame.draw.polygon(self.image, (105, 105, 105), [
                (50, 50),
                (60, 60),
                (35, 60)
            ])
            # 绘制飞船驾驶舱
            pygame.draw.ellipse(self.image, (0, 200, 255), [20, 20, 20, 20])
            # 绘制飞船尾焰（蓝色和橙色）
            pygame.draw.polygon(self.image, (0, 100, 255), [
                (20, 50),
                (40, 50),
                (30, 70)
            ])
            pygame.draw.polygon(self.image, (255, 165, 0), [
                (25, 50),
                (35, 50),
                (30, 65)
            ])
            
        self.rect = self.image.get_rect()
        
        # 将飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 在飞船的属性x和y中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x和y值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            
        # 根据self.x和self.y更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)