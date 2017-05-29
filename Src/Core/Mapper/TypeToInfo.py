from typing import Dict, List


class TypeToInfo(object):
    """"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """

        self.__class_type = kargs.get('class_type')
        self.__mapping = kargs.get('mapping')

        if not self.__class_type:
            raise ValueError('The class_type is required.')

        self.__properties = [p for p in dir(self.__class_type) if isinstance(getattr(self.__class_type, p), property)]

    @property
    def class_type(self) -> int:
        """description of property"""
        return self.__class_type

    @property
    def properties(self) -> List[str]:
        """description of property"""
        return self.__properties[:]

    @property
    def mapping(self) -> Dict:
        """description of property"""
        return self.__mapping
