from abc import ABCMeta
from typing import List

from Src.Core.Filter.FilterEntityListBase import FilterEntityListBase


class FeListSampleBase(FilterEntityListBase, metaclass=ABCMeta):
    """description of class"""

    def __init__(self, **kargs):
        """description of initialize"""

        super().__init__(**kargs)
        self.__patient_id_list = kargs.get("patient_id_list", [])

    @property
    def patient_id_list(self)-> List[str]:
        """description of property"""
        return self.__patient_id_list[:]