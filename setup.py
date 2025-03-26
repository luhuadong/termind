from setuptools import setup, find_packages

setup(
    name="termind",
    version="0.1.0",
    author="luhuadong",
    author_email="luhuadong@163.com",
    description="A command-line AI chat tool for testing various large model APIs",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/luhuadong/termind",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "openai>=0.27.0",
        "requests>=2.26.0",
        "rich>=12.4.0",
        "python-dotenv>=0.19.0"
    ],
    entry_points={
        "console_scripts": [
            "termind=termind.cli:main",
        ],
    },
)