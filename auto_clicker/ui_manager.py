"""UI管理模块

负责UI界面的构建和更新，提供用户交互界面。
"""

import tkinter as tk
from tkinter import ttk
from typing import Dict, Any


class UIManager:
    """UI管理类"""
    
    def __init__(self, root: tk.Tk, config_manager: Any):
        """
        初始化UI管理器
        
        Args:
            root: 主窗口
            config_manager: 配置管理器
        """
        self.root = root
        self.config = config_manager
        self.widgets: Dict[str, Any] = {}
        self.variables: Dict[str, Any] = {}
        self._initialize_variables()
        
    def _initialize_variables(self) -> None:
        """初始化UI变量"""
        self.variables['interval'] = tk.DoubleVar(value=self.config.get('interval', 0.1))
        self.variables['min_interval'] = tk.DoubleVar(value=self.config.get('min_interval', 0.05))
        self.variables['max_interval'] = tk.DoubleVar(value=self.config.get('max_interval', 0.15))
        self.variables['random_interval'] = tk.BooleanVar(value=self.config.get('random_interval', False))
        self.variables['click_count'] = tk.IntVar(value=0)
        self.variables['total_clicks'] = tk.IntVar(value=self.config.get('total_clicks', 100))
        self.variables['infinite_clicks'] = tk.BooleanVar(value=self.config.get('infinite_clicks', False))
        self.variables['hotkey'] = tk.StringVar(value=self.config.get('hotkey', 'ctrl+alt+f6'))
        self.variables['hold_hotkey'] = tk.StringVar(value=self.config.get('hold_hotkey', 'ctrl+alt+f7'))
        self.variables['hold_switch_hotkey'] = tk.StringVar(value=self.config.get('hold_switch_hotkey', 'ctrl+alt+f8'))
        self.variables['background_mode'] = tk.BooleanVar(value=self.config.get('background_mode', True))
        self.variables['hold_mode'] = tk.BooleanVar(value=self.config.get('hold_mode', False))
        self.variables['hold_button'] = tk.StringVar(value=self.config.get('hold_button', 'left'))
        self.variables['hold_duration'] = tk.DoubleVar(value=self.config.get('hold_duration', 2.0))
        self.variables['hold_time_var'] = tk.StringVar(value="00:00:00")
        
    def create_widgets(self) -> None:
        """创建所有UI组件"""
        self._create_main_frame()
        self._create_basic_settings()
        self._create_hold_settings()
        self._create_count_settings()
        self._create_hotkey_settings()
        self._create_background_settings()
        self._create_status_display()
        self._create_control_buttons()
        
    def _create_main_frame(self) -> None:
        """创建主框架"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.widgets['main_frame'] = main_frame
        
        # 创建画布和滚动条
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # 创建内容框架
        content_frame = ttk.Frame(canvas)
        content_window = canvas.create_window((0, 0), window=content_frame, anchor="nw", tags="content")
        
        # 配置画布大小变化时的行为
        def on_content_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        def on_canvas_configure(event):
            # 确保内容框架宽度与画布宽度匹配
            canvas.itemconfig(content_window, width=event.width - 20)
        
        content_frame.bind("<Configure>", on_content_configure)
        canvas.bind("<Configure>", on_canvas_configure)
        
        # 添加鼠标滚轮事件处理
        def on_mouse_wheel(event):
            # 响应鼠标滚轮事件
            canvas.yview_scroll(-1 * (event.delta // 120), "units")
        
        # 绑定鼠标滚轮事件
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)
        
        self.widgets['content_frame'] = content_frame
        
    def _create_basic_settings(self) -> None:
        """创建基本设置区域"""
        content_frame = self.widgets['content_frame']
        
        # 标题
        title_label = ttk.Label(content_frame, text="增强版鼠标连点器", font=("微软雅黑", 16, "bold"))
        title_label.pack(pady=(10, 20))
        
        # 基本设置框架
        basic_frame = ttk.LabelFrame(content_frame, text="基本设置", padding="10")
        basic_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        # 间隔设置
        interval_frame = ttk.Frame(basic_frame)
        interval_frame.pack(fill=tk.X, pady=(0, 10))
        interval_label = ttk.Label(interval_frame, text="点击间隔 (秒):")
        interval_label.pack(side=tk.LEFT, padx=(0, 10))
        interval_entry = ttk.Entry(interval_frame, textvariable=self.variables['interval'], width=10)
        interval_entry.pack(side=tk.LEFT)
        
        # 间隔说明
        interval_note = ttk.Label(basic_frame, text="注意: 已优化为使用Windows API，最小实际点击间隔约为0.01秒", 
                                 font=("微软雅黑", 9), foreground="gray")
        interval_note.pack(pady=(5, 0))
        
        # 随机间隔设置
        random_frame = ttk.Frame(basic_frame)
        random_frame.pack(fill=tk.X, pady=(0, 10))
        random_check = ttk.Checkbutton(random_frame, text="随机时间间隔", 
                                      variable=self.variables['random_interval'])
        random_check.pack(side=tk.LEFT, padx=(0, 20))
        min_label = ttk.Label(random_frame, text="最小间隔:")
        min_label.pack(side=tk.LEFT, padx=(0, 5))
        min_entry = ttk.Entry(random_frame, textvariable=self.variables['min_interval'], width=8)
        min_entry.pack(side=tk.LEFT, padx=(0, 10))
        max_label = ttk.Label(random_frame, text="最大间隔:")
        max_label.pack(side=tk.LEFT, padx=(0, 5))
        max_entry = ttk.Entry(random_frame, textvariable=self.variables['max_interval'], width=8)
        max_entry.pack(side=tk.LEFT)
        
    def _create_hold_settings(self) -> None:
        """创建长按功能设置区域"""
        content_frame = self.widgets['content_frame']
        
        # 长按功能设置
        hold_frame = ttk.LabelFrame(content_frame, text="长按功能", padding="10")
        hold_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        # 长按模式开关
        hold_mode_frame = ttk.Frame(hold_frame)
        hold_mode_frame.pack(fill=tk.X, pady=(0, 10))
        hold_mode_check = ttk.Checkbutton(hold_mode_frame, text="启用长按模式", 
                                         variable=self.variables['hold_mode'])
        hold_mode_check.pack(side=tk.LEFT, padx=(0, 20))
        
        # 长按按钮选择
        hold_button_frame = ttk.Frame(hold_frame)
        hold_button_frame.pack(fill=tk.X, pady=(0, 10))
        hold_button_label = ttk.Label(hold_button_frame, text="长按按钮:")
        hold_button_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_button_left = ttk.Radiobutton(hold_button_frame, text="左键", 
                                          variable=self.variables['hold_button'], value="left")
        hold_button_left.pack(side=tk.LEFT, padx=(0, 10))
        hold_button_right = ttk.Radiobutton(hold_button_frame, text="右键", 
                                           variable=self.variables['hold_button'], value="right")
        hold_button_right.pack(side=tk.LEFT, padx=(0, 10))
        
        # 长按持续时间
        hold_duration_frame = ttk.Frame(hold_frame)
        hold_duration_frame.pack(fill=tk.X, pady=(0, 10))
        hold_duration_label = ttk.Label(hold_duration_frame, text="长按持续时间 (秒):")
        hold_duration_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_duration_entry = ttk.Entry(hold_duration_frame, 
                                       textvariable=self.variables['hold_duration'], width=10)
        hold_duration_entry.pack(side=tk.LEFT)
        
        # 长按功能提示
        hold_note = ttk.Label(hold_frame, text="提示: 启用长按模式后，点击操作会变为长按指定按钮", 
                             font=("微软雅黑", 9), foreground="gray")
        hold_note.pack(pady=(5, 0))
        
    def _create_count_settings(self) -> None:
        """创建点击次数设置区域"""
        content_frame = self.widgets['content_frame']
        
        # 点击次数设置
        count_frame = ttk.LabelFrame(content_frame, text="点击次数控制", padding="10")
        count_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        # 无限次数模式
        infinite_frame = ttk.Frame(count_frame)
        infinite_frame.pack(fill=tk.X, pady=(0, 10))
        infinite_check = ttk.Checkbutton(infinite_frame, text="无限次数点击", 
                                        variable=self.variables['infinite_clicks'])
        infinite_check.pack(side=tk.LEFT, padx=(0, 20))
        
        # 有限次数模式
        finite_frame = ttk.Frame(count_frame)
        finite_frame.pack(fill=tk.X)
        finite_label = ttk.Label(finite_frame, text="有限次数点击 (次数):")
        finite_label.pack(side=tk.LEFT, padx=(0, 10))
        finite_entry = ttk.Entry(finite_frame, textvariable=self.variables['total_clicks'], width=10)
        finite_entry.pack(side=tk.LEFT)
        
    def _create_hotkey_settings(self) -> None:
        """创建快捷键设置区域"""
        content_frame = self.widgets['content_frame']
        
        # 快捷键设置
        hotkey_frame = ttk.LabelFrame(content_frame, text="快捷键设置", padding="10")
        hotkey_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        hotkey_entry_frame = ttk.Frame(hotkey_frame)
        hotkey_entry_frame.pack(fill=tk.X, pady=(0, 10))
        hotkey_label = ttk.Label(hotkey_entry_frame, text="全局快捷键:")
        hotkey_label.pack(side=tk.LEFT, padx=(0, 10))
        hotkey_entry = ttk.Entry(hotkey_entry_frame, textvariable=self.variables['hotkey'], 
                                width=20, state=tk.DISABLED)
        hotkey_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        # 长按功能快捷键设置
        hold_hotkey_frame = ttk.Frame(hotkey_frame)
        hold_hotkey_frame.pack(fill=tk.X, pady=(0, 10))
        hold_hotkey_label = ttk.Label(hold_hotkey_frame, text="长按功能快捷键:")
        hold_hotkey_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_hotkey_entry = ttk.Entry(hold_hotkey_frame, textvariable=self.variables['hold_hotkey'], 
                                     width=20, state=tk.DISABLED)
        hold_hotkey_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        # 切换长按按钮快捷键设置
        hold_switch_hotkey_frame = ttk.Frame(hotkey_frame)
        hold_switch_hotkey_frame.pack(fill=tk.X, pady=(0, 10))
        hold_switch_hotkey_label = ttk.Label(hold_switch_hotkey_frame, text="切换长按按钮快捷键:")
        hold_switch_hotkey_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_switch_hotkey_entry = ttk.Entry(hold_switch_hotkey_frame, 
                                           textvariable=self.variables['hold_switch_hotkey'], 
                                           width=20, state=tk.DISABLED)
        hold_switch_hotkey_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        hotkey_note = ttk.Label(hotkey_frame, text="提示: 点击'捕获热键'后按下要设置的快捷键组合，按回车键结束捕获", 
                               font=("微软雅黑", 9), foreground="gray")
        hotkey_note.pack(pady=(5, 5))
        
        # 紧急停用提示
        esc_note = ttk.Label(hotkey_frame, text="紧急停用: 任何时候按ESC键可立即停止点击", 
                           font=("微软雅黑", 9, "bold"), foreground="red")
        esc_note.pack(pady=(5, 5))
        
    def _create_background_settings(self) -> None:
        """创建后台设置区域"""
        content_frame = self.widgets['content_frame']
        
        # 后台设置
        background_frame = ttk.LabelFrame(content_frame, text="后台设置", padding="10")
        background_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        background_check = ttk.Checkbutton(background_frame, text="后台留存模式", 
                                         variable=self.variables['background_mode'])
        background_check.pack(side=tk.LEFT, padx=(0, 20))
        # 合并提示文字，使用换行显示
        background_note = ttk.Label(background_frame, 
                                  text="开启后程序在后台运行时不会被系统自动关闭\n后台模式开启时，窗口最小化会到系统托盘，关闭窗口不会退出程序", 
                                  font=("微软雅黑", 9), foreground="gray", justify=tk.LEFT)
        background_note.pack(fill=tk.X, pady=(5, 0))
        
    def _create_status_display(self) -> None:
        """创建状态显示区域"""
        content_frame = self.widgets['content_frame']
        
        # 点击计数
        click_count_frame = ttk.Frame(content_frame)
        click_count_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        click_count_label = ttk.Label(click_count_frame, text="已点击次数:")
        click_count_label.pack(side=tk.LEFT, padx=(0, 10))
        click_count_value = ttk.Label(click_count_frame, textvariable=self.variables['click_count'], 
                                     font=("Courier", 10))
        click_count_value.pack(side=tk.LEFT)
        
        # 长按时间计数
        hold_time_frame = ttk.Frame(content_frame)
        hold_time_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        hold_time_label = ttk.Label(hold_time_frame, text="已长按时间:")
        hold_time_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_time_value = ttk.Label(hold_time_frame, textvariable=self.variables['hold_time_var'], 
                                   font=("Courier", 10))
        hold_time_value.pack(side=tk.LEFT)
        
        # 右下角状态标识
        status_label = ttk.Label(self.root, text="连点器未启用", foreground="blue", 
                               font=("微软雅黑", 10, "bold"))
        status_label.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-20, y=-20)
        self.widgets['status_label'] = status_label
        
    def _create_control_buttons(self) -> None:
        """创建控制按钮区域"""
        content_frame = self.widgets['content_frame']
        
        # 按钮框架
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(fill=tk.X, pady=(0, 20), padx=10)
        
        # 开始按钮
        start_button = ttk.Button(button_frame, text="开始")
        start_button.pack(side=tk.LEFT, padx=(0, 10))
        self.widgets['start_button'] = start_button
        
        # 停止按钮
        stop_button = ttk.Button(button_frame, text="停止")
        stop_button.pack(side=tk.LEFT, padx=(0, 10))
        self.widgets['stop_button'] = stop_button
        
        # 重置按钮
        reset_button = ttk.Button(button_frame, text="重置")
        reset_button.pack(side=tk.LEFT)
        self.widgets['reset_button'] = reset_button
        
    def update_status(self, status: str, color: str = "blue") -> None:
        """更新状态显示
        
        Args:
            status: 状态文本
            color: 状态颜色
        """
        if 'status_label' in self.widgets:
            self.widgets['status_label'].config(text=status, foreground=color)
        
    def update_click_count(self, count: int) -> None:
        """更新点击计数
        
        Args:
            count: 点击次数
        """
        self.variables['click_count'].set(count)
        
    def update_hold_time(self, time_str: str) -> None:
        """更新长按时间
        
        Args:
            time_str: 时间字符串
        """
        self.variables['hold_time_var'].set(time_str)
        
    def get_variable(self, name: str) -> Any:
        """获取UI变量
        
        Args:
            name: 变量名
            
        Returns:
            变量值
        """
        return self.variables.get(name)
        
    def get_widget(self, name: str) -> Any:
        """获取UI组件
        
        Args:
            name: 组件名
            
        Returns:
            组件对象
        """
        return self.widgets.get(name)
