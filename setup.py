from setuptools import setup, find_packages

setup(
    name="hexlet-code",
    version="0.1.0",
    description="Compares two configuration files and shows a difference.",
    author="Ваше имя",
    author_email="your.email@example.com",
    url="https://github.com/Grimmlok626/python-project-50",
    python_requires=">=3.6",
    packages=find_packages(where="src"),  # искать пакеты внутри src/
    package_dir={"": "src"},              # src = корень пакетов
    py_modules=["gendiff"],               # добавить одиночный модуль gendiff.py
    entry_points={
        "console_scripts": [
            "gendiff=gendiff:main",       # точка входа для CLI
        ],
    },
    install_requires=[],
)