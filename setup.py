# -*- coding: utf-8 -*-
# Copyright (c) XiMing Xing. All rights reserved.
# Author: XiMing Xing

from setuptools import setup
import os

setup(
    name='pytorch_svgrender',
    version="0.1.0",
    packages=['pytorch_svgrender'],
    package_data={'pytorch_svgrender': ['py.typed']},
    install_requires=[
    ],
    python_requires=">=3.7",
    author='Ximing Xing, Juncheng Hu et al.',
    author_email='ximingxing@gmail.com',
    description='SVG Differentiable Rendering: Generating vector graphics using neural networks.',
    long_description="",
    long_description_content_type="text/markdown",
    keywords=[
        'Artificial Intelligence',
        'AIGC',
        'Generative Models',
        'SVG Generation',
    ],
    url='https://github.com/ximinng/PyTorch-SVGRender',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
