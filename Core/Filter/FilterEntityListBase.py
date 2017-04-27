from typing import List
from abc import ABCMeta


class FilterEntityListBase(metaclass=ABCMeta):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """

        self.__current_page = kargs.get('current_page', 0)
        self.__page_size = kargs.get('page_size', 10)
        self.__page_count = kargs.get('page_count', 0)
        self.__is_paged = kargs.get('is_paged', True)

        self.__result_list = []

    @property
    def page_count(self) -> int:
        """description of property"""
        return self.__page_count

    @page_count.setter
    def page_count(self, value):
        """description of property"""
        self.__page_count = value

    @property
    def result_list(self) -> List:
        """description of property"""
        return self.__result_list

    @result_list.setter
    def result_list(self, value):
        """description of property"""
        self.__result_list = value

    @property
    def current_page(self) -> int:
        """description of property"""
        return self.__current_page

    @current_page.setter
    def current_page(self, value):
        """description of property"""
        self.__current_page = value

    @property
    def page_size(self) -> int:
        """description of property"""
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        """description of property"""
        self.__page_size = value

    @property
    def is_paged(self) -> bool:
        """description of property"""
        return self.__is_paged

    @is_paged.setter
    def is_paged(self, value):
        """description of property"""
        self.__is_paged = value
