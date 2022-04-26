# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
from bpy.types import Context, LayerCollection


class Collections:

    @classmethod
    def set_active(cls, name: str, context: Context = bpy.context):
        """ Set collection active by name

        :param name: collection name
        :type name: str
        :param context: context
        :type context: Context

        """
        if col := cls.layer_collection(name=name, context=context):
            context.view_layer.active_layer_collection = col

    @classmethod
    def layer_collection(cls, name: str, context: Context = bpy.context,
                         _layer_collection: LayerCollection = None) -> LayerCollection:
        """ Return layer collection by collection name

        :param name: collection name
        :type name: str
        :param context: context
        :type context: Context
        :param _layer_collection: inline parameter for recursive call
        :type _layer_collection: LayerCollection
        :return: layer collection
        :rtype: LayerCollection

        """

        if _layer_collection is None:
            _layer_collection = context.view_layer.layer_collection
        if _layer_collection.name == name:
            return _layer_collection
        else:
            for l_col in _layer_collection.children:
                if rez := cls.layer_collection(name=name, context=context, _layer_collection=l_col):
                    return rez
