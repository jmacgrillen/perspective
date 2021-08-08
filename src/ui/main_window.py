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

import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import filedialog as file_dialog
import logging
from maclib.ui.main_window import MacWindow
from src.it_image import ITImage


class MainWindow(object):
    """
    This is the main window that controls image_tools.
    """
    main_window: MacWindow
    menu_bar: tk.Menu
    main_app: tk.Tk
    default_status: str = "Ready"
    logger: logging.Logger = logging.getLogger(name='it_logger')

    def __init__(self):
        """
        Create and run the main window for WAD Walker.
        """
        self.create_window()
        i_image = ITImage()
        i_image.load_image('IMG_2902.JPG')
        self.run()

    def do_nothing(self) -> None:
        """
        A function that literally does nothing.
        """
        pass

    def create_file_menu(self) -> tk.Menu:
        """
        Create the main file menu
        """
        filemenu = tk.Menu(self.main_window.menu_bar, tearoff=0)
        filemenu.add_command(label="Open", command=self.do_nothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.main_app.quit)
        return filemenu

    def create_window(self) -> None:
        """
        Create the main WAD Walker window.
        """
        self.main_app = tk.Tk()
        self.main_app.title("Image Tools")
        self.main_window = MacWindow(parent=self.main_app)
        self.main_window.add_status_bar(self.default_status)
        # Add the menus to the window
        self.main_window.add_menu_bar()
        file_menu = self.create_file_menu()
        self.main_window.menu_bar.add_cascade(label="File",
                                              menu=file_menu)

    def run(self) -> None:
        """
        Run the main window
        """
        # Now show and run the window.
        self.logger.debug("Starting the main loop.")
        self.main_window.mainloop()
