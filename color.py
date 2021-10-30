# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import random


class Color:

    @staticmethod
    def equal(color_1, color_2, rel_tol=1e-09, abs_tol=0.0001) -> bool:
        """ Return True if two colors are equal
            if compare color with alpha and without alpha - compare only color
                (1.0, 1.0, 1.0) is equal (1.0, 1.0, 1.0, 1.0)

        :param color_1: Color 1
        :type color_1: list, tuple
        :param color_2: Color 2
        :type color_2: list, tuple
        :param rel_tol: Relative tolerance
        :type rel_tol: float
        :param abs_tol: Absolute tolerance
        :type abs_tol: float
        :return: compare result
        :rtype: bool

        """
        for i in range(min(len(color_1), len(color_2))):
            if abs(color_1[i] - color_2[i]) > max(rel_tol * max(abs(color_1[i]), abs(color_2[i])), abs_tol):
                return False
        return True

    @staticmethod
    def random(alpha=False) -> tuple:
        """ Return random color

        :param alpha: random alpha or 1.0
        :type alpha: bool
        :return: random color
        :rtype: tuple

        """
        return (
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1) if alpha else 1.0
        )
