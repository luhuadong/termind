import os
import json
from pathlib import Path

class ConfigManager:
    def __init__(self):
        self.config_dir = Path.home() / ".termind"
        self.config_file = self.config_dir / "config.json"
        self.default_config = {
            "models": {
                "chatgpt": {"api_key": None, "enabled": True},
                "deepseek": {"api_key": None, "enabled": True},
                "qwen": {"api_key": None, "enabled": True},
                "doubao": {"api_key": None, "enabled": True}
            },
            "current_model": "chatgpt",
            "language": "zh",
            "context_length": 20
        }
        self.load_config()

    def load_config(self):
        """加载配置文件"""
        if not self.config_file.exists():
            self.save_config()
        with open(self.config_file, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def save_config(self):
        """保存配置文件"""
        os.makedirs(self.config_dir, exist_ok=True)
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def get_api_key(self, model_name):
        """获取指定模型的 API 密钥"""
        return self.config["models"][model_name]["api_key"]

    def set_api_key(self, model_name, api_key):
        """设置指定模型的 API 密钥"""
        self.config["models"][model_name]["api_key"] = api_key
        self.save_config()

    def get_current_model(self):
        """获取当前使用的模型"""
        return self.config["current_model"]

    def set_current_model(self, model_name):
        """设置当前使用的模型"""
        if model_name in self.config["models"]:
            self.config["current_model"] = model_name
            self.save_config()
        else:
            raise ValueError(f"Model {model_name} not found")

    def get_language(self):
        """获取当前语言设置"""
        return self.config["language"]

    def set_language(self, language):
        """设置语言"""
        if language in ["zh", "en"]:
            self.config["language"] = language
            self.save_config()
        else:
            raise ValueError("Invalid language")

    def get_context_length(self):
        """获取上下文长度"""
        return self.config["context_length"]

    def set_context_length(self, length):
        """设置上下文长度"""
        if isinstance(length, int) and length > 0:
            self.config["context_length"] = length
            self.save_config()
        else:
            raise ValueError("Invalid context length")