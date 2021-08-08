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


class EXIFView(object):
    """
    Display any EXIF data embedded in the image.
    """
    logger: logging.Logger = logging.getLogger(name='it_logger')


if __name__ == "__main__":
    pass
