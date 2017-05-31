from abc import ABCMeta, abstractmethod
from typing import List, Dict

from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaGeneTarget import FeListMicroRnaGeneTarget
from Src.Core.Data.MongoRepositoryBase import MongoRepositoryBase


class MicroRnaGeneTargetRepositoryBase(MongoRepositoryBase, metaclass=ABCMeta):
    """description of class"""

    @abstractmethod
    def add_many(self, genes: List[MicroRnaGeneTargetDto]):
        """
        
        :param genes: 
        :return: 
        """
        pass

    @abstractmethod
    def get_many(self, fe_list_gene: FeListMicroRnaGeneTarget,
                 dto_class = None,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListMicroRnaGeneTarget:
        """
        
        :param fe_list_gene: 
        :param dto_class: 
        :param include_or_exclude_fields: 
        :return: 
        """
        pass
