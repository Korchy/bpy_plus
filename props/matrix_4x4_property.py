# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

from bpy.types import PropertyGroup
from bpy.props import FloatProperty
from bpy.utils import register_class
from mathutils import Matrix


class Matrix4x4Property(PropertyGroup):
    """
        Matrix4x4 Property class
    """

    c00: FloatProperty(default=1.0)
    c01: FloatProperty(default=0.0)
    c02: FloatProperty(default=0.0)
    c03: FloatProperty(default=0.0)

    c10: FloatProperty(default=0.0)
    c11: FloatProperty(default=1.0)
    c12: FloatProperty(default=0.0)
    c13: FloatProperty(default=0.0)

    c20: FloatProperty(default=0.0)
    c21: FloatProperty(default=0.0)
    c22: FloatProperty(default=1.0)
    c23: FloatProperty(default=0.0)

    c30: FloatProperty(default=0.0)
    c31: FloatProperty(default=0.0)
    c32: FloatProperty(default=0.0)
    c33: FloatProperty(default=1.0)

    def __repr__(self):
        return '(({0},{1},{2},{3})\n' \
               '({4},{5},{6},{7})\n' \
               '({8},{9},{10},{11})\n' \
               '({12},{13},{14},{15}))'.format(
                    self.c00, self.c01, self.c01, self.c03,
                    self.c10, self.c11, self.c12, self.c13,
                    self.c20, self.c21, self.c22, self.c23,
                    self.c30, self.c31, self.c32, self.c33
                )

    @property
    def matrix(self):
        return Matrix((
            (self.c00, self.c01, self.c02, self.c03),
            (self.c10, self.c11, self.c12, self.c13),
            (self.c20, self.c21, self.c22, self.c23),
            (self.c30, self.c31, self.c32, self.c33),
        ))

    @matrix.setter
    def matrix(self, matrix4x4):
        self.c00 = matrix4x4[0][0]
        self.c01 = matrix4x4[0][1]
        self.c02 = matrix4x4[0][2]
        self.c03 = matrix4x4[0][3]
        self.c10 = matrix4x4[1][0]
        self.c11 = matrix4x4[1][1]
        self.c12 = matrix4x4[1][2]
        self.c13 = matrix4x4[1][3]
        self.c20 = matrix4x4[2][0]
        self.c21 = matrix4x4[2][1]
        self.c22 = matrix4x4[2][2]
        self.c23 = matrix4x4[2][3]
        self.c30 = matrix4x4[3][0]
        self.c31 = matrix4x4[3][1]
        self.c32 = matrix4x4[3][2]
        self.c33 = matrix4x4[3][3]


# register in API
register_class(Matrix4x4Property)
