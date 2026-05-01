import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import ctypes
from tkinter import messagebox
from pystray import Icon as TrayIcon, Menu as TrayMenu, MenuItem as TrayMenuItem
from PIL import Image, ImageDraw

# 尝试导入keyboard模块，如果失败则尝试pynput作为替代
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

# 定义Windows API常量
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

# 导入Windows API函数
user32 = ctypes.windll.user32
# 添加类型注解以解决类型提示问题
user32.mouse_event = ctypes.windll.user32.mouse_event  # type: ignore
user32.SetThreadExecutionState = ctypes.windll.kernel32.SetThreadExecutionState  # type: ignore

# 直接使用Windows API模拟鼠标点击
def windows_api_click(button='left'):
    """使用Windows API模拟鼠标点击"""
    if button == 'left':
        # 模拟左键点击
        user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    elif button == 'right':
        # 模拟右键点击
        user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

class EnhancedAutoClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("增强版鼠标连点器")
        self.root.geometry("600x700")
        # 允许窗口调整大小
        self.root.resizable(True, True)
        
        # 设置变量
        self.clicking = False
        self.click_thread = None
        self.interval = tk.DoubleVar(value=0.1)
        self.min_interval = tk.DoubleVar(value=0.05)
        self.max_interval = tk.DoubleVar(value=0.15)
        self.random_interval = tk.BooleanVar(value=False)
        self.click_count = tk.IntVar(value=0)
        self.total_clicks = tk.IntVar(value=100)
        self.infinite_clicks = tk.BooleanVar(value=False)
        self.hotkey = tk.StringVar(value="ctrl+alt+f6")
        self.hold_hotkey = tk.StringVar(value="ctrl+alt+f7")  # 长按功能快捷键
        self.hold_switch_hotkey = tk.StringVar(value="ctrl+alt+f8")  # 切换长按按钮快捷键
        self.background_mode = tk.BooleanVar(value=True)
        self.is_capturing = False
        self.running = True  # 控制热键监听线程的运行
        self.tray_icon = None  # 系统托盘图标
        self.status_label = None  # 状态标签
        
        # 长按功能变量
        self.hold_mode = tk.BooleanVar(value=False)  # 长按模式开关
        self.hold_button = tk.StringVar(value="left")  # 长按的鼠标按钮
        self.hold_duration = tk.DoubleVar(value=2.0)  # 长按持续时间
        self.hold_start_time = 0.0  # 长按开始时间
        self.total_hold_time = 0.0  # 已长按的总时间
        self.hold_time_var = tk.StringVar(value="00:00:00")  # 格式化的长按时间显示
        
        # 创建界面
        self.create_widgets()
        
        # 启动热键监听线程
        self.hotkey_thread = threading.Thread(target=self.listen_hotkey)
        self.hotkey_thread.daemon = True
        self.hotkey_thread.start()
        
        # 绑定窗口事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.protocol("WM_ICONIFY", self.on_minimize)
        
        # 如果后台留存模式默认开启，创建系统托盘图标
        if self.background_mode.get():
            self.enable_background_mode()
            self.create_tray_icon()
        
    def create_widgets(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
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
        interval_entry = ttk.Entry(interval_frame, textvariable=self.interval, width=10)
        interval_entry.pack(side=tk.LEFT)
        
        # 间隔说明
        interval_note = ttk.Label(basic_frame, text="注意: 已优化为使用Windows API，最小实际点击间隔约为0.01秒", font= ("微软雅黑", 9), foreground="gray")
        interval_note.pack(pady=(5, 0))
        
        # 随机间隔设置
        random_frame = ttk.Frame(basic_frame)
        random_frame.pack(fill=tk.X, pady=(0, 10))
        random_check = ttk.Checkbutton(random_frame, text="随机时间间隔", variable=self.random_interval, command=self.toggle_random_interval)
        random_check.pack(side=tk.LEFT, padx=(0, 20))
        min_label = ttk.Label(random_frame, text="最小间隔:")
        min_label.pack(side=tk.LEFT, padx=(0, 5))
        min_entry = ttk.Entry(random_frame, textvariable=self.min_interval, width=8)
        min_entry.pack(side=tk.LEFT, padx=(0, 10))
        max_label = ttk.Label(random_frame, text="最大间隔:")
        max_label.pack(side=tk.LEFT, padx=(0, 5))
        max_entry = ttk.Entry(random_frame, textvariable=self.max_interval, width=8)
        max_entry.pack(side=tk.LEFT)
        
        # 长按功能设置
        hold_frame = ttk.LabelFrame(content_frame, text="长按功能", padding="10")
        hold_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        # 长按模式开关
        hold_mode_frame = ttk.Frame(hold_frame)
        hold_mode_frame.pack(fill=tk.X, pady=(0, 10))
        hold_mode_check = ttk.Checkbutton(hold_mode_frame, text="启用长按模式", variable=self.hold_mode)
        hold_mode_check.pack(side=tk.LEFT, padx=(0, 20))
        
        # 长按按钮选择
        hold_button_frame = ttk.Frame(hold_frame)
        hold_button_frame.pack(fill=tk.X, pady=(0, 10))
        hold_button_label = ttk.Label(hold_button_frame, text="长按按钮:")
        hold_button_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_button_left = ttk.Radiobutton(hold_button_frame, text="左键", variable=self.hold_button, value="left")
        hold_button_left.pack(side=tk.LEFT, padx=(0, 10))
        hold_button_right = ttk.Radiobutton(hold_button_frame, text="右键", variable=self.hold_button, value="right")
        hold_button_right.pack(side=tk.LEFT, padx=(0, 10))
        
        # 长按持续时间
        hold_duration_frame = ttk.Frame(hold_frame)
        hold_duration_frame.pack(fill=tk.X, pady=(0, 10))
        hold_duration_label = ttk.Label(hold_duration_frame, text="长按持续时间 (秒):")
        hold_duration_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_duration_entry = ttk.Entry(hold_duration_frame, textvariable=self.hold_duration, width=10)
        hold_duration_entry.pack(side=tk.LEFT)
        
        # 长按功能提示
        hold_note = ttk.Label(hold_frame, text="提示: 启用长按模式后，点击操作会变为长按指定按钮", font=("微软雅黑", 9), foreground="gray")
        hold_note.pack(pady=(5, 0))
        
        # 点击次数设置
        count_frame = ttk.LabelFrame(content_frame, text="点击次数控制", padding="10")
        count_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        # 无限次数模式
        infinite_frame = ttk.Frame(count_frame)
        infinite_frame.pack(fill=tk.X, pady=(0, 10))
        infinite_check = ttk.Checkbutton(infinite_frame, text="无限次数点击", variable=self.infinite_clicks, command=self.toggle_infinite_clicks)
        infinite_check.pack(side=tk.LEFT, padx=(0, 20))
        
        # 有限次数模式
        finite_frame = ttk.Frame(count_frame)
        finite_frame.pack(fill=tk.X)
        finite_label = ttk.Label(finite_frame, text="有限次数点击 (次数):")
        finite_label.pack(side=tk.LEFT, padx=(0, 10))
        finite_entry = ttk.Entry(finite_frame, textvariable=self.total_clicks, width=10)
        finite_entry.pack(side=tk.LEFT)
        
        # 快捷键设置
        hotkey_frame = ttk.LabelFrame(content_frame, text="快捷键设置", padding="10")
        hotkey_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        hotkey_entry_frame = ttk.Frame(hotkey_frame)
        hotkey_entry_frame.pack(fill=tk.X, pady=(0, 10))
        hotkey_label = ttk.Label(hotkey_entry_frame, text="全局快捷键:")
        hotkey_label.pack(side=tk.LEFT, padx=(0, 10))
        hotkey_entry = ttk.Entry(hotkey_entry_frame, textvariable=self.hotkey, width=20, state=tk.DISABLED)
        hotkey_entry.pack(side=tk.LEFT, padx=(0, 10))
        capture_button = ttk.Button(hotkey_entry_frame, text="捕获热键", command=self.capture_hotkey)
        capture_button.pack(side=tk.LEFT, padx=(0, 10))
        reset_hotkey_button = ttk.Button(hotkey_entry_frame, text="重置默认", command=self.reset_default_hotkey)
        reset_hotkey_button.pack(side=tk.LEFT)
        
        # 长按功能快捷键设置
        hold_hotkey_frame = ttk.Frame(hotkey_frame)
        hold_hotkey_frame.pack(fill=tk.X, pady=(0, 10))
        hold_hotkey_label = ttk.Label(hold_hotkey_frame, text="长按功能快捷键:")
        hold_hotkey_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_hotkey_entry = ttk.Entry(hold_hotkey_frame, textvariable=self.hold_hotkey, width=20, state=tk.DISABLED)
        hold_hotkey_entry.pack(side=tk.LEFT, padx=(0, 10))
        hold_capture_button = ttk.Button(hold_hotkey_frame, text="捕获热键", command=lambda: self.capture_hotkey(target="hold"))
        hold_capture_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 切换长按按钮快捷键设置
        hold_switch_hotkey_frame = ttk.Frame(hotkey_frame)
        hold_switch_hotkey_frame.pack(fill=tk.X, pady=(0, 10))
        hold_switch_hotkey_label = ttk.Label(hold_switch_hotkey_frame, text="切换长按按钮快捷键:")
        hold_switch_hotkey_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_switch_hotkey_entry = ttk.Entry(hold_switch_hotkey_frame, textvariable=self.hold_switch_hotkey, width=20, state=tk.DISABLED)
        hold_switch_hotkey_entry.pack(side=tk.LEFT, padx=(0, 10))
        hold_switch_capture_button = ttk.Button(hold_switch_hotkey_frame, text="捕获热键", command=lambda: self.capture_hotkey(target="hold_switch"))
        hold_switch_capture_button.pack(side=tk.LEFT, padx=(0, 10))
        
        hotkey_note = ttk.Label(hotkey_frame, text="提示: 点击'捕获热键'后按下要设置的快捷键组合，按回车键结束捕获", font=("微软雅黑", 9), foreground="gray")
        hotkey_note.pack(pady=(5, 5))
        
        # 紧急停用提示
        esc_note = ttk.Label(hotkey_frame, text="紧急停用: 任何时候按ESC键可立即停止点击", font=("微软雅黑", 9, "bold"), foreground="red")
        esc_note.pack(pady=(5, 5))
        
        # 后台设置
        background_frame = ttk.LabelFrame(content_frame, text="后台设置", padding="10")
        background_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        
        background_check = ttk.Checkbutton(background_frame, text="后台留存模式", variable=self.background_mode, command=self.toggle_background_mode)
        background_check.pack(side=tk.LEFT, padx=(0, 20))
        # 合并提示文字，使用换行显示
        background_note = ttk.Label(background_frame, text="开启后程序在后台运行时不会被系统自动关闭\n后台模式开启时，窗口最小化会到系统托盘，关闭窗口不会退出程序", font=("微软雅黑", 9), foreground="gray", justify=tk.LEFT)
        background_note.pack(fill=tk.X, pady=(5, 0))
        
        # 点击计数
        click_count_frame = ttk.Frame(content_frame)
        click_count_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        click_count_label = ttk.Label(click_count_frame, text="已点击次数:")
        click_count_label.pack(side=tk.LEFT, padx=(0, 10))
        click_count_value = ttk.Label(click_count_frame, textvariable=self.click_count, font=("Courier", 10))
        click_count_value.pack(side=tk.LEFT)
        
        # 长按时间计数
        hold_time_frame = ttk.Frame(content_frame)
        hold_time_frame.pack(fill=tk.X, pady=(0, 15), padx=10)
        hold_time_label = ttk.Label(hold_time_frame, text="已长按时间:")
        hold_time_label.pack(side=tk.LEFT, padx=(0, 10))
        hold_time_value = ttk.Label(hold_time_frame, textvariable=self.hold_time_var, font=("Courier", 10))
        hold_time_value.pack(side=tk.LEFT)
        
        # 按钮框架
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(fill=tk.X, pady=(0, 20), padx=10)
        
        # 开始按钮
        start_button = ttk.Button(button_frame, text="开始", command=self.start_clicking)
        start_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 停止按钮
        stop_button = ttk.Button(button_frame, text="停止", command=self.stop_clicking)
        stop_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 重置按钮
        reset_button = ttk.Button(button_frame, text="重置", command=self.reset_clicker)
        reset_button.pack(side=tk.LEFT)
        
        # 右下角状态标识
        self.status_label = ttk.Label(self.root, text="连点器未启用", foreground="blue", font=("微软雅黑", 10, "bold"))
        self.status_label.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-20, y=-20)
        
    def create_tray_icon(self):
        """创建系统托盘图标"""
        # 创建一个简单的图标
        def create_image():
            width = 64
            height = 64
            image = Image.new('RGB', (width, height), (0, 128, 255))
            draw = ImageDraw.Draw(image)
            draw.ellipse((16, 16, 48, 48), fill=(255, 255, 255))
            draw.ellipse((24, 24, 40, 40), fill=(0, 128, 255))
            return image
        
        # 创建菜单
        menu = TrayMenu(
            TrayMenuItem('显示窗口', self.show_window),
            TrayMenuItem('停止点击', self.stop_clicking, checked=lambda item: self.clicking),
            TrayMenuItem('退出', self.quit_program)
        )
        
        # 创建图标
        self.tray_icon = TrayIcon('增强版鼠标连点器', create_image(), menu=menu)
        
        # 启动托盘图标线程
        tray_thread = threading.Thread(target=self.tray_icon.run)
        tray_thread.daemon = True
        tray_thread.start()
    
    def toggle_random_interval(self):
        pass
    
    def toggle_infinite_clicks(self):
        pass
    
    def toggle_background_mode(self):
        if self.background_mode.get():
            self.enable_background_mode()
            # 后台模式开启时创建系统托盘图标
            if self.tray_icon is None:
                self.create_tray_icon()
        else:
            self.disable_background_mode()
            # 后台模式关闭时，停止系统托盘图标
            if self.tray_icon:
                self.tray_icon.stop()
                self.tray_icon = None
    
    def capture_hotkey(self, target="global"):
        """捕获用户按下的热键"""
        self.is_capturing = True
        captured_keys = []
        
        # 创建捕获提示窗口
        capture_window = tk.Toplevel(self.root)
        capture_window.title("捕获热键")
        capture_window.geometry("300x100")
        capture_window.resizable(False, False)
        capture_window.transient(self.root)
        capture_window.grab_set()
        
        # 提示信息
        capture_label = ttk.Label(capture_window, text="请按下要设置的快捷键组合，按回车键结束捕获", padding=20)
        capture_label.pack(fill=tk.BOTH, expand=tk.YES)
        
        # 捕获线程
        def capture_thread_func():
            nonlocal captured_keys
            
            # 移除现有的热键监听，避免干扰
            keyboard.unhook_all()
            
            # 监听键盘事件
            while self.is_capturing:
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
                            self.is_capturing = False
                            capture_window.after(100, capture_window.destroy)
                            
                            # 格式化热键
                            if captured_keys:
                                # 移除回车键
                                if 'enter' in captured_keys:
                                    captured_keys.remove('enter')
                                # 排序按键（ctrl, alt, shift 在前）
                                modifiers = ['ctrl', 'alt', 'shift', 'win']
                                sorted_keys = sorted(captured_keys, key=lambda k: (k not in modifiers, k))
                                hotkey_str = '+'.join(sorted_keys)
                                
                                # 根据目标设置不同的热键
                                if target == "global":
                                    self.hotkey.set(hotkey_str)
                                    messagebox.showinfo("提示", f"全局热键 '{hotkey_str}' 设置成功！")
                                elif target == "hold":
                                    self.hold_hotkey.set(hotkey_str)
                                    messagebox.showinfo("提示", f"长按功能热键 '{hotkey_str}' 设置成功！")
                                elif target == "hold_switch":
                                    self.hold_switch_hotkey.set(hotkey_str)
                                    messagebox.showinfo("提示", f"切换长按按钮热键 '{hotkey_str}' 设置成功！")
                                
                                # 更新热键
                                self.update_hotkey()
                            else:
                                messagebox.showwarning("警告", "未捕获到任何按键")
                                # 重新注册热键
                                self.update_hotkey()
                except Exception as e:
                    # 只捕获特定的异常，而不是所有异常
                    # 这里我们仍然使用广泛的异常捕获，因为keyboard库的异常类型可能不明确
                    # 但至少我们记录了异常信息
                    print(f"捕获热键时发生错误: {e}")
                    pass
        
        # 启动捕获线程
        capture_thread = threading.Thread(target=capture_thread_func)
        capture_thread.daemon = True
        capture_thread.start()
    
    def update_hotkey(self):
        # 移除旧热键
        keyboard.unhook_all()
        # 添加新热键
        try:
            keyboard.add_hotkey(self.hotkey.get(), self.toggle_clicking, suppress=True)
            # 添加长按功能快捷键
            keyboard.add_hotkey(self.hold_hotkey.get(), self.toggle_hold_clicking, suppress=True)
            # 添加切换长按按钮快捷键
            keyboard.add_hotkey(self.hold_switch_hotkey.get(), self.switch_hold_button, suppress=True)
            # 添加ESC紧急停止热键，但只在连点器启用时生效
            keyboard.add_hotkey('esc', lambda: self.stop_clicking() if self.clicking else None, suppress=False)
        except Exception as ex:
            messagebox.showerror("错误", f"热键设置失败: {ex}")
    
    def reset_default_hotkey(self):
        """重置快捷键为默认值"""
        default_hotkey = "ctrl+alt+f6"
        self.hotkey.set(default_hotkey)
        # 更新热键
        self.update_hotkey()
        messagebox.showinfo("提示", f"快捷键已重置为默认值: '{default_hotkey}'")
    
    def listen_hotkey(self):
        """优化的热键监听线程，减少CPU占用"""
        # 初始热键
        try:
            keyboard.add_hotkey(self.hotkey.get(), self.toggle_clicking, suppress=True)
            # 添加长按功能快捷键
            keyboard.add_hotkey(self.hold_hotkey.get(), self.toggle_hold_clicking, suppress=True)
            # 添加切换长按按钮快捷键
            keyboard.add_hotkey(self.hold_switch_hotkey.get(), self.switch_hold_button, suppress=True)
            # 添加ESC紧急停止热键，但只在连点器启用时生效
            keyboard.add_hotkey('esc', lambda: self.stop_clicking() if self.clicking else None, suppress=False)
        except Exception as e:
            # 只捕获特定的异常，而不是所有异常
            # 这里我们仍然使用广泛的异常捕获，因为keyboard库的异常类型可能不明确
            # 但至少我们记录了异常信息
            print(f"设置热键时发生错误: {e}")
            pass
        
        # 保持线程运行，但使用较长的睡眠时间减少CPU占用
        while self.running:
            time.sleep(1)  # 增加睡眠时间，从0.1秒增加到1秒
    
    @staticmethod
    def enable_background_mode():
        # 防止系统进入休眠
        # 使用ctypes.windll.kernel32直接调用
        # 忽略类型提示错误，因为ctypes的类型提示不完善
        kernel32 = ctypes.windll.kernel32
        kernel32.SetThreadExecutionState(0x80000002)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED

    @staticmethod
    def disable_background_mode():
        # 恢复系统默认状态
        # 使用ctypes.windll.kernel32直接调用
        # 忽略类型提示错误，因为ctypes的类型提示不完善
        kernel32 = ctypes.windll.kernel32
        kernel32.SetThreadExecutionState(0x80000000)  # ES_CONTINUOUS
    
    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.click_count.set(0)
            # 重置长按时间
            if self.hold_mode.get():
                self.hold_start_time = time.time()
                self.total_hold_time = 0.0
                self.hold_time_var.set("00:00:00")
            if self.status_label:
                self.status_label.config(text="连点器已开启", foreground="green")
            # 更新系统托盘菜单
            if self.tray_icon:
                self.tray_icon.update_menu()
            self.click_thread = threading.Thread(target=self.click_loop)
            self.click_thread.daemon = True
            self.click_thread.start()
    
    def stop_clicking(self):
        if self.clicking:
            self.clicking = False
            if self.status_label:
                self.status_label.config(text="连点器未启用", foreground="blue")
            # 更新系统托盘菜单
            if self.tray_icon:
                self.tray_icon.update_menu()
    
    def reset_clicker(self):
        self.stop_clicking()
        self.click_count.set(0)
        # 重置已长按时间
        self.total_hold_time = 0.0
        self.hold_time_var.set("00:00:00")
        if self.status_label:
            self.status_label.config(text="连点器未启用", foreground="blue")
    
    def toggle_clicking(self, _event=None):
        if self.clicking:
            self.stop_clicking()
        else:
            # 保持当前长按模式设置，不强制切换回点按功能
            self.start_clicking()
    
    def toggle_hold_clicking(self, _event=None):
        """通过快捷键切换长按模式"""
        # 只切换长按模式的状态，不启动连点器
        current_state = self.hold_mode.get()
        self.hold_mode.set(not current_state)

    def switch_hold_button(self, _event=None):
        """通过快捷键切换长按的鼠标按钮"""
        current_button = self.hold_button.get()
        new_button = "right" if current_button == "left" else "left"
        self.hold_button.set(new_button)
    
    def get_interval(self):
        if self.random_interval.get():
            return random.uniform(self.min_interval.get(), self.max_interval.get())
        else:
            return self.interval.get()
    
    def click_loop(self):
        count = 0
        
        while self.clicking:
            # 检查是否达到点击次数限制
            if not self.infinite_clicks.get() and count >= self.total_clicks.get():
                break
            
            # 执行点击或长按
            if self.hold_mode.get():
                # 更新长按时间
                self.update_hold_time()
                # 执行长按
                self.perform_hold()
                # 如果是无限长按（持续时间为0），则跳出循环
                if self.hold_duration.get() <= 0:
                    break
            else:
                # 执行普通点击（使用Windows API提高速度）
                windows_api_click()
            
            count += 1
            self.click_count.set(count)
            
            # 获取目标间隔时间
            target_interval = self.get_interval()
            
            # 优化时间控制逻辑
            if target_interval > 0:
                # 对于非常小的间隔（小于1ms），直接跳过sleep
                # 因为time.sleep()本身有开销，而且在Windows上最小精度约为1ms
                if target_interval > 0.001:
                    # 对于较大的间隔，使用sleep
                    time.sleep(target_interval)
                # 对于小间隔，我们不使用sleep，直接进行下一次点击
                # 这样可以最大化点击速度
        
        if self.clicking:
            self.clicking = False
            if self.status_label:
                self.status_label.config(text="连点器未启用", foreground="blue")
            # 更新系统托盘菜单
            if self.tray_icon:
                self.tray_icon.update_menu()
    
    def update_hold_time(self):
        """更新长按时间"""
        if self.hold_mode.get() and self.clicking:
            # 计算已长按的时间
            current_time = time.time()
            self.total_hold_time = current_time - self.hold_start_time
            # 格式化时间
            formatted_time = self.format_time(self.total_hold_time)
            self.hold_time_var.set(formatted_time)
    
    @staticmethod
    def format_time(seconds):
        """将秒数格式化为时:分:秒格式"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}:{minutes}:{secs}"
    
    def perform_hold(self):
        """执行长按操作"""
        button = self.hold_button.get()
        duration = self.hold_duration.get()
        
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
    
    def on_minimize(self):
        """窗口最小化事件处理"""
        if self.background_mode.get() and self.tray_icon:
            # 后台模式开启时，最小化到系统托盘
            self.root.withdraw()
        
    def on_closing(self):
        """窗口关闭事件处理"""
        if self.background_mode.get() and self.tray_icon:
            # 后台模式开启时，隐藏窗口而不是关闭
            self.root.withdraw()
        else:
            # 后台模式关闭时，正常退出
            self.quit_program()
    
    def show_window(self):
        """显示窗口"""
        self.root.deiconify()
        self.root.lift()
    
    def quit_program(self):
        """退出程序"""
        self.running = False
        # 移除所有热键
        keyboard.unhook_all()
        # 停止系统托盘
        if self.tray_icon:
            self.tray_icon.stop()
        # 关闭窗口
        self.root.destroy()

if __name__ == "__main__":
    # 使用不同的变量名以避免隐藏外部作用域的名称
    main_root = tk.Tk()
    app = EnhancedAutoClicker(main_root)
    main_root.mainloop()