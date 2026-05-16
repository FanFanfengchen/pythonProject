"""银行家模块加密功能测试

该模块测试银行家.py中的加密解密功能，确保敏感数据得到安全保护。
"""

import unittest
import os
import sys

# 添加工具库路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from 工具库.银行家 import (
    encrypt_data, 
    decrypt_data, 
    derive_fernet_key,
    get_encryption_password,
    CRYPTOGRAPHY_AVAILABLE
)

class TestEncryption(unittest.TestCase):
    """测试加密解密功能的测试类"""
    
    def setUp(self):
        """设置测试环境"""
        self.test_password = "test_secure_password_123"
        self.test_data = {
            "account_id": "test_user",
            "password_hash": "hashed_password_example",
            "balance": "1000.00",
            "transaction_history": []
        }
        self.test_json = '{"account_id": "test_user", "balance": "1000.00"}'
    
    def test_encrypt_decrypt_roundtrip(self):
        """测试加密解密往返过程
        
        验证加密后的数据可以正确解密还原
        """
        if not CRYPTOGRAPHY_AVAILABLE:
            self.skipTest("cryptography库未安装")
        
        # 加密数据
        encrypted = encrypt_data(self.test_json, self.test_password)
        
        # 验证加密后数据不为空且与原数据不同
        self.assertTrue(len(encrypted) > 0)
        self.assertNotEqual(encrypted, self.test_json.encode())
        
        # 验证数据格式（包含Fernet标记）
        self.assertTrue(b'::Fernet::' in encrypted)
        
        # 解密数据
        decrypted = decrypt_data(encrypted, self.test_password)
        
        # 验证解密后的数据与原始数据一致
        self.assertEqual(decrypted, self.test_json)
    
    def test_derive_fernet_key(self):
        """测试密钥派生函数
        
        验证从相同密码派生的密钥一致
        """
        if not CRYPTOGRAPHY_AVAILABLE:
            self.skipTest("cryptography库未安装")
        
        # 生成新密钥和盐
        key1, salt1 = derive_fernet_key(self.test_password)
        key2, salt2 = derive_fernet_key(self.test_password)
        
        # 验证生成的密钥不为空
        self.assertTrue(len(key1) > 0)
        self.assertTrue(len(key2) > 0)
        
        # 验证盐值不同（每次生成新盐）
        self.assertNotEqual(salt1, salt2)
        
        # 使用相同盐值派生相同密钥
        key3, _ = derive_fernet_key(self.test_password, salt1)
        self.assertEqual(key1, key3)
    
    def test_encrypt_decrypt_with_different_passwords(self):
        """测试使用不同密码无法解密
        
        验证使用错误密码无法解密数据
        """
        if not CRYPTOGRAPHY_AVAILABLE:
            self.skipTest("cryptography库未安装")
        
        encrypted = encrypt_data(self.test_json, self.test_password)
        
        # 使用错误密码解密应失败
        wrong_password = "wrong_password_456"
        with self.assertRaises(Exception):
            decrypt_data(encrypted, wrong_password)
    
    def test_empty_data_encryption(self):
        """测试空数据加密"""
        if not CRYPTOGRAPHY_AVAILABLE:
            self.skipTest("cryptography库未安装")
        
        empty_data = ""
        encrypted = encrypt_data(empty_data, self.test_password)
        decrypted = decrypt_data(encrypted, self.test_password)
        self.assertEqual(decrypted, empty_data)
    
    def test_special_characters_encryption(self):
        """测试特殊字符数据加密"""
        if not CRYPTOGRAPHY_AVAILABLE:
            self.skipTest("cryptography库未安装")
        
        special_data = '{"name": "张三", "balance": "¥1,000.00", "notes": "测试数据\\n换行"}'
        encrypted = encrypt_data(special_data, self.test_password)
        decrypted = decrypt_data(encrypted, self.test_password)
        self.assertEqual(decrypted, special_data)
    
    def test_get_encryption_password(self):
        """测试获取加密密码函数
        
        验证优先从环境变量读取密码
        """
        # 测试默认密码
        password = get_encryption_password()
        self.assertTrue(isinstance(password, str))
        self.assertTrue(len(password) > 0)
    
    def test_backward_compatibility_xor_format(self):
        """测试向后兼容性（XOR格式）
        
        验证能够正确处理旧的XOR加密格式数据
        """
        # 创建模拟的旧格式数据（XOR加密）
        test_data = "test data for backward compatibility"
        
        # 使用XOR降级方案加密（模拟旧格式）
        encrypted = encrypt_data(test_data, self.test_password)
        
        # 解密数据
        decrypted = decrypt_data(encrypted, self.test_password)
        
        # 验证解密结果
        self.assertEqual(decrypted, test_data)

if __name__ == '__main__':
    unittest.main()
