#! /usr/bin/env python -*- coding: utf-8 -*-
"""
    Name:
        it_image.py
    Desscription:
        The main image class for Image Tools
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""
from typing import Any, Optional
import logging
from PIL.ExifTags import TAGS, GPSTAGS


class EXIFData(object):
    """
    Handle any EXIF data associated with the image.
    """
    logger: logging.Logger = logging.getLogger(name='it_logger')
    exif_data: dict
    lat: float
    long: float

    def __init__(self, image_data: Any) -> None:
        """
        Strip the EXIF data from the image, decoding and
        storing it for later use.
        """
        super().__init__()
        labeled: dict = {}
        self.logger.debug("Attempting to extract EXIF data.")
        self.exif_data = image_data._getexif()
        if not self.exif_data:
            self.logger.debug("Image does not have any attached EXIF data.")
        else:
            self.logger.debug("Found EXIF data. Attempting decode...")
            for (tag, val) in self.exif_data.items():
                # The MakerNote is in multiple proprietary binary formats
                # with some that can't be decoded. Ignore it.
                tag_label = TAGS.get(tag, tag)
                if tag_label == "GPSInfo":
                    self.logger.info("Found GPS data. Decoding...")
                    gps_data: dict = {}
                    for gps_item in val:
                        gps_decoded = GPSTAGS.get(gps_item, gps_item)
                        gps_data[gps_decoded] = val[gps_item]
                    labeled[tag_label] = gps_data
                elif tag_label != "MakerNote":
                    if isinstance(val, bytes):
                        val = val.decode()
                    labeled[tag_label] = val
            if "GPSInfo" in labeled:
                self.logger.debug("Getting lat and long coords.")
                self.lat, self.long = self._get_lat_lon(exif_data=labeled)
            self.exif_data = labeled
            self.logger.debug("All EXIF data exracted.")

    def _get_lat_lon(self, exif_data: dict) -> tuple:
        """
        Returns the latitude and longitude, if available
        from the provided exif_data.
        """
        lat: Optional[float] = None
        lon: Optional[float] = None

        if "GPSInfo" in exif_data:
            gps_info: dict = exif_data["GPSInfo"]

            gps_latitude: tuple = self._get_if_exist(data=gps_info,
                                                     key='GPSLatitude')
            gps_latitude_ref: str = self._get_if_exist(data=gps_info,
                                                       key='GPSLatitudeRef')
            gps_longitude: tuple = self._get_if_exist(data=gps_info,
                                                      key='GPSLongitude')
            gps_longitude_ref: str = self._get_if_exist(data=gps_info,
                                                        key='GPSLongitudeRef')

            if (gps_latitude and gps_latitude_ref
                    and gps_longitude and gps_longitude_ref):
                lat = self._convert_to_degress(value=gps_latitude)
                if gps_latitude_ref != "N":
                    lat = 0 - lat

                lon = self._convert_to_degress(value=gps_longitude)
                if gps_longitude_ref != "E":
                    lon = 0 - lon
        return lat, lon

    def _get_if_exist(self, data: dict, key: str) -> Any:
        """
        Check if the key exists in the dictionary and return the
        value if it does.
        """
        return data.get(key, None)

    def _convert_to_degress(self, value: tuple) -> float:
        """
        Function to convert the GPS coordinates stored in the EXIF to
        degress in float format
        """
        degrees = value[0]
        minutes = value[1] / 60.0
        seconds = value[2] / 3600.0

        return degrees + minutes + seconds


if __name__ == "__main__":
    pass
