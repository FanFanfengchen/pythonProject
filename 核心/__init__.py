"""核心功能模块

包含计算器、句子处理、购物清单等基础功能
"""

from .简单的数学运算 import my_adder
from .句子的基本操作 import Sentence
from .供购物清单的管理 import ShoppingList

__all__ = ['my_adder', 'Sentence', 'ShoppingList']
