#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        perspective.py
    Desscription:
        Perspective app entry point.
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""
import logging
import maclib.mac_logger as mlogger
from src.perspective_settings import PerspecitveSettings
import src.perspective_uris as uris
from src.ui.main_window import PerspectiveWindow

perspective_settings = PerspecitveSettings()


def create_default_settings():
    """
    If there are no settings in the settings file, create them.
    """
    global perspective_settings

    # App logging level
    perspective_settings.app_settings['app'] = dict()
    perspective_settings.app_settings['app']['log_level'] = 'INFO'
    # UI theme
    perspective_settings.app_settings['ui'] = dict()
    perspective_settings.app_settings['ui']['theme'] = "system"
    # Default window settings
    perspective_settings.app_settings['window'] = dict()
    perspective_settings.app_settings['window']['save_pos'] = "True"
    perspective_settings.app_settings['window']['x_coord'] = 60
    perspective_settings.app_settings['window']['y_coord'] = 60
    perspective_settings.app_settings['window']['width'] = 800
    perspective_settings.app_settings['window']['height'] = 600
    perspective_settings.save_settings()


def main():
    """
    Main entry point for Perspective
    """
    # Setup logging so we can trace any issues.
    global perspective_settings

    perspective_logfile = "{0}/{1}".format(
        uris.perspective_logging_directory,
        uris.perspective_log_file_name)
    logger = mlogger.configure_logger(
        log_file_uri=perspective_logfile,
        logging_level=logging.DEBUG)

    perspective_settings.load_settings()
    if len(perspective_settings.app_settings) == 0:
        create_default_settings()
    if perspective_settings.app_settings['app']['log_level'] == 'DEBUG':
        logger.setLevel(logging.DEBUG)
        logger.debug("Logging level set to DEBUG in settings file.")
    elif perspective_settings.app_settings['app']['log_level'] == 'INFO':
        logger.setLevel(logging.INFO)
    elif perspective_settings.app_settings['app']['log_level'] == 'WARN':
        logger.setLevel(logging.WARN)
    elif perspective_settings.app_settings['app']['log_level'] == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif perspective_settings.app_settings['app']['log_level'] == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)

    PerspectiveWindow()


if __name__ == "__main__":
    main()
