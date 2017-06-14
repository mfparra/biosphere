from yaak import inject

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile


class MicroRnaGeneTargetFileManager(object):
    """description of class"""

    @inject.Param(repository='MicroRnaGeneTargetRepositoryBase')
    def __init__(self, repository):
        """
        
        :param repository: 
        """
        if not repository:
            raise ValueError("The 'repository' is required.")

        self.__repository = repository

    def get(self, fe_target: FeSingleMicroRnaGeneTargetFile) -> FeSingleMicroRnaGeneTargetFile:
        """
        
        :param fe_target: 
        :return: 
        """
        fe_target = self.__repository.get(fe_target)
        fe_target.result = list(set(fe_target.result))
        return fe_target
