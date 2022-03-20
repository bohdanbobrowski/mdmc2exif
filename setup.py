#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from setuptools import setup


setup(
    name="mdmc2exif",
    version="1.2.1",
    description="Simple script to add specific ImageDescription EXIF tag to images, based on data stored in csv file.",
    url="https://github.com/bohdanbobrowski/mdmc2exif",
    author="Bohdan Bobrowski",
    author_email="bohdanbobrowski@gmail.com",
    license="MIT",
    packages=["mdmc2exif"],
    install_requires=[
        "piexif",
    ],
    entry_points={
        "console_scripts": [
            "mdmc2exif = mdmc2exif.mdmc2exif:main",
        ]
    },
)
