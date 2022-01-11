# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/bpy_plus

import re


class Names:

    """ Static class for managing names
    """

    @staticmethod
    def clear(name: str):
        """ Return a clear name (without .001, .002 postfix)

        :param name: name of the object/material/etc.
        :type name: str
        :return: clear name without postfix
        :rtype: str

        """
        regexp = re.compile(r'(\.\d{3}$)')
        return regexp.split(name)[0]

    @staticmethod
    def increase(name: str):
        """ Increase name index .001 -> .002

        :param name: name of the object/material/etc.
        :type name: str
        :return: name with increased index
        :rtype: str

        """
        regexp = re.compile(r'\.(\d{3}$)')
        spl_name = regexp.split(name)
        if len(spl_name) == 1:
            # no index
            name += '.001'
        else:
            # already indexed
            name = spl_name[0] + '.' + str(int(spl_name[1]) + 1).zfill(3)
        return name
