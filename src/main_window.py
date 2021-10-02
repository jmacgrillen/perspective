#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        mac_window.py
    Desscription:
        The main window for mac_lib/ui.
    Version:
        1 - Initial release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""

# import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QStatusBar
import qdarkstyle
from maclib.mac_detect import MacDetect


class MacWindow(QMainWindow):
    """
    Base window for mac_lib ui
    """
    menu_bar: QMenuBar
    status_bar: QStatusBar
    scaling_ratio: float
    mac_detect: MacDetect = MacDetect()

    def __init__(self,
                 window_name: str,
                 main_app: QApplication,
                 window_width: int = 800,
                 window_height: int = 600,
                 window_icon: object = None,
                 *args,
                 **kwargs):
        """
        Create a QT main window
        """
        super(MacWindow, self).__init__(*args, **kwargs)
        if self.mac_detect.os_theme == "Dark":
            main_app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        else:
            pass
        self.setWindowTitle(window_name)
        self.resize(window_width, window_height)
        self.status_bar = self.statusBar()
        self.menu_bar = self.menuBar()
        self.show()


if __name__ == "__main__":
    pass
