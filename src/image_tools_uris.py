#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        image_tools_uris.py
    Desscription:
        Define all the directories that the wadwalker
        program needs for housekeeping.
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""
from pathlib import Path


base_directory = Path(__file__).resolve().parents[1]
user_home_directory = Path.home()
it_base_directory = Path(
    "{0}/.image_tools".format(
        user_home_directory))
it_settings_directory = Path(
    "{0}/settings".format(
        it_base_directory))
it_settings_file_name = "settings.yaml"
it_logging_directory = Path(
     "{0}/logs".format(
        it_base_directory))
it_temp_directory = Path(
    "{0}/temp".format(
        it_base_directory))
it_log_file_name = "image_tools.log"


if __name__ == "__main__":
    pass
