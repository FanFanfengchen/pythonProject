"""购物清单模块

该模块提供购物清单的管理功能，包括计算商品数量和总价格。
"""

class ShoppingList:
    """购物清单类
    
    提供对购物清单的管理功能，如计算商品数量和总价格。
    """
    
    def __init__(self, shopping_list):
        """初始化购物清单
        
        Args:
            shopping_list: 字典类型，包括商品名称和对应价格
            例子：{"牙刷": 5, "沐浴露": 20, "毛巾": 15, "洗发水": 30, "电池": 7}
        """
        self.shopping_list = shopping_list
    
    def get_item_count(self):
        """返回购物清单上有多少项商品
        
        Returns:
            整数，购物清单中的商品数量
        
        Examples:
            >>> items = {"牙刷": 5, "沐浴露": 20}
            >>> sl = ShoppingList(items)
            >>> sl.get_item_count()
            2
        """
        return len(self.shopping_list)

    def get_total_price(self):
        """返回购物清单商品价格总额数字
        
        遍历购物清单中的所有商品价格并求和。
        
        Returns:
            数字，购物清单中所有商品的总价格
        
        Examples:
            >>> items = {"牙刷": 5, "沐浴露": 20}
            >>> sl = ShoppingList(items)
            >>> sl.get_total_price()
            25
        """
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price