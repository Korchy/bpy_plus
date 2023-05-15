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

    @staticmethod
    def linear_to_srgb(color_value: float) -> int:
        """
        Convert color value from Linear color space (Blender native) to sRGB color space (commonly used)
        :param color_value: color value in Linear color space in 0.0 ... 1.0 range
        :return: color value in sRGB color space in 0 - 255 range
        """
        if color_value <= 0.0031308:
            return int(12.92 * color_value * 255.99)
        else:
            return int((1.055 * color_value ** (1 / 2.4) - 0.055) * 255.99)

    @staticmethod
    def srgb_to_linear(color_value: int) -> float:
        """
        Convert color value from sRGB color space (commonly used) to Linear color space (Blender native)
        :param color_value: color value in sRGB color space in 0 - 255 range
        :return: color value in Linear color space in 0.0 - 1.0 range
        """
        color_value /= 255.99
        if color_value <= 0.04045:
            return color_value / 12.92
        else:
            return ((color_value + 0.055) / 1.055) ** 2.4

    @staticmethod
    def rgba_to_rgb565(rgba: [list, tuple]) -> int:
        """
        Convert color from RGBA format to RGB565 format
        :param rgba: color in RGBA format, list/tuple of 4 color components (R, G, B, A)
            in range (0-255, 0-255, 0-255, 0-255)
        :return: color in RGB565 format, 2-bytes int, in 0-65535 range
        """
        r, g, b, a = rgba
        r = r >> 3
        g = g >> 2
        b = b >> 3
        rgb565 = 0x0000
        rgb565 |= ((r & 0x1F) << 11)
        rgb565 |= ((g & 0x3F) << 5)
        rgb565 |= (b & 0x1F)
        return rgb565
