# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
import functools
import os
import re
from .output import Output


class RenderSequence:
    """ Static class for render sequence of frames

    """
    mode = 'IDLE'  # current mode (IDLE, RENDER, CANCEL)
    _render_retry_interval = 0.5  # sek
    _render_call_interval = 0.25  # sek
    _frames = []  # frames to render
    _context_override = None    # Need for 2.83 because in this version context is not enabled from timers

    @classmethod
    def start(cls, context, frames=None):
        """ Start render sequence of frames

        :param context: context
        :type context: 'context'
        :param frames: list of frames to render, None - all frames from the timeline
        :type frames: list

        """
        frames = frames if frames else []
        cls.mode = 'IDLE'
        # frames
        cls._process_frames(frames=frames)
        # 0 frame to start count from
        context.scene.frame_current = context.scene.frame_start - 1
        # render handlers
        if cls.on_render_complete not in bpy.app.handlers.render_complete:
            bpy.app.handlers.render_complete.append(cls.on_render_complete)
        if cls.on_render_cancel not in bpy.app.handlers.render_cancel:
            bpy.app.handlers.render_cancel.append(cls.on_render_cancel)
        # start
        if bpy.app.version[:2] < (2, 93):
            cls._get_context_override(context=context)
        bpy.app.timers.register(
            functools.partial(cls.next_frame, context),
            first_interval=0.5
        )

    @classmethod
    def stop(cls, context):
        """ Manually stop render sequence

        :param context: context
        :type context: 'context'

        """
        # 1 frame
        context.scene.frame_current = context.scene.frame_start
        # render handlers
        if cls.on_render_complete in bpy.app.handlers.render_complete:
            bpy.app.handlers.render_complete.remove(cls.on_render_complete)
        if cls.on_render_cancel in bpy.app.handlers.render_cancel:
            bpy.app.handlers.render_cancel.remove(cls.on_render_cancel)
        cls.mode = 'IDLE'

    @classmethod
    def next_frame(cls, context):
        """ Switch to the next frame from the sequence to render it

        :param context: context
        :type context: 'context'
        :return: interval to make another attempt or None
        :rtype: [int, None]


        """
        # move to the next frame and render it
        if cls.mode == 'RENDER':
            # if rendering - retry after interval
            return cls._render_retry_interval
        elif cls.mode == 'IDLE':
            # if in idle
            next_frame = cls._get_next_frame(context=context)
            if next_frame:
                # continue with the next frame
                context.scene.frame_current = next_frame
                cls.mode = 'RENDER'  # current step in progress
                # execute render
                if not bpy.app.timers.is_registered(cls._render_frame):
                    bpy.app.timers.register(
                        cls._render_frame,
                        first_interval=cls._render_call_interval
                    )
                return cls._render_retry_interval
            else:
                # finish
                cls.stop(context=context)
                return None
        elif cls.mode == 'CANCEL':
            # manual finish by the user
            cls.stop(context=context)
            return None

    @classmethod
    def _render_frame(cls):
        """ Render frame

        :return: interval to make another attempt or None
        :rtype: [int, None]

        """
        # start render current frame
        if bpy.app.version[:2] < (2, 93) and cls._context_override:
            # for 2.83 with override context
            rez = bpy.ops.render.render(cls._context_override, 'INVOKE_DEFAULT', use_viewport=True)
        else:
            rez = bpy.ops.render.render('INVOKE_DEFAULT', use_viewport=True)
        if rez == {'CANCELLED'}:
            # retry with timer
            return cls._render_call_interval

    @classmethod
    def on_render_complete(cls, *args):
        """ On complete rendering the frame

        :param args: arguments
        :type args: *

        """
        output_path = Output.path()
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # save image
        bpy.data.images['Render Result'].save_render(
            os.path.join(
                output_path,
                str(bpy.context.scene.frame_current).zfill(4) + bpy.context.scene.render.file_extension
            )
        )
        cls.mode = 'IDLE'

    @classmethod
    def on_render_cancel(cls, *args):
        """ On cancel rendering the frame by the user

        :param args: arguments
        :type args: *

        """
        cls.mode = 'CANCEL'

    @classmethod
    def _process_frames(cls, frames):
        """ Process frames sequence

        :param frames: frames sequence
        :type frames: [list, str]

        """
        if isinstance(frames, str):
            cls._frames = list(map(int, re.findall('\d+', frames)))
        elif isinstance(frames, list):
            cls._frames = frames
        if cls._frames:
            cls._frames.sort()
            cls._frames.append(None)

    @classmethod
    def _get_next_frame(cls, context):
        """ Get next frame number

        :param context: context
        :type context: 'context'
        :return: next frame to render
        :rtype: [int, None]

        """
        next_frame = None
        if cls._frames:
            # by frames
            next_frame = cls._frames.pop(0)
        else:
            # all sequence
            if context.scene.frame_current + context.scene.frame_step <= context.scene.frame_end:
                next_frame = context.scene.frame_current + context.scene.frame_step
        return next_frame

    @classmethod
    def _get_context_override(cls, context):
        """ Creates copy of the context for override in render for 2.83

        :param context: context
        :type context: 'context'

        """
        cls._context_override = context.copy()
        cls._context_override['window'] = context.window
        cls._context_override['screen'] = context.screen
        cls._context_override['scene'] = context.scene
