#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        image_tools.py
    Desscription:
        image_tools entry point.
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""
import logging
import maclib.mac_logger as mlogger
import src.image_tools_uris as uris
from src.ui.main_window import MainWindow


def main():
    """
    Main entry point for image_tools
    """
    # Setup logging so we can trace any issues.
    it_logfile = "{0}/{1}".format(
        uris.it_logging_directory,
        uris.it_log_file_name)
    mlogger.configure_logger(
        log_file_uri=it_logfile,
        logging_level=logging.DEBUG,
        logger_name="it_logger")

    MainWindow()


if __name__ == "__main__":
    main()
