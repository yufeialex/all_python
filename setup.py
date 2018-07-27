# coding:utf8
from setuptools import setup, find_packages

setup(
    name='MyApp',  # 应用名
    version='1.0',  # 版本号
    # packages=['myapp'],  # 包括在安装包内的Python包
    packages=find_packages(),  # 包括在安装包内的Python包
    include_package_data=True,  # 启用清单文件MANIFEST.in
    exclude_package_date={'': ['.gitignore']},
    # install_requires=[  # 依赖列表
    #     'Flask>=0.10',
    #     'Flask-SQLAlchemy>=1.5,<=2.1'
    # ],
    dependency_links=[  # 依赖包下载路径
        'http://example.com/dependency.tar.gz'
    ],
    # 提供了更多当前应用的细节信息，对打包安装并无任何影响
    author="Billy He",
    author_email="billy@bjhee.com",
    description="This is a sample package",
    license="MIT",
    keywords="hello world example",
    url="http://example.com/HelloWorld/",  # 项目主页
    long_description=__doc__, install_requires=['tornado', 'prometheus_client']  # 从代码中获取文档注释
)
