#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        image_view.py
    Desscription:
        Take the supplied image and display it.
    Version:
        1 - Initial release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""

from PyQt5.QtWidgets import QLabel
import PyQt5.QtGui as QtGui
from src.perspective_image import PerspectiveImage
import imutils
import cv2


class PerspectiveImageView(QLabel):
    """
    A warpper around the view and screen
    """
    p_image: PerspectiveImage
    local_image: QtGui.QPixmap

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialise the components
        """
        super(PerspectiveImageView, self).__init__(*args, **kwargs)

    def load_image(self, image_path: str) -> None:
        """
        Load the image and display.
        """
        self.p_image = PerspectiveImage(image_path)
        self.draw_image(self.p_image.per_image)

    def draw_image(self, image) -> None:
        """
        Draw the image to fit the view.
        """
        imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(frame, frame.shape[1],
                             frame.shape[0], frame.strides[0],
                             QtGui.QImage.Format_RGB888)
        self.setPixmap(QtGui.QPixmap.fromImage(image))


if __name__ == "__main__":
    pass
