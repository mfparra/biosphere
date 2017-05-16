from Src.BioDataFileManagement.CrossCutting.Entities.GeneAnnotationFile import GeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleGeneAnnotationFile import FeSingleGeneAnnotationFile
from Src.BioDataFileManagement.CrossCutting.Contracts.GeneAnnotationFileRepositoryBase import \
    GeneAnnotationFileRepositoryBase


class GeneAnnotationFileManager(object):
    """description of class"""

    def __init__(self, repository: GeneAnnotationFileRepositoryBase):
        """
        
        :param repository: 
        """
        if not repository:
            raise ValueError("The 'repository' is required.")

        self.__repository = repository

    def get(self, fe_gene: FeSingleGeneAnnotationFile) -> FeSingleGeneAnnotationFile:
        """
        
        :param fe_gene: 
        :return: 
        """
        fe_gene = self.__repository.get(fe_gene)
        fe_gene.result = [GeneAnnotationFile(id_entrez=g.id_entrez,
                                             symbol=g.symbol,
                                             synonyms_genes=None if '-' in g.synonyms_genes else g.synonyms_genes)
                          for g in fe_gene.result]

        fe_gene.result = list(set(fe_gene.result))
        return fe_gene