from abc import ABCMeta, abstractmethod


class BioDataImporterBase(metaclass=ABCMeta):
    """
    An abstract class responsible for importing biological data
    """

    @abstractmethod
    def execute(self):
        """
        Execute the import data process for specific biological data.
        This method must be implemented.
        """
        pass
