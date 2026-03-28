"""购物清单模块测试

该模块测试 shopping_list.py 中的 ShoppingList 类功能。
"""

import unittest
from 核心.供购物清单的管理 import ShoppingList

class TestShoppingList(unittest.TestCase):
    """测试 ShoppingList 类的测试类
    
    测试 ShoppingList 类的各种方法在不同输入情况下的行为。
    """
    
    def setUp(self):
        """设置测试环境
        
        在每个测试方法执行前创建一个 ShoppingList 实例，包含多个商品及其价格。
        """
        self.shopping_list = ShoppingList({"牙刷": 5, "沐浴露": 20, "毛巾": 15, "洗发水": 30, "电池": 7})
    
    def test_get_item_count(self):
        """测试商品数量计算
        
        验证 get_item_count 方法能够正确计算购物清单中的商品数量。
        """
        self.assertEqual(self.shopping_list.get_item_count(), 5)
    
    def test_get_total_price(self):
        """测试总价格计算
        
        验证 get_total_price 方法能够正确计算购物清单中所有商品的总价格。
        """
        self.assertEqual(self.shopping_list.get_total_price(), 77)
