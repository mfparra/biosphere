from typing import Dict, List

from Src.Core.Mapper.MapperUtils import MapperUtils


class ToTypeInfo(object):
    """"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """

        self.__class_type = kargs.get('class_type')
        self.__mapping = kargs.get('mapping')

        if not self.__class_type:
            raise ValueError('The class_type is required.')

        self.__properties = MapperUtils.get_properties_from_class(self.__class_type)

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
