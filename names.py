# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import re


def clear_name(name: str):
    """ Return a clear name (without .001, .002 postfix)

    :param name: name of the object/material/etc
    :type name: str
    :return: clear name without postfix
    :rtype: str

    """
    regexp = re.compile(r'(\.\d{3}$)')
    return regexp.split(name)[0]
