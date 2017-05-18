from abc import ABCMeta, abstractmethod

from Src.BioDataFileManagement.CrossCutting.Filters.FeListMessengerRnaSampleFile import FeListMessengerRnaSampleFile
from Src.Core.Data.FileRepositoryBase import FileRepositoryBase


class MessengerRnaSampleFileRepositoryBase(FileRepositoryBase, metaclass=ABCMeta):
    """
    Class responsible for manipulates gene annotation file
    """

    def __init__(self, directory):
        """
        Constructor.
        :param directory: 
        """

        super().__init__(directory)

    @abstractmethod
    def get(self, fe_mrna: FeListMessengerRnaSampleFile) -> FeListMessengerRnaSampleFile:
        """

        :param fe_mrna: 
        :return: 
        """
        pass
