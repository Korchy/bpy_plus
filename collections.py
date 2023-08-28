# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
from bpy.types import Context, Collection, LayerCollection, Operator
from bpy.utils import register_class
from .context import Context as Cntx


class Collections:

    @staticmethod
    def active(context: Context = bpy.context) -> Collection:
        """ Get active collection

        :param context: context
        :type context: Context
        :return: Active collection
        :rtype: Collection

        """
        return context.collection

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

    @staticmethod
    def selected() -> tuple:
        """ Return selected collections list

        :return: selected collections list
        :rtype: tuple

        """

        class OUTLINER_OT_selected_collections(Operator):
            bl_idname = 'outliner.selected_collections'
            bl_label = 'Selected Collections'

            def execute(self, context):
                selected_ids = context.selected_ids
                context.window_manager['selected_collections'] = tuple(sel for sel in selected_ids
                                                                       if sel.rna_type.name == 'Collection')
                return {'FINISHED'}

        if not hasattr(bpy.types, bpy.ops.outliner.selected_collections.idname()):
            register_class(OUTLINER_OT_selected_collections)

        override_context = Cntx.override(area_type='OUTLINER')
        if override_context:
            bpy.ops.outliner.selected_collections(override_context)
            selected_collections = tuple(bpy.context.window_manager['selected_collections'][:])
            del bpy.context.window_manager['selected_collections']
            return selected_collections
        else:
            return ()

    @staticmethod
    def all(context: Context = bpy.context) -> list:
        """ Get all scene collection

        :param context: context
        :type context: Context
        :return: Collection list
        :rtype: list

        """
        all_collections = context.blend_data.collections[:]
        all_collections.append(context.scene.collection)
        return all_collections

    @classmethod
    def parent(cls, context: Context = bpy.context, collection: Collection = None) -> Collection:
        """ Get active collection

        :param context: context
        :type context: Context
        :param collection: Collection to get parent for
        :type collection: Collection
        :return: Collection
        :rtype: Collection

        """
        collection = collection if collection else cls.active(context=context)
        all_collections = cls.all(context=context)
        return next((_collection for _collection in all_collections
                     if collection.name in _collection.children),
                    None)

    @classmethod
    def move(cls, collection: Collection, to: Collection) -> None:
        """ Get active collection

        :param collection: collection to move
        :type collection: Collection
        :param to: move to this collection
        :type to: Collection
        :return None
        :rtype None

        """
        parent = cls.parent(collection=collection)
        if parent:
            parent.children.unlink(collection)
        to.children.link(collection)
