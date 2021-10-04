#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        main_window.py
    Desscription:
        The main window for image_tools. This uses Tkinter to
        make the GUI.
    Version:
        1 - Initial release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QApplication, QAction
from src.perspective_image import PerspectiveImage
import logging
import maclib.mac_logger as mac_logger
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QStatusBar
import qdarkstyle
from src.perspective_settings import PerspecitveSettings
from maclib.mac_detect import MacDetect


class MacWindow(QMainWindow):
    """
    Base window for mac_lib ui
    """
    menu_bar: QMenuBar
    status_bar: QStatusBar
    scaling_ratio: float
    mac_detect: MacDetect
    logger: logging.Logger
    perspective_settings: PerspecitveSettings

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
        self.logger = logging.getLogger(name=mac_logger.LOGGER_NAME)
        self.mac_detect = MacDetect()
        self.perspective_settings = PerspecitveSettings()
        # Decide whether to use the light or dark theme.
        if self.perspective_settings.app_settings['ui']['theme'] == 'system':
            self.logger.debug("Using system UI theme...")
            if self.mac_detect.os_theme == "Dark":
                main_app.setStyleSheet(qdarkstyle.load_stylesheet(
                    qt_api='pyqt5'))
            else:
                pass
        elif self.perspective_settings.app_settings['ui']['theme'] == 'dark':
            self.logger.debug("Enabling dark theme from saved setting.")
            main_app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        else:
            self.logger.debug("Using default light theme.")
        self.setWindowTitle(window_name)
        # If the window position has been saved in settings, use them to
        # set the position on the window.
        if self.perspective_settings.key_exists('window'):
            if self.perspective_settings.app_settings[
                            'window']['save_pos'] == "True":
                self.logger.debug(
                    "Using settings to place window and set size.")
                self.move(
                    self.perspective_settings.app_settings[
                        'window']['x_coord'],
                    self.perspective_settings.app_settings[
                        'window']['y_coord']
                )
                self.resize(
                    self.perspective_settings.app_settings[
                        'window']['width'],
                    self.perspective_settings.app_settings[
                        'window']['height']
                )
            else:
                self.resize(window_width, window_height)
        else:
            self.resize(window_width, window_height)
        self.status_bar = self.statusBar()
        self.menu_bar = self.menuBar()
        self.show()

    def save_window_geometry(self) -> None:
        """
        Save the window position to the settings file.
        """
        self.logger.debug("Saving window coords before closing app")
        self.perspective_settings.app_settings[
            'window']['width'] = self.width()
        self.perspective_settings.app_settings[
            'window']['height'] = self.height()
        self.perspective_settings.app_settings[
            'window']['x_coord'] = self.x()
        self.perspective_settings.app_settings[
            'window']['y_coord'] = self.y()
        self.perspective_settings.save_settings()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.logger.debug("User pressed the window close button.")
        self.save_window_geometry()
        return super().closeEvent(a0)


class MainWindow(object):
    """
    This is the main window that controls image_tools.
    """
    main_app: QApplication
    main_window: MacWindow
    default_status: str = "Ready"
    logger: logging.Logger
    perspective_settings: PerspecitveSettings

    def __init__(self):
        """
        Create and run the main window for WAD Walker.
        """
        super(MainWindow, self).__init__()
        self.logger = logging.getLogger(name=mac_logger.LOGGER_NAME)
        # Handle high dpi display scaling
        if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
            QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
        self.perspective_settings = PerspecitveSettings()
        self.create_window()
        self.run()

    def load_image(self) -> None:
        """
        Load an image.
        """
        self.main_window.status_bar.showMessage("Loading image")
        p_image = PerspectiveImage()
        p_image.load_image('IMG_2902.JPG')
        self.main_window.status_bar.showMessage("Image loaded successfully")

    def do_nothing(self) -> None:
        """
        Literlly do nothing!
        """
        self.logger.debug("I ain't doin' nuffink.")

    def quit_application(self) -> None:
        """
        Update the settings with the window geometry.
        """
        self.main_window.save_window_geometry()
        self.main_app.quit()

    def create_file_menu(self) -> None:
        """
        Create the main file menu
        """
        open_action = QAction('&Open', self.main_window)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open an image')
        open_action.triggered.connect(self.load_image)

        quit_action = QAction('&Quit', self.main_window)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.setStatusTip('Quit application')
        quit_action.triggered.connect(self.quit_application)

        file_menu = self.main_window.menu_bar.addMenu('&File')
        file_menu.addAction(open_action)
        file_menu.addAction(quit_action)

    def create_edit_menu(self) -> None:
        """
        Create the main Edit menu
        """
        settings_action = QAction('&Settings', self.main_window)
        settings_action.setShortcut('Ctrl+S')
        settings_action.setStatusTip('Adjust application settings')
        settings_action.triggered.connect(self.do_nothing)

        file_menu = self.main_window.menu_bar.addMenu('&Edit')
        file_menu.addAction(settings_action)

    def create_window(self) -> None:
        """
        Create the main WAD Walker window.
        """
        self.main_app = QApplication([])
        self.main_window = MacWindow("Perspective", self.main_app)
        self.create_file_menu()
        self.create_edit_menu()

    def run(self) -> None:
        """
        Run the main window
        """
        # Now show and run the window.
        self.logger.debug("Starting the main application loop.")
        self.main_app.exec()


if __name__ == "__main__":
    pass
