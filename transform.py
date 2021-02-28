# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

from mathutils import Matrix


class Transform:
    """ Abstract class for simplify working with transformations

    """

    @staticmethod
    def apply(obj):
        """ Apply all transform for the object

        :param obj: Object
        :type obj: bpy.types.Object

        """
        obj_world_matrix = obj.matrix_world.copy()
        for vert in obj.data.vertices:
            vert.co = obj_world_matrix @ vert.co
        obj.matrix_world.identity()

    @staticmethod
    def matrix_scale(factor: float, axis: tuple = (1, 1, 1), size: int = 4) -> 'Matrix':
        """ Return a scale matrix

        :param factor: Scale factor
        :type factor: float
        :param axis: XYZ-axis to apply the scale. Can be combined.
        :type axis: tuple
        :param size: the size of the resulting matrix
        :type size: int
        :return: scale matrix
        :rtype: 'Matrix'

        """
        scale_matrix = Matrix()
        if axis[0]:
            scale_matrix_x = Matrix.Scale(factor, size, (1.0, 0.0, 0.0))
            scale_matrix @= scale_matrix_x
        if axis[1]:
            scale_matrix_y = Matrix.Scale(factor, size, (0.0, 1.0, 0.0))
            scale_matrix @= scale_matrix_y
        if axis[2]:
            scale_matrix_z = Matrix.Scale(factor, size, (0.0, 0.0, 1.0))
            scale_matrix @= scale_matrix_z
        return scale_matrix
