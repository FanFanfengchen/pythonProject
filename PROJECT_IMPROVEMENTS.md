# Python 学习项目整理说明

## 📁 项目结构

本项目是 Python 学习和练习的记录，按功能分类整理如下：

```
pythonProject/
├── 核心/                    # 核心功能模块（类与对象练习）
│   ├── 简单的数学运算.py     # 计算器类
│   ├── 句子的基本操作.py     # 字符串处理类
│   └── 供购物清单的管理.py   # 购物清单类
├── 测试/                    # 单元测试
│   ├── test_calculator.py
│   ├── test_sentence.py
│   └── test_shopping_list.py
├── 基础学习/                # Python 基础语法学习
│   ├── 变量.py
│   ├── 字符串.py
│   ├── 列表.py
│   ├── 字典.py
│   ├── 运算法则.py
│   ├── 程序设计入门.py
│   └── ...
├── 教程练习/                # 教程配套练习
├── 旅途的开始/              # 早期练习代码
├── 数学算法/                # 算法练习
├── 图形界面/                # GUI 编程（tkinter）
├── 游戏/                    # 小游戏项目
├── 工具/                    # 实用工具
├── 认证/                    # 登录认证相关
├── Python数据分析/          # 数据分析学习
├── 爬虫学习.py              # 爬虫入门
├── scrape_douban.py         # 豆瓣爬虫
├── 增强版鼠标连点器.py       # GUI 工具
├── 练习.py                  # 函数式编程练习
├── 用Beautiful Soup解析HTML内容.py
├── README.md                # 项目说明
├── config.json              # 爬虫配置
└── requirements.txt         # 依赖列表
```

## ✅ 已完成的整理

### 1. 删除的无用文件
- ~~test_import.py~~（拼写错误）
- ~~compile_commands.json~~（编译配置）
- ~~main.c~~（C语言文件）
- ~~demo.html / script.js / styles.css~~（前端文件）
- ~~工具/比如说.py~~（临时文件）
- ~~工具/哦.py~~（临时文件）
- ~~基础学习/列表（学习中）.py~~（临时文件）
- ~~基础学习/字体（学习中）.py~~（临时文件）

### 2. 添加的文件
- `核心/__init__.py` - 使核心模块可作为包导入
- `测试/__init__.py` - 使测试模块可作为包导入
- `requirements.txt` - 项目依赖列表

## 📝 文件分类说明

| 文件夹 | 内容说明 | 学习重点 |
|--------|----------|----------|
| 核心/ | 面向对象编程练习 | 类、对象、封装 |
| 测试/ | 单元测试练习 | unittest 框架 |
| 基础学习/ | Python 基础语法 | 变量、数据类型、控制流 |
| 数学算法/ | 算法实现 | 逻辑、数学运算 |
| 图形界面/ | GUI 编程 | tkinter 库 |
| 游戏/ | 小游戏项目 | 综合应用 |
| 爬虫学习.py | 网络爬虫入门 | requests、BeautifulSoup |
| 增强版鼠标连点器.py | 高级 GUI 工具 | tkinter、线程、Windows API |

## 🔧 依赖安装

如需运行相关代码，安装依赖：

```bash
pip install -r requirements.txt
```

主要依赖：
- requests - HTTP 请求
- beautifulsoup4 - HTML 解析
- keyboard / pynput - 键盘控制
- pystray - 系统托盘
- Pillow - 图像处理

## ⚠️ 注意事项

1. **增强版鼠标连点器.py** 使用 Windows API，仅在 Windows 系统有效
2. 部分代码需要管理员权限（如 keyboard 模块）
3. 爬虫代码请遵守网站 robots.txt 和相关法律法规

---
*整理日期：2026年4月6日*
