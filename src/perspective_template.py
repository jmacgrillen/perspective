"""
    Name:
        perspective_template.py
    Desscription:
        Base class for a factory pattern
    Version:
        1 - Inital release
    Author:
        J.MacGrillen <macgrillen@gmail.com>
    Copyright:
        Copyright (c) John MacGrillen. All rights reserved.
"""

from abc import ABC, abstractmethod


class PerspectivePlugin(ABC):
    """
    Base class for all prespective plugins
    """

    @abstractmethod
    def register_plugin(self):
        """
        Register the plugin with the factory
        """
        pass


if __name__ == "__main__":
    pass
