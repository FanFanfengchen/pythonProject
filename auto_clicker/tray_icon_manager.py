"""系统托盘管理模块

负责系统托盘图标的创建和管理，提供系统托盘功能。
"""

import threading
from pystray import Icon as TrayIcon, Menu as TrayMenu, MenuItem as TrayMenuItem
from PIL import Image, ImageDraw
from typing import Optional, Callable, Any


class TrayIconManager:
    """系统托盘管理类"""
    
    def __init__(self, root: Any, config_manager: Any):
        """
        初始化系统托盘管理器
        
        Args:
            root: 主窗口
            config_manager: 配置管理器
        """
        self.root = root
        self.config = config_manager
        self.tray_icon: Optional[TrayIcon] = None
        self.is_running = False
        self.tray_thread: Optional[threading.Thread] = None
        self.on_show_window: Optional[Callable] = None
        self.on_stop_clicking: Optional[Callable] = None
        self.on_quit: Optional[Callable] = None
        
    def set_callbacks(self, on_show_window: Callable, 
                     on_stop_clicking: Callable, 
                     on_quit: Callable) -> None:
        """设置回调函数
        
        Args:
            on_show_window: 显示窗口回调
            on_stop_clicking: 停止点击回调
            on_quit: 退出程序回调
        """
        self.on_show_window = on_show_window
        self.on_stop_clicking = on_stop_clicking
        self.on_quit = on_quit
        
    def create_tray_icon(self) -> None:
        """创建系统托盘图标"""
        if self.tray_icon is not None:
            return
            
        # 创建一个简单的图标
        image = self._create_icon_image()
        
        # 创建菜单
        menu = self._create_menu()
        
        # 创建图标
        self.tray_icon = TrayIcon('增强版鼠标连点器', image, menu=menu)
        
        # 启动托盘图标线程
        self.is_running = True
        self.tray_thread = threading.Thread(target=self._run_tray)
        self.tray_thread.daemon = True
        self.tray_thread.start()
        
    def stop(self) -> None:
        """停止系统托盘"""
        self.is_running = False
        if self.tray_icon:
            self.tray_icon.stop()
            self.tray_icon = None
        if self.tray_thread:
            self.tray_thread.join(timeout=2.0)
            self.tray_thread = None
            
    def update_menu(self) -> None:
        """更新系统托盘菜单"""
        if self.tray_icon:
            self.tray_icon.menu = self._create_menu()
            self.tray_icon.update_menu()
            
    def _run_tray(self) -> None:
        """运行系统托盘"""
        if self.tray_icon:
            self.tray_icon.run()
            
    def _create_icon_image(self) -> Image.Image:
        """创建图标图像
        
        Returns:
            图标图像
        """
        try:
            width = 64
            height = 64
            image = Image.new('RGB', (width, height), (0, 128, 255))
            draw = ImageDraw.Draw(image)
            draw.ellipse((16, 16, 48, 48), fill=(255, 255, 255))
            draw.ellipse((24, 24, 40, 40), fill=(0, 128, 255))
            return image
        except Exception as e:
            print(f"创建图标失败: {e}")
            # 提供默认图标
            width = 64
            height = 64
            default_image = Image.new('RGB', (width, height), (255, 0, 0))
            draw = ImageDraw.Draw(default_image)
            draw.text((10, 25), "AC", fill=(255, 255, 255), font=None)
            return default_image
        
    def _create_menu(self) -> TrayMenu:
        """创建系统托盘菜单
        
        Returns:
            菜单对象
        """
        menu_items = []
        
        # 显示窗口菜单项
        if self.on_show_window:
            menu_items.append(TrayMenuItem('显示窗口', self.on_show_window))
        
        # 停止点击菜单项
        if self.on_stop_clicking:
            menu_items.append(TrayMenuItem('停止点击', self.on_stop_clicking))
        
        # 退出菜单项
        if self.on_quit:
            menu_items.append(TrayMenuItem('退出', self.on_quit))
        
        return TrayMenu(*menu_items)
