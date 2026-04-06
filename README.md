# Python 项目整理 🐍

<div align="center">
  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Python%20project%20logo%20with%20colorful%20code%20snippets%20and%20modern%20design&image_size=square" alt="Python Project Logo" width="200">
  
  <p align="center">
    <a href="#项目概述"><img src="https://img.shields.io/badge/项目-概述-blue" alt="项目概述"></a>
    <a href="#技术栈"><img src="https://img.shields.io/badge/技术-栈-orange" alt="技术栈"></a>
    <a href="#核心功能模块"><img src="https://img.shields.io/badge/核心-功能-green" alt="核心功能"></a>
    <a href="#测试"><img src="https://img.shields.io/badge/测试-通过-brightgreen" alt="测试通过"></a>
  </p>
</div>

## 项目概述

本项目是一个综合性 Python 学习和实践项目，涵盖了从基础学习到高级应用的多个方面。项目结构清晰，代码组织规范，包含核心功能模块、测试用例、图形界面、数学算法、游戏开发、认证系统以及数据分析等多种实用工具和示例代码。

项目旨在为 Python 学习者提供一个全面的学习资源，从基础概念到实际应用，帮助用户快速掌握 Python 编程技能。同时，项目也包含了一些实用工具和有趣的小项目，供用户在学习过程中实践和探索。

---

## 技术栈

| 类别 | 技术 | 版本 |
|------|------|------|
| 编程语言 | Python | 3.13+ |
| 测试框架 | unittest | 标准库 |
| 网络请求 | requests | - |
| 网页解析 | BeautifulSoup | - |
| 开发工具 | PyCharm, VS Code | - |
| 版本控制 | Git | - |

---

## 项目结构

```
PythonProject/
├── 📁 核心/                  # 核心功能模块
│   ├── 简单的数学运算.py     # 计算器功能
│   ├── 句子的基本操作.py     # 句子处理功能
│   └── 供购物清单的管理.py   # 购物清单功能
├── 📁 测试/                 # 测试文件
│   ├── 计算器模块测试.py      # 计算器测试
│   ├── 句子处理模块测试.py    # 句子处理测试
│   └── 购物清单模块测试.py    # 购物清单测试
├── 📁 图形界面/              # 图形界面相关代码
│   ├── 13动画显示文字.py
│   ├── 15法国国旗.py
│   ├── 16五星红旗.py
│   ├── 17随机气球.py
│   └── 考场计时器（UI）.py
├── 📁 基础学习/              # 基础学习代码
│   ├── 12循环与列表.py
│   ├── 3角古猜想实现.py
│   ├── 9两数大小比较.py
│   ├── 列表.py
│   ├── 变量.py
│   ├── 字典.py
│   ├── 字符串.py
│   └── 程序设计入门.py
├── 📁 工具/                  # 工具类代码
│   ├── 内存燃烧器.py
│   ├── 按键控制LED灯电路.py
│   └── 银行家.py
├── 📁 教程练习/              # 教程练习代码
│   ├── 小小心意，不足挂齿.py
│   ├── 小小练习.py
│   ├── 核弹加判断布尔.py
│   └── 横刀向渊.py
├── 📁 数学算法/              # 数学算法相关代码
│   ├── 11报时器（10秒）.py
│   ├── 6分数排行.py
│   ├── 8考试计时器.py
│   ├── 时间戳.py
│   ├── 生日判断十二生肖.py
│   ├── 能被5整除的列表数.py
│   └── 金字塔.py
├── 📁 旅途的开始/            # 项目初始代码
│   ├── 好玩的.py
│   ├── 好玩的2.4.py
│   ├── 好玩的2.5.py
│   ├── 好玩的2.6.py
│   └── 王权0.27.py
├── 📁 游戏/                  # 游戏相关代码
│   ├── 20made_in_heaven.py
│   ├── 5猜数字.py
│   ├── 7骰子.py
│   ├── 火柴人vs编程.py
│   ├── 贪吃蛇.py
│   └── 追杀游戏.py
├── 📁 认证/                  # 认证相关代码
│   ├── 18注册和登录.py
│   └── 4指定账号密码登录.py
├── 📁 Python数据分析/        # 数据分析相关代码
│   ├── 第一篇 Python编程基础/
│   │   └── 项目1 搭建运动员欢迎系统_基础知识.py
│   └── 封面.py
├── README.md              # 项目说明文件
├── .gitignore             # Git 忽略文件配置
├── config.json            # 配置文件
├── scrape_douban.py       # 豆瓣爬虫
└── 爬虫学习.py             # 爬虫学习代码
```

---

## 核心功能模块

### 1. 计算器模块 (`核心/my_calculator.py`)
- **功能**: 提供简单的加法运算
- **函数**: `my_adder(x, y)` - 返回两个数的和
- **参数**: 
  - `x`: 第一个加数
  - `y`: 第二个加数
- **返回值**: 两个数的和

### 2. 句子处理模块 (`核心/sentence.py`)
- **功能**: 提供句子的基本操作
- **类**: `Sentence`
  - **构造函数**: `__init__(self, sentence)` - 初始化句子对象
  - **方法**: 
    - `letter_count()` - 返回句子的字母数量
    - `word_count()` - 返回句子的单词数量
    - `upper()` - 返回句子的大写形式

### 3. 购物清单模块 (`核心/shopping_list.py`)
- **功能**: 提供购物清单的管理功能
- **类**: `ShoppingList`
  - **构造函数**: `__init__(self, shopping_list)` - 初始化购物清单
    - `shopping_list`: 字典类型，包含商品名称和对应价格
  - **方法**: 
    - `get_item_count()` - 返回购物清单的商品数量
    - `get_total_price()` - 返回购物清单的总价格

---

## 环境要求

- Python 3.13 或更高版本
- 部分代码需要安装依赖（见 requirements.txt）

### 安装依赖

```bash
pip install -r requirements.txt
```

---

## 核心模块说明

### 1. 计算器模块 (`核心/简单的数学运算.py`)

```python
from 核心.简单的数学运算 import my_adder

result = my_adder(5, 3)
print(f"5 + 3 = {result}")  # 输出: 5 + 3 = 8
```

### 2. 句子处理模块 (`核心/句子的基本操作.py`)

```python
from 核心.句子的基本操作 import Sentence

my_sentence = Sentence("Hello, world!")
print(f"字母数量: {my_sentence.letter_count()}")
print(f"单词数量: {my_sentence.word_count()}")
print(f"大写形式: {my_sentence.upper()}")
```

### 3. 购物清单模块 (`核心/供购物清单的管理.py`)

```python
from 核心.供购物清单的管理 import ShoppingList

items = {"牙刷": 5, "沐浴露": 20, "毛巾": 15, "洗发水": 30, "电池": 7}
my_list = ShoppingList(items)
print(f"商品数量: {my_list.get_item_count()}")
print(f"总价格: {my_list.get_total_price()}")
```

---

## 测试

项目包含单元测试练习，使用 Python 的 `unittest` 框架：

- `测试/test_calculator.py` - 计算器功能测试
- `测试/test_sentence.py` - 句子处理测试
- `测试/test_shopping_list.py` - 购物清单测试

运行测试：

```bash
python -m unittest discover 测试
```

---

## 其他目录说明

| 目录 | 描述 |
|------|------|
| **图形界面/** | 包含使用 Python 编写的图形界面相关代码，如动画显示文字、国旗绘制等 |
| **基础学习/** | 包含 Python 基础学习相关的代码，如变量、字符串、列表等基础概念 |
| **工具/** | 包含各种实用工具的代码，如内存燃烧器、按键控制 LED 灯电路等 |
| **教程练习/** | 包含教程练习相关的代码，如条件判断、循环等练习 |
| **数学算法/** | 包含数学算法相关的代码，如报时器、分数排行、金字塔等 |
| **旅途的开始/** | 包含项目初始阶段的代码，如简单的游戏和交互程序 |
| **游戏/** | 包含游戏相关的代码，如猜数字、贪吃蛇等 |
| **认证/** | 包含认证相关的代码，如注册和登录功能 |

---

## 代码规范

- 遵循 PEP 8 代码风格指南
- 保持代码简洁明了
- 添加适当的注释说明

---

<div align="center">
  <h3>🌟 感谢您使用本项目！</h3>
  <p>希望它能为您的 Python 学习和开发提供帮助。</p>
  <p>只要记录下来，就不会被放弃。</p>
</div>
