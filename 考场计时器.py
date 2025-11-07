import sys
import json
from datetime import datetime, timedelta
from tkinter import messagebox, Tk, Label, Entry, Button
from pathlib import Path

if sys.platform == "win32":
    import winsound

CONFIG_FILE = "exam_config.json"
HISTORY_FILE = "exam_history.log"

class ExamManager:
    """考试管理核心类"""

    def __init__(self):
        self.exam_queue = []
        self.current_exam = None
        self.history = []
        self._load_config()

    def _load_config(self):
        """加载JSON配置文件"""
        try:
            config_path = Path(CONFIG_FILE)
            if not config_path.exists():
                self._create_sample_config()

            with open(config_path, 'r', encoding='utf-8') as f:
                exams = json.load(f)
                self.exam_queue = sorted(
                    [self._parse_exam(e) for e in exams],
                    key=lambda x: x["start_time"]
                )
        except Exception as e:
            messagebox.showerror("配置错误", f"配置文件加载失败: {str(e)}")
            sys.exit(1)

    @staticmethod
    def _parse_exam(exam_data):
        """解析考试数据"""
        return {
            "subject": exam_data["subject"],
            "start_time": datetime.strptime(
                exam_data["start_time"], "%Y-%m-%d %H:%M"
            ),
            "duration": exam_data["duration"] * 60  # 转换为秒
        }

    @staticmethod
    def _create_sample_config():
        """创建示例配置文件"""
        sample_data = [
            {
                "subject": "数学期末考试",
                "start_time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "duration": 120
            },
            {
                "subject": "英语模拟考",
                "start_time": (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M"),
                "duration": 90
            }
        ]
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, indent=2, ensure_ascii=False)

    def get_next_exam(self):
        """获取下一个有效考试"""
        now = datetime.now()
        for exam in self.exam_queue:
            if exam["start_time"] > now - timedelta(seconds=exam["duration"]):
                return exam
        return None

    def record_history(self, exam, status):
        """记录考试历史"""
        entry = {
            "subject": exam["subject"],
            "start": exam["start_time"].isoformat(),
            "end": datetime.now().isoformat(),
            "duration": exam["duration"],
            "status": status
        }
        self.history.append(entry)
        self._save_history()

    def _save_history(self):
        """保存历史记录到文件"""
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(self.history[-1], ensure_ascii=False) + '\n')


class EnhancedExamTimer(ExamManager):
    _SOUND_MAP = {
        "start": lambda: winsound.Beep(800, 500) if sys.platform == "win32" else None,
        "end": lambda: winsound.Beep(2000, 1000) if sys.platform == "win32" else None,
    }

    def __init__(self):
        super().__init__()
        self._running = False
        self.root = Tk()
        self.root.title("智能考场管理系统 v3.0")
        self.root.geometry("400x300")

        self._setup_ui()
        self._init_exam()

    def _setup_ui(self):
        """初始化增强界面"""
        Label(self.root, text="当前时间:").grid(row=0, column=0, padx=10, pady=5)
        self.current_time_label = Label(self.root, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.current_time_label.grid(row=0, column=1, padx=10, pady=5)

        Label(self.root, text="考试科目:").grid(row=1, column=0, padx=10, pady=5)
        self.subject_entry = Entry(self.root)
        self.subject_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.root, text="开始时间:").grid(row=2, column=0, padx=10, pady=5)
        self.start_time_entry = Entry(self.root)
        self.start_time_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.root, text="结束时间:").grid(row=3, column=0, padx=10, pady=5)
        self.end_time_entry = Entry(self.root)
        self.end_time_entry.grid(row=3, column=1, padx=10, pady=5)

        Button(self.root, text="开始考试", command=self._start_exam_timer).grid(row=4, column=0, columnspan=2, pady=10)
        Button(self.root, text="暂停/继续", command=self.toggle_pause).grid(row=5, column=0, columnspan=2, pady=5)
        Button(self.root, text="退出", command=self._safe_shutdown).grid(row=6, column=0, columnspan=2, pady=5)

    def _start_exam_timer(self):
        """启动考试计时"""
        try:
            subject = self.subject_entry.get()
            start_time = datetime.strptime(self.start_time_entry.get(), "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(self.end_time_entry.get(), "%Y-%m-%d %H:%M")
            duration = (end_time - start_time).total_seconds()

            self.current_exam = {
                "subject": subject,
                "start_time": start_time,
                "duration": duration
            }

            self.play_sound("start")
            self._running = True
            self.record_history(self.current_exam, "started")
            self.time_left = duration
            self._update_loop()
        except Exception as inner_e:
            messagebox.showerror("输入错误", f"输入格式错误: {str(inner_e)}")
            print(f"输入错误: {str(inner_e)}")  # 打印详细的错误信息到控制台

    def _update_loop(self):
        """主计时循环"""
        if not self._running or self.time_left <= 0:
            return

        self._update_display()
        self.time_left -= 1

        if self.time_left == 0:
            self._handle_exam_end()
        else:
            self.root.after(1000, self._update_loop)

    def _handle_exam_end(self):
        """处理考试结束"""
        self.play_sound("end")
        self.record_history(self.current_exam, "completed")
        messagebox.showinfo(
            "考试结束",
            f"{self.current_exam['subject']} 已完成！\n"
            f"时长：{self.current_exam['duration'] // 60}分钟"
        )
        self._init_exam()

    def toggle_pause(self):
        """暂停/继续控制"""
        self._running = not self._running
        if self._running:
            self._update_loop()

    def _update_display(self):
        """更新所有显示组件"""
        # 考试信息
        self.current_time_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if self.current_exam:
            info_text = [
                f"当前科目：{self.current_exam['subject']}",
                f"计划时间：{self.current_exam['start_time'].strftime('%Y-%m-%d %H:%M')}",
                f"剩余时间：{self.time_left // 60:02d}:{self.time_left % 60:02d}"
            ]
            self.current_time_label.config(text="\n".join(info_text))

    def play_sound(self, sound_type):
        """跨平台声音处理"""
        if sys.platform != "win32":
            return
        if sound_func := self._SOUND_MAP.get(sound_type):
            try:
                sound_func()
            except Exception as sound_e:
                print(f"声音播放失败：{str(sound_e)}")

    def _safe_shutdown(self):
        """安全关闭程序"""
        self._running = False
        if self.current_exam:
            self.record_history(self.current_exam, "interrupted")
        self.root.destroy()

    def _init_exam(self):
        """初始化考试状态"""
        self.current_exam = None
        self.time_left = 0
        self._update_display()


if __name__ == "__main__":
    try:
        app = EnhancedExamTimer()
        app.root.mainloop()
    except Exception as main_e:
        messagebox.showerror("系统错误", f"程序异常终止: {str(main_e)}")
        print(f"系统错误: {str(main_e)}")  # 打印详细的错误信息到控制台
