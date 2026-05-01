"""句子处理模块测试

该模块测试 句子的基本操作.py 中的 Sentence 类功能。
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

    def test_word_count_with_multiple_spaces(self):
        """测试包含连续空格的单词数量计算

        验证 word_count 方法能够正确处理包含连续空格的句子。
        """
        sentence = Sentence("Hello,  world!")
        self.assertEqual(sentence.word_count(), 2)

    def test_word_count_with_tab(self):
        """测试包含制表符的单词数量计算

        验证 word_count 方法能够正确处理包含制表符的句子。
        """
        sentence = Sentence("Hello,\tworld!")
        self.assertEqual(sentence.word_count(), 2)

    def test_word_count_with_newline(self):
        """测试包含换行符的单词数量计算

        验证 word_count 方法能够正确处理包含换行符的句子。
        """
        sentence = Sentence("Hello,\nworld!")
        self.assertEqual(sentence.word_count(), 2)

    def test_word_count_with_mixed_whitespace(self):
        """测试包含混合空白字符的单词数量计算

        验证 word_count 方法能够正确处理包含多种空白字符的句子。
        """
        sentence = Sentence("Hello,  \t\n  world!")
        self.assertEqual(sentence.word_count(), 2)

    def test_upper(self):
        """测试大写转换
        
        验证 upper 方法能够正确将句子转换为大写形式。
        """
        self.assertEqual(self.sentence.upper(), "HELLO WORLD!")


