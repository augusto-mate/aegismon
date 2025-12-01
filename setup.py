# /setup.py
from setuptools import setup, find_packages

# Função para ler o número da versão do arquivo VERSION
def read_version():
    with open("VERSION", "r") as f:
        return f.read().strip()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='aegismon',
    version=read_version(), # LÊ DO ARQUIVO VERSION
    description='AegisMon - Advanced Security Scanner Toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='augusto-mate', 
    url='https://github.com/augusto-mate/aegismon',
    packages=find_packages(),
    install_requires=[
        'pyyaml>=6.0',
    ],
    entry_points={
        'console_scripts': [
            'aegismon=aegismon.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.8',
)