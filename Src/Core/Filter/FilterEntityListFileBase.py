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


    @property
    def pattern(self) -> str:
        """description of property"""
        return self.__pattern