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
from src.tools.exif_data import EXIFData
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class EXIFModel(QtCore.QAbstractTableModel):
    """
    Data model for displaying EXIF in a QT Table view
    """
    _data: dict
    _headers: list
    logger: logging.Logger = logging.getLogger(name='it_logger')

    def __init__(self, exif_data: dict, columnm_headers: list) -> None:
        """
        Initialise the data class
        """
        super(EXIFModel, self).__init__()
        self.logger.debug("Initialising the EXIF data model")
        self._data = exif_data
        self._headers = columnm_headers

    def data(self, index, role):
        """
        Handle the call to get the data
        """
        if role == Qt.DisplayRole:
            # Look up the key by header index.
            column = index.column()
            column_key = self._headers[column]
            return self._data[index.row()][column_key]

    def rowCount(self, index):
        """
        Return the size of data set
        """
        return len(self._data)

    def columnCount(self, index):
        """
        Return the numberof columns based on the headers
        """
        return len(self._headers)

    def headerData(self, section, orientation, role):
        """
        Handle the display.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                return str(section)


if __name__ == "__main__":
    pass
