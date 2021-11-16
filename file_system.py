# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
import os
import site
import sys
import tempfile


class Path:

    @staticmethod
    def python() -> str:
        """ Return absolute path to the Blender python.exe executable

        :return: absolute path to python.exe
        :rtype: str

        """
        if bpy.app.version[:2] <= (2, 92):
            # 2.92 and older
            path = bpy.app.binary_path_python
        else:
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

    @staticmethod
    def blender() -> str:
        """ Return path to the blender installation directory

        :return: absolute path
        :rtype: str

        """
        return os.path.dirname(bpy.app.binary_path)

    @classmethod
    def blender_v(cls) -> str:
        """ Return path to the blender version installation directory

        :return: absolute path
        :rtype: str

        """
        return os.path.join(cls.blender(), '.'.join(map(str, bpy.app.version[:2])))

    @classmethod
    def scripts(cls, source='USER') -> str:
        """ Return path to the 'scripts' directory

        :param source: ['USER', 'SYSTEM'] - from where directory is
        :type source: str
        :return: absolute path
        :rtype: str

        """
        rez = None
        if source == 'USER':
            rez = bpy.utils.user_resource('SCRIPTS')
        elif source == 'SYSTEM':
            rez = os.path.join(cls.blender_v(), 'scripts')
        return rez

    @classmethod
    def site_packages(cls, source='USER') -> str:
        """ Return path to the 'site-packages' directory

        :param source: ['USER', 'SYSTEM'] - from where directory is
        :type source: str
        :return: absolute path
        :rtype: str

        """
        site_packages_dir = None
        if source == 'USER':
            site_packages_dir = site.getusersitepackages()
            if not os.path.exists(site_packages_dir):
                site_packages_dir = os.path.join(cls.scripts(source=source), 'site-packages')
                if not os.path.exists(site_packages_dir):
                    os.makedirs(site_packages_dir)
        elif source == 'SYSTEM':
            site_packages_dir = next((path for path in site.getsitepackages() if 'site-packages' in path), None)
        return site_packages_dir

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
