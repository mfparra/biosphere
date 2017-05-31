from typing import Deque

from Src.BioDataImporter.Contracts.BioDataImporterBase import BioDataImporterBase
from Src.BioDataImporter.Entities.ImportationInfo import ImportationInfo
from Src.BioDataImporter.Entities.ImportationStatus import ImportationStatus


class BioImporterManager:
    """
    This class is responsible for executing all the biological data importations.
    """

    @staticmethod
    def execute(importers: Deque[BioDataImporterBase]) -> ImportationInfo:
        """
        Execute each importer.
        :param importers: contains a queue of importers
        :return: status about the importation process
        """
        importation_details = []

        while importers:
            importer = importers.pop()
            importation_info = importer.execute()

            if importation_info.status != ImportationStatus.OK:
                importation_details.append('{0}. {1}'.format(importation_info.status, importation_info.message))
                return ImportationInfo(status=ImportationStatus.Fail,
                                       message='Importation process has been stopped. See details to more information.',
                                       details=importation_details)

            importation_details.append('{0}. {1} data has imported successfull.'.format(importation_info.status,
                                                                                        importer.name.title()))


        return ImportationInfo(status=ImportationStatus.Fail,
                               message='Importation process has been successfull. See details to more information.',
                               details=importation_details)



