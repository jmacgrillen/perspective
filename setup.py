#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        setup.py
    Desscription:
        Install the maclib package.
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requirements = [
    "maclib",
    "opencv-python",
    "numpy",
    "Pillow",
    "charset-normalizer"
]


def setup_perspective_package() -> None:
    """
    Install and configure Perspective for use
    """
    setup(
        name='Perspective',
        version="0.0.1",
        description='Analyse images using the range of tools provided',
        long_description=long_description,
        author='J.MacGrillen',
        scripts=[],
        packages=find_packages(exclude=['tests*']),
        include_package_data=True,
        install_requires=install_requirements,
        license="MIT License",
        python_requires=">= 3.7.*",
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
        ],
    )


if __name__ == "__main__":
    setup_perspective_package()
