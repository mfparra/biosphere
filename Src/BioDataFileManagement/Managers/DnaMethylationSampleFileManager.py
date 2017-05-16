from Src.BioDataFileManagement.CrossCutting.Contracts.DnaMethylationSampleFileRepositoryBase import \
    DnaMethylationSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Filters.FeListDnaMethylationSampleFile import FeListDnaMethylationSampleFile


class DnaMethylationSampleFileManager(object):
    """description of class"""

    def __init__(self, repository: DnaMethylationSampleFileRepositoryBase):
        """
        
        :param repository: 
        """
        if not repository:
            raise ValueError("The 'repository' is required.")

        self.__repository = repository

    def get(self, fe_dna_methylation: FeListDnaMethylationSampleFile) -> FeListDnaMethylationSampleFile:
        """
        
        :param fe_dna_methylation: 
        :return: 
        """
        fe_dna_methylation = self.__repository.get(fe_dna_methylation)
        fe_dna_methylation.result_list = list(set(fe_dna_methylation.result_list))
        return fe_dna_methylation