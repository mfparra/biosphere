from abc import ABCMeta


class FilterEntitySingleBase(metaclass=ABCMeta):
    """description of class"""

    def __init__(self):
        """
        """
        self.__result = None

    @property
    def result(self):
        """description of property"""
        return self.__result

    @result.setter
    def result(self, value):
        """description of property"""
        self.__result = value
