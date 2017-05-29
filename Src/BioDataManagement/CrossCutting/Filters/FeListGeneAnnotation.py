from typing import List

from Src.Core.Filter.FilterEntityListBase import FilterEntityListBase


class FeListGeneAnnotation(FilterEntityListBase):
    """description of class"""

    def __init__(self, **kargs):
        """
        
        :param kargs: 
        """
        super().__init__(**kargs)
        self.__id_entrez_list = kargs.get("id_entrez_list", [])

    @property
    def id_entrez_list(self) -> List[int]:
        """description of property"""
        return self.__id_entrez_list
