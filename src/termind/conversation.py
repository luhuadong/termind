from termind.config import ConfigManager

class ConversationManager:
    def __init__(self):
        self.config = ConfigManager()
        self.history = []

    def add_message(self, role, content):
        """添加消息到对话历史"""
        self.history.append({"role": role, "content": content})
        # 保持上下文长度
        max_length = self.config.get_context_length()
        if len(self.history) > max_length:
            self.history = self.history[-max_length:]

    def get_history(self):
        """获取对话历史"""
        return self.history

    def clear_history(self):
        """清除对话历史"""
        self.history = []