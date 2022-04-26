# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
from bpy.types import Context as BpyContext


class Context:

    @staticmethod
    def override(area_type: str, context: BpyContext = bpy.context) -> dict:
        """ Return context from the required area for override
            The required area must be opened

        :param area_type: area type
        :type area_type: str
        :param context: context
        :type context: BpyContext
        :return: context data for override
        :rtype: dict

        """
        override_context = context.copy()
        area = next((area for area in context.screen.areas if area.type == area_type), None)
        if area:
            override_context['window'] = context.window
            override_context['screen'] = context.screen
            override_context['area'] = area
            override_context['region'] = area.regions[-1]
            override_context['scene'] = context.scene
            override_context['space_data'] = area.spaces.active
            return override_context
        else:
            print('The required area must be opened')
