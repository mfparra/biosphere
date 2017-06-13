from typing import List


class ToTypeClass2(object):
    """description of class"""

    def __init__(self, **kargs):
        """

        :param kargs: 
        """

        self.__id = kargs.get('id', None)
        self.__symbol = kargs.get('symbol', '')
        self.__synonyms = kargs.get('synonyms', [])
        self.__locus = kargs.get('locus', '')

    @property
    def id(self) -> int:
        """description of property"""
        return self.__id

    @id.setter
    def id(self, value):
        """

        :param value: 
        :return: 
        """
        self.__id = value

    @property
    def symbol(self) -> str:
        """description of property"""
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        """

        :param value: 
        :return: 
        """
        self.__symbol = value

    @property
    def synonyms(self) -> List[str]:
        """descrzption of property"""
        return self.__synonyms[:]

    @synonyms.setter
    def synonyms(self, value):
        """

        :param value: 
        :return: 
        """
        self.__synonyms = value

    @property
    def locus(self) -> str:
        """descrzption of property"""
        return self.__locus

    @locus.setter
    def locus(self, value):
        """

        :param value: 
        :return: 
        """
        self.__locus = value