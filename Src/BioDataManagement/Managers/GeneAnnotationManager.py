from typing import List, Dict
from yaak import inject

from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation
from Src.Core.Manager.ManagerBase import ManagerBase


class GeneAnnotationManager(ManagerBase):
    """description of class"""

    @inject.Param(repository='GeneAnnotationRepositoryBase')
    def __init__(self, repository):
        """
        
        :param repository: 
        """
        super().__init__(repository)


    def add_many(self, genes: List[GeneAnnotationDto]):
        """
        
        :param genes: 
        :return: 
        """
        fe_gene_list = self._repository.get_many(
            FeListGeneAnnotation(is_paged=False, id_entrez_list=[g.id_entrez for g in genes]),
            {'id_entrez':1})

        new_genes = [g for g in genes if g.id_entrez not in fe_gene_list.result_list]

        if not new_genes:
            return

        self._repository.add_many(new_genes)

    def get_many(self, fe_gene: FeListGeneAnnotation, include_or_exclude_fields: Dict[str, int] = None) -> FeListGeneAnnotation:
        """
        
        :param fe_gene: 
        :param include_or_exclude_fields: 
        :return: 
        """
        return self._repository.get_many(fe_gene, GeneAnnotationDto, include_or_exclude_fields)

