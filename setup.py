from setuptools import setup, find_packages

setup(
    name="gendiff",
    version="0.1.0",
    description="Compares two configuration files and shows a difference.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gendiff=gendiff.gendiff:main",
        ],
    },
    install_requires=[
        # Укажите зависимости, если есть
    ],
    author="Ваше имя",
    author_email="your.email@example.com",
    url="https://github.com/Grimmlok626/python-project-50",
    python_requires=">=3.6",
)
