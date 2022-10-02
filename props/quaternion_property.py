# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

from bpy.types import PropertyGroup
from bpy.props import FloatProperty
from bpy.utils import register_class
from mathutils import Quaternion


class QuaternionProperty(PropertyGroup):
    """
        Quaternion Property class
    """

    w: FloatProperty(default=1.0)
    x: FloatProperty(default=0.0)
    y: FloatProperty(default=0.0)
    z: FloatProperty(default=0.0)

    def __repr__(self):
        return '((w={0},x={1},y={2},z={3})'.format(
                    self.w, self.x, self.y, self.z
                )

    @property
    def quaternion(self):
        return Quaternion(
            (self.w, self.x, self.y, self.z)
        )

    @quaternion.setter
    def quaternion(self, _quaternion: Quaternion):
        self.w = _quaternion.w
        self.x = _quaternion.x
        self.y = _quaternion.y
        self.z = _quaternion.z


# register in API
register_class(QuaternionProperty)
