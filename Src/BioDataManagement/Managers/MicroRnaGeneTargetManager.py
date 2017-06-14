from typing import List, Dict

from yaak import inject

from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaGeneTargetDto import MicroRnaGeneTargetDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMicroRnaGeneTarget import FeListMicroRnaGeneTarget
from Src.Core.Manager.ManagerBase import ManagerBase


class MicroRnaGeneTargetManager(ManagerBase):
    """description of class"""

    @inject.Param(repository='MicroRnaGeneTargetRepositoryBase')
    def __init__(self, repository):
        """
        
        :param repository: 
        """
        super().__init__(repository)


    def add_many(self, targets: List[MicroRnaGeneTargetDto]):
        """
        
        :param targets: 
        :return: 
        """
        fe_target_list = self._repository.get_many(
            FeListMicroRnaGeneTarget(is_paged=False, mirna_symbol_list=[t.micro_rna_symbol for t in targets]),
            {'micro_rna_symbol':1})

        new_targets = [t for t in targets if t.micro_rna_symbol not in fe_target_list.result_list]

        if not new_targets:
            return

        self._repository.add_many(new_targets)

    def get_many(self, fe_gene: FeListMicroRnaGeneTarget,
                 include_or_exclude_fields: Dict[str, int] = None) -> FeListMicroRnaGeneTarget:
        """
        
        :param fe_gene: 
        :param include_or_exclude_fields: 
        :return: 
        """
        return self._repository.get_many(fe_gene, MicroRnaGeneTargetDto, include_or_exclude_fields)

