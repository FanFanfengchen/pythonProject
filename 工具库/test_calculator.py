"""计算器模块测试

该模块测试 简单的数学运算.py 中的 my_adder 函数功能。
"""

import unittest
from 工具库.简单的数学运算 import my_adder

class TestMyAdder(unittest.TestCase):
    """测试 my_adder 函数的测试类
    
    测试 my_adder 函数在不同输入情况下的行为。
    """
    
    def test_positive_with_positive(self):
        """测试正数与正数相加
        
        验证 my_adder 函数能够正确处理两个正数的加法运算。
        """
        self.assertEqual(my_adder(2, 3), 5)

    def test_negative_with_positive(self):
        """测试负数与正数相加
        
        验证 my_adder 函数能够正确处理负数与正数的加法运算。
        """
        self.assertEqual(my_adder(-2, 3), 1)