# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy


def select_all(context=bpy.context):
    """ Select all objects

    """
    for obj in context.blend_data.objects:
        obj.select_set(True)


def deselect_all(context=bpy.context):
    """ Deselect all objects

    """
    for obj in context.blend_data.objects:
        obj.select_set(False)
