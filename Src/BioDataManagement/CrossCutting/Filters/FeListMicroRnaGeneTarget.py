from typing import List

from Src.Core.Filter.FilterEntityListBase import FilterEntityListBase


class FeListMicroRnaGeneTarget(FilterEntityListBase):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        super().__init__(**kargs)
        self.__mirna_symbol_list = kargs.get("mirna_symbol_list", [])

    @property
    def mirna_symbol_list(self) -> List[int]:
        """description of property"""
        return self.__mirna_symbol_list
