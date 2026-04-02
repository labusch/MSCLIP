import os

from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name="msclip",
    py_modules=["msclip"],
    version="1.0",
    description="",
    author="Hxyou",
    packages=find_packages(exclude=["tests*"]),
    install_requires=install_requires,
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
