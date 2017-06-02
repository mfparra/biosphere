from abc import ABCMeta, abstractmethod
from typing import List

from Src.BioDataFileManagement.CrossCutting.Filters.FeListMicroRnaSampleFile import FeListMicroRnaSampleFile
from Src.BioDataManagement.CrossCutting.DTOs.MicroRnaSampleDto import MicroRnaSampleDto
from Src.Core.Data.FileRepositoryBase import FileRepositoryBase


class MicroRnaSampleRepositoryBase(FileRepositoryBase, metaclass=ABCMeta):
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
    def add_many(self, mirna_samples: List[MicroRnaSampleDto]):
        """

        :param mirna_samples: 
        :return: 
        """
        pass

    @abstractmethod
    def get_many(self, fe_mirna: FeListMicroRnaSampleFile) -> FeListMicroRnaSampleFile:
        """

        :param fe_mrna: 
        :return: 
        """
        pass
