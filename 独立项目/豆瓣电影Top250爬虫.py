import requests
from requests.exceptions import RequestException
import logging
import json
import os
from typing import Optional, Dict, Any

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Config:
    """配置管理类"""

    def __init__(self, config_file: str = "config.json"):
        """
        初始化配置

        Args:
            config_file: 配置文件路径
        """
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        加载配置文件

        Returns:
            Dict: 配置字典
        """
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                logger.info(f"配置文件加载成功: {self.config_file}")
                return config
        except FileNotFoundError:
            logger.warning(f"配置文件不存在: {self.config_file}，使用默认配置")
            return self._get_default_config()
        except UnicodeDecodeError as e:
            logger.error(f"配置文件编码错误: {str(e)}，使用默认配置")
            return self._get_default_config()
        except json.JSONDecodeError as e:
            logger.error(f"配置文件格式错误: {str(e)}，使用默认配置")
            return self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """
        获取默认配置

        Returns:
            Dict: 默认配置字典
        """
        return {
            "douban": {
                "base_url": "https://movie.douban.com/top250",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "timeout": 10
            }
        }

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置项

        Args:
            key: 配置键，支持点分隔的嵌套键，如"douban.base_url"
            default: 默认值

        Returns:
            Any: 配置值
        """
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        # 支持环境变量覆盖
        env_key = key.upper().replace('.', '_')
        env_value = os.getenv(env_key)
        if env_value is not None:
            logger.info(f"使用环境变量覆盖配置: {env_key}")
            return env_value

        return value


class DoubanSpider:
    """豆瓣爬虫类"""

    def __init__(self, config: Config):
        """
        初始化豆瓣爬虫

        Args:
            config: 配置对象
        """
        self.config = config
        self.base_url = config.get("douban.base_url")
        self.headers = {"User-Agent": config.get("douban.user_agent")}
        self.timeout = config.get("douban.timeout", 10)

    def fetch_page(self, url: Optional[str] = None) -> Optional[str]:
        """
        获取页面内容

        Args:
            url: 请求URL，如果为None则使用base_url

        Returns:
            str: 页面内容，失败时返回None
        """
        target_url = url or self.base_url

        try:
            response = requests.get(
                target_url,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            logger.info(
                f"请求成功，URL: {target_url}, "
                f"状态码: {response.status_code}"
            )
            return response.text
        except requests.exceptions.Timeout:
            logger.error(f"请求超时，URL: {target_url}")
        except requests.exceptions.ConnectionError:
            logger.error(f"连接错误，请检查网络连接，URL: {target_url}")
        except requests.exceptions.HTTPError as e:
            logger.error(
                f"HTTP错误，状态码: {e.response.status_code}, "
                f"URL: {target_url}"
            )
        except RequestException as e:
            logger.error(f"请求异常: {str(e)}, URL: {target_url}")
        except Exception as e:
            logger.error(f"未知异常: {str(e)}, URL: {target_url}")

        return None

    def fetch_top250(self) -> Optional[str]:
        """
        获取豆瓣Top250数据

        Returns:
            str: 页面内容，失败时返回None
        """
        return self.fetch_page()


def main():
    """主函数"""
    config = Config()
    spider = DoubanSpider(config)
    content = spider.fetch_top250()

    if content:
        print(content)
    else:
        print("获取数据失败")


if __name__ == "__main__":
    main()
