from abc import ABCMeta, abstractmethod

from Src.BioDataImporter.Entities.ImportationInfo import ImportationInfo


class BioDataImporterBase(metaclass=ABCMeta):
    """
    Abstract class responsible for importing biological data
    """
    def __init__(self, name):
        """

        :param name: 
        """
        if not name:
            raise ValueError('The name is required.')

        self.__name = name

    @abstractmethod
    def execute(self) -> ImportationInfo:
        """
        Execute the import data process for specific biological data.
        This method must be implemented.
        :return: information about the importation
        """
        pass

    @property
    def name(self) -> str:
        """description of property"""
        return self.__name
