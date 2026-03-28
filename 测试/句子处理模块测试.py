"""句子处理模块测试

该模块测试 sentence.py 中的 Sentence 类功能。
"""

import unittest
from 核心.句子的基本操作 import Sentence

class TestSentence(unittest.TestCase):
    """测试 Sentence 类的测试类
    
    测试 Sentence 类的各种方法在不同输入情况下的行为。
    """
    
    def setUp(self):
        """设置测试环境
        
        在每个测试方法执行前创建一个 Sentence 实例。
        """
        self.sentence = Sentence("hello world!")

    def test_str_count(self):
        """测试字母数量计算
        
        验证 letter_count 方法能够正确计算句子的长度。
        """
        self.assertEqual(self.sentence.letter_count(), 12)

    def test_word_count(self):
        """测试单词数量计算
        
        验证 word_count 方法能够正确计算句子中的单词数量。
        """
        self.assertEqual(self.sentence.word_count(), 2)

    def test_upper(self):
        """测试大写转换
        
        验证 upper 方法能够正确将句子转换为大写形式。
        """
        self.assertEqual(self.sentence.upper(), "HELLO WORLD!")


