import cmd
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from termind.config import ConfigManager
from termind.models import ModelAdapter
from termind.conversation import ConversationManager

class TermindCLI(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.config = ConfigManager()
        self.model_adapter = ModelAdapter()
        self.conversation = ConversationManager()
        self.prompt = "Termind > "
        self.intro = self._get_intro()

    def _get_intro(self):
        """获取欢迎信息"""
        lang = self.config.get_language()
        if lang == "zh":
            return "欢迎使用 Termind 命令行 AI 聊天工具！输入 'help' 查看可用命令。"
        else:
            return "Welcome to Termind Command-line AI Chat Tool! Type 'help' to see available commands."

    def do_chat(self, arg):
        """开始聊天"""
        lang = self.config.get_language()
        if lang == "zh":
            print("\n[bold green]开始聊天 [/bold green]")
            print("输入内容后按回车发送，输入 'exit' 结束聊天，输入 'clear' 清除历史")
        else:
            print("\n[bold green]Start Chat [/bold green]")
            print("Type your message and press Enter to send, type 'exit' to end chat, type 'clear' to clear history")

        while True:
            try:
                user_input = Prompt.ask("You")
                if user_input.lower() == "exit":
                    break
                elif user_input.lower() == "clear":
                    self.conversation.clear_history()
                    print("[bold yellow]History cleared[/bold yellow]")
                    continue

                self.conversation.add_message("user", user_input)
                current_model = self.config.get_current_model()
                try:
                    response = self.model_adapter.get_response(current_model, self.conversation.get_history())
                except Exception as e:
                    print(f"[bold red]Error:[/bold red] {str(e)}")
                    continue

                self.conversation.add_message("assistant", response)
                print(Panel.fit(response, title="Assistant", border_style="blue"))

            except KeyboardInterrupt:
                print("\n[bold yellow]Chat interrupted[/bold yellow]")
                break

    def do_setmodel(self, arg):
        """设置当前使用的模型"""
        models = ["chatgpt", "deepseek", "qwen", "doubao"]
        if arg not in models:
            print(f"[bold red]Invalid model. Available models: {', '.join(models)}[/bold red]")
            return

        self.config.set_current_model(arg)
        lang = self.config.get_language()
        if lang == "zh":
            print(f"[bold green]当前模型已设置为 {arg}[/bold green]")
        else:
            print(f"[bold green]Current model set to {arg}[/bold green]")

    def do_setkey(self, arg):
        """设置模型的 API 密钥"""
        args = arg.split()
        if len(args) != 2:
            print("[bold red]Usage: setkey <model_name> <api_key>[/bold red]")
            return

        model_name, api_key = args
        self.config.set_api_key(model_name, api_key)
        lang = self.config.get_language()
        if lang == "zh":
            print(f"[bold green]模型 {model_name} 的 API 密钥已设置[/bold green]")
        else:
            print(f"[bold green]API key for model {model_name} set[/bold green]")

    def do_setlang(self, arg):
        """设置语言"""
        if arg not in ["zh", "en"]:
            print("[bold red]Invalid language. Available options: zh, en[/bold red]")
            return

        self.config.set_language(arg)
        lang = self.config.get_language()
        if lang == "zh":
            print(f"[bold green]语言已设置为中文[/bold green]")
        else:
            print(f"[bold green]Language set to English[/bold green]")

    def do_setcontext(self, arg):
        """设置上下文长度"""
        try:
            length = int(arg)
            if length <= 0:
                raise ValueError
            self.config.set_context_length(length)
            print(f"[bold green]Context length set to {length}[/bold green]")
        except ValueError:
            print("[bold red]Invalid context length. Please enter a positive integer[/bold red]")

    def do_config(self, arg):
        """显示当前配置"""
        current_model = self.config.get_current_model()
        language = self.config.get_language()
        context_length = self.config.get_context_length()
        models = self.config.config["models"]

        print("\n[bold green]Current Configuration:[/bold green]")
        print(f"  Current Model: {current_model}")
        print(f"  Language: {'中文' if language == 'zh' else 'English'}")
        print(f"  Context Length: {context_length}")
        print("\n  Models API Keys:")
        for model, info in models.items():
            key_status = "configured" if info["api_key"] else "not configured"
            print(f"    {model}: {key_status}")

    def do_exit(self, arg):
        """退出程序"""
        print("[bold green]Thank you for using Termind. Goodbye![/bold green]")
        return True

    def do_help(self, arg):
        """显示帮助信息"""
        lang = self.config.get_language()
        if lang == "zh":
            help_text = """
            Termind 命令行 AI 聊天工具命令列表:

            chat        - 开始与当前模型聊天
            setmodel <model_name> - 设置当前使用的模型
            setkey <model_name> <api_key> - 设置模型的 API 密钥
            setlang <zh|en> - 设置语言为中文或英文
            setcontext <length> - 设置上下文长度
            config      - 显示当前配置
            exit        - 退出程序
            help        - 显示帮助信息
            """
        else:
            help_text = """
            Termind Command-line AI Chat Tool Command List:

            chat        - Start chatting with the current model
            setmodel <model_name> - Set the current model
            setkey <model_name> <api_key> - Set API key for a model
            setlang <zh|en> - Set language to Chinese or English
            setcontext <length> - Set context length
            config      - Show current configuration
            exit        - Exit the program
            help        - Show help information
            """
        print(Panel.fit(help_text, title="Help", border_style="blue"))

    def emptyline(self):
        """忽略空行"""
        pass

    def default(self, line):
        """处理未知命令"""
        lang = self.config.get_language()
        if lang == "zh":
            print(f"[bold red]未知命令: {line}。输入 'help' 查看可用命令。[/bold red]")
        else:
            print(f"[bold red]Unknown command: {line}. Type 'help' to see available commands.[/bold red]")