# Termind

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/) [![PyPI Version](https://img.shields.io/pypi/v/termind.svg)](https://pypi.org/project/termind/)

[中文](README_zh.md) | [English](README.md)

Termind is a command-line AI chat tool focused on providing simple and efficient chat conversation functionality. It supports calling multiple LLM APIs and can be used as a testing tool for various LLM APIs.

## Features

- **Multi-model Support**: Supports calling APIs of multiple LLMs such as ChatGPT, DeepSeek, Qwen, and Doubao.
- **Context Memory**: Can remember chat context to provide a coherent conversation experience.
- **Command-line Interaction**: Interacts with users through a command-line interface, simple and efficient.
- **API Key Management**: Supports configuration and management of API keys for multiple models.
- **Multi-language Support**: Supports chat conversations in multiple languages including Chinese and English.
- **Custom Commands**: Users can define custom commands for quick execution of specific operations.

## Architecture

The architecture of Termind is designed with modularity in mind and mainly consists of the following core modules:

- **Model Adapters**: Responsible for connecting with different large model APIs and handling API requests and responses.
- **Conversation Manager**: Manages the context of chat conversations to ensure conversational coherence.
- **Command-line Interface**: Provides a user-friendly command-line interaction interface.
- **API Key Manager**: Securely stores and manages API keys for each model.
- **Configuration Manager**: Handles the project's configuration files, including model selection, language settings, etc.

### Session Management

```mermaid
sequenceDiagram
    participant User
    participant Termind
    participant LLM

    User->>Termind: termind ask "你好"
    Termind->>Termind: 生成 session_id=20240520_1530
    Termind->>LLM: 发送初始请求
    LLM-->>Termind: 响应内容
    Termind-->>User: 显示回复 + 保存session

    User->>Termind: termind ask "继续上文" --session 20240520_1530
    Termind->>Termind: 加载历史消息
    Termind->>LLM: 发送完整上下文
    LLM-->>Termind: 基于上下文的响应
```

## Installation and Usage

### Installation

Install Termind via PyPI:

```bash
pip install termind
```

### Configuration

For the first use, you need to configure the API keys for each model:

```bash
termind config
```

Follow the prompts to enter the API keys for each model and complete the configuration.

### Usage

Start Termind:

```bash
termind
```

In the command-line interface, you can chat with the selected large model. You can enter commands to switch models, view history, etc.

## Contribution Guidelines

Welcome developers to contribute code, suggest improvements, or report issues for Termind. For specific contribution methods, please refer to the project's contribution guidelines.

## License

Termind is licensed under the MIT License, allowing free use, modification, and distribution.
