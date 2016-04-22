import sys, os
from setuptools import setup, find_packages
import subprocess

setup(
    name="Layback Machine",
    version="0.0.1.dev1",
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
    ],
    keywords="wayback machine archive mementos",
    packages=find_packages(exclude=['selenium', 'imageio']),
    install_requires=['selenium', 'imageio'],
    entry_points={
        "console_scripts": [ "layback = layback_machine.cli:main" ]
    }
)
