from abc import ABCMeta, abstractmethod

from Src.BioDataFileManagement.CrossCutting.Filters.FeListMicroRnaSampleFile import FeListMicroRnaSampleFile
from Src.Core.Data.FileRepositoryBase import FileRepositoryBase


class MicroRnaSampleFileRepositoryBase(FileRepositoryBase, metaclass=ABCMeta):
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
    def get(self, fe_mirna: FeListMicroRnaSampleFile) -> FeListMicroRnaSampleFile:
        """

        :param fe_mrna: 
        :return: 
        """
        pass
