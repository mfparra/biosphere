from typing import List, Dict

from Src.BioDataManagement.CrossCutting.Contracts.MicroRnaGeneTargetRepositoryBase import \
    MicroRnaGeneTargetRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaGeneTarget import FeListMicroRnaGeneTarget
from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation
from Src.BioDataManagement.DataAccess.Entities.MicroRnaGeneTarget import MicroRnaGeneTarget
from Src.Core.Data.MongoRepositoryActions import MongoRepositoryActions


class MicroRnaGeneTargetRepository(MicroRnaGeneTargetRepositoryBase):
    """description of class"""

    def __init__(self, db):
        """
        
        :param db: 
        """
        super().__init__(db, 'micro_rna_gene_target')
        self.__mongo_actions = MongoRepositoryActions(self._collection)

    def add_many(self, mirna_gene_targets: List[MicroRnaGeneTargetDto]):
        """
        
        :param mirna_gene_targets: 
        """
        self.__mongo_actions.add_many(mirna_gene_targets, MicroRnaGeneTarget)

    def get_many(self, fe_list_targets: FeListMicroRnaGeneTarget, dto_class = None,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListMicroRnaGeneTarget:
        """
        
        :param fe_list_targets: 
        :param dto_class: 
        :param include_or_exclude_fields: 
        :return: 
        """
        query = {} if not fe_list_targets.mirna_symbol_list \
            else {'mirna_symbol': {'$in': fe_list_targets.mirna_symbol_list}}

        return self.__mongo_actions.get_many(query, fe_list_targets, MicroRnaGeneTarget, dto_class, include_or_exclude_fields)
