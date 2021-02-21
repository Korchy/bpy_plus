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
    def matrix_scale(factor: float, axis: tuple = (1, 1, 1), size: int = 4) -> 'Matrix':
        """ Return a scale matrix

        :param factor: Scale factor
        :type factor: float
        :param axis: XYZ-axis to apply scale
        :type axis: tuple
        :param size: size of resulting matrix
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
