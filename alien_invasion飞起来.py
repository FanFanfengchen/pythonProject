import sys
import pygame

from settings飞起来附属1 import Settings
from ship飞起来附属2 import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # 设置游戏帧率
        self.clock = pygame.time.Clock()
        
        # 创建飞船
        self.ship = Ship(self)
        
        # 创建外星人编队
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
        # 创建子弹编组
        self.bullets = pygame.sprite.Group()
        
        # 连续射击标志和时间控制
        self.shooting = False
        self.last_bullet_time = 0
        
        # 创建星空背景
        self.stars = self._create_stars()
        
    def _create_stars(self):
        """创建星空背景"""
        stars = []
        for _ in range(100):  # 创建100颗星星
            x = pygame.time.get_ticks() % self.settings.screen_width
            y = pygame.time.get_ticks() * 7 % self.settings.screen_height
            size = pygame.time.get_ticks() % 3 + 1
            brightness = pygame.time.get_ticks() % 155 + 100
            stars.append((x, y, size, brightness))
        return stars
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            # 处理连续射击
            if self.shooting:
                self._fire_bullet()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """响应按键按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.shooting = True
            
    def _check_keyup_events(self, event):
        """响应按键松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_SPACE:
            self.shooting = False
            
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组"""
        current_time = pygame.time.get_ticks()
        # 检查是否到了发射子弹的时间
        if current_time - self.last_bullet_time > self.settings.bullet_fire_delay:
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
                self.last_bullet_time = current_time
            
    def _update_bullets(self):
        """更新子弹的位置，并删除消失的子弹"""
        # 更新子弹位置
        self.bullets.update()
        
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
        # 检查是否有子弹击中了外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
            
    def _update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        
    def _create_fleet(self):
        """创建外星人编队"""
        # 创建一个外星人并计算一行可容纳多少个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # 根据设置创建指定数量的外星人
        for row_number in range(self.settings.fleet_rows):
            for alien_number in range(self.settings.fleet_columns):
                self._create_alien(alien_number, row_number)
                
    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = 100 + alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = 50 + alien.rect.height + 2 * alien.rect.height * row_number
        alien.y = float(alien.rect.y)  # 添加y坐标存储
        self.aliens.add(alien)
        
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            alien.y = float(alien.rect.y)
        self.settings.fleet_direction *= -1
        
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        
        # 绘制星空背景
        for star in self.stars:
            x, y, size, brightness = star
            color = (brightness, brightness, brightness)
            pygame.draw.circle(self.screen, color, (x, y), size)
        
        self.ship.blitme()
        
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # 绘制外星人
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

class Bullet(pygame.sprite.Sprite):
    """管理子弹的类"""
    
    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                               self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        
    def update(self):
        """向上移动子弹"""
        # 更新子弹位置的小数值
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Alien(pygame.sprite.Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # 加载外星人图像并设置其rect属性
        try:
            self.image = pygame.image.load('images/alien.bmp')
        except (pygame.error, FileNotFoundError):
            # 如果没有找到图片，创建一个更酷的外星人图形
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            # 绘制外星人主体（绿色圆形）
            pygame.draw.circle(self.image, (0, 200, 0), (25, 20), 15)
            # 绘制外星人身体（椭圆）
            pygame.draw.ellipse(self.image, (0, 180, 0), [10, 25, 30, 25])
            # 绘制外星人眼睛（红色圆形）
            pygame.draw.circle(self.image, (255, 0, 0), (18, 18), 5)
            pygame.draw.circle(self.image, (255, 0, 0), (32, 18), 5)
            # 绘制外星人触角
            pygame.draw.line(self.image, (0, 150, 0), (20, 5), (15, -5), 3)
            pygame.draw.line(self.image, (0, 150, 0), (30, 5), (35, -5), 3)
            
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕顶部附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的精确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
            
    def update(self):
        """向左或向右移动外星人，并缓慢向下移动"""
        self.x += self.settings.alien_speed_x * self.settings.fleet_direction
        self.y += self.settings.alien_speed_y  # 持续向下移动
        self.rect.x = self.x
        self.rect.y = self.y

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()