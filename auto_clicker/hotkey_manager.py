"""热键管理模块

负责热键的注册、监听和捕获，提供热键管理功能。
"""

import threading
import time
from tkinter import messagebox
from typing import Dict, Callable, Optional, Any

# 尝试导入keyboard模块，如果失败则尝试pynput作为替代
KEYBOARD_AVAILABLE = False
try:
    import keyboard
    KEYBOARD_AVAILABLE = True
except ImportError:
    try:
        from pynput import keyboard as pynput_keyboard
        KEYBOARD_AVAILABLE = False  # 使用pynput模式
        print("提示：使用pynput替代keyboard模块")
    except ImportError:
        print("错误：未找到keyboard或pynput模块")
        print("请安装其中一个：pip install keyboard 或 pip install pynput")
        raise


class HotkeyManager:
    """热键管理类"""
    
    def __init__(self):
        """初始化热键管理器"""
        self.hotkeys: Dict[str, Dict[str, Any]] = {}
        self.running = False
        self.listener_thread: Optional[threading.Thread] = None
        
    def register_hotkey(self, name: str, key_combination: str, 
                       callback: Callable, suppress: bool = True) -> bool:
        """注册热键
        
        Args:
            name: 热键名称
            key_combination: 按键组合
            callback: 回调函数
            suppress: 是否抑制默认行为
            
        Returns:
            是否注册成功
        """
        if not KEYBOARD_AVAILABLE:
            print("热键功能不可用，缺少keyboard模块")
            return False
            
        try:
            keyboard.add_hotkey(key_combination, callback, suppress=suppress)
            self.hotkeys[name] = {
                'combination': key_combination,
                'callback': callback,
                'suppress': suppress
            }
            return True
        except Exception as e:
            print(f"注册热键失败: {e}")
            return False
            
    def unregister_all(self) -> None:
        """移除所有热键"""
        if KEYBOARD_AVAILABLE:
            keyboard.unhook_all()
        self.hotkeys.clear()
        
    def start_listening(self) -> None:
        """启动热键监听线程"""
        self.running = True
        if self.listener_thread is None:
            self.listener_thread = threading.Thread(target=self._listen_loop)
            self.listener_thread.daemon = True
            self.listener_thread.start()
            
    def stop_listening(self) -> None:
        """停止热键监听"""
        self.running = False
        if self.listener_thread:
            self.listener_thread.join(timeout=2.0)
            self.listener_thread = None
        self.unregister_all()
        
    def _listen_loop(self) -> None:
        """热键监听循环"""
        while self.running:
            time.sleep(1)  # 减少CPU占用
            
    def capture_hotkey(self, root: Any, target: str = "global") -> Optional[str]:
        """捕获用户按下的热键组合
        
        Args:
            root: 主窗口
            target: 目标热键类型
            
        Returns:
            捕获的热键组合
        """
        if not KEYBOARD_AVAILABLE:
            messagebox.showerror("错误", "热键功能不可用，缺少keyboard模块")
            return None
            
        captured_keys = []
        is_capturing = True
        
        # 创建捕获提示窗口
        capture_window = self._create_capture_window(root)
        
        # 捕获线程
        def capture_thread_func():
            nonlocal captured_keys, is_capturing
            
            # 移除现有的热键监听，避免干扰
            keyboard.unhook_all()
            
            # 监听键盘事件
            while is_capturing:
                try:
                    # 使用阻塞方式读取事件，减少CPU占用
                    event = keyboard.read_event(suppress=True)
                    
                    if event.event_type == 'down':
                        key = event.name
                        if key not in captured_keys:
                            captured_keys.append(key)
                    elif event.event_type == 'up':
                        if event.name == 'enter':
                            # 回车键结束捕获
                            is_capturing = False
                            capture_window.after(100, capture_window.destroy)
                except Exception as e:
                    print(f"捕获热键时发生错误: {e}")
                    pass
        
        # 启动捕获线程
        capture_thread = threading.Thread(target=capture_thread_func)
        capture_thread.daemon = True
        capture_thread.start()
        
        # 等待捕获完成
        root.wait_window(capture_window)
        
        # 格式化热键
        if captured_keys:
            # 移除回车键
            if 'enter' in captured_keys:
                captured_keys.remove('enter')
            # 排序按键（ctrl, alt, shift 在前）
            modifiers = ['ctrl', 'alt', 'shift', 'win']
            sorted_keys = sorted(captured_keys, key=lambda k: (k not in modifiers, k))
            hotkey_str = '+'.join(sorted_keys)
            return hotkey_str
        
        return None
        
    def _create_capture_window(self, root: Any) -> Any:
        """创建热键捕获窗口
        
        Args:
            root: 主窗口
            
        Returns:
            捕获窗口
        """
        capture_window = type(root)()
        capture_window.title("捕获热键")
        capture_window.geometry("300x100")
        capture_window.resizable(False, False)
        capture_window.transient(root)
        capture_window.grab_set()
        
        # 提示信息
        capture_label = type(root.children.values().__iter__().__next__())(capture_window, 
                          text="请按下要设置的快捷键组合，按回车键结束捕获", padding=20)
        capture_label.pack(fill='both', expand=True)
        
        return capture_window
