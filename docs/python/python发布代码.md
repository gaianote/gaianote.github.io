# 使用 setup.py 构建和发布 python 包

## 1. 查看已安装的第三方库

使用 pipenv graph 查看虚拟环境中已安装的第三方库

```bash
✗ pipenv graph
autopep8==1.5.4
  - pycodestyle [required: >=2.6.0, installed: 2.6.0]
  - toml [required: Any, installed: 0.10.2]
black==20.8b1
  - appdirs [required: Any, installed: 1.4.4]
  - click [required: >=7.1.2, installed: 7.1.2]
  - mypy-extensions [required: >=0.4.3, installed: 0.4.3]
  - pathspec [required: >=0.6,<1, installed: 0.8.1]
  - regex [required: >=2020.1.8, installed: 2020.11.13]
  - toml [required: >=0.10.1, installed: 0.10.2]
  - typed-ast [required: >=1.4.0, installed: 1.4.2]
  - typing-extensions [required: >=3.7.4, installed: 3.7.4.3]
```

## 2. 编写 setup 文件

按照以下模版编写 setup.py 文件, 并将需要的第三方库的名称和版本复制到 setup.py 中

```python
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

VERSION = "0.0.3"

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pwork",
    version=VERSION,
    packages=["pwork"],
    url="https://github.com/gaianote/python-framework",
    author="gaianote",
    author_email="gaianote311@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    entry_points={"console_scripts": ["pwork = pwork.app:main"]},
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "mypy",
            "flake8",
            "black",
            "isort",
            "pytest-cov",
            "pre-commit",
        ]
    },
)
```

### 3. 安装项目和依赖

在开发过程中,我们可以使用命令安装到本地

```bash
pip install -e ".[dev]"
```

### 4. 打包上传到pypi

使用check命令查看是否存在语法问题，使用sdist进行打包。

```bash
python3 setup.py check
python3 setup.py sdist
```

发布前，需要到 [pypi官网](https://pypi.org/) 注册一个账号，并在用户目录新建文件 ~/.pypirc ，并键入以下内容

```bash
[distutils]
index-servers = pypi
[pypi]
repository: https://pypi.python.org/pypi
username: yourname
password: yourpwd
```

执行以下内容进行打包上传，服务器返回Server response (200): OK表示上传成功

```bash
python3 setup.py sdist upload
```

发布成功后就可以使用 pip install安装你自己的python包了！