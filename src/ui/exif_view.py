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
import tkinter as tk
from tkinter import ttk
from src.tools.exif_data import EXIFData
# import typing


class EXIFView(tk.Frame):
    """
    Display any EXIF data embedded in the image.
    """
    logger: logging.Logger = logging.getLogger(name='it_logger')
    exif_data: EXIFData
    __exif_box: ttk.Treeview

    def __init__(self,
                 parent: tk.Misc,
                 width: int = 50,
                 *args,
                 **kwargs):
        """
        Handle the display of the EXIF data
        """
        super(EXIFView, self).__init__(parent, *args, **kwargs)
        self.grid(row=0, sticky='ns', padx=5.0, pady=2.0)
        self.grid_propagate(True)
        self.__exif_box = ttk.Treeview(master=self,
                                       show='headings',
                                       columns="2")
        self.__exif_box['columns'] = ('key', 'value')
        self.__exif_box.column('#0', width=0, stretch=False)
        self.__exif_box.column('key', width=150, stretch=False)
        self.__exif_box.column('value', width=150)

        self.__exif_box.heading('#0', text='')
        self.__exif_box.heading('key', text='EXIF Data type')
        self.__exif_box.heading('value', text='Value')

        self.__exif_box.grid(row=0, column=1, sticky='ns')
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

    def add_data(self, exif_data: EXIFData):
        """
        Store the EXIF data
        """
        self.logger.debug("Storing exif data.")
        self.exif_data = exif_data
        self.update_data_view()

    def update_data_view(self) -> None:
        """
        Show the exif data
        """
        display_index: int = 0
        self.__exif_box.delete(*self.__exif_box.get_children())
        if hasattr(self, 'exif_data'):
            for index, item in enumerate(self.exif_data.exif_data.items()):
                self.__exif_box.insert(
                    parent='',
                    index=display_index,
                    values=(item[0], item[1])
                )
                display_index = display_index + 1
            self.__exif_box.update()


if __name__ == "__main__":
    pass
