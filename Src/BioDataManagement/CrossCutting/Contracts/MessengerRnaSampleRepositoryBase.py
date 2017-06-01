from abc import ABCMeta, abstractmethod
from typing import List

from Src.BioDataManagement.CrossCutting.DTOs.MessengerRnaSampleDto import MessengerRnaSampleDto
from Src.BioDataManagement.CrossCutting.Filters.FeListMessengerRnaSample import FeListMessengerRnaSample
from Src.Core.Data.MongoRepositoryBase import MongoRepositoryBase


class MessengerRnaSampleRepositoryBase(MongoRepositoryBase, metaclass=ABCMeta):
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
    def add_many(self, mrna_samples: List[MessengerRnaSampleDto]):
        """
        
        :param mrna_samples: 
        :return: 
        """
        pass

    @abstractmethod
    def get_many(self, fe_mrna: FeListMessengerRnaSample) -> FeListMessengerRnaSample:
        """

        :param fe_mrna: 
        :return: 
        """
        pass
