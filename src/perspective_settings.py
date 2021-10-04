#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        perspective_settings.py
    Desscription:
        Manage Perspective settings.
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""

from typing import Optional
import logging
import yaml
import maclib.mac_file_management as file_m
import maclib.mac_logger as mac_logger
from maclib.mac_single import MacSingleInstance
import src.perspective_uris as uris


class PerspecitveSettings(object, metaclass=MacSingleInstance):
    """
    Handle the settings for Perspective
    """
    app_settings: dict
    mac_logger: logging.Logger
    settings_file_directory: str = str(uris.perspective_settings_directory)
    settings_file: str = uris.perspective_settings_file_name
    settings_file_full_path: str = "{0}/{1}".format(
                                    settings_file_directory,
                                    settings_file)

    def __init__(self) -> None:
        super(PerspecitveSettings, self).__init__()
        self.app_settings = dict()
        self.mac_logger = logging.getLogger(mac_logger.LOGGER_NAME)

    def load_settings(self) -> Optional[dict]:
        """
        Load the settings.
        """
        # Check the file exists before trying to open it
        if not file_m.does_exist(os_path=self.settings_file_full_path):
            self.mac_logger.info(
                "The settings file %s does not exist. Creating a new one...",
                self.settings_file_full_path)
            if not file_m.does_exist(os_path=self.settings_file_directory):
                if not file_m.create_dir(
                            dir_path=self.settings_file_directory):
                    err_msg = "Could not create the settings " \
                                "directory {0}".format(
                                    self.settings_file_directory)
                    self.mac_logger.error(err_msg)
                    return None
                else:
                    self.save_settings()
            else:
                self.save_settings()
        # Read the settings from a YAML file.
        try:
            with open(file=self.settings_file_full_path,
                      mode='rb') as yml_file:
                self.app_settings = yaml.safe_load(stream=yml_file)
            self.mac_logger.info("Successfully loaded the settings.")
        except yaml.YAMLError as yaml_error:
            self.mac_logger.error("There was a problem parsing"
                                  " the file %s.\n%s", self.settings_file,
                                  yaml_error)
        return self.app_settings

    def save_settings(self) -> None:
        """
        Save all the settings back to the settings file.
        """
        try:
            self.mac_logger.debug("Saving settings to {0}".format(
                self.settings_file_full_path
            ))
            with open(file=self.settings_file_full_path,
                      mode='w',) as yml_file:
                yaml.dump(data=self.app_settings,
                          stream=yml_file, indent=4,
                          default_flow_style=False)
            self.mac_logger.debug("Successfully saved settings.")
        except Exception as err:
            self.mac_logger.error("Unable to save settings. {0}", err)

    def key_exists(self, key_name: str) -> bool:
        """
        Check whether the key exists.
        """
        if key_name in self.app_settings.keys():
            return True
        return False


if __name__ == "__main__":
    pass
