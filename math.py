# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

def clip(value, _min=0.0, _max=1.0):
    """
    clip value to min-max range

    :param value:
    :type value: int, float
    :param _min:
    :type _min: int, float
    :param _max:
    :type _max: int, float
    :return: clipped value
    :rtype: int, float
    """
    value = min(value, _max)
    value = max(value, _min)
    return value


def range(value, min_src=0.0, max_src=1.0, min_dest=0.0, max_dest=1.0):
    """
    convert value from one range (0...100) to anther (-1...1)

    :param value:
    :type value: int, float
    :param min_src:
    :type min_src: int, float
    :param min_dest:
    :type min_dest: int, float
    :param max_src:
    :type max_src: int, float
    :param max_dest:
    :type max_dest: int, float
    :return: value converted to the dest range
    :rtype: int, float
    """

    if max_src == min_src:
        return None  # no src range
    else:
        return ((value - min_src) / (max_src - min_src)) * (max_dest - min_dest) + min_dest
