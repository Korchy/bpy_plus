# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
from bpy.types import Context
from .file_system import Path


class Output:

    @staticmethod
    def extension(context: Context = bpy.context, animation: bool = False) -> str:
        """ Return output file extension

        :param context: context
        :type context: Context
        :param animation: False - for single image, True - for animation
        :type animation: bool
        :return: extension
        :rtype: str

        """
        if animation:
            if context.scene.render.image_settings.file_format in ['AVI_JPEG', 'AVI_RAW']:
                return 'avi'
            elif context.scene.render.image_settings.file_format == 'FFMPEG':
                ext = {
                    'MPEG1': 'mpeg1',
                    'MPEG2': 'mpeg2',
                    'MPEG4': 'mp4',
                    'AVI': 'avi',
                    'QUICKTIME': 'mov',
                    'DV': 'dv',
                    'OGG': 'ogg',
                    'MKV': 'mkv',
                    'FLASH': 'flv',
                    'WEBM': 'webm'
                }
                return ext[context.scene.render.ffmpeg.format]
        else:
            return context.scene.render.file_extension[1:]

    @staticmethod
    def path(context: Context = bpy.context) -> str:
        """ Return output render path

        :param context: context
        :type context: Context
        :return: render absolute output path
        :rtype: str

        """
        return Path.abs(
            path=context.scene.render.filepath
        )
