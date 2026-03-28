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

本项目是一个综合性 Python 学习和实践项目，包含核心功能模块、测试用例以及多种实用工具和示例代码。项目结构清晰，代码组织规范，适合作为 Python 学习和开发的参考。

---

## 技术栈

| 类别 | 技术 | 版本 |
|------|------|------|
| 编程语言 | Python | 3.13+ |
| 测试框架 | unittest | 标准库 |
| 开发工具 | PyCharm, VS Code | - |
| 版本控制 | Git | - |

---

## 项目结构

```
PythonProject/
├── 📁 核心/                  # 核心功能模块
│   ├── my_calculator.py   # 计算器功能
│   ├── sentence.py        # 句子处理功能
│   └── shopping_list.py   # 购物清单功能
├── 📁 测试/                 # 测试文件
│   ├── test_my_calculator.py  # 计算器测试
│   ├── test_sentence.py       # 句子处理测试
│   └── test_shopping_list.py  # 购物清单测试
├── 📁 图形界面/              # 图形界面相关代码
├── 📁 基础学习/              # 基础学习代码
├── 📁 工具/                  # 工具类代码
├── 📁 教程练习/              # 教程练习代码
├── 📁 数学算法/              # 数学算法相关代码
├── 📁 旅途的开始/            # 项目初始代码
├── 📁 游戏/                  # 游戏相关代码
├── 📁 认证/                  # 认证相关代码
├── README.md              # 项目说明文件
└── .gitignore             # Git 忽略文件配置
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

## 安装与设置

### 1. 克隆项目

```bash
git clone https://github.com/FanFanfengchen/pythonProject.git
cd pythonProject
```

### 2. 环境要求

- Python 3.13 或更高版本
- 标准库（无需额外依赖）

### 3. 验证安装

```bash
# 检查 Python 版本
python --version

# 运行测试
python -m unittest discover 测试
```

---

## 使用方法

### 1. 导入核心模块

```python
# 导入计算器模块
from 核心.my_calculator import my_adder

# 导入句子处理模块
from 核心.sentence import Sentence

# 导入购物清单模块
from 核心.shopping_list import ShoppingList
```

### 2. 使用示例

#### 计算器模块

```python
# 使用计算器
result = my_adder(5, 3)
print(f"5 + 3 = {result}")  # 输出: 5 + 3 = 8
```

#### 句子处理模块

```python
# 使用句子处理
my_sentence = Sentence("Hello, world!")
print(f"字母数量: {my_sentence.letter_count()}")  # 输出: 字母数量: 13
print(f"单词数量: {my_sentence.word_count()}")  # 输出: 单词数量: 2
print(f"大写形式: {my_sentence.upper()}")  # 输出: 大写形式: HELLO, WORLD!
```

#### 购物清单模块

```python
# 使用购物清单
items = {"牙刷": 5, "沐浴露": 20, "毛巾": 15, "洗发水": 30, "电池": 7}
my_list = ShoppingList(items)
print(f"商品数量: {my_list.get_item_count()}")  # 输出: 商品数量: 5
print(f"总价格: {my_list.get_total_price()}")  # 输出: 总价格: 77
```

---

## 测试

项目包含完整的测试文件，使用 Python 的 `unittest` 框架进行测试：

- `测试/test_my_calculator.py` - 测试计算器功能
- `测试/test_sentence.py` - 测试句子处理功能
- `测试/test_shopping_list.py` - 测试购物清单功能

### 运行测试

```bash
# 运行所有测试
python -m unittest discover 测试

# 运行特定测试文件
python -m unittest 测试/test_my_calculator.py
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

## 贡献指南

### 如何贡献

1. **Fork 项目**
2. **创建分支** (`git checkout -b feature/AmazingFeature`)
3. **提交更改** (`git commit -m 'Add some AmazingFeature'`)
4. **推送到分支** (`git push origin feature/AmazingFeature`)
5. **创建 Pull Request**

### 代码规范

- 遵循 PEP 8 代码风格指南
- 为新功能添加测试用例
- 保持代码简洁明了
- 添加适当的注释说明

---

## 故障排除

### 常见问题

1. **导入错误**: 确保 Python 解释器能够找到核心模块
   - 解决方案: 在项目根目录运行代码，或确保核心目录在 Python 路径中

2. **测试失败**: 检查测试用例是否与代码实现一致
   - 解决方案: 查看测试错误信息，修复代码或更新测试用例

3. **Git 拉取错误**: 遇到远程仓库访问问题
   - 解决方案: 确保网络连接正常，或使用 HTTPS 协议访问仓库

### 联系支持

如果遇到其他问题，请通过 GitHub Issues 提交问题描述，我们会尽快回复。

---

## 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

---

## 后续规划

- [ ] 添加更多核心功能模块
- [ ] 完善测试覆盖
- [ ] 添加项目依赖管理
- [ ] 提供更多使用示例和文档
- [ ] 扩展图形界面功能
- [ ] 添加更多算法实现

---

<div align="center">
  <h3>🌟 感谢您使用本项目！</h3>
  <p>希望它能为您的 Python 学习和开发提供帮助。</p>
  <p>只要记录下来，就不会被放弃。</p>
</div>
