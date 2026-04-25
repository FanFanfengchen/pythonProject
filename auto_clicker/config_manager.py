"""配置管理模块

负责配置的加载、保存和管理，提供统一的配置访问接口。
"""

import json
import os
from typing import Any, Optional


class ConfigManager:
    """配置管理类"""
    
    def __init__(self, config_file: str = 'autoclicker_config.json'):
        """
        初始化配置管理器
        
        Args:
            config_file: 配置文件路径
        """
        self.config_file = config_file
        self.settings = self._load_default_settings()
        self._load_config()
        
    def _load_default_settings(self) -> dict:
        """加载默认配置"""
        return {
            'interval': 0.1,
            'min_interval': 0.05,
            'max_interval': 0.15,
            'random_interval': False,
            'total_clicks': 100,
            'infinite_clicks': False,
            'hotkey': 'ctrl+alt+f6',
            'hold_hotkey': 'ctrl+alt+f7',
            'hold_switch_hotkey': 'ctrl+alt+f8',
            'hold_mode': False,
            'hold_button': 'left',
            'hold_duration': 2.0,
            'background_mode': True
        }
        
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项
        
        Args:
            key: 配置键
            default: 默认值
            
        Returns:
            配置值
        """
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """设置配置项
        
        Args:
            key: 配置键
            value: 配置值
        """
        self.settings[key] = value
        self._save_config()
        
    def _load_config(self) -> None:
        """从文件加载配置"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                    self.settings.update(loaded_config)
        except Exception as e:
            print(f"加载配置失败: {e}")
            
    def _save_config(self) -> None:
        """保存配置到文件"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存配置失败: {e}")
