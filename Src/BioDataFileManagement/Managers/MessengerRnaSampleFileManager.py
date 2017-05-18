from Src.BioDataFileManagement.CrossCutting.Contracts.MessengerRnaSampleFileRepositoryBase import \
    MessengerRnaSampleFileRepositoryBase
from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile


class MessengerRnaSampleFileManager(object):
    """description of class"""

    def __init__(self, repository: MessengerRnaSampleFileRepositoryBase):
        """
        
        :param repository: 
        """
        if not repository:
            raise ValueError("The 'repository' is required.")

        self.__repository = repository

    def get(self, fe_mrna: FeListMessengerRnaSampleFile) -> FeListMessengerRnaSampleFile:
        """
        
        :param fe_mrna: 
        :return: 
        """
        fe_mrna = self.__repository.get(fe_mrna)
        fe_mrna.result_list = list(set(fe_mrna.result_list))
        return fe_mrna