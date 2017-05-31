from abc import ABCMeta

from Src.Core.Filter.FilterEntityListBase import FilterEntityListBase


class FilterEntityListFileBase(FilterEntityListBase, metaclass=ABCMeta):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        super().__init__(**kargs)
        self.__pattern = kargs.get('pattern')
        self.__sub_directory = kargs.get('sub_directory')


    @property
    def pattern(self) -> str:
        """description of property"""
        return self.__pattern

    @property
    def sub_directory(self) -> str:
        """description of property"""
        return self.__sub_directory