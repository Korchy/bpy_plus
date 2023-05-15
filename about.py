# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy


class BPYPlus:
    """ Abstract class with common project info

        :param _current_version: Current version
        :type _current_version : tuple
        :param _blender_version: Blender version with which BPY_plus is compatible
        :type _blender_version : tuple

    """

    _current_version = (1, 8, 2)
    _blender_version = ((2, 93), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6))

    @classmethod
    def version(cls) -> tuple:
        """ Return a current version of the BPY_plus project

        :return: current version number
        :rtype: tuple

        """
        return cls._current_version

    @classmethod
    def compatible_with(cls) -> tuple:
        """ Blender version with which BPY_plus is compatible

        :return: Blender version with which BPY_plus is compatible
        :rtype: tuple

        """
        return cls._blender_version

    @classmethod
    def is_compatible(cls) -> bool:
        """ Check if the BPY_plus is compatible with the current Blender version

        :return: True if compatible, False - if not
        :rtype: bool

        """
        return bpy.app.version[:2] in cls._blender_version
