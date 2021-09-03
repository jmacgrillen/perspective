#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        mac_dockable.py
    Desscription:
        Dockable widget.
    Version:
        1 - Initial release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""

import tkinter as tk
from tkinter import ttk


class MacDockable(ttk.Frame):
    """
    Base class for all dockable widgets.
    """
    docked: bool
    widget_name: str

    def __init__(self,
                 parent: tk.Misc,
                 name: str,
                 *args,
                 **kwargs):
        """
        Initialise the widget
        """
        super(ttk.Frame, self).__init__(parent,
                                        widgetname=name,
                                        *args,
                                        **kwargs)
        self.widget_name = name
        self.bind("<ButtonPress-1>", self.start_resize)
        self.bind("<ButtonRelease-1>", self.stop_resize)

    def start_resize(self, event):
        """
        Start resizing the frame view
        """
        print("Button down detected")
        print(type(event))

    def stop_resize(self, event):
        """
        Stop resizing the frame view
        """
        print("Button up detected")
        print(type(event))


if __name__ == "__main__":
    pass
