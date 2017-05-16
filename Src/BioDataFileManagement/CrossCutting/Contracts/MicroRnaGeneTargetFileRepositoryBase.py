from abc import ABCMeta, abstractmethod

from Src.BioDataFileManagement.CrossCutting.Filters.FeSingleMicroRnaGeneTargetFile import FeSingleMicroRnaGeneTargetFile
from Src.Core.Data.FileRepositoryBase import FileRepositoryBase


class MicroRnaGeneTargetFileRepositoryBase(FileRepositoryBase, metaclass=ABCMeta):
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
    def get(self, fe_target: FeSingleMicroRnaGeneTargetFile) -> FeSingleMicroRnaGeneTargetFile:
        """

        :param fe_target: 
        :return: 
        """
        pass
