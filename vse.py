# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
from bpy.types import Context


class VSE:

    @staticmethod
    def next_empty_channel(context: Context = bpy.context) -> int:
        """ Return number of the next empty channel

        :param context: context
        :type context: Context
        :return: next empty channel number
        :rtype: int

        """
        return max([0] + [seq.channel for seq in context.scene.sequence_editor.sequences_all]) + 1
