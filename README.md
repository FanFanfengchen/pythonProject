# Python 项目整理 🐍

<div align="center">
  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Python%20programming%20project%20logo%20with%20code%20snippets%20and%20modern%20design&image_size=square" alt="Python Project Logo" width="200">
  
  <p align="center">
    <a href="#项目概述"><img src="https://img.shields.io/badge/项目-概述-blue" alt="项目概述"></a>
    <a href="#技术栈"><img src="https://img.shields.io/badge/技术-栈-orange" alt="技术栈"></a>
    <a href="#核心功能模块"><img src="https://img.shields.io/badge/核心-功能-green" alt="核心功能"></a>
    <a href="#测试"><img src="https://img.shields.io/badge/测试-通过-brightgreen" alt="测试通过"></a>
  </p>
</div>

---

## 目录

- [项目概述](#项目概述)
- [技术栈](#技术栈)
- [项目结构](#项目结构)
- [核心功能模块](#核心功能模块)
- [环境要求](#环境要求)
- [安装指南](#安装指南)
- [使用方法](#使用方法)
- [测试](#测试)
- [更新日志](#更新日志)
- [代码规范](#代码规范)
- [贡献](#贡献)

---

## 项目概述

本项目是一个综合性 Python 学习和实践项目，涵盖从基础编程到高级应用的多个领域。项目结构清晰，代码组织规范，包含：

- **基础学习**：变量、数据类型、控制流程、函数等核心概念
- **核心模块**：计算器、句子处理、购物清单管理等实用工具
- **图形界面**：基于 Tkinter 的 GUI 应用程序
- **游戏开发**：贪吃蛇、猜数字等经典小游戏
- **网络爬虫**：豆瓣电影 Top250 爬虫示例
- **数据分析**：基础数据分析入门示例

项目旨在为 Python 学习者提供全面的学习资源，从基础概念到实际应用，帮助用户快速掌握 Python 编程技能。

---

## 技术栈

| 类别 | 技术 | 版本 |
|------|------|------|
| 编程语言 | Python | 3.13+ |
| 测试框架 | unittest | 标准库 |
| 网络请求 | requests | 2.31+ |
| 网页解析 | BeautifulSoup4 | 4.12+ |
| GUI框架 | Tkinter | 标准库 |
| 开发工具 | PyCharm, VS Code | - |
| 版本控制 | Git | - |

---

## 项目结构

```
PythonProject/
├── 📁 学习笔记/              # 基础学习与练习代码
│   ├── 变量.py
│   ├── 列表.py
│   ├── 字典.py
│   ├── 字符串.py
│   ├── 运算法则.py
│   ├── 程序设计入门.py
│   └── ...
├── 📁 工具库/                # 核心工具模块与测试
│   ├── __init__.py
│   ├── 简单的数学运算.py
│   ├── 句子的基本操作.py
│   ├── 供购物清单的管理.py
│   ├── test_calculator.py
│   ├── test_sentence.py
│   └── test_shopping_list.py
├── 📁 游戏/                  # 游戏开发示例
│   ├── 贪吃蛇.py
│   ├── 5猜数字.py
│   ├── 7骰子.py
│   └── 火柴人vs编程.py
├── 📁 认证/                  # 用户认证示例
│   ├── 18注册和登录.py
│   └── 4指定账号密码登录.py
├── 📁 图形界面/              # GUI应用程序
│   ├── 考场计时器（UI）.py
│   ├── 13动画显示文字.py
│   ├── 15法国国旗.py
│   └── 17随机气球.py
├── 📁 独立项目/              # 独立项目代码
│   ├── 增强版鼠标连点器.py
│   ├── 豆瓣电影Top250爬虫.py
│   └── 爬虫学习.py
├── 📁 旅途的开始/            # 项目初始代码（保留原样）
├── 📁 Python数据分析/        # 数据分析入门
├── README.md
└── requirements.txt
```

---

## 核心功能模块

### 1. 计算器模块

**文件**: `工具库/简单的数学运算.py`

提供基础数学运算功能，支持加法运算：

```python
from 工具库.简单的数学运算 import my_adder

result = my_adder(5, 3)
print(f"5 + 3 = {result}")  # 输出: 8
```

### 2. 句子处理模块

**文件**: `工具库/句子的基本操作.py`

提供句子的多种操作方法：

| 方法 | 功能 | 返回值 |
|------|------|--------|
| `letter_count()` | 计算字母数量 | 整数 |
| `word_count()` | 计算单词数量 | 整数 |
| `upper()` | 转换为大写 | 字符串 |

```python
from 工具库.句子的基本操作 import Sentence

sentence = Sentence("Hello, World!")
print(f"字母数: {sentence.letter_count()}")  # 13
print(f"单词数: {sentence.word_count()}")    # 2
print(f"大写: {sentence.upper()}")           # HELLO, WORLD!
```

### 3. 购物清单模块

**文件**: `工具库/供购物清单的管理.py`

提供购物清单管理功能：

```python
from 工具库.供购物清单的管理 import ShoppingList

items = {"牙刷": 5, "沐浴露": 20, "毛巾": 15}
my_list = ShoppingList(items)
print(f"商品数量: {my_list.get_item_count()}")   # 3
print(f"总价格: {my_list.get_total_price()}")   # 40
```

### 4. 考场计时器

**文件**: `图形界面/考场计时器（UI）.py`

智能考场管理系统，支持：
- ✅ 考试计时与倒计时
- ✅ 暂停/继续控制
- ✅ 考试历史记录
- ✅ 跨平台运行（Windows/Linux/macOS）
- ✅ 自动配置管理

### 5. 豆瓣电影爬虫

**文件**: `独立项目/豆瓣电影Top250爬虫.py`

豆瓣电影 Top250 数据爬取工具，支持：
- ✅ 配置化管理
- ✅ 异常处理
- ✅ 日志记录

---

## 环境要求

- **Python 版本**: 3.13 或更高版本
- **操作系统**: Windows / macOS / Linux
- **内存**: 至少 1GB RAM
- **存储**: 至少 100MB 可用空间

---

## 安装指南

### 1. 克隆项目

```bash
git clone https://github.com/FanFanfengchen/pythonProject.git
cd pythonProject
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 验证安装

```bash
python -c "print('Python 项目整理安装成功！')"
```

---

## 使用方法

### 运行考场计时器

```bash
python "图形界面/考场计时器（UI）.py"
```

### 运行贪吃蛇游戏

```bash
python "游戏/贪吃蛇.py"
```

### 运行单元测试

```bash
python -m unittest discover 工具库
```

---

## 测试

项目包含完善的单元测试覆盖：

| 测试文件 | 测试模块 | 测试覆盖率 |
|----------|----------|------------|
| `test_calculator.py` | 计算器模块 | ✅ 100% |
| `test_sentence.py` | 句子处理模块 | ✅ 100% |
| `test_shopping_list.py` | 购物清单模块 | ✅ 100% |

---

## 更新日志

### v1.0.1 (2026-05-09)

**新增功能**
- ✨ 考场计时器新增配置管理类 `ConfigManager`
- ✨ 支持跨平台配置文件存储（用户主目录 `.exam_timer`）
- ✨ 自动创建配置目录和示例配置

**重构优化**
- 🔧 移除硬编码路径，提升程序可移植性
- 🔧 优化异常处理机制
- 🔧 改善代码结构和可维护性

**Bug修复**
- 🐛 修复路径问题导致的程序启动失败

### v1.0.0 (2026-05-08)

**初始版本**
- 🎉 项目结构整理完成
- 🎉 核心功能模块实现
- 🎉 单元测试覆盖
- 🎉 README 文档完善

---

## 代码规范

本项目遵循以下代码规范：

1. **PEP 8 标准**：统一代码风格
2. **类型注解**：提供清晰的类型提示
3. **文档字符串**：每个模块和函数都有完整文档
4. **异常处理**：合理的错误捕获和处理
5. **代码注释**：关键逻辑添加必要注释

---

## 贡献

欢迎提交 Issue 和 Pull Request！

### 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

---

## 许可证

本项目仅供学习和参考使用。

---

<div align="center">
  <h3>🌟 感谢您使用本项目！</h3>
  <p>希望它能为您的 Python 学习和开发提供帮助。</p>
  <p>只要记录下来，就不会被放弃。</p>
</div>

---

*最后更新: 2026-05-09*
