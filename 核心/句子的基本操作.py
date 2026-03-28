"""句子处理模块

该模块提供句子的基本操作功能，包括计算字母数量、单词数量和转换为大写形式。
"""

class Sentence:
    """句子处理类
    
    提供对句子的各种操作方法，如计算字母数量、单词数量和转换为大写形式。
    """
    
    def __init__(self, sentence):
        """初始化句子对象
        
        Args:
            sentence: 字符串类型，要处理的句子
        """
        self.sentence = sentence

    def letter_count(self):
        """计算句子的字母数量
        
        Returns:
            整数，句子的长度（包含所有字符，包括空格和标点符号）
        
        Examples:
            >>> s = Sentence("Hello, world!")
            >>> s.letter_count()
            13
        """
        return len(self.sentence)

    def word_count(self):
        """计算句子的单词数量
        
        通过空格分割句子来计算单词数量，注意连续空格会被视为单个分隔符。
        
        Returns:
            整数，句子中的单词数量
        
        Examples:
            >>> s = Sentence("Hello, world!")
            >>> s.word_count()
            2
        """
        return len(self.sentence.split(" "))

    def upper(self):
        """将句子转换为大写形式
        
        Returns:
            字符串，转换为大写后的句子
        
        Examples:
            >>> s = Sentence("Hello, world!")
            >>> s.upper()
            'HELLO, WORLD!'
        """
        return self.sentence.upper()
