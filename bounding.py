# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import bpy
from mathutils import Vector


class Bounding:
    """ Static class for bounding objects

    """

    @staticmethod
    def sphere(objects: list, context=bpy.context, mode: str = 'BBOX'):
        """ Return bounding sphere data

        :param objects: List of objects or object to make bounding sphere around
        :type objects: list
        :param context: context
        :type context: 'context'
        :param mode: 'BBOX' or 'GEOMETRY' - mode to calculate bounding sphere
        :type mode: str
        :return: bounding sphere center and radius
        :rtype: tuple

        """
        if not isinstance(objects, list):
            objects = [objects]
        points_co_global = []
        if mode == 'GEOMETRY':
            # GEOMETRY - by all vertices/points - more precis, more slow
            for obj in objects:
                # to take into modifiers and transforms
                depsgraph = context.evaluated_depsgraph_get()
                obj = obj.evaluated_get(depsgraph)
                if obj.type == 'MESH':
                    points_co_global.extend([obj.matrix_world @ vertex.co for vertex in obj.data.vertices])
                elif obj.type == 'CURVE':
                    for spline in obj.data.splines:
                        points_co_global.extend([obj.matrix_world @ point.co for point in spline.bezier_points])
                else:
                    # can't get all points - use bbox
                    points_co_global.extend([obj.matrix_world @ Vector(bbox) for bbox in obj.bound_box])
        elif mode == 'BBOX':
            # BBOX - by object bounding boxes - less precis, quick
            for obj in objects:
                depsgraph = context.evaluated_depsgraph_get()
                obj_eval = obj.evaluated_get(depsgraph)
                points_co_global.extend([obj_eval.matrix_world @ Vector(bbox) for bbox in obj_eval.bound_box])
        elif mode == 'ORIGIN':
            # ORIGIN - by object origins, not precis but maybe useful in some cases
            points_co_global = [obj.location for obj in objects]

        def get_center(l):
            return (max(l) + min(l)) / 2 if l else 0.0

        x, y, z = [[point_co[i] for point_co in points_co_global] for i in range(3)]
        b_sphere_center = Vector([get_center(axis) for axis in [x, y, z]]) if (x and y and z) else None
        b_sphere_radius = max(((point - b_sphere_center) for point in points_co_global)) if b_sphere_center else None
        return b_sphere_center, b_sphere_radius.length if b_sphere_radius else None
