from yaak import inject

from Src.BioDataFileManagement.CrossCutting.Filters.FeListMicroRnaSampleFile import FeListMicroRnaSampleFile


class MicroRnaSampleFileManager(object):
    """description of class"""

    @inject.Param(repository='MicroRnaSampleFileRepositoryBase')
    def __init__(self, repository):
        """
        
        :param repository: 
        """
        if not repository:
            raise ValueError("The 'repository' is required.")

        self.__repository = repository

    def get(self, fe_mirna: FeListMicroRnaSampleFile) -> FeListMicroRnaSampleFile:
        """
        
        :param fe_mirna: 
        :return: 
        """
        fe_mirna = self.__repository.get(fe_mirna)
        fe_mirna.result_list = list(set(fe_mirna.result_list))
        return fe_mirna