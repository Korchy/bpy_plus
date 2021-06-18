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


def set_active(obj, context=bpy.context):
    """ Set object as active

    """
    if obj:
        context.view_layer.objects.active = obj


def duplicate(obj, data=True, actions=True, collection=None, context=bpy.context):
    """ Duplicate object

    :param obj: source object
    :type obj: Object
    :param data: True - copy object's data, False - linked
    :type data: bool
    :param actions: True - copy object's actions, False - linked
    :type actions: bool
    :param collection: collection to place object's copy, None - active collection
    :type collection: Collection
    :param context: context
    :type context: context
    :return: copy of the source object
    :rtype: Object

    """
    if obj:
        obj_copy = obj.copy()
        if data:
            obj_copy.data = obj_copy.data.copy()
        if actions and obj_copy.animation_data:
            obj_copy.animation_data.action = obj_copy.animation_data.action.copy()
        if not collection:
            collection = context.collection
        collection.objects.link(obj_copy)
        return obj_copy
    else:
        return None
