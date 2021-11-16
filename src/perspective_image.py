#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        perspective_image.py
    Desscription:
        The main image class for Perspective
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""
import logging
import maclib.mac_logger as mac_logger
from maclib.mac_exception import MacException
import numpy
import cv2


class PerspectiveImageLoadError(MacException):
    """
    Throw an exception if the image fails to load
    """


class PerspectiveImage(object):
    """
    This is the class that stores the main image.
    """
    logger: logging.Logger
    per_image: numpy.ndarray
    image_load_error: bool

    def __init__(self, image_path: str) -> None:
        self.logger = logging.getLogger(name=mac_logger.LOGGER_NAME)
        self.logger.debug("Prespective image created.")
        self.image_load_error = True
        self.load_image(image_path)
        super().__init__()

    def load_image(self, image_path: str) -> None:
        """
        Use Pillow to load the image.
        """
        self.logger.info(f"Opening image {image_path}...")
        self.per_image = cv2.imread(filename=image_path)
        # Check the image has loaded.
        if self.per_image.size == 0:
            self.image_load_error = True
            raise(PerspectiveImageLoadError(
                f"Image {image_path} loaded successfully."))
        else:
            self.logger.debug(f"Image {image_path} successfully loaded.")
            self.image_load_error = False


if __name__ == "__main__":
    pass
