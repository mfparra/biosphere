from Core.File.FileUtils import FileUtils
from Core.Filter.FilterEntitySingleBase import FilterEntitySingleBase


class FeSingleGeneAnnotation(FilterEntitySingleBase):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """
        if not FileUtils.is_file(kargs.get('file', None)):
            raise FileNotFoundError('File not found.')

        self.__file = kargs.get('file')

    @property
    def file(self) -> str:
        """description of property"""
        return self.__file