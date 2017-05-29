from abc import ABCMeta, abstractmethod
from typing import List, Dict

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation
from Src.Core.Data.MongoRepositoryBase import MongoRepositoryBase


class GeneAnnotationRepositoryBase(MongoRepositoryBase, metaclass=ABCMeta):
    """description of class"""

    @abstractmethod
    def add_many(self, genes: List[GeneAnnotationDto]):
        pass

    @abstractmethod
    def get_many(self, fe_list_gene: FeListGeneAnnotation, dto_class = None, include_or_exclude_fields: Dict[str, int] = None) -> FeListGeneAnnotation:
        pass
