#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        exif_view.py
    Desscription:
        Display any EXIF data attached to the image.
    Version:
        1 - Initial release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""
import logging

from PyQt5.QtWidgets import QDockWidget, QVBoxLayout
from src.tools.exif_data import EXIFData
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

self.logger.debug("Trying to extract EXIF data...")
self.exif_data = EXIFData(self.pil_image)
class EXIFView(QDockWidget):
    """
    EXIF viewer
    """
    v_layout: QVBoxLayout

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()


if __name__ == "__main__":
    pass
