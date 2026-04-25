"""点击控制模块

负责点击逻辑的控制和执行，包括普通点击和长按功能。
"""

import threading
import time
import random
import ctypes
from typing import Optional, Callable, Any

# 定义Windows API常量
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

# 导入Windows API函数
user32 = ctypes.windll.user32
# 添加类型注解以解决类型提示问题
user32.mouse_event = ctypes.windll.user32.mouse_event  # type: ignore


class ClickController:
    """点击控制器类"""
    
    def __init__(self, config_manager: Any, ui_callback: Optional[Callable] = None):
        """
        初始化点击控制器
        
        Args:
            config_manager: 配置管理器
            ui_callback: UI回调函数
        """
        self.config = config_manager
        self.ui_callback = ui_callback
        self.clicking = False
        self.click_thread: Optional[threading.Thread] = None
        self.hold_start_time = 0.0
        self.total_hold_time = 0.0
        
    def start_clicking(self) -> None:
        """开始点击"""
        if not self.clicking:
            self.clicking = True
            if self.ui_callback:
                self.ui_callback('update_count', 0)
            
            # 重置长按时间
            if self.config.get('hold_mode'):
                self.hold_start_time = time.time()
                self.total_hold_time = 0.0
                if self.ui_callback:
                    self.ui_callback('update_hold_time', "00:00:00")
            
            if self.ui_callback:
                self.ui_callback('update_status', '连点器已开启', 'green')
                
            self.click_thread = threading.Thread(target=self._click_loop)
            self.click_thread.daemon = True
            self.click_thread.start()
            
    def stop_clicking(self) -> None:
        """停止点击"""
        self.clicking = False
        if self.ui_callback:
            self.ui_callback('update_status', '连点器未启用', 'blue')
            
    def is_clicking(self) -> bool:
        """检查是否正在点击
        
        Returns:
            是否正在点击
        """
        return self.clicking
        
    def _click_loop(self) -> None:
        """点击循环"""
        count = 0
        
        while self.clicking:
            # 检查点击次数限制
            if not self.config.get('infinite_clicks') and count >= self.config.get('total_clicks'):
                break
                
            # 执行点击操作
            if self.config.get('hold_mode'):
                # 更新长按时间
                self._update_hold_time()
                # 执行长按
                self._perform_hold()
                # 如果是无限长按（持续时间为0），则跳出循环
                if self.config.get('hold_duration') <= 0:
                    break
            else:
                # 执行普通点击
                self._perform_normal_click()
            
            # 更新计数
            count += 1
            if self.ui_callback:
                self.ui_callback('update_count', count)
                
            # 获取目标间隔时间
            target_interval = self._get_interval()
            
            # 优化时间控制逻辑
            if target_interval > 0:
                # 对于非常小的间隔（小于1ms），直接跳过sleep
                # 因为time.sleep()本身有开销，而且在Windows上最小精度约为1ms
                if target_interval > 0.001:
                    # 对于较大的间隔，使用sleep
                    time.sleep(target_interval)
                # 对于小间隔，我们不使用sleep，直接进行下一次点击
                # 这样可以最大化点击速度
        
        # 点击结束
        if self.clicking:
            self.clicking = False
            if self.ui_callback:
                self.ui_callback('update_status', '连点器未启用', 'blue')
                
    def _update_hold_time(self) -> None:
        """更新长按时间"""
        if self.clicking:
            # 计算已长按的时间
            current_time = time.time()
            self.total_hold_time = current_time - self.hold_start_time
            # 格式化时间
            formatted_time = self._format_time(self.total_hold_time)
            if self.ui_callback:
                self.ui_callback('update_hold_time', formatted_time)
                
    def _perform_normal_click(self) -> None:
        """执行普通点击"""
        button = self.config.get('hold_button', 'left')
        self._windows_api_click(button)
        
    def _perform_hold(self) -> None:
        """执行长按操作"""
        button = self.config.get('hold_button', 'left')
        duration = self.config.get('hold_duration', 2.0)
        
        # 根据按钮类型选择对应的鼠标事件常量
        if button == "left":
            down_event = MOUSEEVENTF_LEFTDOWN
            up_event = MOUSEEVENTF_LEFTUP
        elif button == "right":
            down_event = MOUSEEVENTF_RIGHTDOWN
            up_event = MOUSEEVENTF_RIGHTUP
        else:
            return
        
        # 使用Windows API模拟鼠标按下
        user32.mouse_event(down_event, 0, 0, 0, 0)
        
        if duration > 0:
            time.sleep(duration)
            # 使用Windows API模拟鼠标释放
            user32.mouse_event(up_event, 0, 0, 0, 0)
        else:
            # 持续时间为0时，无限长按，直到停止信号
            while self.clicking:
                time.sleep(0.1)
            # 使用Windows API模拟鼠标释放
            user32.mouse_event(up_event, 0, 0, 0, 0)
            
    def _get_interval(self) -> float:
        """获取点击间隔
        
        Returns:
            间隔时间（秒）
        """
        if self.config.get('random_interval'):
            return random.uniform(
                self.config.get('min_interval', 0.05),
                self.config.get('max_interval', 0.15)
            )
        else:
            return self.config.get('interval', 0.1)
            
    def _windows_api_click(self, button: str = 'left') -> None:
        """使用Windows API模拟鼠标点击
        
        Args:
            button: 按钮类型 ('left' 或 'right')
        """
        if button == 'left':
            # 模拟左键点击
            user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        elif button == 'right':
            # 模拟右键点击
            user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
            
    def _format_time(self, seconds: float) -> str:
        """将秒数格式化为时:分:秒格式
        
        Args:
            seconds: 秒数
            
        Returns:
            格式化的时间字符串
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}:{minutes}:{secs}"
