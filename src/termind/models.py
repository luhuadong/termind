import openai
import requests
from termind.config import ConfigManager

class ModelAdapter:
    def __init__(self):
        self.config = ConfigManager()

    def get_response(self, model_name, messages):
        """获取模型响应的通用接口"""
        if model_name == "chatgpt":
            return self._get_chatgpt_response(messages)
        elif model_name == "deepseek":
            return self._get_deepseek_response(messages)
        elif model_name == "qwen":
            return self._get_qwen_response(messages)
        elif model_name == "doubao":
            return self._get_doubao_response(messages)
        else:
            raise ValueError(f"Model {model_name} not supported")

    def _get_chatgpt_response(self, messages):
        """获取 ChatGPT 的响应"""
        api_key = self.config.get_api_key("chatgpt")
        if not api_key:
            raise ValueError("ChatGPT API key not configured")

        openai.api_key = api_key
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            raise RuntimeError(f"ChatGPT API request failed: {str(e)}")

    def _get_deepseek_response(self, messages):
        """获取 DeepSeek 的响应"""
        api_key = self.config.get_api_key("deepseek")
        if not api_key:
            raise ValueError("DeepSeek API key not configured")

        url = "https://api.deepseek.ai/v1/chat"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": messages
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise RuntimeError(f"DeepSeek API request failed: {str(e)}")

    def _get_qwen_response(self, messages):
        """获取 Qwen 的响应"""
        api_key = self.config.get_api_key("qwen")
        if not api_key:
            raise ValueError("Qwen API key not configured")

        url = "https://api.qwen.ai/v1/chat"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": messages
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise RuntimeError(f"Qwen API request failed: {str(e)}")

    def _get_doubao_response(self, messages):
        """获取豆包的响应"""
        api_key = self.config.get_api_key("doubao")
        if not api_key:
            raise ValueError("Doubao API key not configured")

        url = "https://api.doubao.com/v1/chat"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": messages
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise RuntimeError(f"Doubao API request failed: {str(e)}")