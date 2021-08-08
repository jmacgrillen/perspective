#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        it_image.py
    Desscription:
        The main image class for Image Tools
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""
from typing import Any
import logging
from PIL import Image
from src.tools.exif_data import EXIFData


class ITImage(object):
    """
    This is the class that stores the main image.
    """
    logger: logging.Logger = logging.getLogger(name='it_logger')
    pil_image: Any
    exif_data: EXIFData

    def __init__(self) -> None:
        super().__init__()

    def load_image(self, image_path: str) -> None:
        """
        Use Pillow to load the image.
        """
        self.logger.info(f"Opening image {image_path}...")
        self.pil_image = Image.open(image_path)
        try:
            self.pil_image.verify()
            self.logger.info(f"Image {image_path} loaded sucessfully.")
        except Exception:
            self.logger.error(f"Unable to load image {image_path}")
        self.logger.debug("Trying to extract EXIF data...")
        self.exif_data = EXIFData(self.pil_image)


if __name__ == "__main__":
    pass
