# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus


class Mesh:
    """ Abstract class for working with meshes

    """

    @staticmethod
    def tris(obj) -> int:
        """ Return a number of triangles in the mesh object

        :param obj: mesh
        :type obj: bpy.types.Object
        :return: number of triangles in the mesh object
        :rtype: int

        """
        return sum(len(polygon.vertices) - 2 for polygon in obj.data.polygons)
