from typing import List, Dict

from Src.BioDataManagement.CrossCutting.Contracts.GeneAnnotationRepositoryBase import GeneAnnotationRepositoryBase
from Src.BioDataManagement.CrossCutting.DTOs.GeneAnnotationDto import GeneAnnotationDto
from Src.BioDataManagement.CrossCutting.Filters.FeListGeneAnnotation import FeListGeneAnnotation
from Src.BioDataManagement.DataAccess.Entities.GeneAnnotation import GeneAnnotation


class GeneAnnotationRepository(GeneAnnotationRepositoryBase):
    """description of class"""

    def __init__(self, db):
        """
        
        :param db: 
        """
        super().__init__(db, 'gene_annotation')

    def add_many(self, genes: List[GeneAnnotationDto]):
        """
        
        :param genes: 
        """
        self._add_many(genes, GeneAnnotation)

    def get_many(self, fe_list_gene: FeListGeneAnnotation, dto_class = None, include_or_exclude_fields: Dict[str, int] = None) -> FeListGeneAnnotation:
        """
        
        :param fe_list_gene: 
        :param include_or_exclude_fields: 
        :return: 
        """

        query = {}

        if fe_list_gene.id_entrez_list:
            query = {'id_entrez': {'$in': fe_list_gene.id_entrez_list}}
        #elif fe_list_gene.symbol_list:
            #query = {"$or": [{'symbol': {'$in': fe_list_gene.symbol_list}},
                             #{'synonyms_genes': {'$in': fe_list_gene.symbol_list}}]}

        return self.__get_many(query, fe_list_gene, GeneAnnotation, dto_class, include_or_exclude_fields)
