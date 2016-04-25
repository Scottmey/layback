import sys, os
from setuptools import setup, find_packages
import subprocess

setup(
    name="Layback",
    version="0.0.2",
    description="Command-line tool which creates an animated GIF of a given URLs history.",
    long_description=open('README.md').read(),
    url="http://github.com/scottmey/layback",
    author="Scott Meyers",
    author_email="scottmey@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5.1'
    ],
    keywords="wayback machine archive mementos",
    packages=find_packages(),
    install_requires=['imageio', 'numpy', 'selenium'],
    entry_points={
        "console_scripts": [ "layback = layback_machine.cli:main" ]
    }
)
