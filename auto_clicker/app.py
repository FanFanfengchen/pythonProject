"""主应用程序模块

作为模块的协调者，整合所有功能模块，提供完整的应用程序功能。
"""

import tkinter as tk
from tkinter import messagebox
import ctypes
from typing import Any

from .config_manager import ConfigManager
from .ui_manager import UIManager
from .hotkey_manager import HotkeyManager
from .click_controller import ClickController
from .tray_icon_manager import TrayIconManager


class AutoClickerApp:
    """主应用程序类"""
    
    def __init__(self):
        """初始化应用程序"""
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("增强版鼠标连点器 v2.0")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # 初始化各个管理器
        self.config_manager = ConfigManager()
        self.ui_manager = UIManager(self.root, self.config_manager)
        self.hotkey_manager = HotkeyManager()
        self.click_controller = ClickController(self.config_manager, self._ui_callback)
        self.tray_manager = TrayIconManager(self.root, self.config_manager)
        
        # 设置系统托盘回调
        self.tray_manager.set_callbacks(
            on_show_window=self._show_window,
            on_stop_clicking=self.stop_clicking,
            on_quit=self.quit_program
        )
        
        # 初始化UI
        self.ui_manager.create_widgets()
        
        # 设置按钮回调
        self._setup_button_callbacks()
        
        # 启动热键监听
        self._setup_hotkeys()
        
        # 创建系统托盘
        if self.config_manager.get('background_mode'):
            self.tray_manager.create_tray_icon()
        
        # 绑定窗口事件
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.root.protocol("WM_ICONIFY", self._on_minimize)
        
    def _setup_button_callbacks(self) -> None:
        """设置按钮回调"""
        start_button = self.ui_manager.get_widget('start_button')
        if start_button:
            start_button.config(command=self.start_clicking)
        
        stop_button = self.ui_manager.get_widget('stop_button')
        if stop_button:
            stop_button.config(command=self.stop_clicking)
        
        reset_button = self.ui_manager.get_widget('reset_button')
        if reset_button:
            reset_button.config(command=self.reset_clicker)
        
    def _setup_hotkeys(self) -> None:
        """设置热键"""
        # 注册全局热键
        self.hotkey_manager.register_hotkey(
            'toggle_clicking',
            self.config_manager.get('hotkey'),
            self.toggle_clicking,
            suppress=True
        )
        
        # 注册长按功能热键
        self.hotkey_manager.register_hotkey(
            'toggle_hold',
            self.config_manager.get('hold_hotkey'),
            self.toggle_hold_mode,
            suppress=True
        )
        
        # 注册切换长按按钮热键
        self.hotkey_manager.register_hotkey(
            'switch_hold_button',
            self.config_manager.get('hold_switch_hotkey'),
            self.switch_hold_button,
            suppress=True
        )
        
        # 注册ESC紧急停止热键
        self.hotkey_manager.register_hotkey(
            'emergency_stop',
            'esc',
            lambda: self.stop_clicking() if self.click_controller.is_clicking() else None,
            suppress=False
        )
        
        # 启动热键监听
        self.hotkey_manager.start_listening()
        
    def _ui_callback(self, event: str, *args: Any) -> None:
        """UI回调处理
        
        Args:
            event: 事件类型
            *args: 事件参数
        """
        if event == 'update_count':
            if args:
                self.ui_manager.update_click_count(args[0])
        elif event == 'update_hold_time':
            if args:
                self.ui_manager.update_hold_time(args[0])
        elif event == 'update_status':
            if len(args) >= 2:
                self.ui_manager.update_status(args[0], args[1])
            elif args:
                self.ui_manager.update_status(args[0])
        
    def start_clicking(self) -> None:
        """开始点击"""
        # 保存当前配置
        self._save_current_config()
        self.click_controller.start_clicking()
        # 更新系统托盘菜单
        self.tray_manager.update_menu()
        
    def stop_clicking(self) -> None:
        """停止点击"""
        self.click_controller.stop_clicking()
        # 更新系统托盘菜单
        self.tray_manager.update_menu()
        
    def reset_clicker(self) -> None:
        """重置点击器"""
        self.stop_clicking()
        self.ui_manager.update_click_count(0)
        self.ui_manager.update_hold_time("00:00:00")
        
    def toggle_clicking(self, _event: Any = None) -> None:
        """切换点击状态"""
        if self.click_controller.is_clicking():
            self.stop_clicking()
        else:
            self.start_clicking()
            
    def toggle_hold_mode(self, _event: Any = None) -> None:
        """切换长按模式"""
        current_mode = self.config_manager.get('hold_mode')
        self.config_manager.set('hold_mode', not current_mode)
        # 更新UI变量
        hold_mode_var = self.ui_manager.get_variable('hold_mode')
        if hold_mode_var:
            hold_mode_var.set(not current_mode)
            
    def switch_hold_button(self, _event: Any = None) -> None:
        """切换长按按钮"""
        current_button = self.config_manager.get('hold_button')
        new_button = "right" if current_button == "left" else "left"
        self.config_manager.set('hold_button', new_button)
        # 更新UI变量
        hold_button_var = self.ui_manager.get_variable('hold_button')
        if hold_button_var:
            hold_button_var.set(new_button)
            
    def _save_current_config(self) -> None:
        """保存当前配置"""
        # 从UI获取当前配置
        interval_var = self.ui_manager.get_variable('interval')
        if interval_var:
            self.config_manager.set('interval', interval_var.get())
        
        min_interval_var = self.ui_manager.get_variable('min_interval')
        if min_interval_var:
            self.config_manager.set('min_interval', min_interval_var.get())
        
        max_interval_var = self.ui_manager.get_variable('max_interval')
        if max_interval_var:
            self.config_manager.set('max_interval', max_interval_var.get())
        
        random_interval_var = self.ui_manager.get_variable('random_interval')
        if random_interval_var:
            self.config_manager.set('random_interval', random_interval_var.get())
        
        total_clicks_var = self.ui_manager.get_variable('total_clicks')
        if total_clicks_var:
            self.config_manager.set('total_clicks', total_clicks_var.get())
        
        infinite_clicks_var = self.ui_manager.get_variable('infinite_clicks')
        if infinite_clicks_var:
            self.config_manager.set('infinite_clicks', infinite_clicks_var.get())
        
        hotkey_var = self.ui_manager.get_variable('hotkey')
        if hotkey_var:
            self.config_manager.set('hotkey', hotkey_var.get())
        
        hold_hotkey_var = self.ui_manager.get_variable('hold_hotkey')
        if hold_hotkey_var:
            self.config_manager.set('hold_hotkey', hold_hotkey_var.get())
        
        hold_switch_hotkey_var = self.ui_manager.get_variable('hold_switch_hotkey')
        if hold_switch_hotkey_var:
            self.config_manager.set('hold_switch_hotkey', hold_switch_hotkey_var.get())
        
        hold_mode_var = self.ui_manager.get_variable('hold_mode')
        if hold_mode_var:
            self.config_manager.set('hold_mode', hold_mode_var.get())
        
        hold_button_var = self.ui_manager.get_variable('hold_button')
        if hold_button_var:
            self.config_manager.set('hold_button', hold_button_var.get())
        
        hold_duration_var = self.ui_manager.get_variable('hold_duration')
        if hold_duration_var:
            self.config_manager.set('hold_duration', hold_duration_var.get())
        
        background_mode_var = self.ui_manager.get_variable('background_mode')
        if background_mode_var:
            self.config_manager.set('background_mode', background_mode_var.get())
            
    def _on_closing(self) -> None:
        """窗口关闭事件处理"""
        if self.config_manager.get('background_mode') and self.tray_manager.tray_icon:
            # 后台模式开启时，隐藏窗口而不是关闭
            self.root.withdraw()
        else:
            # 后台模式关闭时，正常退出
            self.quit_program()
            
    def _on_minimize(self) -> None:
        """窗口最小化事件处理"""
        if self.config_manager.get('background_mode') and self.tray_manager.tray_icon:
            # 后台模式开启时，最小化到系统托盘
            self.root.withdraw()
            
    def _show_window(self) -> None:
        """显示窗口"""
        self.root.deiconify()
        self.root.lift()
        
    def quit_program(self) -> None:
        """退出程序"""
        # 停止点击
        self.stop_clicking()
        # 停止热键监听
        self.hotkey_manager.stop_listening()
        # 停止系统托盘
        self.tray_manager.stop()
        # 保存配置
        self._save_current_config()
        # 关闭窗口
        self.root.destroy()
        
    def run(self) -> None:
        """运行应用程序"""
        self.root.mainloop()


def main():
    """主函数"""
    try:
        app = AutoClickerApp()
        app.run()
    except Exception as e:
        messagebox.showerror("系统错误", f"程序异常终止: {str(e)}")
        print(f"系统错误: {str(e)}")


if __name__ == "__main__":
    main()
