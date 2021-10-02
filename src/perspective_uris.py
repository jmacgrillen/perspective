#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        perspective_uris.py
    Desscription:
        Define all the directories that Perspective
        needs for housekeeping.
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
perspective_base_directory = Path(
    "{0}/.perspective".format(
        user_home_directory))
perspective_settings_directory = Path(
    "{0}/settings".format(
        perspective_base_directory))
perspective_settings_file_name = "settings.yaml"
perspective_logging_directory = Path(
     "{0}/logs".format(
        perspective_base_directory))
perspective_temp_directory = Path(
    "{0}/temp".format(
        perspective_base_directory))
perspective_log_file_name = "perspective.log"


if __name__ == "__main__":
    pass
