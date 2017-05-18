from typing import Deque

from Src.BioDataImporter.Contracts.BioDataImporterBase import BioDataImporterBase


class BioImporterManager:
    """
    This class is responsible for executing all the biological data importations.
    """

    @staticmethod
    def execute(importers: Deque[BioDataImporterBase]):
        """
        Execute each importer.
        :param importers: contains a queue of importers
        :return:
        """
        pass
