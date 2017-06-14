from abc import ABCMeta, abstractmethod

from Src.BioDataImporter.Entities.ImportationInfo import ImportationInfo


class BioDataImporterBase(metaclass=ABCMeta):
    """
    Abstract class responsible for importing biological data
    """
    @abstractmethod
    def execute(self) -> ImportationInfo:
        """
        Execute the import data process for specific biological data.
        This method must be implemented.
        :return: information about the importation
        """
        pass