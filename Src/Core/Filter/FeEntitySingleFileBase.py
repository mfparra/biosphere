from abc import ABCMeta

from Src.Core.Filter.FilterEntitySingleBase import FilterEntitySingleBase


class FeEntitySingleFileBase(FilterEntitySingleBase, metaclass=ABCMeta):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        if not kargs.get('file'):
            raise ValueError("The 'file' is required.")

        self.__file = kargs.get('file')

    @property
    def file(self) -> str:
        """description of property"""
        return self.__file