from abc import ABCMeta, abstractmethod
from typing import List

from Src.BioDataManagement.CrossCutting.DTOs.DnaMethylationSampleDto import DnaMethylationSampleDto
from Src.BioDataManagement.CrossCutting.Filters import FeListDnaMethylationSample
from Src.Core.Data.MongoRepositoryBase import MongoRepositoryBase


class DnaMethylationSampleRepositoryBase(MongoRepositoryBase, metaclass=ABCMeta):
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
    def add_many(self, dna_methylation_samples: List[DnaMethylationSampleDto]):
        """
        
        :param dna_methylation_samples: 
        :return: 
        """
        pass

    @abstractmethod
    def get_many(self, fe_dna_methylation: FeListDnaMethylationSample) -> FeListDnaMethylationSample:
        """

        :param fe_dna_methylation: 
        :return: 
        """
        pass
