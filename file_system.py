# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
import os
import sys
import tempfile


class Path:

    @staticmethod
    def python() -> str:
        """ Return absolute path to the Blender python.exe executable

        :return: absolute path to python.exe
        :rtype: str

        """
        try:
            # 2.92 and older
            path = bpy.app.binary_path_python
        except AttributeError:
            # 2.93 and later
            path = sys.executable
        return os.path.abspath(path)

    @classmethod
    def current(cls) -> str:
        """ Return path to current open project directory

        :return: absolute path
        :rtype: str

        """
        if bpy.data.filepath:
            return os.path.dirname(os.path.abspath(bpy.data.filepath))
        else:
            return cls.temp()

    @staticmethod
    def temp() -> str:
        """ Return path to the system temporary directory

        :return: absolute path
        :rtype: str

        """
        return tempfile.gettempdir()

    @classmethod
    def abs(cls, path: str) -> str:
        """ Return absolute file path from Blender path

        :param path: Blender path
        :type path: str
        :return: absolute path
        :rtype: str

        """
        if path[:2] == '//':
            return os.path.abspath(
                os.path.join(
                    cls.current(),
                    path[2:]
                )
            )
        else:
            return os.path.abspath(path)
